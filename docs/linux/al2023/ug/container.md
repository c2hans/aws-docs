---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/container.html
---

# Using AL2023 in containers
<a name="container"></a>

**Note**
 For more information about how to use AL2023 to host containerized workloads on Amazon ECS, see [AL2023 for Amazon ECS container hosts](ecs.md).

 There are several ways that AL2023 can be used inside containers depending on the use case. The [AL2023 Base Container Image](base-container.md) is most similar to an Amazon Linux 2 container image and the AL2023 minimal AMI.

 For advanced users, we offer a minimal container image, introduced in the AL2023.2 release, along with documentation that describes how to build [bare-bones containers](barebones-containers.md).

 AL2023 can also be used to host containerized workloads, either of AL2023 based container images, or containers based on other Linux distributions. You can use [AL2023 for Amazon ECS container hosts](ecs.md), or use the provided container runtime packages directly. The `docker`, `containerd`, and `nerdctl` packages are available to be installed and used on AL2023.

**Topics**
+ [Using the AL2023 base container image](base-container.md)
+ [AL2023 Minimal container image](minimal-container.md)
+ [Building bare-bones AL2023 container images](barebones-containers.md)
+ [Comparing packages installed on Amazon Linux 2023 Container Images](al2023-container-image-types.md)
+ [Comparing packages installed on Amazon Linux 2023 Minimal AMI and Container Images](al2023-container-ami.md)
