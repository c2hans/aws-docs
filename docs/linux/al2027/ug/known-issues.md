---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/known-issues.html
---

# Known issues and preview limitations
<a name="known-issues"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

Review these known issues before you deploy AL2027 workloads.

**Topics**
+ [NVIDIA drivers](#known-issues-nvidia)
+ [On-premises VM images](#known-issues-vm-images)
+ [SSM Patch Manager](#known-issues-ssm-patch-manager)
+ [Attestable image examples](#known-issues-attestable-images)
+ [Reporting issues and feedback](#known-issues-feedback)

## NVIDIA drivers
<a name="known-issues-nvidia"></a>

NVIDIA drivers are not available in the initial preview release of AL2027. Follow the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html) for updates.

## On-premises VM images
<a name="known-issues-vm-images"></a>

AL2027 VM images for on-premises use (Hyper-V, KVM, and VMware) are not available in the initial preview release of AL2027. Follow the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html) for updates.

## SSM Patch Manager
<a name="known-issues-ssm-patch-manager"></a>

SSM Patch Manager patching operations will not succeed on AL2027 at this time. To receive updates, you can run `dnf update` commands manually. For more information, see [Updating AL2027](updating.md).

## Attestable image examples
<a name="known-issues-attestable-images"></a>

The Amazon Linux Attestable Image Examples repository, which provides recipes for building AMIs with cryptographic attestation support, does not yet include recipes for AL2027. For more information about Attestable Image recipes, see [Amazon Linux Kiwi Image Descriptions Examples](https://github.com/amazonlinux/kiwi-image-descriptions-examples) on GitHub.

## Reporting issues and feedback
<a name="known-issues-feedback"></a>

To report an issue, request a package, or share feedback on the AL2027 public preview, visit the [AL2027 repository](https://github.com/amazonlinux/amazon-linux-2027/issues) on GitHub.
