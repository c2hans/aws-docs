---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem-slash-boot.html
---

# `/boot` (kernel, initramfs, bootloader)
<a name="filesystem-slash-boot"></a>

Bootable AL2027 images are configured with `/boot` on the root file system. It holds the files needed to boot, such as the Linux kernel and the initramfs. Change the content of this directory only through the tools provided with the OS. The `/boot` path is only relevant for bootable images; it is unused in AL2027 container images.

## `/boot/efi` (EFI System Partition)
<a name="filesystem-slash-boot-efi"></a>

Bootable AL2027 images mount the EFI System partition at `/boot/efi`. AL2027 AMIs boot with UEFI on arm64 and UEFI-preferred on x86\_64, so this file system contains code and configuration critical to booting the system. It is managed by the OS. This path is not relevant for container images.
