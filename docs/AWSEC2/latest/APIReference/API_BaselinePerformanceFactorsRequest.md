---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BaselinePerformanceFactorsRequest.html
---

# BaselinePerformanceFactorsRequest
<a name="API_BaselinePerformanceFactorsRequest"></a>

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application.

Currently, this parameter only supports CPU performance as a baseline performance factor. For example, specifying `c6i` would use the CPU performance of the `c6i` family as the baseline reference.

## Contents
<a name="API_BaselinePerformanceFactorsRequest_Contents"></a>

 ** Cpu **
The CPU performance to consider, using an instance family as the baseline reference.
Type: [CpuPerformanceFactorRequest](API_CpuPerformanceFactorRequest.md) object
Required: No

## See Also
<a name="API_BaselinePerformanceFactorsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/BaselinePerformanceFactorsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/BaselinePerformanceFactorsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/BaselinePerformanceFactorsRequest)
