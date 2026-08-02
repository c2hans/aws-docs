---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/core-glibc.html
---

# Core toolchain packages glibc, gcc, binutils
<a name="core-glibc"></a>

A subset of packages in Amazon Linux is designated as core toolchain packages. As a major part of AL2023, core packages receive five years of support. We might change the version of a package, but long-term support applies to the package included in the Amazon Linux release.

These three core packages provide a system toolchain that's used to build most software in the Amazon Linux distribution.

| Package | Definition | Purpose |
| --- | --- | --- |
| glibc 2.34 | System C library | Used by most binary programs that provide standard functions and by the interface between programs and the kernel. |
| gcc 11.2 | gcc compiler suite | Compiles C, C\+\+, Fortran. |
| binutils 2.35 | Assembler and linker plus other binary tools | Manipulates or inspects binary programs. |

We recommend that updates to any glibc libraries are followed by a reboot. For updates to packages that control services, it might be sufficient to restart the services to pick up the updates. However, a system reboot ensures that all previous package and library updates are complete.
