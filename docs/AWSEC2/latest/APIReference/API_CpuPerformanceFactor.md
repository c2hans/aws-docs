---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CpuPerformanceFactor.html
---

# CpuPerformanceFactor
<a name="API_CpuPerformanceFactor"></a>

The CPU performance to consider, using an instance family as the baseline reference.

## Contents
<a name="API_CpuPerformanceFactor_Contents"></a>

 ** ReferenceSet.N **
Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.
Currently, only one instance family can be specified in the list.
Type: Array of [PerformanceFactorReference](API_PerformanceFactorReference.md) objects
Required: No

## See Also
<a name="API_CpuPerformanceFactor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CpuPerformanceFactor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CpuPerformanceFactor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CpuPerformanceFactor)
