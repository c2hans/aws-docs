---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/cgroupv2.html
---

# Unified Control Group hierarchy (cgroup v2)
<a name="cgroupv2"></a>

 A Control Group (cgroup) is a Linux kernel feature to hierarchically organize processes and distribute system resources between them. Control Groups are used extensively to implement a container runtime, and by `systemd`.

 AL2 supports cgroupv1, and AL2023 supports cgroupv2. This is notable if running containerized workloads, such as when [Using AL2023 based Amazon ECS AMIs to host containerized workloads](ecs.md).

 Although AL2023 still includes code that can make the system run using cgroupv1, this is not a recommended or supported configuration, and will be completely removed in a future major release of Amazon Linux.

 There is extensive documentation regarding the [low-level Linux Kernel interfaces](https://docs.kernel.org/admin-guide/cgroup-v2.html), as well as [systemd cgroup delegation documentation](https://systemd.io/CGROUP_DELEGATION/).

 A common use case outside of containers is for creating `systemd` units that have limits placed on the system resources they can use. For more information, see [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/systemd.resource-control.html).
