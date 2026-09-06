---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/kernel-hardening.html
---

# AL2027 kernel hardening
<a name="kernel-hardening"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

The 7.1 Linux kernel in AL2027 is configured and built with a number of hardening options and features. Many of these follow the [Kernel Self Protection Project (KSPP) Recommended Settings](https://kspp.github.io/Recommended_Settings). Where AL2027 deviates from a KSPP recommendation, the deviation is a deliberate choice that balances hardening against the performance, compatibility, and operational needs of a general-purpose cloud operating system.

The following table lists notable kernel hardening configuration options and their status in the AL2027 7.1 kernel for both the `x86_64` and `aarch64` architectures. The values have the following meaning.
+ `y` – the option is built into the kernel.
+ `m` – the option is built as a loadable kernel module.
+ `n` – the option exists in this kernel but is disabled.
+ A number or string (for example `0`, `65536`, or `sha512`) – the configured value of the option.
+ `N/A` – the configuration symbol is not present in this kernel on this architecture. This happens when the option was removed or renamed upstream, when it belongs to the other architecture, or when a different choice within the same option group is selected.

| `CONFIG` option | AL2027/7.1/aarch64 | AL2027/7.1/x86\_64 |
| --- | --- | --- |
|  CONFIG\_ACPI\_CUSTOM\_METHOD  | N/A | N/A |
|  CONFIG\_AMD\_IOMMU  | N/A |  y  |
|  CONFIG\_AMD\_IOMMU\_V2  | N/A | N/A |
|  CONFIG\_ARM64\_BTI  |  y  | N/A |
|  CONFIG\_ARM64\_BTI\_KERNEL  | N/A | N/A |
|  CONFIG\_ARM64\_E0PD  |  y  | N/A |
|  CONFIG\_ARM64\_EPAN  |  y  | N/A |
|  CONFIG\_ARM64\_MTE  |  y  | N/A |
|  CONFIG\_ARM64\_PTR\_AUTH  |  y  | N/A |
|  CONFIG\_ARM64\_PTR\_AUTH\_KERNEL  |  y  | N/A |
|  CONFIG\_ARM64\_SW\_TTBR0\_PAN  |  y  | N/A |
|  CONFIG\_BINFMT\_MISC  |  m  |  m  |
|  CONFIG\_BUG  |  y  |  y  |
|  CONFIG\_BUG\_ON\_DATA\_CORRUPTION  |  y  |  y  |
|  CONFIG\_CFI\_CLANG  | N/A | N/A |
|  CONFIG\_CFI\_PERMISSIVE  | N/A | N/A |
|  CONFIG\_COMPAT  |  y  |  y  |
|  CONFIG\_COMPAT\_BRK  |  n  |  n  |
|  CONFIG\_COMPAT\_VDSO  | N/A |  n  |
|  CONFIG\_DEBUG\_KERNEL  |  y  |  y  |
|  CONFIG\_DEBUG\_LIST  |  y  |  y  |
|  CONFIG\_DEBUG\_NOTIFIERS  |  n  |  n  |
|  CONFIG\_DEBUG\_SG  |  n  |  n  |
|  CONFIG\_DEBUG\_VIRTUAL  |  n  |  n  |
|  CONFIG\_DEBUG\_WX  |  n  |  n  |
|  CONFIG\_DEFAULT\_MMAP\_MIN\_ADDR  |  65536  |  65536  |
|  CONFIG\_DEVKMEM  | N/A | N/A |
|  CONFIG\_DEVMEM  |  n  |  n  |
|  CONFIG\_EFI\_DISABLE\_PCI\_DMA  |  n  |  n  |
|  CONFIG\_FORTIFY\_SOURCE  |  y  |  y  |
|  CONFIG\_HARDENED\_USERCOPY  |  y  |  y  |
|  CONFIG\_HIBERNATION  |  y  |  y  |
|  CONFIG\_HW\_RANDOM\_TPM  | N/A | N/A |
|  CONFIG\_IA32\_EMULATION  | N/A |  y  |
|  CONFIG\_INET\_DIAG  |  m  |  m  |
|  CONFIG\_INIT\_ON\_ALLOC\_DEFAULT\_ON  |  n  |  n  |
|  CONFIG\_INIT\_ON\_FREE\_DEFAULT\_ON  |  n  |  n  |
|  CONFIG\_INIT\_STACK\_ALL\_ZERO  | N/A | N/A |
|  CONFIG\_INTEL\_IOMMU  | N/A |  y  |
|  CONFIG\_INTEL\_IOMMU\_DEFAULT\_ON  | N/A |  n  |
|  CONFIG\_INTEL\_IOMMU\_SVM  | N/A |  n  |
|  CONFIG\_IOMMU\_DEFAULT\_DMA\_STRICT  |  n  |  n  |
|  CONFIG\_IOMMU\_SUPPORT  |  y  |  y  |
|  CONFIG\_IO\_STRICT\_DEVMEM  | N/A | N/A |
|  CONFIG\_KASAN\_HW\_TAGS  | N/A | N/A |
|  CONFIG\_KEXEC  |  y  |  y  |
|  CONFIG\_KFENCE  |  n  |  n  |
|  CONFIG\_LDISC\_AUTOLOAD  |  n  |  n  |
|  CONFIG\_LEGACY\_PTYS  |  n  |  n  |
|  CONFIG\_LEGACY\_TIOCSTI  |  n  |  n  |
|  CONFIG\_LEGACY\_VSYSCALL\_NONE  | N/A |  n  |
|  CONFIG\_LIST\_HARDENED  |  y  |  y  |
|  CONFIG\_LOCK\_DOWN\_KERNEL\_FORCE\_CONFIDENTIALITY  |  n  |  n  |
|  CONFIG\_MAGIC\_SYSRQ\_DEFAULT\_ENABLE  |  0x1  |  0x1  |
|  CONFIG\_MITIGATION\_PAGE\_TABLE\_ISOLATION  | N/A |  y  |
|  CONFIG\_MITIGATION\_SLS  | N/A |  n  |
|  CONFIG\_MODIFY\_LDT\_SYSCALL  | N/A |  n  |
|  CONFIG\_MODULE\_FORCE\_LOAD  |  y  |  y  |
|  CONFIG\_MODULES  |  y  |  y  |
|  CONFIG\_MODULE\_SIG  |  y  |  y  |
|  CONFIG\_MODULE\_SIG\_ALL  |  y  |  y  |
|  CONFIG\_MODULE\_SIG\_FORCE  |  n  |  n  |
|  CONFIG\_MODULE\_SIG\_HASH  |  sha512  |  sha512  |
|  CONFIG\_MODULE\_SIG\_KEY  |  certs/signing\_key.pem  |  certs/signing\_key.pem  |
|  CONFIG\_MODULE\_SIG\_SHA512  |  y  |  y  |
|  CONFIG\_PAGE\_TABLE\_CHECK  |  n  |  n  |
|  CONFIG\_PANIC\_ON\_OOPS  |  y  |  y  |
|  CONFIG\_PANIC\_TIMEOUT  |  0  |  0  |
|  CONFIG\_PROC\_KCORE  |  y  |  y  |
|  CONFIG\_PROC\_MEM\_ALWAYS\_FORCE  |  n  |  n  |
|  CONFIG\_PROC\_MEM\_FORCE\_PTRACE  |  y  |  y  |
|  CONFIG\_PROC\_MEM\_NO\_FORCE  |  n  |  n  |
|  CONFIG\_RANDOMIZE\_BASE  |  n  |  y  |
|  CONFIG\_RANDOMIZE\_KSTACK\_OFFSET\_DEFAULT  |  n  |  n  |
|  CONFIG\_RANDOMIZE\_MEMORY  | N/A |  y  |
|  CONFIG\_RANDOM\_KMALLOC\_CACHES  |  n  |  n  |
|  CONFIG\_RANDOM\_TRUST\_BOOTLOADER  | N/A | N/A |
|  CONFIG\_RANDOM\_TRUST\_CPU  | N/A | N/A |
|  CONFIG\_RANDSTRUCT\_FULL  | N/A | N/A |
|  CONFIG\_RESET\_ATTACK\_MITIGATION  |  n  |  n  |
|  CONFIG\_SCHED\_CORE  | N/A |  y  |
|  CONFIG\_SCHED\_STACK\_END\_CHECK  |  y  |  y  |
|  CONFIG\_SECCOMP  |  y  |  y  |
|  CONFIG\_SECCOMP\_FILTER  |  y  |  y  |
|  CONFIG\_SECURITY  |  y  |  y  |
|  CONFIG\_SECURITY\_DMESG\_RESTRICT  |  y  |  y  |
|  CONFIG\_SECURITY\_LANDLOCK  |  y  |  y  |
|  CONFIG\_SECURITY\_LOCKDOWN\_LSM  |  y  |  y  |
|  CONFIG\_SECURITY\_LOCKDOWN\_LSM\_EARLY  |  y  |  y  |
|  CONFIG\_SECURITY\_SELINUX\_BOOTPARAM  |  y  |  y  |
|  CONFIG\_SECURITY\_SELINUX\_DEBUG  |  n  |  n  |
|  CONFIG\_SECURITY\_SELINUX\_DEVELOP  |  y  |  y  |
|  CONFIG\_SECURITY\_SELINUX\_DISABLE  | N/A | N/A |
|  CONFIG\_SECURITY\_WRITABLE\_HOOKS  | N/A | N/A |
|  CONFIG\_SECURITY\_YAMA  |  y  |  y  |
|  CONFIG\_SHADOW\_CALL\_STACK  | N/A | N/A |
|  CONFIG\_SHUFFLE\_PAGE\_ALLOCATOR  |  y  |  y  |
|  CONFIG\_SLAB\_BUCKETS  |  y  |  y  |
|  CONFIG\_SLAB\_FREELIST\_HARDENED  |  y  |  y  |
|  CONFIG\_SLAB\_FREELIST\_RANDOM  |  y  |  y  |
|  CONFIG\_SLAB\_MERGE\_DEFAULT  |  y  |  y  |
|  CONFIG\_SLUB\_DEBUG  |  y  |  y  |
|  CONFIG\_STACKPROTECTOR  |  y  |  y  |
|  CONFIG\_STACKPROTECTOR\_STRONG  |  y  |  y  |
|  CONFIG\_STATIC\_USERMODEHELPER  |  n  |  n  |
|  CONFIG\_STRICT\_DEVMEM  |  n  |  n  |
|  CONFIG\_STRICT\_KERNEL\_RWX  |  y  |  y  |
|  CONFIG\_STRICT\_MODULE\_RWX  |  y  |  y  |
|  CONFIG\_SYN\_COOKIES  |  y  |  y  |
|  CONFIG\_UBSAN  |  n  |  n  |
|  CONFIG\_UNMAP\_KERNEL\_AT\_EL0  |  y  | N/A |
|  CONFIG\_VMAP\_STACK  |  y  |  y  |
|  CONFIG\_WERROR  |  n  |  n  |
|  CONFIG\_X86\_64  | N/A |  y  |
|  CONFIG\_X86\_KERNEL\_IBT  | N/A |  n  |
|  CONFIG\_X86\_MSR  | N/A |  y  |
|  CONFIG\_X86\_USER\_SHADOW\_STACK  | N/A |  n  |
|  CONFIG\_X86\_VSYSCALL\_EMULATION  | N/A |  y  |
|  CONFIG\_X86\_X32  | N/A | N/A |
|  CONFIG\_X86\_X32\_ABI  | N/A |  n  |
|  CONFIG\_ZERO\_CALL\_USED\_REGS  |  n  |  n  |
