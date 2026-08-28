---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/performance-optimizations.html
---

# Performance and operational optimizations
<a name="performance-optimizations"></a>

**Amazon Linux 6.1 kernel**
+ AL2023 uses the latest drivers for Elastic Network Adapter (ENA) and Elastic Fabric Adapter (EFA) devices. AL2023 focuses on performance and functionality backports for hardware in Amazon EC2 infrastructure.
+ Kernel live patching is available for the `x86_64` and `aarch64` instance types. This reduces the need for frequent reboots.
+ All kernel build and runtime configurations include many of the same performance and operational optimizations of AL2.

**Base toolchain selection and default build flags**
+ AL2023 packages are built with compiler optimizations (`-O2`) enabled by default
+ AL2023 packages are built requiring `x86-64v2` for `x86-64` systems (`-march=x86-64-v2`), and Graviton 2 or higher for `aarch64` (`-march=armv8.2-a+crypto -mtune=neoverse-n1`).
+ AL2023 packages are built with auto-vectorization enabled (`-ftree-vectorize`).
+ AL2023 packages are built with Link Time Optimization (LTO) enabled.
+ AL2023 uses the updated versions of Rust, Clang/LLVM, and Go.

**Package selection and versions**
+ Select backports to major system components include several performance improvements for running on Amazon EC2 infrastructure, especially Graviton instances.
+ AL2023 is integrated with several AWS services and features. This includes the AWS CLI, SSM Agent, Amazon Kinesis Agent, and CloudFormation.
+ AL2023 uses Amazon Corretto as the Java Development Kit (JDK).
+ AL2023 provides database engines and programming language runtime updates to newer versions as they're released by upstream projects. Programming language runtimes with new versions are added when they're released.

**Deployment in a cloud environment**
+ The base AL2023 AMI and container images are frequently updated to support patching instance replacement.
+ Kernel updates are included in AL2023 AMI updates. This means that you don't need to use commands such as `yum update` and `reboot` to update your kernel.
+ In addition to the standard AL2023 AMI, a minimal AMI and container image is also available. Choose the minimal AMI to run an environment with the minimal number of packages that's required to run your service.
+ By default, AL2023 AMIs and containers are locked to a specific version of the package repositories. There's no auto-update when they're launched. This means that you're always in control of when you ingest any package update. You can always test in a beta/gamma environment before rolling out to production. If there's a problem, you can use the pre-validated rollback path.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
