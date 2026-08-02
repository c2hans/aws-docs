---
source_url: https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/software-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Software considerations
<a name="software-considerations"></a>

 Compiler selection is another consideration. The use of a complier that is optimized for the target CPU architecture can yield performance improvements. For example, quantitative analysts might see value in developing analytics using the Intel Compiler when targeting x86-based Amazon EC2 instances offering AVX-512 SIMD instructions. The AVX-512 instruction set allows developers to run twice the number of floating-point operations per second (FLOPS) per clock-cycle. Similarly, AMD offers the AMD Optimizing C/C\+\+ Compiler which optimizes for AMD EPYC architectures and 4th generation AMD EPYC processors like c7a also support AVX-512.

 On AWS Graviton-based Amazon EC2 instances, AWS highly recommends using optimization flags specifically targeting AWS Graviton processors as documented in the [Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started/blob/main/c-c%2B%2B.md) and using recent versions of the compilers. Optimized mathematical functions provided by ARM can be found in [libamath](https://developer.arm.com/documentation/102574/0100/Optimized-math-routines---libamath).

 Graviton processors are compliant with the IEEE 754 standard, so they treat floating point numbers the same way as x86 processors. It is important to note that different compilers may generate numerical conversions in varying ways. This highlights the importance of ensuring [floating point error mitigation is properly accounted for in code](https://dl.acm.org/doi/10.1145/103162.103163).
