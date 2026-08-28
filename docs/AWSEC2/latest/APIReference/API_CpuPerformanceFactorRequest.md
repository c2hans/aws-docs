---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CpuPerformanceFactorRequest.html
---

# CpuPerformanceFactorRequest
<a name="API_CpuPerformanceFactorRequest"></a>

The CPU performance to consider, using an instance family as the baseline reference.

## Contents
<a name="API_CpuPerformanceFactorRequest_Contents"></a>

 ** Reference.N **
Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.
Currently, only one instance family can be specified in the list.
Type: Array of [PerformanceFactorReferenceRequest](API_PerformanceFactorReferenceRequest.md) objects
Required: No

## See Also
<a name="API_CpuPerformanceFactorRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CpuPerformanceFactorRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CpuPerformanceFactorRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CpuPerformanceFactorRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
