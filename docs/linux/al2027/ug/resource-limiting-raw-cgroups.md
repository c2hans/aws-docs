---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/resource-limiting-raw-cgroups.html
---

# Limiting process resource usage in AL2027 using cgroups
<a name="resource-limiting-raw-cgroups"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

While it is recommended to use [Resource control with systemd](resource-limiting-systemd.md), this section covers basic usage of the base `libcgroup-tools` utilities to limit CPU and memory usage of processes. Both methods are alternatives to using the `cpulimit` utility.

The following example covers running the `stress-ng` stress test (from the `stress-ng` package) while limiting its CPU and memory usage using utilities from the `libcgroup-tools` package, and the tunables in `sysfs`.

**Use `libcgroup-tools` on the command line to limit resource usage**

1. Install the `libcgroup-tools` package.

   ```
   [ec2-user ~]$ sudo dnf install {{libcgroup-tools}}
   ```

1. Create a `cgroup` with the `memory` and `cpu` controllers, and give it a name (`our-example-limits`). Using the `-a` and `-t` options to allow the `ec2-user` user to control the tunables of the `cgroup`.

   ```
   [ec2-user ~]$ sudo cgcreate -a {{ec2-user}} -t {{ec2-user}} -g memory,cpu:{{our-example-limits}}
   ```

   There is now a `/sys/fs/cgroup/our-example-limits/` directory that contains files that can be used to control each tunable.

1. Limit memory usage of all processes in our `cgroup` to 100 million bytes.

   ```
   [ec2-user ~]$ echo {{100000000}} > /sys/fs/cgroup/{{our-example-limits}}/memory.max
   ```

1. Limit CPU usage of all processes in our `cgroup` to 10%. The format of the `cpu.max` file is `$MAX $PERIOD`, limiting the group to consuming `$MAX` for every `$PERIOD`.

   ```
   [ec2-user ~]$ echo {{10000 100000}} > /sys/fs/cgroup/{{our-example-limits}}/cpu.max
   ```

1. The following example runs `stress-ng` (which can be installed by running `dnf install -y stress-ng`) in the `our-example-limits` cgroup. While the `stress-ng` command is running, you can observe using `top` that it is limited to 10% of CPU time.

   ```
   [ec2-user ~]$ sudo cgexec -g memory,cpu:our-example-limits {{stress-ng --cpu 1}}
   ```

1. Clean up by removing the cgroup.

   ```
   [ec2-user ~]$ sudo cgdelete -g memory,cpu:{{our-example-limits}}
   ```

The [Linux Kernel documentation for `cgroup-v2`](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) on the kernel.org website contains extensive details about how they work. The documentation of the [cpu](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#cpu) and [memory](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html#memory) controllers, both on the kernel.org website, covers the details of how to use each tunable option.
