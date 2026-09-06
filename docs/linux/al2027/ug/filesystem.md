---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/filesystem.html
---

# Filesystem layout
<a name="filesystem"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

This section covers the filesystem layout of an AL2027 system, including details specific to instances and to AL2027 based containers. The layout follows the Filesystem Hierarchy Standard (FHS). For more information, see the `file-hierarchy(7)` man page.

AL2027 completes the merge of `/usr/sbin` into `/usr/bin`. This is the one structural change from AL2023. For details, see [Unified `/usr/bin` and `/usr/sbin`](filesystem-slash-usr.md#filesystem-bin-sbin-merge).

**Topics**
+ [`/` (the root directory)](filesystem-root.md)
+ [`/boot` (kernel, initramfs, bootloader)](filesystem-slash-boot.md)
+ [`/etc` (system configuration)](filesystem-slash-etc.md)
+ [`/home` (user home directories)](filesystem-slash-home.md)
+ [`/root` (root user home directory)](filesystem-slash-root.md)
+ [`/srv` (server payload)](filesystem-slash-srv.md)
+ [`/tmp` (small temporary files)](filesystem-slash-tmp.md)
+ [`/run` (runtime data)](filesystem-slash-run.md)
+ [`/usr` (system resources)](filesystem-slash-usr.md)
+ [`/var` (persistent variable system data)](filesystem-slash-var.md)
