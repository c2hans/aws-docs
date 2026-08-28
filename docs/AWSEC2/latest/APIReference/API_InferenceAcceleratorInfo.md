---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InferenceAcceleratorInfo.html
---

# InferenceAcceleratorInfo
<a name="API_InferenceAcceleratorInfo"></a>

**Note**
Amazon Elastic Inference is no longer available.

Describes the Inference accelerators for the instance type.

## Contents
<a name="API_InferenceAcceleratorInfo_Contents"></a>

 ** Accelerators.N **
Describes the Inference accelerators for the instance type.
Type: Array of [InferenceDeviceInfo](API_InferenceDeviceInfo.md) objects
Required: No

 ** totalInferenceMemoryInMiB **
The total size of the memory for the inference accelerators for the instance type, in MiB.
Type: Integer
Required: No

## See Also
<a name="API_InferenceAcceleratorInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InferenceAcceleratorInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InferenceAcceleratorInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InferenceAcceleratorInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
