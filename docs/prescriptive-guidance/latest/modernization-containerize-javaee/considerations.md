---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-containerize-javaee/considerations.html
---

# Additional considerations
<a name="considerations"></a>

This section covers general considerations on Java containerization that are not specific to Java EE applications.

## Use a small base image
<a name="base-image"></a>

We recommend that you create a small (less than 500 MB) and well-maintained base image. Decreasing the base image size reduces your network and operating costs. A smaller base image can also improve security by reducing the number of components that can be exploited. You can use one of the distroless images based on Debian. The images have the minimum number of tools installed on them and don't contain package managers or shells. These distroless images also reduce the overall surface of attack. Distroless images can be smaller than 150 MB. For more information, see the ["Distroless" Container Images](https://github.com/GoogleContainerTools/distroless) GitHub repository.

It's a best practice to follow the disposability principle and develop a fast startup time for your container images. By using techniques such as [ahead-of-time-compilation](https://openjdk.java.net/jeps/295) (OpenJDK documentation) or [application class data sharing](https://openjdk.java.net/jeps/310) (OpenJDK documentation), you can improve the overall startup time by compiling Java classes to native code prior to launching the virtual machine and by allowing a set of classes to be pre-processed into a shared archive file. You can also use GraalVM to build minimal docker images for Java applications. For more information, see the [Using GraalVM to Build Minimal Docker Images for Java Applications](https://aws.amazon.com/blogs/opensource/using-graalvm-build-minimal-docker-images-java-applications/) AWS blog post.

## Upgrade to a container-aware JDK version
<a name="jdk-version"></a>

Before JDK 8u131, the JVM did not recognize memory or CPU limits set by the Docker engine using flags. This means that whenever you run your application in a container, JVM "sees" the total number of processors available on the system, or in the case of virtual machines, the virtual system. The same is true for default memory limits: the JVM will look at the host's overall memory and use that for setting its defaults. Consequently, the JVM can claim more memory than the container platform allows it to, which results in ending the Java process by the container platform (Docker). One solution to this problem is to migrate your Java application to either Java 9 or 8u131\+ before containerizing. Java 10 and later versions have full container awareness and support.
