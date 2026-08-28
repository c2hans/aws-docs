---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/filesystem-slash-boot.html
---

# `/boot` (Kernel, initramfs, etc.)
<a name="filesystem-slash-boot"></a>

 By default, bootable AL2023 images are configured with `/boot` being on the root file system. The `/boot` path is only relevant for bootable images, so is unused in AL2023 container images.

 This directory is home to files needed for AL2023 to boot such as the Linux kernel and initramfs. The content of this directory should only be manipulated using the tools provided with the OS.

## `/boot/efi` (EFI System Partition)
<a name="filesystem-slash-boot-efi"></a>

 By default, bootable AL2023 images are configured with the EFI System partition being mounted at `/boot/efi`. This file system is managed by the OS and contains code and configuration critical to booting the system.

 This path is not relevant for container images.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
