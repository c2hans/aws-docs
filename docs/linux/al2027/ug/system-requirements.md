---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/system-requirements.html
---

# AL2027 system requirements
<a name="system-requirements"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This section describes the system requirements for using AL2027.

**Topics**
+ [CPU requirements for running AL2027](#system-requirements-cpu)
+ [Memory (RAM) requirements for running AL2027](#system-requirements-memory)

## CPU requirements for running AL2027
<a name="system-requirements-cpu"></a>

To run any AL2027 code, the processor used needs to meet certain minimum requirements. Attempts to run AL2027 on CPUs that do not meet these requirements might result in illegal instruction errors very early in code execution.

The minimum requirements apply to [AL2027 on Amazon EC2](ec2.md) and [AL2027 in containers](container.md).

### ARM CPU requirements for AL2027
<a name="system-requirements-cpu-aarch64"></a>

All AL2027 `aarch64` (ARM) binaries are built for 64-bit. No 32-bit ARM binaries are available, so a 64-bit ARM CPU is required.

**Note**
For Arm-based instances, AL2027 only supports instance types that use Graviton2 or later processors. AL2027 doesn't support A1 instances.

AL2027 requires an ARMv8.2 compliant processor with the Cryptography Extension. All AL2027 packages for `aarch64` are built with the `-march=armv8.2-a+crypto -mtune=neoverse-n1` compiler flags. Although we attempt to print graceful error messages when AL2027 code is attempted to be run on older ARM processors, it is possible that the first error message may be an illegal instruction error.

**Note**
Because of the AL2027 `aarch64` base CPU requirements, all Raspberry Pi systems prior to the Raspberry Pi 5 do not meet the minimum CPU requirements.

### x86-64 CPU requirements for AL2027
<a name="system-requirements-cpu-x86-64"></a>

All AL2027 `x86-64` binaries are built for the `x86-64-v3` revision of the `x86-64` architecture by passing `-march=x86-64-v3` to the compiler, with auto-vectorization enabled by default.

The `x86-64-v3` revision of the architecture requires the following CPU features on top of the `x86-64-v2` baseline:
+ `AVX`
+ `AVX2`
+ `BMI1`
+ `BMI2`
+ `F16C`
+ `FMA`
+ `LZCNT`
+ `MOVBE`
+ `XSAVE`

This roughly maps to `x86-64` processors released in 2015 or later. Examples include the Intel Haswell and AMD Excavator microarchitectures and later.

Because of this requirement, AL2027 does not support several previous generation Amazon EC2 instance types that predate the `x86-64-v3` baseline. For the list of unsupported instance types, see [AL2027 on Amazon EC2](ec2.md).

AL2027 does not support 32-bit x86 (i686) at all. No 32-bit AL2027 binaries are built, the repositories contain no i686 packages, and running 32-bit userspace binaries is not supported. For more information, see [32bit x86 (i686) runtime support](deprecated-al2023.md#deprecated-32bit).

## Memory (RAM) requirements for running AL2027
<a name="system-requirements-memory"></a>

The Amazon EC2 `.nano` family of instance types (`t3.nano`, `t3a.nano`, and `t4g.nano`) have 512 MB RAM, which is the minimum requirement for AL2027.

**Note**
Although 512 MB is the minimum requirement, these instance types are memory constrained and functionality and performance may be limited.

AL2027 images have not been tested on systems with less than 512 MB RAM. Running AL2027 based container images in less than 512 MB RAM will be dependent on the containerized workload.

For instances with less than 800 MB of RAM, AL2027 enables `zram` based swap by default. For containerized workloads, this means that some workloads might run fine on AL2027 instances with this amount of memory, but fail when run in a container restricted to this amount of memory usage.

Examples of Amazon EC2 instance types with less than 800 MB memory include `t4g.nano`, `t3a.nano`, and `t3.nano`. Enabling `zram` means fewer out of memory scenarios for these instance types, because AL2027 will on-demand compress and decompress memory pages. This enables workloads that would otherwise require an instance type with more memory, at the expense of CPU usage needed to do the compression.
