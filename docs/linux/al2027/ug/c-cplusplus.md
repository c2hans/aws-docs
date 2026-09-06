---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/c-cplusplus.html
---

# C, C\+\+, and Fortran in AL2027
<a name="c-cplusplus"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

AL2027 includes both the GNU Compiler Collection (GCC) and the Clang frontend for LLVM (Low Level Virtual Machine).

 AL2027 includes GCC 16.1 as the default compiler with the C (`gcc`), C\+\+ (`g++`), and Fortran (`gfortran`) frontends. This is a significant upgrade from GCC 11.5 in AL2023, which is not available in AL2027. AL2027 also includes LLVM/Clang 22.

 GCC 16.1 is currently the only GCC version in AL2027. AL2027 does not currently provide a second GCC version.

The major version of GCC will remain constant throughout the life time of AL2027. Minor releases bring bug fixes and might be included in AL2027 releases. Other bug, performance, and security fixes might be backported to the major version of GCC that ships in AL2027.

 AL2027 does not enable the Ada (`gnat`), Go (`gcc-go`), Objective-C, or Objective-C\+\+ frontends.

 The default compiler flags that AL2027 RPMs are built with include optimization and hardening flags. To build your own code with GCC, we recommend you include optimization and hardening flags.

**Note**
 The GCC 11 to 16 upgrade is the largest toolchain change in AL2027. Code compiled on AL2023 will run on AL2027, but recompilation might expose new warnings or errors due to stricter defaults in GCC 16.

**Note**
When `gcc --version` is invoked, a version string such as `gcc (GCC) 16.1.1 ... (Red Hat 16.1.1-1)` is displayed. `Red Hat` refers to the [GCC vendor branch](https://gcc.gnu.org/gitwrite.html#vendor) that the Amazon Linux GCC package is based upon. According to the bug report URL shown by `gcc --help`, all bug reports and support requests should be directed to Amazon Linux.
For more information about some of the long-term changes in this vendor branch, such as the `__GNUC_RH_RELEASE__` macro, see [Fedora package sources](https://src.fedoraproject.org/rpms/gcc/pull-request/27).

For more information on the core toolchain, see [Core toolchain packages glibc, gcc, binutils](core-toolchain.md).

For more information on AL2027 and its relationship to other Linux distributions, see [Relationship to Fedora](relationship-to-fedora.md).

**Topics**
+ [LLVM/Clang 22](#llvm-clang22)
+ [Language standard versions comparison](#language-standards-comparison)

## LLVM/Clang 22
<a name="llvm-clang22"></a>

 AL2027 includes LLVM/Clang 22, which provides the Clang C and C\+\+ compilers along with the broader LLVM toolchain.

To install Clang and related tools, use the following command:

```
sudo dnf install clang lld lldb
```

 The Clang compilers are invoked with the following commands:
+ `clang` - C compiler
+ `clang++` - C\+\+ compiler

Example usage:

```
clang -o myprogram myprogram.c
clang++ -o mycppprogram mycppprogram.cpp
```

 You can verify the installed version by running:

```
clang --version
```

**Note**
 In AL2027, LLVM/Clang 22 is built from a single unified SRPM. The separate `clang`, `lld`, and `lldb` source packages no longer exist. This change affects only how the software is packaged at the source level; the installation commands and the names of the installed binary packages are unchanged.

## Language standard versions comparison
<a name="language-standards-comparison"></a>

 The following table compares the default language standard versions across different Amazon Linux versions and GCC compiler versions:

| Amazon Linux Version | C Standard (Default) | C\+\+ Standard (Default) | Fortran Standard |
| --- | --- | --- | --- |
| AL2023 with GCC 11 (default) | C17/C18 (201710L) | C\+\+17 (201703L) | Fortran 2008 |
| AL2023 with GCC 14 (optional) | C17/C18 (201710L) | C\+\+17 (201703L) | Fortran 2018 |
| AL2027 with GCC 16.1 (default) | C23 (202311L) | C\+\+20 (202002L) | Fortran 2018 |

 **Key improvements by GCC version:**
+  **GCC 16.1 vs GCC 11:** Upgraded the default C standard to C23 and the default C\+\+ standard to C\+\+20, added full C23 support and enhanced C\+\+23 support, introduced initial C\+\+26 features, and improved optimization, diagnostics, and standards compliance. Because the default C standard moved to C23 and the default C\+\+ standard moved to C\+\+20, recompiling AL2023 sources might surface new warnings or errors.

 **Supported language standards:**
+  **C Standards:** The GCC versions in the preceding table support C90, C99, C11, and C17/C18. GCC 16.1 defaults to C23 and provides full C23 support, along with initial support for later draft C standards.
+  **C\+\+ Standards:** The GCC versions in the preceding table support C\+\+98, C\+\+03, C\+\+11, C\+\+14, C\+\+17, and C\+\+20. GCC 16.1 defaults to C\+\+20, provides enhanced C\+\+23 support, and includes initial C\+\+26 features.
+  **Fortran Standards:** GCC 16.1 provides broad Fortran 2018 support, with ongoing work toward Fortran 2023 features.

**Note**
 You can select a specific language standard by using the `-std=` flag (for example, `-std=c17`, `-std=c++20`, or `-std=f2008`) to override the compiler default and target a particular standard when building your code.
