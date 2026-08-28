---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2-kernel.html
---

# AL2023 kernel changes from AL2
<a name="compare-with-al2-kernel"></a>

AL2023 brings the 6.1 kernel, as well as many configuration changes to further optimize Amazon Linux for the cloud. For most users, these changes should be completely transparent.

## IPv4 TTL
<a name="ipv4-ttl"></a>

The TTL for IPv4 is configured via `sysctl`, with the default values being present in `/etc/sysctl.d/00-defaults.conf`. This value can be customized through the usual `sysctl` methods. For more information, see the `sysctl` `man` page.

 AL2 set the `net.ipv4.ip_default_ttl` value to to 255, while AL2023 sets it to 127. This brings Amazon Linux defaults in line with other major Linux distributions. It is not recommended to change this default without a demonstrated need to.

## Security focused kernel config changes
<a name="security-kernel-config-changes"></a>

| `CONFIG` option | AL2/4.14/aarch64 | AL2/4.14/x86\_64 | AL2/5.10/aarch64 | AL2/5.10/x86\_64 | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_BUG_ON_DATA_CORRUPTION`](kernel-hardening.md#CONFIG_BUG_ON_DATA_CORRUPTION)  |  n  |  y  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_DEFAULT_MMAP_MIN_ADDR`](kernel-hardening.md#CONFIG_DEFAULT_MMAP_MIN_ADDR)  |  4096  |  4096  |  4096  |  4096  |  65536  |  65536  |  65536  |  65536  |  65536  |  65536  |
|  [`CONFIG_DEVMEM`](#CONFIG_DEVMEM)  |  n  |  y  |  n  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DEVPORT`](#CONFIG_DEVPORT)  |  n  |  y  |  n  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_FORTIFY_SOURCE`](#CONFIG_FORTIFY_SOURCE)  |  n  |  y  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_HARDENED_USERCOPY_FALLBACK`](kernel-hardening.md#CONFIG_HARDENED_USERCOPY_FALLBACK)  | N/A | N/A |  y  |  y  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_INIT_ON_ALLOC_DEFAULT_ON`](kernel-hardening.md#CONFIG_INIT_ON_ALLOC_DEFAULT_ON)  | N/A | N/A |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_INIT_ON_FREE_DEFAULT_ON`](kernel-hardening.md#CONFIG_INIT_ON_FREE_DEFAULT_ON)  | N/A | N/A |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_IOMMU_DEFAULT_DMA_STRICT`](kernel-hardening.md#CONFIG_IOMMU_DEFAULT_DMA_STRICT)  | N/A | N/A | N/A | N/A |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LDISC_AUTOLOAD`](#CONFIG_LDISC_AUTOLOAD)  |  y  |  y  |  y  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_SCHED_CORE`](kernel-hardening.md#CONFIG_SCHED_CORE)  | N/A | N/A | N/A | N/A | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_SCHED_STACK_END_CHECK`](kernel-hardening.md#CONFIG_SCHED_STACK_END_CHECK)  |  n  |  y  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_DMESG_RESTRICT`](#CONFIG_SECURITY_DMESG_RESTRICT)  |  n  |  n  |  n  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_SELINUX_DISABLE`](#CONFIG_SECURITY_SELINUX_DISABLE)  |  y  |  y  |  y  |  y  |  n  |  n  | N/A | N/A | N/A | N/A |
|  [`CONFIG_SHUFFLE_PAGE_ALLOCATOR`](kernel-hardening.md#CONFIG_SHUFFLE_PAGE_ALLOCATOR)  | N/A | N/A |  y  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLAB_FREELIST_HARDENED`](kernel-hardening.md#CONFIG_SLAB_FREELIST_HARDENED)  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLAB_FREELIST_RANDOM`](kernel-hardening.md#CONFIG_SLAB_FREELIST_RANDOM)  |  n  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |

### x86-64 Specific Security focused kernel config changes
<a name="security-kernel-config-changes-x86-64-specific"></a>

| `CONFIG` option | AL2/4.14/x86\_64 | AL2/5.10/x86\_64 | AL2023/6.1/x86\_64 | AL2023/6.12/x86\_64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- |
|  [`CONFIG_AMD_IOMMU`](kernel-hardening.md#CONFIG_AMD_IOMMU)  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_AMD_IOMMU_V2`](kernel-hardening.md#CONFIG_AMD_IOMMU_V2)  |  m  |  m  |  y  | N/A | N/A |
|  [`CONFIG_RANDOMIZE_MEMORY`](kernel-hardening.md#CONFIG_RANDOMIZE_MEMORY)  | N/A |  y  |  y  |  y  |  y  |

### aarch64 (ARM/Graviton) Specific Security focused kernel config changes
<a name="security-kernel-config-changes-aarch64-specific"></a>

| `CONFIG` option | AL2/4.14/aarch64 | AL2/5.10/aarch64 | AL2023/6.1/aarch64 | AL2023/6.12/aarch64 | AL2023/6.18/aarch64 |
| --- | --- | --- | --- | --- | --- |
|  [`CONFIG_ARM64_PTR_AUTH`](kernel-hardening.md#CONFIG_ARM64_PTR_AUTH)  | N/A |  y  |  y  |  y  |  y  |
|  [`CONFIG_ARM64_PTR_AUTH_KERNEL`](kernel-hardening.md#CONFIG_ARM64_PTR_AUTH_KERNEL)  | N/A | N/A |  y  |  y  |  y  |
|  [`CONFIG_ARM64_SW_TTBR0_PAN`](kernel-hardening.md#CONFIG_ARM64_SW_TTBR0_PAN)  |  y  |  y  |  y  |  y  |  y  |

### `/dev/mem`, `/dev/kmem` and `/dev/port`
<a name="CONFIG_DEVMEM"></a>

 Amazon Linux 2023 disables `/dev/mem`, and `/dev/port` (`CONFIG_DEVMEM` and `CONFIG_DEVPORT`) completely, building on the restrictions already in place in AL2.

 The `/dev/kmem` code was completely removed from Linux in the 5.13 kernel, and while it was disabled in AL2, it is now not applicable to AL2023.

This option is one of the [Kernel Self Protection Project Recommended Settings](https://kspp.github.io/Recommended_Settings).

### `FORTIFY_SOURCE`
<a name="CONFIG_FORTIFY_SOURCE"></a>

 AL2023 enables `CONFIG_FORTIFY_SOURCE` on all supported architectures. This feature is a security hardening feature. Where the compiler can determine and validate the buffer sizes, this feature can detect buffer overflows in common string and memory functions.

This option is one of the [Kernel Self Protection Project Recommended Settings](https://kspp.github.io/Recommended_Settings).

### Line Discipline autoload (`CONFIG_LDISC_AUTOLOAD`)
<a name="CONFIG_LDISC_AUTOLOAD"></a>

 The AL2023 kernel will not automatically load line disciplines, such as by software using the `TIOCSETD` `ioctl`, unless the request comes from a process with the `CAP_SYS_MODULE` permissions.

This option is one of the [Kernel Self Protection Project Recommended Settings](https://kspp.github.io/Recommended_Settings).

### `dmesg` access for unprivileged users (`CONFIG_SECURITY_DMESG_RESTRICT`)
<a name="CONFIG_SECURITY_DMESG_RESTRICT"></a>

 By default, AL2023 does not allow unprivileged users access to `dmesg`.

This option is one of the [Kernel Self Protection Project Recommended Settings](https://kspp.github.io/Recommended_Settings).

### SELinux `selinuxfs` disable
<a name="CONFIG_SECURITY_SELINUX_DISABLE"></a>

 AL2023 disables the deprecated `CONFIG_SECURITY_SELINUX_DISABLE` kernel option, which enabled a runtime method of disabling SELinux prior to policy being loaded.

This option is one of the [Kernel Self Protection Project Recommended Settings](https://kspp.github.io/Recommended_Settings).

## Other kernel configuration changes
<a name="general-kernel-config-changes"></a>

| `CONFIG` option | AL2/4.14/aarch64 | AL2/4.14/x86\_64 | AL2/5.10/aarch64 | AL2/5.10/x86\_64 | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_HZ`](#CONFIG_HZ)  |  100  |  250  |  100  |  250  |  100  |  100  |  100  |  100  |  100  |  100  |
|  [`CONFIG_NR_CPUS`](#CONFIG_NR_CPUS)  |  4096  |  8192  |  4096  |  8192  |  4096  |  8192  |  4096  |  8192  |  4096  |  8192  |
|  [`CONFIG_PANIC_ON_OOPS`](#CONFIG_PANIC_ON_OOPS)  |  y  |  n  |  y  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_PANIC_ON_OOPS_VALUE`](#CONFIG_PANIC_ON_OOPS_VALUE)  |  1  |  0  |  1  |  0  |  1  |  1  |  1  |  1  | N/A | N/A |
|  [`CONFIG_PPP`](#CONFIG_PPP)  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_SLIP`](#CONFIG_SLIP)  |  m  |  m  |  m  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_XEN_PV`](#CONFIG_XEN_PV)  | N/A |  y  | N/A |  n  | N/A |  n  | N/A |  n  | N/A |  n  |

### CONFIG\_HZ
<a name="CONFIG_HZ"></a>

 AL2023 sets `CONFIG_HZ` to 100 on both `x86-64` and `aarch64` platforms.

### CONFIG\_NR\_CPUS
<a name="CONFIG_NR_CPUS"></a>

 AL2023 sets `CONFIG_NR_CPUS` to a number closer to the maximum number of CPU cores found in Amazon EC2.

### Panic on OOPS
<a name="CONFIG_PANIC_ON_OOPS"></a>

 The AL2023 kernel will panic when it oopses. This feature is equivalent to booting with `oops=panic` on the kernel command line.

 A kernel oops is where the kernel has detected an internal error which may affect the further reliability of the system.

### PPP and SLIP Support
<a name="CONFIG_PPP"></a>

 AL2023 does not support the SLIP protocol but can support PPP protocol in latest AL2023 kernels.

### Xen PV Guest Support
<a name="CONFIG_XEN_PV"></a>

 AL2023 does not support running as a Xen PV guest.

## Kernel Filesystem support
<a name="kernel-fs-changes"></a>

There have been several changes in the file systems that the kernel in AL2 will support mounting, along with changes in the partitioning schemes that the kernel will parse.

| `CONFIG` option | AL2/4.14/aarch64 | AL2/4.14/x86\_64 | AL2/5.10/aarch64 | AL2/5.10/x86\_64 | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_AFS_FS`](#CONFIG_AFS_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_AF_RXRPC`](#CONFIG_AF_RXRPC)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_BSD_DISKLABEL`](#CONFIG_BSD_DISKLABEL)  |  y  |  y  |  y  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_CRAMFS`](#CONFIG_CRAMFS)  |  m  |  m  |  m  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_CRAMFS_BLOCKDEV`](#CONFIG_CRAMFS_BLOCKDEV)  | N/A | N/A |  y  |  n  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_DM_CLONE`](#CONFIG_DM_CLONE)  | N/A | N/A |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DM_ERA`](#CONFIG_DM_ERA)  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DM_INTEGRITY`](#CONFIG_DM_INTEGRITY)  |  n  |  m  |  n  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_DM_LOG_WRITES`](#CONFIG_DM_LOG_WRITES)  |  n  |  n  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_DM_SWITCH`](#CONFIG_DM_SWITCH)  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DM_VERITY`](#CONFIG_DM_VERITY)  |  m  |  n  |  m  |  n  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_ECRYPT_FS`](#CONFIG_ECRYPT_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_EXFAT_FS`](#CONFIG_EXFAT_FS)  | N/A | N/A |  m  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_EXT2_FS`](#CONFIG_EXT2_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_EXT3_FS`](#CONFIG_EXT3_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  | N/A | N/A |
|  [`CONFIG_GFS2_FS`](#CONFIG_GFS2_FS)  |  m  |  m  |  m  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_HFSPLUS_FS`](#CONFIG_HFSPLUS_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_HFS_FS`](#CONFIG_HFS_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_JFS_FS`](#CONFIG_JFS_FS)  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LDM_PARTITION`](#CONFIG_LDM_PARTITION)  |  n  |  y  |  n  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_MAC_PARTITION`](#CONFIG_MAC_PARTITION)  |  n  |  y  |  n  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_NFS_V2`](#CONFIG_NFS_V2)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_NTFS_FS`](#CONFIG_NTFS_FS)  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_ROMFS_FS`](#CONFIG_ROMFS_FS)  |  n  |  m  |  n  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_SOLARIS_X86_PARTITION`](#CONFIG_SOLARIS_X86_PARTITION)  |  n  |  y  |  n  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_SQUASHFS_ZSTD`](#CONFIG_SQUASHFS_ZSTD)  |  n  |  y  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SUN_PARTITION`](#CONFIG_SUN_PARTITION)  |  n  |  y  |  n  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |

### Andrew File System support (AFS)
<a name="CONFIG_AFS_FS"></a>

The kernel is no longer built with support for the `afs` file system. AL2 did not ship with user-space support for `afs`.

### cramfs support
<a name="CONFIG_CRAMFS"></a>

 The kernel is no longer built with support for the `cramfs` file system. The successor in AL2023 is the `squashfs` file system.

### BSD disklabel support
<a name="CONFIG_BSD_DISKLABEL"></a>

 The kernel is no longer built with support for BSD disk labels. If reading volumes with BSD disk labels is required, various BSDs can be launched.

### Device Mapper changes
<a name="device-mapper"></a>

 There have been several changes to the Device Mapper targets configured in the AL2023 kernel.

### eCryptFs support
<a name="CONFIG_ECRYPT_FS"></a>

 The `ecryptfs` file system has been deprecated in Amazon Linux. The user-space components of `ecryptfs` were present in AL1, removed in AL2, and AL2023 no longer builds the kernel with `ecryptfs` support.

### exFAT
<a name="CONFIG_EXFAT_FS"></a>

 Support for the `exFAT` file system was added in the 5.10 kernel in AL2. It was not present at AL2 launch with a 4.14 kernel. AL2023 continues to support the `exFAT` file system.

### The ext2, ext3, and ext4 file systems
<a name="ext4"></a>

 AL2023 ships with the `CONFIG_EXT4_USE_FOR_EXT2` option, which means that the `ext4` file system code will be used to read legacy `ext2` file systems.

### CONFIG\_GFS2\_FS
<a name="CONFIG_GFS2_FS"></a>

 The kernel is no longer built with CONFIG\_GFS2\_FS.

### Apple Extended HFS file system support (HFS\+)
<a name="CONFIG_HFSPLUS_FS"></a>

 In AL2, only the `x86-64` kernels were built with the `hfsplus` file system support. The AL2 5.15 kernel does not include `hfsplus` support on any architecture. In AL2023, we complete the deprecation of `hfsplus` support in Amazon Linux.

### HFS file system support
<a name="CONFIG_HFS_FS"></a>

 In AL2, only the `x86-64` kernels were built with the `hfs` file system support. The AL2 5.15 kernel does not include `hfs` support on any architecture. In AL2023, we complete the deprecation of `hfs` support in Amazon Linux.

### JFS file system support
<a name="CONFIG_JFS_FS"></a>

 Older AL2 `x86-64` kernels were built with `jfs` file system support. The AL2 5.15 kernel does not include `jfs` support on any architecture. Neither AL1 or AL2 shipped with JFS userspace. In AL2023, we complete the deprecation of `jfs` support in Amazon Linux.

 The upstream Linux kernel is [considering the removal of `JFS`](https://lore.kernel.org/lkml/Y8DvK281ii6yPRcW@infradead.org/). Therefore, if you have data on a `JFS` file system, you should migrate it to another file system. In 2024, `JFS` was removed from all current Amazon Linux kernels.

### Windows Logical Disk Manager (Dynamic Disk) support (`CONFIG_LDM_PARTITION`)
<a name="CONFIG_LDM_PARTITION"></a>

 AL2023 no longer supports Windows 2000, Windows XP, or Windows Vista *dynamic disks* with MS-DOS style partitions. This code did not ever support the newer GPT based dynamic disks introduced with Windows Vista.

### Macintosh partition map support
<a name="CONFIG_MAC_PARTITION"></a>

 AL2023 no longer supports the classic Macintosh partition map. Modern macOS versions will create modern GPT partition tables by default over this older type.

### NFSv2 support
<a name="CONFIG_NFS_V2"></a>

 AL2023 no longer supports NFSv2, but continues to support NFSv3, NFSv4, NFSv4.1, and NFSv4.2. We recommend that you migrate to NFSv3 or newer.

### NTFS (`CONFIG_NTFS_FS`)
<a name="CONFIG_NTFS_FS"></a>

 The `ntfs3` code replaced `ntfs` for accessing NTFS file systems on Amazon Linux as of the 5.10 kernel in AL2. AL2023 no longer includes the `ntfs` code, and relies exclusively on the `ntfs3` code for accessing NTFS file systems.

### romfs file system
<a name="CONFIG_ROMFS_FS"></a>

 The `squashfs` file system is the successor of the `romfs` file system in Amazon Linux, and the AL2023 kernel is no longer built with support for `romfs`.

### Solaris x86 hard disk partition format
<a name="CONFIG_SOLARIS_X86_PARTITION"></a>

 AL2023 no longer supports the Solaris x86 hard disk partition format.

### `squashfs` zstd compression
<a name="CONFIG_SQUASHFS_ZSTD"></a>

 AL2023 adds support for zstd compressed `squashfs` file systems on all supported architectures.

### Sun partition table support
<a name="CONFIG_SUN_PARTITION"></a>

 AL2023 no longer includes support for the Sun partition table format (`CONFIG_SUN_PARTITION`).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
