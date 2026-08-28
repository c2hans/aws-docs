---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/system-requirements.html
---

# AL2023 system requirements
<a name="system-requirements"></a>

 This section describes the system requirements for using AL2023.

**Topics**
+ [CPU requirements for running AL2023](#system-requirements-cpu)
+ [Memory (RAM) requirements for running AL2023](#system-requirements-memory)

## CPU requirements for running AL2023
<a name="system-requirements-cpu"></a>

 To run any AL2023 code, the processor used needs to meet certain minimum requirements. Attempts to run AL2023 on CPUs that do not meet these requirements might result in illegal instruction errors very early in code execution.

 The minimum requirements apply to [AL2023 on Amazon EC2](ec2.md), [AL2023 in containers](container.md), and [AL2023 outside Amazon EC2](outside-ec2.md).

### ARM CPU Requirements for AL2023
<a name="system-requirements-cpu-aarch64"></a>

 All AL2023 `aarch64` (ARM) binaries are built for 64-bit. No 32-bit ARM binaries are available, so a 64-bit ARM CPU is required.

**Note**
 For Arm-based instances, AL2023 only supports instance types that use Graviton2 or later processors. AL2023 doesn't support A1 instances.

 AL2023 requires an ARMv8.2 compliant processor with the Cryptography Extension (`ARMv8.2+crypto`). All AL2023 packages for `aarch64` are built with the `-march=armv8.2-a+crypto` compiler flag. Although we attempt to print graceful error messages when AL2023 code is attempted to be run on older ARM processors, it is possible that the first error message may be an illegal instruction error.

**Note**
 Because of the AL2023 `aarch64` base CPU requirements, all Raspberry Pi systems prior to the Raspberry Pi 5 do not meet the minimum CPU requirements.

### x86-64 CPU Requirements for AL2023
<a name="system-requirements-cpu-x86-64"></a>

 All AL2023 `x86-64` binaries are built for the `x86-64v2` revision of the `x86-64` architecture by passing `-march=x86-64-v2` to the compiler.

 The `x86-64v2` revision of the architecture adds the following CPU features on top of the baseline `x86-64` architecture:
+ `CMPXCHG16B`
+ `LAHF-SAHF`
+ `POPCNT`
+ `SSE3`
+ `SSE4_1`
+ `SSE4_2`
+ `SSSE3`

This roughly maps to `x86-64` processors released in 2009 or later. Examples include the Intel Nehalem, AMD Jaguar, Atom Silvermont, along with the VIA Nano and Eden C microarchitectures.

 In Amazon EC2, all `x86-64` instance types support `x86-64v2`, including `M1`, `C1`, and `M2` instance families.

No 32-bit x86 (i686) AL2023 binaries are built. Although AL2023 retains support for running 32-bit userspace binaries, this functionality is deprecated and might be removed in a future major version of Amazon Linux. For more information, see [32bit x86 (i686) Packages](compare-with-al2.md#i686).

## Memory (RAM) requirements for running AL2023
<a name="system-requirements-memory"></a>

 The Amazon EC2 `.nano` family of instance types (`t2.nano`, `t3.nano`, `t3a.nano`, and `t4g.nano`) have 512 MB RAM which is the minimum requirement for AL2023.

**Note**
 Although 512 MB is the miminum requirement, these instance types are memory constrained and functionality and performance may be limited.

 AL2023 images have not been tested on systems with less than 512 MB RAM. Running AL2023 based container images in less than 512 MB RAM will be dependent on the containerized workload.

 Some workloads, such as `dnf upgrade` between some AL2023 releases can require more than 512 MB RAM. For this reason, the [AL2023.3](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20230920.html) release introduced enabling `zram` by default for instances with less than 800 MB of RAM. For containerized workloads, this means that some workloads might run fine on AL2023 instances with this amount of memory, but fail when run in a container restricted to this amount of memory usage.

 For instance types with less than 800 MB of RAM, AL2023 (as of [ AL2023.3 ](https://docs.aws.amazon.com/linux/al2023/release-notes/relnotes-2023.2.20230920.html) or newer) will enable `zram` based swap by default. Examples of Amazon EC2 instance types with less than 800 MB memory include `t4g.nano`, `t3a.nano`, `t3.nano`, `t2.nano`, and `t1.micro`. This means fewer out of memory scenarios for these instance types, because AL2023 will on-demand compress and decompress memory pages. This enables workloads that would otherwise require an instance type with more memory, at the expense of CPU usage needed to do the compression.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
