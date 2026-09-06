---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/container.html
---

# Using AL2027 in containers
<a name="container"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Containers provide a consistent AL2027 environment for developing and running applications. Choose an option based on how you want to create the container.
+ Use the [AL2027 base container image](container-base.md) for a ready-to-run AL2027 environment or as the base for your own container image.
+ Use the [AL2027 minimal container image](container-minimal.md) as a separate image variant. Add the packages that your application requires.
+ Use the [Bare-bones AL2027 container images](barebones-containers.md) workflow to build an application-specific root filesystem. DNF5 resolves the package dependencies.

**Topics**
+ [Using the AL2027 base container image](container-base.md)
+ [AL2027 minimal container image](container-minimal.md)
+ [Building bare-bones AL2027 container images](barebones-containers.md)
+ [Comparing packages installed on Amazon Linux 2027 Container Images](al2027-container-image-types.md)
+ [Comparing packages installed on Amazon Linux 2027 Minimal AMI and Container Images](al2027-container-ami.md)
