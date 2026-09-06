---
source_url: https://docs.aws.amazon.com/linux/al2/ug/c-cplusplus.html
---

# C, C\+\+, and Fortran in AL2
<a name="c-cplusplus"></a>

AL2 includes both the GNU Compiler Collection (GCC) and the Clang frontend for LLVM.

The major version of GCC will remain constant throughout the lifetime of AL2. Bug and security fixes might be backported to the major version of GCC that ships in AL2.

 By default, AL2 includes version 7.3 of GCC which builds almost all packages. The `gcc10` package makes GCC 10 available to a limited extent, but we don't recommend using GCC 10 to build packages.

 The default compiler flags that build AL2 RPMs include some optimization and hardening flags. We recommend that you include some optimization and hardening flags if you are building your own code with GCC.

 The default compiler and optimization flags in AL2023 improve upon what is present in AL2.
