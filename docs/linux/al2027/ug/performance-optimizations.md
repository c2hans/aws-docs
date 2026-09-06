---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/performance-optimizations.html
---

# Performance and operational optimizations
<a name="performance-optimizations"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

**Amazon Linux 7.1 kernel**
+ AL2027 uses the latest drivers for Elastic Network Adapter (ENA) and Elastic Fabric Adapter (EFA) devices. AL2027 focuses on performance and functionality backports for hardware in Amazon EC2 infrastructure.
+ All kernel build and runtime configurations include many of the same performance and operational optimizations of AL2023.

**Base toolchain selection and default build flags**
+ AL2027 packages are built with compiler optimizations (`-O2`) enabled by default.
+ AL2027 packages are built requiring `x86-64-v3` for `x86-64` systems (`-march=x86-64-v3`), and Graviton 2 or higher for `aarch64` (`-march=armv8.2-a+crypto -mtune=neoverse-n1`). This enables the compiler to use AVX and AVX2 instructions for improved performance on `x86-64` systems.
+ AL2027 packages are built with auto-vectorization enabled (`-ftree-vectorize`).
+ AL2027 packages are built with Link Time Optimization (LTO) enabled.
+ AL2027 uses GCC 16.1 as the default compiler, along with updated versions of Rust, Clang/LLVM 22, and Go.
+ On `aarch64` (Graviton) instances, AL2027 enables transparent huge pages (THP) for `malloc` heap arenas by default, with glibc using 2 MB huge pages for heap arenas. For workloads with a large memory working set and frequent random memory accesses, this can improve performance. Workloads running in memory-constrained cgroups (such as containers with low memory limits) might experience increased memory consumption. To disable THP for `malloc`, set the environment variable `GLIBC_TUNABLES=glibc.malloc.hugetlb=0`.
+ Some workloads, such as certain database engines, perform better with transparent huge pages disabled system-wide. To disable THP at runtime, run `echo never > /sys/kernel/mm/transparent_hugepage/enabled` as root. To persist the setting across reboots, add `transparent_hugepage=never` to the kernel command line.

**Package selection and versions**
+ AL2027 uses DNF5 as its package manager. DNF5 is a C\+\+ rewrite of DNF (version 4) that provides faster package operations, lower memory usage, and quicker repository metadata handling. For more information, see [Package management tool](package-management.md).
+ Select backports to major system components include several performance improvements for running on Amazon EC2 infrastructure, especially Graviton instances.
+ AL2027 is integrated with several AWS services and features. This includes the AWS CLI and SSM Agent.
+ AL2027 uses Amazon Corretto as the Java Development Kit (JDK).
+ AL2027 provides database engines and programming language runtime updates to newer versions as they're released by upstream projects. Programming language runtimes with new versions are added when they're released.

**Deployment in a cloud environment**
+ The base AL2027 AMI and container images are frequently updated to support patching instance replacement.
+ Kernel updates are included in AL2027 AMI updates. This means that you don't need to use commands such as `dnf upgrade` and `reboot` to update your kernel.
+ In addition to the standard AL2027 AMI, a minimal AMI and container image is also available. Choose the minimal AMI to run an environment with the minimal number of packages that's required to run your service.
+ By default, AL2027 AMIs and containers are locked to a specific version of the package repositories. There's no auto-update when they're launched. This means that you're always in control of when you ingest any package update. You can always test in a beta/gamma environment before rolling out to production. If there's a problem, you can use the pre-validated rollback path. For more information, see [Deterministic upgrades through versioned repositories on AL2027](deterministic-upgrades.md).
