---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al1-kernel.html
---

# AL2023 kernel changes from Amazon Linux 1 (AL1)
<a name="compare-with-al1-kernel"></a>

## Kernel Live Patching
<a name="al1-kernel-livepatch"></a>

 Both AL2023 and AL2 add support for kernel live-patching functionality. This allows you to patch critical and important security vulnerabilities in the Linux kernel without reboot or downtime. For more information, see [Kernel Live Patching on AL2023](live-patching.md).

## Kernel file system support
<a name="al1-kernel-fs-changes"></a>

There have been several changes in the file systems that the kernel in AL1 will support mounting, along with changes in the partitioning schemes that the kernel will parse.

| `CONFIG` option | AL1/4.14/x86\_64 | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_AFS_FS`](compare-with-al2-kernel.md#CONFIG_AFS_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_AF_RXRPC`](compare-with-al2-kernel.md#CONFIG_AF_RXRPC)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_BSD_DISKLABEL`](compare-with-al2-kernel.md#CONFIG_BSD_DISKLABEL)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_CRAMFS`](compare-with-al2-kernel.md#CONFIG_CRAMFS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_CRAMFS_BLOCKDEV`](compare-with-al2-kernel.md#CONFIG_CRAMFS_BLOCKDEV)  | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_DM_CLONE`](compare-with-al2-kernel.md#CONFIG_DM_CLONE)  | N/A |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DM_ERA`](compare-with-al2-kernel.md#CONFIG_DM_ERA)  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DM_INTEGRITY`](compare-with-al2-kernel.md#CONFIG_DM_INTEGRITY)  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_DM_LOG_WRITES`](compare-with-al2-kernel.md#CONFIG_DM_LOG_WRITES)  |  n  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_DM_SWITCH`](compare-with-al2-kernel.md#CONFIG_DM_SWITCH)  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DM_VERITY`](compare-with-al2-kernel.md#CONFIG_DM_VERITY)  |  n  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_ECRYPT_FS`](compare-with-al2-kernel.md#CONFIG_ECRYPT_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_EXFAT_FS`](compare-with-al2-kernel.md#CONFIG_EXFAT_FS)  | N/A |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_EXT2_FS`](compare-with-al2-kernel.md#CONFIG_EXT2_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_EXT3_FS`](compare-with-al2-kernel.md#CONFIG_EXT3_FS)  |  m  |  n  |  n  |  n  |  n  | N/A | N/A |
|  [`CONFIG_GFS2_FS`](compare-with-al2-kernel.md#CONFIG_GFS2_FS)  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_HFSPLUS_FS`](compare-with-al2-kernel.md#CONFIG_HFSPLUS_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_HFS_FS`](compare-with-al2-kernel.md#CONFIG_HFS_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_JFS_FS`](compare-with-al2-kernel.md#CONFIG_JFS_FS)  |  n  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LDM_PARTITION`](compare-with-al2-kernel.md#CONFIG_LDM_PARTITION)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_MAC_PARTITION`](compare-with-al2-kernel.md#CONFIG_MAC_PARTITION)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_NFS_V2`](compare-with-al2-kernel.md#CONFIG_NFS_V2)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_NTFS_FS`](compare-with-al2-kernel.md#CONFIG_NTFS_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_ROMFS_FS`](compare-with-al2-kernel.md#CONFIG_ROMFS_FS)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_SOLARIS_X86_PARTITION`](compare-with-al2-kernel.md#CONFIG_SOLARIS_X86_PARTITION)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_SQUASHFS_ZSTD`](compare-with-al2-kernel.md#CONFIG_SQUASHFS_ZSTD)  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SUN_PARTITION`](compare-with-al2-kernel.md#CONFIG_SUN_PARTITION)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |

## Security focused kernel config changes
<a name="al1-security-kernel-config-changes"></a>

| `CONFIG` option | AL1/4.14/x86\_64 | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_BUG_ON_DATA_CORRUPTION`](kernel-hardening.md#CONFIG_BUG_ON_DATA_CORRUPTION)  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_DEFAULT_MMAP_MIN_ADDR`](kernel-hardening.md#CONFIG_DEFAULT_MMAP_MIN_ADDR)  |  4096  |  65536  |  65536  |  65536  |  65536  |  65536  |  65536  |
|  [`CONFIG_DEVMEM`](compare-with-al2-kernel.md#CONFIG_DEVMEM)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DEVPORT`](compare-with-al2-kernel.md#CONFIG_DEVPORT)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_FORTIFY_SOURCE`](compare-with-al2-kernel.md#CONFIG_FORTIFY_SOURCE)  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_HARDENED_USERCOPY_FALLBACK`](kernel-hardening.md#CONFIG_HARDENED_USERCOPY_FALLBACK)  | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_INIT_ON_ALLOC_DEFAULT_ON`](kernel-hardening.md#CONFIG_INIT_ON_ALLOC_DEFAULT_ON)  | N/A |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_INIT_ON_FREE_DEFAULT_ON`](kernel-hardening.md#CONFIG_INIT_ON_FREE_DEFAULT_ON)  | N/A |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_IOMMU_DEFAULT_DMA_STRICT`](kernel-hardening.md#CONFIG_IOMMU_DEFAULT_DMA_STRICT)  | N/A |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LDISC_AUTOLOAD`](compare-with-al2-kernel.md#CONFIG_LDISC_AUTOLOAD)  |  y  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_SCHED_CORE`](kernel-hardening.md#CONFIG_SCHED_CORE)  | N/A | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_SCHED_STACK_END_CHECK`](kernel-hardening.md#CONFIG_SCHED_STACK_END_CHECK)  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_DMESG_RESTRICT`](compare-with-al2-kernel.md#CONFIG_SECURITY_DMESG_RESTRICT)  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_SELINUX_DISABLE`](compare-with-al2-kernel.md#CONFIG_SECURITY_SELINUX_DISABLE)  |  y  |  n  |  n  | N/A | N/A | N/A | N/A |
|  [`CONFIG_SHUFFLE_PAGE_ALLOCATOR`](kernel-hardening.md#CONFIG_SHUFFLE_PAGE_ALLOCATOR)  | N/A |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLAB_FREELIST_HARDENED`](kernel-hardening.md#CONFIG_SLAB_FREELIST_HARDENED)  |  y  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLAB_FREELIST_RANDOM`](kernel-hardening.md#CONFIG_SLAB_FREELIST_RANDOM)  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |

## Other kernel configuration changes
<a name="al1-general-kernel-config-changes"></a>

| `CONFIG` option | AL1/4.14/x86\_64 | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_HZ`](compare-with-al2-kernel.md#CONFIG_HZ)  |  250  |  100  |  100  |  100  |  100  |  100  |  100  |
|  [`CONFIG_NR_CPUS`](compare-with-al2-kernel.md#CONFIG_NR_CPUS)  |  8192  |  4096  |  8192  |  4096  |  8192  |  4096  |  8192  |
|  [`CONFIG_PANIC_ON_OOPS`](compare-with-al2-kernel.md#CONFIG_PANIC_ON_OOPS)  |  n  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_PANIC_ON_OOPS_VALUE`](compare-with-al2-kernel.md#CONFIG_PANIC_ON_OOPS_VALUE)  |  0  |  1  |  1  |  1  |  1  | N/A | N/A |
|  [`CONFIG_PPP`](compare-with-al2-kernel.md#CONFIG_PPP)  |  m  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_SLIP`](compare-with-al2-kernel.md#CONFIG_SLIP)  |  m  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_XEN_PV`](compare-with-al2-kernel.md#CONFIG_XEN_PV)  |  y  | N/A |  n  | N/A |  n  | N/A |  n  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
