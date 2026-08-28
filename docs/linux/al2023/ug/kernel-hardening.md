---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/kernel-hardening.html
---

# AL2023 Kernel Hardening
<a name="kernel-hardening"></a>

 The 6.1 Linux kernel in AL2023 is configured and built with several hardening options and features.

## Kernel Hardening options (architecture independent)
<a name="kernel-hardening-common"></a>

| `CONFIG` option | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_ACPI_CUSTOM_METHOD`](#CONFIG_ACPI_CUSTOM_METHOD)  |  n  |  n  | N/A | N/A | N/A | N/A |
|  [`CONFIG_BINFMT_MISC`](#CONFIG_BINFMT_MISC)  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_BUG`](#CONFIG_BUG)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_BUG_ON_DATA_CORRUPTION`](#CONFIG_BUG_ON_DATA_CORRUPTION)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_CFI_CLANG`](#CONFIG_CFI_CLANG)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_CFI_PERMISSIVE`](#CONFIG_CFI_PERMISSIVE)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_COMPAT`](#CONFIG_COMPAT)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_COMPAT_BRK`](#CONFIG_COMPAT_BRK)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_COMPAT_VDSO`](#CONFIG_COMPAT_VDSO)  | N/A |  n  | N/A |  n  | N/A |  n  |
|  [`CONFIG_DEBUG_CREDENTIALS`](#CONFIG_DEBUG_CREDENTIALS)  |  n  |  n  | N/A | N/A | N/A | N/A |
|  [`CONFIG_DEBUG_LIST`](#CONFIG_DEBUG_LIST)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_DEBUG_NOTIFIERS`](#CONFIG_DEBUG_NOTIFIERS)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DEBUG_SG`](#CONFIG_DEBUG_SG)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DEBUG_VIRTUAL`](#CONFIG_DEBUG_VIRTUAL)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DEBUG_WX`](#CONFIG_DEBUG_WX)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_DEFAULT_MMAP_MIN_ADDR`](#CONFIG_DEFAULT_MMAP_MIN_ADDR)  |  65536  |  65536  |  65536  |  65536  |  65536  |  65536  |
|  [`CONFIG_DEVKMEM`](compare-with-al2-kernel.md#CONFIG_DEVKMEM)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_DEVMEM`](compare-with-al2-kernel.md#CONFIG_DEVMEM)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_EFI_DISABLE_PCI_DMA`](#CONFIG_EFI_DISABLE_PCI_DMA)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_FORTIFY_SOURCE`](compare-with-al2-kernel.md#CONFIG_FORTIFY_SOURCE)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_HARDENED_USERCOPY`](#CONFIG_HARDENED_USERCOPY)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_HARDENED_USERCOPY_FALLBACK`](#CONFIG_HARDENED_USERCOPY_FALLBACK)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_HARDENED_USERCOPY_PAGESPAN`](#CONFIG_HARDENED_USERCOPY_PAGESPAN)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_HIBERNATION`](#CONFIG_HIBERNATION)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_HW_RANDOM_TPM`](#CONFIG_HW_RANDOM_TPM)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_INET_DIAG`](#CONFIG_INET_DIAG)  |  m  |  m  |  m  |  m  |  m  |  m  |
|  [`CONFIG_INIT_ON_ALLOC_DEFAULT_ON`](#CONFIG_INIT_ON_ALLOC_DEFAULT_ON)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_INIT_ON_FREE_DEFAULT_ON`](#CONFIG_INIT_ON_FREE_DEFAULT_ON)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_INIT_STACK_ALL_ZERO`](#CONFIG_INIT_STACK_ALL_ZERO)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_IOMMU_DEFAULT_DMA_STRICT`](#CONFIG_IOMMU_DEFAULT_DMA_STRICT)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_IOMMU_SUPPORT`](#CONFIG_IOMMU_SUPPORT)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_IO_STRICT_DEVMEM`](compare-with-al2-kernel.md#CONFIG_IO_STRICT_DEVMEM)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_KEXEC`](#CONFIG_KEXEC)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_KFENCE`](#CONFIG_KFENCE)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LDISC_AUTOLOAD`](compare-with-al2-kernel.md#CONFIG_LDISC_AUTOLOAD)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LEGACY_PTYS`](#CONFIG_LEGACY_PTYS)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_LOCK_DOWN_KERNEL_FORCE_CONFIDENTIALITY`](#CONFIG_LOCK_DOWN_KERNEL_FORCE_CONFIDENTIALITY)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_MODULES`](#CONFIG_MODULES)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_MODULE_SIG`](#CONFIG_MODULE_SIG)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_MODULE_SIG_ALL`](#CONFIG_MODULE_SIG_ALL)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_MODULE_SIG_FORCE`](#CONFIG_MODULE_SIG_FORCE)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_MODULE_SIG_HASH`](#CONFIG_MODULE_SIG_HASH)  |  sha512  |  sha512  |  sha512  |  sha512  |  sha512  |  sha512  |
|  [`CONFIG_MODULE_SIG_KEY`](#CONFIG_MODULE_SIG_KEY)  |  certs/signing\_key.pem  |  certs/signing\_key.pem  |  certs/signing\_key.pem  |  certs/signing\_key.pem  |  certs/signing\_key.pem  |  certs/signing\_key.pem  |
|  [`CONFIG_MODULE_SIG_SHA512`](#CONFIG_MODULE_SIG_SHA512)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_PAGE_POISONING`](#CONFIG_PAGE_POISONING)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_PAGE_POISONING_NO_SANITY`](#CONFIG_PAGE_POISONING_NO_SANITY)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_PAGE_POISONING_ZERO`](#CONFIG_PAGE_POISONING_ZERO)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_PANIC_ON_OOPS`](compare-with-al2-kernel.md#CONFIG_PANIC_ON_OOPS)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_PANIC_TIMEOUT`](#CONFIG_PANIC_TIMEOUT)  |  0  |  0  |  0  |  0  |  0  |  0  |
|  [`CONFIG_PROC_KCORE`](#CONFIG_PROC_KCORE)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT`](#CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_RANDOM_TRUST_BOOTLOADER`](#CONFIG_RANDOM_TRUST_BOOTLOADER)  |  y  |  y  | N/A | N/A | N/A | N/A |
|  [`CONFIG_RANDOM_TRUST_CPU`](#CONFIG_RANDOM_TRUST_CPU)  |  y  |  y  | N/A | N/A | N/A | N/A |
|  [`CONFIG_REFCOUNT_FULL`](#CONFIG_REFCOUNT_FULL)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_SCHED_CORE`](#CONFIG_SCHED_CORE)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_SCHED_STACK_END_CHECK`](#CONFIG_SCHED_STACK_END_CHECK)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECCOMP`](#CONFIG_SECCOMP)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECCOMP_FILTER`](#CONFIG_SECCOMP_FILTER)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY`](#CONFIG_SECURITY)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_DMESG_RESTRICT`](compare-with-al2-kernel.md#CONFIG_SECURITY_DMESG_RESTRICT)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_LANDLOCK`](#CONFIG_SECURITY_LANDLOCK)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_LOCKDOWN_LSM`](#CONFIG_SECURITY_LOCKDOWN_LSM)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_LOCKDOWN_LSM_EARLY`](#CONFIG_SECURITY_LOCKDOWN_LSM_EARLY)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_SELINUX_BOOTPARAM`](#CONFIG_SECURITY_SELINUX_BOOTPARAM)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_SELINUX_DEVELOP`](#CONFIG_SECURITY_SELINUX_DEVELOP)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SECURITY_SELINUX_DISABLE`](compare-with-al2-kernel.md#CONFIG_SECURITY_SELINUX_DISABLE)  |  n  |  n  | N/A | N/A | N/A | N/A |
|  [`CONFIG_SECURITY_WRITABLE_HOOKS`](#CONFIG_SECURITY_WRITABLE_HOOKS)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_SECURITY_YAMA`](#CONFIG_SECURITY_YAMA)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SHUFFLE_PAGE_ALLOCATOR`](#CONFIG_SHUFFLE_PAGE_ALLOCATOR)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLAB_FREELIST_HARDENED`](#CONFIG_SLAB_FREELIST_HARDENED)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLAB_FREELIST_RANDOM`](#CONFIG_SLAB_FREELIST_RANDOM)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SLUB_DEBUG`](#CONFIG_SLUB_DEBUG)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_STACKPROTECTOR`](#CONFIG_STACKPROTECTOR)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_STACKPROTECTOR_STRONG`](#CONFIG_STACKPROTECTOR_STRONG)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_STATIC_USERMODEHELPER`](#CONFIG_STATIC_USERMODEHELPER)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_STRICT_DEVMEM`](compare-with-al2-kernel.md#CONFIG_STRICT_DEVMEM)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_STRICT_KERNEL_RWX`](#CONFIG_STRICT_KERNEL_RWX)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_STRICT_MODULE_RWX`](#CONFIG_STRICT_MODULE_RWX)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_SYN_COOKIES`](#CONFIG_SYN_COOKIES)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_VMAP_STACK`](#CONFIG_VMAP_STACK)  |  y  |  y  |  y  |  y  |  y  |  y  |
|  [`CONFIG_WERROR`](#CONFIG_WERROR)  |  n  |  n  |  n  |  n  |  n  |  n  |
|  [`CONFIG_ZERO_CALL_USED_REGS`](#CONFIG_ZERO_CALL_USED_REGS)  |  n  |  n  |  n  |  n  |  n  |  n  |

### Allow ACPI methods to be inserted/replaced at runtime (CONFIG\_ACPI\_CUSTOM\_METHOD)
<a name="CONFIG_ACPI_CUSTOM_METHOD"></a>

Amazon Linux disables this option as it allows `root` users to write to arbitrary kernel memory.

This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Miscellaneous Binary Formats (`binfmt_misc`)
<a name="CONFIG_BINFMT_MISC"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. In AL2023, this feature is optional, and is built as a kernel module.

### `BUG()` support
<a name="CONFIG_BUG"></a>

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### `BUG()` if kernel encounters data corruption in when checking kernel memory structures for validity
<a name="CONFIG_BUG_ON_DATA_CORRUPTION"></a>

 Some parts of the Linux kernel will check the internal consistency of data structures and can `BUG()` when they detect data corruption.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### `COMPAT_BRK`
<a name="CONFIG_COMPAT_BRK"></a>

 With this option disabled (which is how Amazon Linux configures the kernel), the `randomize_va_space` `sysctl` setting defaults to `2`, which also enables heap randomization on top of `mmap` base, stack, and VDSO page randomization.

 This option exists in the kernel to provide compatibility with some ancient `libc.so.5` binaries from 1996 and earlier.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### `COMPAT_VDSO`
<a name="CONFIG_COMPAT_VDSO"></a>

 This configuration option is relevant to `x86-64` and not `aarch64`. By setting this to `n`, the Amazon Linux kernel does not make a 32-bit virtual Dynamic Shared Object (VDSO) visible at a predictable address. The most recent `glibc` known to be broken by this option being set to `n` is `glibc` 2.3.3, from 2004.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### `CONFIG_DEBUG` gated hardening
<a name="CONFIG_DEBUG_KERNEL"></a>

 Linux kernel configuration options gated by `CONFIG_DEBUG` are typically designed for use in kernels built for debugging issues, and things like performance are not a priority. AL2023 enables the `CONFIG_DEBUG_LIST` hardening option.

### Disable DMA for PCI devices in EFI stub before configuring the IOMMU
<a name="CONFIG_EFI_DISABLE_PCI_DMA"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Hardening for copying memory between kernel and userspace
<a name="CONFIG_HARDENED_USERCOPY"></a>

 When the kernel needs to copy memory to or from userspace, this option enables some checks which can protect against some classes of heap overflow issues.

 The `CONFIG_HARDENED_USERCOPY_FALLBACK` option existed in kernels 4.16 through 5.15 to help kernel developers discover any missing allowlist entries via a `WARN()`. Because AL2023 ships a 6.1 kernel, this option is no longer relevant to AL2023.

 The `CONFIG_HARDENED_USERCOPY_PAGESPAN` option existed in kernels primarily as a debugging option for developers and no longer applies to the 6.1 kernel in AL2023.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Hibernation Support
<a name="CONFIG_HIBERNATION"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This option needs to be enabled in order to support the ability to [Hibernate your On-Demand Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html), and to support the ability to [Hibernate interrupted Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hibernate-spot-instances.html)

### Random Number Generation
<a name="kernel-rng"></a>

 The AL2023 kernel is configured to ensure adequate entropy is available for usage within EC2.

### `CONFIG_INET_DIAG`
<a name="CONFIG_INET_DIAG"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. In AL2023, this feature is optional, and is built as a kernel module.

### Zero all kernel page and slab allocator memory on allocation and deallocation
<a name="kernel-init-on-alloc-free"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. These options are disabled in AL2023 due to the possible performance impact of enabling this functionality by default. The `CONFIG_INIT_ON_ALLOC_DEFAULT_ON` behavior can be enabled by adding `init_on_alloc=1` to the kernel command line, and the `CONFIG_INIT_ON_FREE_DEFAULT_ON` behavior can be enabled by adding `init_on_free=1`.

### Initialize all stack variables as zero (`CONFIG_INIT_STACK_ALL_ZERO`)
<a name="CONFIG_INIT_STACK_ALL_ZERO"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This option requires GCC 12 or higher, while AL2023 ships with GCC 11.

### Kernel Module Signing
<a name="kernel-config-modules"></a>

 AL2023 signs and validates the signatures of kernel modules. The `CONFIG_MODULE_SIG_FORCE` option, which would require modules to have a valid signature is not enabled in order to preserve compatibility for users building third party modules. For users wanting to ensure that all kernel modules are signed, the [  Lockdown Linux Security Module (LSM)](#CONFIG_SECURITY_LOCKDOWN_LSM) can be configured to enforce this.

### `kexec`
<a name="CONFIG_KEXEC"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This option is enabled so that `kdump` functionality can be used.

### `IOMMU` Support
<a name="CONFIG_IOMMU_SUPPORT"></a>

 AL2023 enables IOMMU support. The `CONFIG_IOMMU_DEFAULT_DMA_STRICT` option is not enabled by default, but this functionality can be configured by adding `iommu.passthrough=0 iommu.strict=1` to the kernel command line.

### `kfence`
<a name="CONFIG_KFENCE"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Legacy `pty` Support
<a name="CONFIG_LEGACY_PTYS"></a>

 AL2023 uses the modern PTY interface (`devpts`).

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Lockdown Linux Security Module (LSM)
<a name="CONFIG_SECURITY_LOCKDOWN_LSM"></a>

 AL2023 builds the `lockdown` LSM, which will automatically lock down the kernel when using Secure Boot.

 The `CONFIG_LOCK_DOWN_KERNEL_FORCE_CONFIDENTIALITY` option is not enabled. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. When not using Secure Boot, it is possible to enable the lockdown LSM and configure as wanted.

### Page Poisoning
<a name="CONFIG_PAGE_POISONING"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. Similarly to [  Zero all kernel page and slab allocator memory on allocation and deallocation](#kernel-init-on-alloc-free), this is disabled in the AL2023 kernel due to the possible impact on performance.

### Stack Protector
<a name="CONFIG_STACKPROTECTOR"></a>

 The AL2023 kernel is built with the stack-protector feature of GCC enabled with the `-fstack-protector-strong` option.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### seccomp BPF API
<a name="CONFIG_SECCOMP"></a>

 The seccomp hardening feature is used by software such as `systemd` and container runtimes to harden userspace applications.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### `panic()` timeout
<a name="CONFIG_PANIC_TIMEOUT"></a>

 The AL2023 kernel is configured with this value set to `0`, meaning that the kernel will not reboot after it panics. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This is configurable through `sysctl`, `/proc/sys/kernel/panic`, and on the kernel command line.

### Security Models
<a name="CONFIG_SECURITY"></a>

 AL2023 enables SELinux in Permissive mode by default. For more information, see [Setting SELinux modes for AL2023](selinux-modes.md).

 The [  Lockdown Linux Security Module (LSM)](#CONFIG_SECURITY_LOCKDOWN_LSM) and `yama` modules are also enabled.

### `/proc/kcore`
<a name="CONFIG_PROC_KCORE"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Kernel stack offset randomization on syscall entry
<a name="CONFIG_RANDOMIZE_KSTACK_OFFSET_DEFAULT"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This can be enabled by setting `randomize_kstack_offset=on` on the kernel command line.

### Reference counting checks (`CONFIG_REFCOUNT_FULL`)
<a name="CONFIG_REFCOUNT_FULL"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This option is not curretly enabled due to its possible impact on performance.

### Scheduler awareness of SMT cores (`CONFIG_SCHED_CORE`)
<a name="CONFIG_SCHED_CORE"></a>

 The AL2023 kernel is built with `CONFIG_SCHED_CORE`, which enables userspace applications to use `prctl(PR_SCHED_CORE)`. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Check for stack corruption on calls to `schedule()` (`CONFIG_SCHED_STACK_END_CHECK`)
<a name="CONFIG_SCHED_STACK_END_CHECK"></a>

 The AL2023 kernel is built with `CONFIG_SCHED_STACK_END_CHECK` enabled. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Memory allocator hardening
<a name="kernel-allocator-hardening"></a>

 The AL2023 kernel enables hardening of the kernel memory allocator with the `CONFIG_SHUFFLE_PAGE_ALLOCATOR`, `CONFIG_SLAB_FREELIST_HARDENED`, and `CONFIG_SLAB_FREELIST_RANDOM` options. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### SLUB debugging support
<a name="CONFIG_SLUB_DEBUG"></a>

 The AL2023 kernel enables `CONFIG_SLUB_DEBUG` as this option enables optional debugging features for the allocator that can be enabled on the kernel command line. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### CONFIG\_STATIC\_USERMODEHELPER
<a name="CONFIG_STATIC_USERMODEHELPER"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends. This is because `CONFIG_STATIC_USERMODEHELPER` requires special support from the distribution, which is not currently present in Amazon Linux.

### Read-Only kernel text and rodata (`CONFIG_STRICT_KERNEL_RWX` and `CONFIG_STRICT_MODULE_RWX`)
<a name="CONFIG_STRICT_KERNEL_RWX"></a>

 The AL2023 kernel is configured to mark kernel and kernel module text and rodata memory as read-only, and non-text memory marked as not executable. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### TCP syncookie support (`CONFIG_SYN_COOKIES`)
<a name="CONFIG_SYN_COOKIES"></a>

 The AL2023 kernel is built with support for TCP syncookies. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Virtually mapped stack with guard pages (`CONFIG_VMAP_STACK`)
<a name="CONFIG_VMAP_STACK"></a>

 The AL2023 kernel is built with `CONFIG_VMAP_STACK`, enabling virtually mapped kernel stacks with guard pages. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Build with compiler warnings as errors (`CONFIG_WERROR`)
<a name="CONFIG_WERROR"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Register zeroing on function exit (`CONFIG_ZERO_CALL_USED_REGS`)
<a name="CONFIG_ZERO_CALL_USED_REGS"></a>

 Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Minimum address for userspace allocation
<a name="CONFIG_DEFAULT_MMAP_MIN_ADDR"></a>

 This hardening option can help reduce the impact of kernel NULL pointer bugs. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### `clang` specific hardening options
<a name="kernel-hardening-clang"></a>

 The AL2023 kernel is built with GCC rather than clang, so the `CONFIG_CFI_CLANG` hardening option cannot be enabled, which also makes `CONFIG_CFI_PERMISSIVE` not applicable. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

## x86-64 specific Kernel Hardening options
<a name="kernel-hardening-x86-64"></a>

| `CONFIG` option | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_AMD_IOMMU`](#CONFIG_AMD_IOMMU)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_AMD_IOMMU_V2`](#CONFIG_AMD_IOMMU_V2)  | N/A |  y  | N/A | N/A | N/A | N/A |
|  [`CONFIG_IA32_EMULATION`](#CONFIG_IA32_EMULATION)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_INTEL_IOMMU`](#CONFIG_INTEL_IOMMU)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_INTEL_IOMMU_DEFAULT_ON`](#CONFIG_INTEL_IOMMU_DEFAULT_ON)  | N/A |  n  | N/A |  n  | N/A |  n  |
|  [`CONFIG_INTEL_IOMMU_SVM`](#CONFIG_INTEL_IOMMU_SVM)  | N/A |  n  | N/A |  n  | N/A |  n  |
|  [`CONFIG_LEGACY_VSYSCALL_NONE`](#CONFIG_LEGACY_VSYSCALL_NONE)  | N/A |  n  | N/A |  n  | N/A |  n  |
|  [`CONFIG_MODIFY_LDT_SYSCALL`](#CONFIG_MODIFY_LDT_SYSCALL)  | N/A |  n  | N/A |  n  | N/A |  n  |
|  [`CONFIG_PAGE_TABLE_ISOLATION`](#CONFIG_PAGE_TABLE_ISOLATION)  | N/A |  y  | N/A | N/A | N/A | N/A |
|  [`CONFIG_RANDOMIZE_MEMORY`](#CONFIG_RANDOMIZE_MEMORY)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_X86_64`](#CONFIG_X86_64)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_X86_MSR`](#CONFIG_X86_MSR)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_X86_VSYSCALL_EMULATION`](#CONFIG_X86_VSYSCALL_EMULATION)  | N/A |  y  | N/A |  y  | N/A |  y  |
|  [`CONFIG_X86_X32`](#CONFIG_X86_X32)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_X86_X32_ABI`](#CONFIG_X86_X32_ABI)  | N/A |  n  | N/A |  n  | N/A |  n  |

### x86-64 Support
<a name="CONFIG_X86_64"></a>

 Base x86-64 support includes the Physical Address Extension (PAE) and no-execute (NX) bit support. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### AMD and Intel IOMMU support
<a name="kernel-x86-64-iommu"></a>

 The AL2023 kernel builds with support for the AMD and Intel IOMMUs. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

 The `CONFIG_INTEL_IOMMU_DEFAULT_ON` option is not set, but can be enabled by passing `intel_iommu=on` to the kernel command line. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

 The `CONFIG_INTEL_IOMMU_SVM` option is not currently enabled in AL2023. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Support for 32bit userspace
<a name="kernel-hardening-32bit-support"></a>

**Important**
 Support for 32bit x86 userspace is deprecated and support for running 32bit userspace binaries might be removed in a future major version of Amazon Linux.

**Note**
 While AL2023 no longer includes any 32bit packages, the kernel will still support running 32bit userspace. See [32bit x86 (i686) Packages](compare-with-al2.md#i686) for more information.

 To support running 32bit userspace applications, AL2023 does not enable the `CONFIG_X86_VSYSCALL_EMULATION` option, and enables the `CONFIG_IA32_EMULATION`, `CONFIG_COMPAT`, and `CONFIG_X86_VSYSCALL_EMULATION` options. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

 The x32 native 32-bit ABI for 64-bit processors is not enabled (`CONFIG_X86_X32` and `CONFIG_X86_X32_ABI`). This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### x86 Model Specific Register (MSR) support
<a name="CONFIG_X86_MSR"></a>

 The `CONFIG_X86_MSR` option is enabled in order to support `turbostat`. Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### `modify_ldt` syscall
<a name="CONFIG_MODIFY_LDT_SYSCALL"></a>

 AL2023 does not allow user programs to modify the x86 Local Descriptor Table (LDT) with the `modify_ldt` syscall. This call is required to run 16-bit or segmented code, and its absence may break software such as `dosemu`, running some programs under WINE, and some very old threading libraries. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Remove kernel mapping in user mode
<a name="CONFIG_PAGE_TABLE_ISOLATION"></a>

 AL2023 configures the kernel so that the majority of kernel addresses are not mapped into userspace. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Randomize kernel memory sections
<a name="CONFIG_RANDOMIZE_MEMORY"></a>

 AL2023 configures the kernel to randomize the base virtual addresses of kernel memory sections. This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

## aarch64 specific Kernel Hardening options
<a name="kernel-hardening-aarch64"></a>

| `CONFIG` option | AL2023/6.1/aarch64 | AL2023/6.1/x86\_64 | AL2023/6.12/aarch64 | AL2023/6.12/x86\_64 | AL2023/6.18/aarch64 | AL2023/6.18/x86\_64 |
| --- | --- | --- | --- | --- | --- | --- |
|  [`CONFIG_ARM64_BTI`](#CONFIG_ARM64_BTI)  |  y  | N/A |  y  | N/A |  y  | N/A |
|  [`CONFIG_ARM64_BTI_KERNEL`](#CONFIG_ARM64_BTI_KERNEL)  | N/A | N/A | N/A | N/A | N/A | N/A |
|  [`CONFIG_ARM64_PTR_AUTH`](#CONFIG_ARM64_PTR_AUTH)  |  y  | N/A |  y  | N/A |  y  | N/A |
|  [`CONFIG_ARM64_PTR_AUTH_KERNEL`](#CONFIG_ARM64_PTR_AUTH_KERNEL)  |  y  | N/A |  y  | N/A |  y  | N/A |
|  [`CONFIG_ARM64_SW_TTBR0_PAN`](#CONFIG_ARM64_SW_TTBR0_PAN)  |  y  | N/A |  y  | N/A |  y  | N/A |
|  [`CONFIG_UNMAP_KERNEL_AT_EL0`](#CONFIG_UNMAP_KERNEL_AT_EL0)  |  y  | N/A |  y  | N/A |  y  | N/A |

### Branch Target Identification
<a name="CONFIG_ARM64_BTI"></a>

 The AL2023 kernel enables support for Branch Target Identification (`CONFIG_ARM64_BTI`). This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

 The `CONFIG_ARM64_BTI_KERNEL` option is not enabled in AL2023 as it is built with GCC, and support for building the kernel with this option is [currently disabled in the upstream kernel](https://github.com/torvalds/linux/commit/c0a454b9044fdc99486853aa424e5b3be2107078) due to a [gcc bug](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=106671). Although this option is one of the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings), AL2023 does not set this configuration option to what KSPP recommends.

### Pointer Authentication (`CONFIG_ARM64_PTR_AUTH`)
<a name="CONFIG_ARM64_PTR_AUTH"></a>

 The AL2023 kernel is built with support for the Pointer Authentication extension (part of the ARMv8.3 Extensions), which can be used to help mitigate Return Oriented Programming (ROP) techniques. The required hardware support for pointer authentication on [Graviton](https://aws.amazon.com/ec2/graviton) was introduced with Graviton 3.

 The `CONFIG_ARM64_PTR_AUTH` option is enabled and provides support for pointer authentication for userspace. Because the `CONFIG_ARM64_PTR_AUTH_KERNEL` option is also enabled, the AL2023 kernel is able to use the return address protection for itself.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Emulate Privileged Access Never using `TTBR0_EL1` switching
<a name="CONFIG_ARM64_SW_TTBR0_PAN"></a>

 This option prevents the kernel from accessing userspace memory directly, with `TTBR0_EL1` being only temporarily set to a valid value by the user access routines.

 This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

### Unmap kernel when running in userspace
<a name="CONFIG_UNMAP_KERNEL_AT_EL0"></a>

 The AL2023 kernel is configured to unmap the kernel when running in userspace (`CONFIG_UNMAP_KERNEL_AT_EL0`). This option is one of the [Kernel Self Protection Project Recommended Settings](https://kernsec.org/wiki/index.php/Kernel_Self_Protection_Project/Recommended_Settings).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
