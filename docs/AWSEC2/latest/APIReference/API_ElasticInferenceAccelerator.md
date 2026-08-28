---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ElasticInferenceAccelerator.html
---

# ElasticInferenceAccelerator
<a name="API_ElasticInferenceAccelerator"></a>

**Note**
Amazon Elastic Inference is no longer available.

 Describes an elastic inference accelerator.

## Contents
<a name="API_ElasticInferenceAccelerator_Contents"></a>

 ** Type **
 The type of elastic inference accelerator. The possible values are `eia1.medium`, `eia1.large`, `eia1.xlarge`, `eia2.medium`, `eia2.large`, and `eia2.xlarge`.
Type: String
Required: Yes

 ** Count **
 The number of elastic inference accelerators to attach to the instance.
Default: 1
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ElasticInferenceAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ElasticInferenceAccelerator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ElasticInferenceAccelerator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ElasticInferenceAccelerator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
