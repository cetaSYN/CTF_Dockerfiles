# CTF_Dockerfiles

This repo is a collection of personal resources for a dockerized CTF environment.

Images:

- `parrot`
  - Modded version of ParrotOS (`parrotsec/security:latest`)
  - Adds utilities common in CTFs
  - Adds logging for all commands and output (nice for write-ups and reports)
- `revr-multiarch`
  - Modded version of `ubuntu`
  - Heavily influcenced by skysider/multiarch-docker
  - Build for cross-architecture reverse engineering / vulnerability research, especially in CTF environments

## Setup

`./build.py`

## Usage

### Run

Examples:

`docker run --rm -it -v$(pwd):/root/ --net host parrot`

`docker run --rm -it -v$(pwd):/root/ parrot-re`

Explanation:

- `--rm`
  - Tells Docker to remove the container when exiting
  - The data is stored in a mapped mount between the host `./root/` and container `/root`
  - All other data is removed when exiting. Be sure to store it correctly!
- `-it`
  - Tells Docker to set up an interactive pseudo-terminal
- `-v$(pwd):/root/`: Create a mapped mount
  - As written the map is between the host working directory and container `/root/`
  - **NOTE:** Never map to a folder with any private or system files from the host.
- `--net host`
  - Tells Docker to use the host's networking stack instead a Docker network
  - This allows utilization of ssh tunnels, reverse shells, whatever to the host instead of traversing Docker NAT
- `parrot`
  - Tells Docker to use our updated/modded image
  - All options available in this repo are listed at the top of this README
  - If you prefer the official build it is `parrotsec/security:latest`

If you need to use well-known ports you should add the `--privileged` flag.

### In-Container

## Why

Dockerizing my CTF setup enables me to use a few lightweight images to perform different tasks with the data shared to a mount. The ephemeral nature of the containers ensures that I have a clean environment for each new challenge.

**NOTE:** Docker is not perfect isolation. Do not use this for anything like malware analysis or CTFs where you know you may be attacked.
