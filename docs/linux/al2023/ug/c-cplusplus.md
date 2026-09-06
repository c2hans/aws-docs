---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/c-cplusplus.html
---

# C, C\+\+, and Fortran in AL2023
<a name="c-cplusplus"></a>

AL2023 includes both the GNU Compiler Collection (GCC) and the Clang frontend for LLVM (Low Level Virtual Machine).

The major version of GCC will remain constant throughout the life time of AL2023. Minor releases bring bug fixes and might be included in AL2023 releases. Other bug, performance, and security fixes might be backported to the major version of GCC that ships in AL2023.

 AL2023 includes version 11 of GCC as the default compiler with the C (`gcc`), C\+\+ (`g++`), and Fortran (`gfortran`) frontends. Additionally, AL2023 provides GCC version 14 as an optional alternative compiler that can be installed alongside the default version.

 AL2023 does not enable the Ada (`gnat`), Go (`gcc-go`), Objective-C, or Objective-C\+\+ frontends.

 The default compiler flags that AL2023 RPMs are built with include optimization and hardening flags. To build your own code with GCC, we recommend you include optimization and hardening flags.

**Note**
When `gcc --version` is invoked, a version string such as `gcc (GCC) 11.3.1 20221121 (Red Hat 11.3.1-4)` is displayed. `Red Hat` refers to the [GCC vendor branch](https://gcc.gnu.org/gitwrite.html#vendor) that the Amazon Linux GCC package is based upon. According to the bug report URL shown by `gcc --help`, all bug reports and support requests should be directed to Amazon Linux.
For more information about some of the long-term changes in this vendor branch, such as the `__GNUC_RH_RELEASE__` macro, see [Fedora package sources](https://src.fedoraproject.org/rpms/gcc/pull-request/27).

For more information on the core toolchain, see [Core toolchain packages glibc, gcc, binutils](core-glibc.md).

For more information on AL2023 and its relationship to other Linux distributions, see [Relationship to Fedora](relationship-to-fedora.md).

For more information on the compiler triplet change in AL2023 compared to AL2, see [Compiler Triplet](compare-with-al2.md#compiler-triplet).

**Topics**
+ [GCC 14](#gcc14)
+ [Language Standard Versions Comparison](#language-standards-comparison)

## GCC 14
<a name="gcc14"></a>

 AL2023 provides GCC 14 as an optional compiler that can be installed alongside the default GCC 11. GCC 14 includes the latest language features and optimizations, making it suitable for projects that require newer C, C\+\+, or Fortran standards support.

To install GCC 14, use the following command:

```
sudo dnf install gcc14 gcc14-c++ gcc14-gfortran
```

 The GCC 14 compilers are installed with version-specific command names to avoid conflicts with the default GCC 11:
+ `gcc14-gcc` - C compiler
+ `gcc14-g++` - C\+\+ compiler
+ `gcc14-gfortran` - Fortran compiler

Example usage:

```
gcc14-gcc -o myprogram myprogram.c
gcc14-g++ -o mycppprogram mycppprogram.cpp
gcc14-gfortran -o myfortranprogram myfortranprogram.f90
```

 You can verify the installed version by running:

```
gcc14-gcc --version
```

 This will display version information similar to: `gcc14-gcc (GCC) 14.2.1 20250110 (Red Hat 14.2.1-7)`

**Note**
 Both GCC 11 and GCC 14 can be installed simultaneously on the same system. The default `gcc`, `g++`, and `gfortran` commands will continue to use GCC 11, while GCC 14 is accessed through the version-specific commands.

## Language Standard Versions Comparison
<a name="language-standards-comparison"></a>

 The following table compares the default language standard versions across different Amazon Linux versions and GCC compiler versions:

| Amazon Linux Version | C Standard (Default) | C\+\+ Standard (Default) | Fortran Standard |
| --- | --- | --- | --- |
| AL2 with GCC 7 (default) | C11 (201112L) | C\+\+14 (201402L) | Fortran 2008 |
| AL2 with GCC 10 (optional) | C17/C18 (201710L) | C\+\+14 (201402L) | Fortran 2008 |
| AL2023 with GCC 11 (default) | C17/C18 (201710L) | C\+\+17 (201703L) | Fortran 2008 |
| AL2023 with GCC 14 (optional) | C17/C18 (201710L) | C\+\+17 (201703L) | Fortran 2008 |

 **Key improvements by GCC version:**
+  **GCC 10 vs GCC 7:** Upgraded default C standard from C11 to C17/C18, added support for C\+\+20 features, and improved optimization capabilities.
+  **GCC 11 vs GCC 10:** Upgraded default C\+\+ standard from C\+\+14 to C\+\+17, enhanced C\+\+20 support, and added experimental C\+\+23 features.
+  **GCC 14 vs GCC 11:** Added full C23 standard support, enhanced C\+\+23 features, improved optimization, and better standards compliance.

 **Supported language standards:**
+  **C Standards:** All versions support C90, C99, C11, and C17/C18. GCC 10\+ supports C2x (draft C23), while GCC 14 provides full C23 support.
+  **C\+\+ Standards:** All versions support C\+\+98, C\+\+03, C\+\+11, C\+\+14, C\+\+17, and C\+\+20. GCC 11\+ provides experimental C\+\+23 support, with GCC 14 offering enhanced C\+\+23 features.
+  **Fortran Standards:** All versions primarily support Fortran 2008, with varying levels of Fortran 2018 features depending on the GCC version.

**Note**
 While the default standards remain consistent between GCC 11 and 14, GCC 14 provides significantly improved language feature support, better optimization, enhanced diagnostics, and more complete implementation of newer standards when explicitly requested using `-std=` flags.
