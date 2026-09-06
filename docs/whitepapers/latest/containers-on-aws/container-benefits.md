---
source_url: https://docs.aws.amazon.com/whitepapers/latest/containers-on-aws/container-benefits.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Container benefits
<a name="container-benefits"></a>

The rapid growth of containers is fueled by the many benefits it provides. If you have applications that run on VMs or bare metal servers today, you can consider containerizing them to take advantages of the benefits from containers. The primary benefits of container are speed, consistency, density, resource efficiency, and portability.

## Speed
<a name="speed"></a>

 Thanks to its lightweight and modular nature, containers can enable rapid iteration of your applications. Your development speed improves through the ability to deconstruct applications into smaller units. This is advantageous because it reduces shared resources among application components, leading to fewer compatibility issues between required libraries or packages. The container startup time primarily depends on the size of the container image, cache, the time to pull the image and start the container on host. To improve the container startup time, keep the size of your container image as small as possible. You can use techniques like multi-stage builds, local cache, and [Seekable OCI](https://aws.amazon.com/about-aws/whats-new/2022/09/introducing-seekable-oci-lazy-loading-container-images/) (SOCI) when applicable.

## Consistency
<a name="consistency"></a>

 The consistency and fidelity of a modular development environment provides predictable results when moving code between development, test, and production systems. By ensuring that the container encapsulates exact versions of necessary libraries and packages, it is possible to minimize the risk of any compatibility issue.

 This concept easily lends itself to a *disposable system* approach, in which patching individual containers is less preferable than building new containers in parallel, testing, and replacing the old. This practice helps avoid *drift* of packages across a fleet of containers, versions of your application, or dev/test/prod environments; the result is more consistent, predictable, and stable applications.

## Density and resource efficiency
<a name="density-and-resource-efficiency"></a>

 Containers facilitate enhanced resource efficiency by allowing multiple containers to run on a single host system. Resource efficiency is a natural result of the isolation and allocation techniques that containers use. You can restrict your containers to a required number of CPUs and allocate specific amount of memory. By understanding the resources needs for your container and the resources available to your VM or the underlying host, it’s possible to maximize the containers running on a single host. This results in higher density, increased efficiency of compute resources, and less wastage on excess capacity. We will discuss more about container scheduling details in the [Scheduling](scheduling.md) section.

## Portability
<a name="portability"></a>

 The flexibility of containers is based on its portability, ease of deployment, and smaller size compared to virtual machines. The [Open Container Initiative](https://opencontainers.org/about/overview/) (OCI), was formed to support fully interoperable container open standards with 3 specifications:
+  The Runtime Specification (runtime-spec)
+  The Image Specification (image-spec)
+  The Distribution Specification (distribution-spec)

 The OCI image specification defines an OCI Image, consisting of an [image manifest](https://github.com/opencontainers/image-spec/blob/main/manifest.md), which contains metadata about contents and dependencies of the image; an [image index](https://github.com/opencontainers/image-spec/blob/main/image-index.md) (optional); a set of [filesystem layers](https://github.com/opencontainers/image-spec/blob/main/layer.md); and a [configuration](https://github.com/opencontainers/image-spec/blob/main/config.md), such as arguments and environment variables. You can run the OCI compliant container image on any supported version of Linux or Windows, if you have the OCI compliant container runtime installed on the host.

 OCI allows a compliant container to be portable across all major operating systems and platforms without worrying that their current choice of any infrastructure, cloud provider, or tool will lock them into any technology provider as a container format is not bound to any higher level constructs.

 Containers also provide the flexibility which makes micro-services architecture possible. In common infrastructure models, a virtual machine runs multiple services. In contrast, containers package services in isolation, on top of a common host OS. This allows a service to move between hosts, stay isolated from failure of other adjacent services, and stay protected from errant patches or software upgrades on the host system. Because containers provide clean, reproducible, and modular environments, it streamlines both code deployment and infrastructure management.
