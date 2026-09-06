---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/barebones-containers.html
---

# Building bare-bones AL2027 container images
<a name="barebones-containers"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

A bare-bones container image starts with an empty root filesystem. You add the packages that your application requires. Use a multi-stage build to resolve and install those packages with DNF5. The final stage copies the root filesystem into a `FROM scratch` image.

**Runtime dependencies**
The final image contains only the packages and files that the build stage adds to `/sysroot`. The examples on this page don't include the `dnf` or `rpm` commands, common diagnostic utilities such as `ls` and `du`, or the CA certificate bundle. Add every tool and runtime dependency that your application requires.
Rebuild the image from an updated AL2027 base image to include package updates.

## Prerequisites
<a name="barebones-containers-prerequisites"></a>

Install and start Docker on the system that you use to build the image. On AL2027, run the following commands.

```
$ sudo dnf install -y docker
$ sudo systemctl start docker
```

The examples assume that your user can run `docker` commands without `sudo`. For information about configuring access to the Docker daemon, see [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/) in the Docker documentation.

## Build an image with Bash
<a name="barebones-containers-bash"></a>

The following procedure creates a container image that contains Bash and the package dependencies that DNF5 resolves for it.

**To build a bare-bones image with Bash**

1. Create and open a directory for the example.

   ```
   $ mkdir al2027-barebones-bash-example
   $ cd al2027-barebones-bash-example
   ```

1. Create a file named `Dockerfile` with the following content.

   ```
   FROM public.ecr.aws/amazonlinux/amazonlinux:2027 AS build
   RUN mkdir /sysroot
   RUN dnf --releasever=$(rpm -q system-release --qf '%{VERSION}') \
     --installroot /sysroot \
     --use-host-config \
     -y \
     --setopt=install_weak_deps=False \
     install bash \
     && dnf --installroot /sysroot clean all

   FROM scratch
   COPY --from=build /sysroot /
   WORKDIR /
   ENTRYPOINT ["/bin/bash"]
   ```

   In the build stage, DNF5 uses the repository configuration from the AL2027 base image to install packages into `/sysroot`. The following options configure the installation.
   + `--releasever` uses the version of the `system-release` package in the build-stage image.
   + `--installroot` installs packages into `/sysroot` instead of the build-stage root filesystem.
   + `--use-host-config` uses the DNF5 configuration and repositories from the build-stage image. It applies this configuration to the empty install root.
   + `--setopt=install_weak_deps=False` excludes suggested and recommended packages from dependency resolution.

   After DNF5 removes its cached repository data, the final stage copies `/sysroot` into an empty image and sets Bash as the entry point.

1. Build the container image.

   ```
   $ docker build -t al2027-barebones-bash-example .
   ```

1. Run Bash in the container.

   ```
   $ docker run --rm -it al2027-barebones-bash-example
   ```

## Build an image for a compiled application
<a name="barebones-containers-c"></a>

The following procedure compiles a C application in the build stage and copies the application and its DNF5-resolved runtime package closure into the final image.

**To build a bare-bones image for a C application**

1. Create and open a directory for the example.

   ```
   $ mkdir al2027-barebones-c-example
   $ cd al2027-barebones-c-example
   ```

1. Create a file named `hello-world.c` with the following content.

   ```
   #include <stdio.h>

   int main(void)
   {
       printf("Hello World!\n");
       return 0;
   }
   ```

1. Create a file named `Dockerfile` with the following content.

   ```
   FROM public.ecr.aws/amazonlinux/amazonlinux:2027 AS build
   COPY hello-world.c /
   RUN dnf -y install gcc
   RUN gcc -o hello-world hello-world.c
   RUN mkdir /sysroot
   RUN mv hello-world /sysroot/
   RUN dnf --releasever=$(rpm -q system-release --qf '%{VERSION}') \
     --installroot /sysroot \
     --use-host-config \
     -y \
     --setopt=install_weak_deps=False \
     install glibc \
     && dnf --installroot /sysroot clean all

   FROM scratch
   COPY --from=build /sysroot /
   WORKDIR /
   ENTRYPOINT ["/hello-world"]
   ```

   The compiler remains in the build stage. DNF5 installs `glibc` and its complete dependency closure into `/sysroot` for the final image. The dependency closure can contain packages in addition to the package that the `install` command names.

1. Build the container image.

   ```
   $ docker build -t al2027-barebones-c-example .
   ```

1. Run the application.

   ```
   $ docker run --rm al2027-barebones-c-example
   Hello World!
   ```
