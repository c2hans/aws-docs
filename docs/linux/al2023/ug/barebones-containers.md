---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/barebones-containers.html
---

# Building bare-bones AL2023 container images
<a name="barebones-containers"></a>

The AL2023 container image is built from the same software components that are included in the AL2023 AMI. It includes a software that enables the base container layer to behave similarly to running on an Amazon EC2 instance, such as the package manager `dnf`. This section explains how you can construct a container from scratch that includes only the bare minimum dependencies needed for an application.

**Note**
The standard AL2023 container images are suitable for most use cases. Using the standard container image makes it easy to build on top of your image. A bare-bones container image makes it more difficult to build on top of your image.

**To create a container with bare minimum dependencies for an application**

1. Determine your runtime dependencies. This will vary based on your application.

1. Construct a `Dockerfile` / `Containerfile` that builds `FROM scratch`. The following example of a `Dockerfile` can be used to build a container that contains only the `bash` shell and its dependencies.

   ```
   FROM public.ecr.aws/amazonlinux/amazonlinux:2023 as build
   RUN mkdir /sysroot
   RUN dnf --releasever=$(rpm -q system-release --qf '%{VERSION}') \
     --installroot /sysroot \
     -y \
     --setopt=install_weak_deps=False \
     install bash

   FROM scratch
   COPY --from=build /sysroot /
   WORKDIR /
   ENTRYPOINT ["/bin/bash"]
   ```

   1. This `Dockerfile` works by:

     1.  Starting a AL2023 container named `build`. This container will be used to bootstrap the barebones container, this container is not deployed itself, but generates the container to be deployed.

     1.  Creating the `/sysroot` directory. This directory will be where the `build` container will install the dependencies needed for the barebones container. In a subsequent step, the `/sysroot` path will be packaged up to be the root directory of our barebones image.

         Using the `--installroot` option to `dnf` in this manner is how we create the other AL2023 images. It's a feature of `dnf` that allows installers and image creation tooling to work.

     1.  Invoking `dnf` to install packages into `/sysroot`.

         The `rpm -q system-release --qf '%{VERSION}'` command queries (`-q`) the `system-release` package, setting the query format (`--qf`) to print out the version of the package being queried (the `%{VERSION}` variable is the `rpm` variable for the version of the `RPM`).

         By setting the `--releasever` argument of `dnf` to the version of `system-release` in the `build` container, this `Dockerfile` can be used to rebuild the barebones container whenever an updated container base image of Amazon Linux is released.

         It is possible to set the `--releasever` to any Amazon Linux 2023 version, such as 2023.12.20260724. Doing this would mean that the `build` container would run as the latest AL2023 version, but build the barebones container from 2023.12.20260724 regardless of what was the current AL2023 release.

         The `--setopt=install_weak_deps=False` configuration option tells `dnf` to only install dependencies that are *required* rather than recommended or suggested.

     1. Copying the installed system into the root of a blank (`FROM scratch`) container.

     1. Setting the `ENTRYPOINT` to be the desired binary, in this case `/bin/bash`.

1. Create an empty directory and add the content of the example in Step 2 to a file named `Dockerfile`.

   ```
   $ mkdir al2023-barebones-bash-example
   	$ cd al2023-barebones-bash-example
   	$ cat > Dockerfile <<EOF
   FROM public.ecr.aws/amazonlinux/amazonlinux:2023 as build
   RUN mkdir /sysroot
   RUN dnf --releasever=$(rpm -q system-release --qf '%{VERSION}') \
     --installroot /sysroot \
     -y \
     --setopt=install_weak_deps=False \
     install bash && dnf --installroot /sysroot clean all

   FROM scratch
   COPY --from=build /sysroot /
   WORKDIR /
   ENTRYPOINT ["/bin/bash"]
   EOF
   ```

1. Build the container by running the following command.

   ```
   $ docker build -t al2023-barebones-bash-example
   ```

1. Run the container using the following command to see how minimal a `bash`-only container is.

   ```
   $ docker run -it --rm al2023-barebones-bash-example
   bash-5.2# rpm
   bash: rpm: command not found
   bash-5.2# du -sh /usr/
   bash: du: command not found
   bash-5.2# ls
   bash: ls: command not found
   bash-5.2# echo /bin/*
   /bin/alias /bin/bash /bin/bashbug /bin/bashbug-64 /bin/bg /bin/catchsegv /bin/cd /bin/command /bin/fc /bin/fg /bin/gencat /bin/getconf /bin/getent /bin/getopts /bin/hash /bin/iconv /bin/jobs /bin/ld.so /bin/ldd /bin/locale /bin/localedef /bin/pldd /bin/read /bin/sh /bin/sotruss /bin/sprof /bin/type /bin/tzselect /bin/ulimit /bin/umask /bin/unalias /bin/wait /bin/zdump
   ```

For a more practical example, the following procedure builds a container for a C application that displays `Hello World!`.

1. Create an empty directory and add the C source code and `Dockerfile`.

   ```
   $ mkdir al2023-barebones-c-hello-world-example
   $ cd al2023-barebones-c-hello-world-example
   $ cat > hello-world.c <<EOF
   #include <stdio.h>
   int main(void)
   {
     printf("Hello World!\n");
     return 0;
   }
   EOF

   $ cat > Dockerfile <<EOF
   FROM public.ecr.aws/amazonlinux/amazonlinux:2023 as build
   COPY hello-world.c /
   RUN dnf -y install gcc
   RUN gcc -o hello-world hello-world.c
   RUN mkdir /sysroot
   RUN mv hello-world /sysroot/
   RUN dnf --releasever=$(rpm -q system-release --qf '%{VERSION}') \
     --installroot /sysroot \
     -y \
     --setopt=install_weak_deps=False \
     install glibc && dnf --installroot /sysroot clean all

   FROM scratch
   COPY --from=build /sysroot /
   WORKDIR /
   ENTRYPOINT ["/hello-world"]
   EOF
   ```

1. Build the container using the following command.

   ```
   $ docker build -t al2023-barebones-c-hello-world-example .
   ```

1. Run the container using the following command.

   ```
   $ docker run -it --rm al2023-barebones-c-hello-world-example
   Hello World!
   ```
