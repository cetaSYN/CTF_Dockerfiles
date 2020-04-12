#!/usr/bin/env python3

"""Docker image build automation"""

import os
import subprocess

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[39m"


def main():
    build_context = os.path.dirname(__file__)
    dockerfiles = sorted(  # Ensure predictable build order for dependency mgmt
        [f for f in os.listdir(build_context) if f.startswith("Dockerfile")]
    )

    results = dict()  # {tag_name : successful_bool}
    for name in dockerfiles:
        tag_name = "_".join(name.split("_")[1:])
        cmd = f"docker build -f {name} -t {tag_name} {build_context}"
        try:
            print(f"Building {tag_name}...")
            output = subprocess.check_output(cmd.split(" "))
            if f"Successfully tagged {tag_name}:latest" in output.decode().split("\n")[-3:]:
                results[tag_name] = True
                continue
            results[tag_name] = False
        except Exception:
            results[tag_name] = False

    # Print summary as Docker will eat the terminal during build
    for tag, success in results.items():
        if success:
            print(f"Build for {tag} {GREEN}Successful{RESET}")
        else:
            print(f"Build for {tag} {RED}FAILED{RESET}")


if __name__ == "__main__":
    main()
