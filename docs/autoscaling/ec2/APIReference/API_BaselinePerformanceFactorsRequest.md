---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BaselinePerformanceFactorsRequest.html
---

# BaselinePerformanceFactorsRequest
<a name="API_BaselinePerformanceFactorsRequest"></a>

 The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Auto Scaling uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application.

Currently, this parameter only supports CPU performance as a baseline performance factor. For example, specifying `c6i` uses the CPU performance of the `c6i` family as the baseline reference.

## Contents
<a name="API_BaselinePerformanceFactorsRequest_Contents"></a>

 ** Cpu **
 The CPU performance to consider, using an instance family as the baseline reference.
Type: [CpuPerformanceFactorRequest](API_CpuPerformanceFactorRequest.md) object
Required: No

## See Also
<a name="API_BaselinePerformanceFactorsRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/BaselinePerformanceFactorsRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/BaselinePerformanceFactorsRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/BaselinePerformanceFactorsRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
