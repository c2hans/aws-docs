---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/core-toolchain.html
---

# Core toolchain packages glibc, gcc, binutils
<a name="core-toolchain"></a>

AL2027 includes the following core toolchain versions:
+ **GCC 16.1** (up from 11.5 in AL2023)
+ **glibc 2.44** (up from 2.34 in AL2023)
+ **binutils 2.46** (up from 2.41 in AL2023)

The GCC 11 to 16 upgrade is the largest toolchain change. Code compiled on AL2023 will run on AL2027, but recompilation may expose new warnings or errors due to stricter defaults.

LLVM/Clang 22 is built from a single unified SRPM. The separate `clang`, `lld`, and `lldb` source packages no longer exist.
