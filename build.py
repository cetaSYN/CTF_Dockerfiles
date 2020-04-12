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

    for name in dockerfiles:
        tag_name = "_".join(name.split("_")[1:])
        cmd = f"docker build -f {name} -t {tag_name} {build_context}"
        try:
            print(f"Building {tag_name}...\n\tThis may take a while.")
            output = subprocess.check_output(cmd.split(" "))
            if f"Successfully tagged {tag_name}:latest" in output.decode().split("\n")[-3:]:
                print(f"Build for {tag_name} {GREEN}Successful{RESET}")
                continue
            print(f"Build for {tag_name} {RED}FAILED{RESET}")
        except Exception:
            print(f"Build for {tag_name} {RED}FAILED{RESET}")


if __name__ == "__main__":
    main()
