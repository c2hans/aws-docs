---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ami-support-policy.html
---

# Amazon SageMaker HyperPod AMI support policy

Amazon SageMaker HyperPod provides pre-built Amazon Machine Images (AMIs) optimized for distributed training and inference workloads. This page details the support policy for HyperPod AMI releases.

## Scope
<a name="sagemaker-hyperpod-ami-support-scope"></a>

This support policy applies to the following HyperPod AMI components:
+ EFA (Elastic Fabric Adapter)
+ NVIDIA Driver
+ NCCL (aws-ofi-nccl)
+ CUDA
+ OS Kernel

The policy defines the window during which HyperPod will ship security patches for a given AMI version.

## Support policy
<a name="sagemaker-hyperpod-ami-support-policy-windows"></a>

The following table outlines the release schedule for HyperPod AMI versions and their planned support timelines. AWS provides ongoing security patches for supported AMI versions. In some cases, an AMI version might need to be designated end of support earlier than originally planned if:

1. security issues cannot be addressed while maintaining semantic versioning guidelines,

1. any of the core dependencies (for example, NVIDIA driver, CUDA, OS kernel) reach end-of-life, or

1. upstream vendors discontinue support for a bundled component.

| Version | Description | Support window |
| --- | --- | --- |
| Major | HyperPod AMI major version releases involve upgrading core components (EFA, NVIDIA driver, NCCL, CUDA, OS kernel) to new major versions. These releases might introduce breaking changes, such as NVIDIA driver changes from 570.x to 580.x, that require workload validation. Major versions are denoted by the first number in the version string (for example, 1.0, 2.0, 3.0). | 12 months |
| Minor | HyperPod AMI minor version releases include upgrading core components to newer compatible minor versions within the same major version. Minor versions are denoted by the second number in the version string (for example, 1.1, 1.2, 2.1). | 6 months |
| Patch | HyperPod AMI patch version releases include security fixes and bug fixes for the supported components. Patch releases do not change the major or minor versions of any bundled component. Patch versions are denoted by the third number in the version string (for example, 1.1.1, 1.2.1, 2.1.3). | Until a new patch version is released |

## Vulnerability management
<a name="sagemaker-hyperpod-ami-vulnerability-management"></a>

AWS continuously monitors supported HyperPod AMI versions for security vulnerabilities affecting the in-scope components (EFA, NVIDIA driver, NCCL, CUDA, OS kernel). When vulnerabilities are detected and a fix is available that satisfies the semantic versioning constraints for the given AMI version, AWS will release a patch update to remediate the issue.

## HyperPod EKS
<a name="sagemaker-hyperpod-ami-support-eks"></a>

HyperPod EKS AMI versions are tracked separately for each Kubernetes minor version and CPU architecture. The same AMI version number can bundle different component versions on different Kubernetes versions, and some AMI version lines are available only on specific Kubernetes versions. Before you create or update a cluster, check the AMI versions available for your Kubernetes version and architecture.

### Major versions support policy
<a name="sagemaker-hyperpod-ami-support-eks-major"></a>

| AMI version | Supported until |
| --- | --- |
| 3.x.x | September 2027 |
| 2.x.x | July 2027 |
| 1.x.x | January 2027 |

### AMI version list
<a name="sagemaker-hyperpod-ami-support-eks-version-list"></a>

The following tabs list the supported HyperPod EKS AMI versions for each Kubernetes version, with the latest patch for each CPU architecture. When creating or updating clusters, choose a supported AMI version from the tab for your Kubernetes version. Patch numbers are tracked separately for x86\_64 and arm64, so the latest patch can differ between the two. AMI versions are numbered separately for each Kubernetes version. Kubernetes 1.36 AMIs use their own version track, which started at 1.0.0 when Kubernetes 1.36 support was released. The **Supported package versions** column lists the in-scope components covered by this support policy; for the full list of bundled packages in each release, see the Amazon SageMaker HyperPod AMI release notes for Amazon EKS in [SageMaker HyperPod AMI releases for Amazon EKS](sagemaker-hyperpod-release-ami-eks.md).

------
#### [ Kubernetes 1.36 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.36.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 1.5.x | 1.5.3 | 1.5.1 |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.12.x   | November 5, 2026 |
| 1.4.x | 1.4.6 | 1.4.2 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.12.x   | September 29, 2026 |
| 1.3.x | 1.3.0 | 1.3.0 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 11, 2026 |
| 1.2.x | 1.2.0 | 1.2.0 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 1.1.x | 1.1.0 | 1.1.0 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 1.0.x | 1.0.2 | 1.0.2 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 24, 2026 |

------
#### [ Kubernetes 1.35 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.35.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 2.3.x | 2.3.3 | 2.3.1 |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.12.x   | November 5, 2026 |
| 2.2.x | 2.2.8 | 2.2.3 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.12.x   | September 29, 2026 |
| 2.1.x | 2.1.4 | 2.1.3 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 2.0.x | 2.0.5 | 2.0.3 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 23, 2026 |
| 1.4.x | 1.4.6 | 1.4.1 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 6, 2026 |
| 1.3.x | 1.3.6 | 1.3.1 |  +  NVIDIA Driver: 580.167.08 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 24, 2026 |
| 1.2.x | 1.2.7 | 1.2.1 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 18, 2026 |
| 1.1.x | 1.1.11 | 1.1.4 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | April 23, 2026 |

------
#### [ Kubernetes 1.34 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.34.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 2.3.x | 2.3.3 | 2.3.1 |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.12.x   | November 5, 2026 |
| 2.2.x | 2.2.7 | 2.2.4 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.12.x   | September 29, 2026 |
| 2.1.x | 2.1.4 | 2.1.3 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 2.0.x | 2.0.5 | 2.0.3 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 23, 2026 |
| 1.4.x | 1.4.6 | 1.4.4 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 6, 2026 |
| 1.3.x | 1.3.6 | 1.3.3 |  +  NVIDIA Driver: 580.167.08 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 24, 2026 |
| 1.2.x | 1.2.6 | 1.2.3 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 18, 2026 |
| 1.1.x | 1.1.10 | 1.1.5 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | April 23, 2026 |
| 1.0.x | 1.0.3 | 1.0.3 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.45.0 (arm64: 1.43.3) <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | January 25, 2026 |

------
#### [ Kubernetes 1.33 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.33.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 4.0.x | 4.0.0 | Not applicable |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.12.x   | November 20, 2026 |
| 2.1.x | Not applicable | 2.1.1 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 2.0.x | 2.0.5 | 2.0.5 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 23, 2026 |
| 1.4.x | 1.4.6 | 1.4.5 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 6, 2026 |
| 1.3.x | 1.3.6 | 1.3.5 |  +  NVIDIA Driver: 580.167.08 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 24, 2026 |
| 1.2.x | 1.2.5 | 1.2.5 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 18, 2026 |
| 1.1.x | 1.1.10 | 1.1.8 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | April 23, 2026 |
| 1.0.x | 1.0.3 | 1.0.3 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.45.0 (arm64: 1.43.3) <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | January 25, 2026 |

------
#### [ Kubernetes 1.32 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.32.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 2.3.x | 2.3.3 | 2.3.2 |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.12.x   | November 5, 2026 |
| 2.2.x | 2.2.7 | 2.2.6 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.12.x   | September 29, 2026 |
| 2.1.x | 2.1.3 | 2.1.3 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 2.0.x | 2.0.5 | 2.0.5 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 23, 2026 |
| 1.4.x | 1.4.6 | 1.4.5 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 6, 2026 |
| 1.3.x | 1.3.6 | 1.3.4 |  +  NVIDIA Driver: 580.167.08 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 24, 2026 |
| 1.2.x | 1.2.6 | 1.2.5 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 18, 2026 |
| 1.1.x | 1.1.10 | 1.1.8 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | April 23, 2026 |
| 1.0.x | 1.0.3 | 1.0.3 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.45.0 (arm64: 1.43.3) <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | January 25, 2026 |

------
#### [ Kubernetes 1.31 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.31.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 2.3.x | 2.3.3 | 2.3.3 |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.12.x   | November 5, 2026 |
| 2.2.x | 2.2.7 | 2.2.7 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.12.x   | September 29, 2026 |
| 2.1.x | 2.1.3 | 2.1.4 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 2.0.x | 2.0.5 | 2.0.6 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 23, 2026 |
| 1.4.x | 1.4.6 | 1.4.6 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 6, 2026 |
| 1.3.x | 1.3.6 | 1.3.6 |  +  NVIDIA Driver: 580.167.08 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 24, 2026 |
| 1.2.x | 1.2.6 | 1.2.5 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 18, 2026 |
| 1.1.x | 1.1.9 | 1.1.9 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | April 23, 2026 |
| 1.0.x | 1.0.3 | 1.0.3 |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.45.0 (arm64: 1.43.3) <br />+  OS Kernel: 6.1.x (arm64: 6.12.x)   | January 25, 2026 |

------
#### [ Kubernetes 1.30 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.30.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 2.2.x | 2.2.0 | Not applicable |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.12.x   | September 29, 2026 |
| 2.1.x | 2.1.4 | Not applicable |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.49.0 <br />+  OS Kernel: 6.12.x   | September 2, 2026 |
| 2.0.x | 2.0.6 | Not applicable |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 23, 2026 |
| 1.4.x | 1.4.6 | Not applicable |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | July 6, 2026 |
| 1.3.x | 1.3.14 | Not applicable |  +  NVIDIA Driver: 580.167.08 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 24, 2026 |
| 1.2.x | 1.2.15 | Not applicable |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.12.x   | June 18, 2026 |
| 1.1.x | 1.1.20 | Not applicable |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x   | April 23, 2026 |
| 1.0.x | 1.0.3 | Not applicable |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.45.0 <br />+  OS Kernel: 6.1.x   | January 25, 2026 |

------
#### [ Kubernetes 1.29 ]

The following table lists the AMI versions and supported package versions for Kubernetes 1.29.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 1.2.x | 1.2.16 | Not applicable |  +  NVIDIA Driver: 580.150 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x   | June 18, 2026 |
| 1.1.x | 1.1.19 | Not applicable |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.1.x   | April 23, 2026 |
| 1.0.x | 1.0.3 | Not applicable |  +  NVIDIA Driver: 580.126.09 <br />+  CUDA Toolkit: 12.8 <br />+  EFA Installer: 1.45.0 <br />+  OS Kernel: 6.1.x   | January 25, 2026 |

------

## HyperPod Slurm
<a name="sagemaker-hyperpod-ami-support-slurm"></a>

HyperPod Slurm AMI versions are numbered separately for each operating system release and tracked separately for each CPU architecture. Before you create or update a cluster, check the AMI versions available for your operating system and architecture.

### AMI version list
<a name="sagemaker-hyperpod-ami-support-slurm-version-list"></a>

The following table lists the supported HyperPod Slurm AMI versions for Ubuntu 22.04, with the latest patch for each CPU architecture.

| AMI version | Latest patch x86\_64 | Latest patch arm64 | Supported package versions | First released |
| --- | --- | --- | --- | --- |
| 2.3.x | 2.3.1 | 2.3.1 |  +  NVIDIA Driver: 595.112.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.51.0 <br />+  OS Kernel: 6.8.x <br />+  Slurm: 25.11   | November 5, 2026 |
| 2.2.x | 2.2.3 | 2.2.3 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.50.0 <br />+  OS Kernel: 6.8.x <br />+  Slurm: 25.11   | September 29, 2026 |
| 2.1.x | 2.1.3 | 2.1.3 |  +  NVIDIA Driver: 595.91.07 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.8.x <br />+  Slurm: 25.11   | August 17, 2026 |
| 2.0.x | 2.0.1 | 2.0.1 |  +  NVIDIA Driver: 595.71.05 <br />+  CUDA Toolkit: 13.2 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.8.x   | July 23, 2026 |
| 1.1.x | Not applicable | 1.1.1 |  +  NVIDIA Driver: 580.159.04 <br />+  CUDA Toolkit: 13.0 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.8.x   | July 6, 2026 |
| 1.0.x | 1.0.3 | 1.0.1 |  +  NVIDIA Driver: 580.159.04 (arm64: 580.167.08) <br />+  CUDA Toolkit: 13.0 <br />+  EFA Installer: 1.47.0 <br />+  OS Kernel: 6.8.x   | June 24, 2026 |

## Frequently asked questions
<a name="sagemaker-hyperpod-ami-support-faq"></a>

**Can I still use an older AMI after it is no longer supported?**

Older AMIs remain available on existing HyperPod clusters after they reach end of support. However, you cannot create a new cluster using an end-of-support AMI. We strongly recommend upgrading to a supported AMI version, which continues to receive security patches. You are responsible for managing any vulnerabilities that might arise from running an AMI version no longer supported by AWS.

**What happens when a new patch version is released?**

When a new patch version is released, the previous patch version within the same minor version reaches end of support. If auto-patching is enabled, HyperPod applies patch updates automatically without disrupting running workloads.

**How will I be notified about new AMI versions or end-of-support dates?**

AWS will notify customers through Personal Health Dashboard (PHD) notifications and the HyperPod console when AMI updates are available or when their current AMI version is approaching end of support.

**Does this policy apply to custom AMIs?**

No. This support policy applies only to AWS-vended HyperPod AMIs. If you use a custom AMI, you are responsible for maintaining and patching all components. For more information about custom AMIs, see [Custom Amazon Machine Images (AMIs) for SageMaker HyperPod clusters](hyperpod-custom-ami-support.md).
