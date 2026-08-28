---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CfnStackParameter.html
---

# CfnStackParameter
<a name="API_CfnStackParameter"></a>

 A key-value pair representing a parameter used in the CloudFormation stack.

## Contents
<a name="API_CfnStackParameter_Contents"></a>

 ** Key **   <a name="sagemaker-Type-CfnStackParameter-Key"></a>
 The name of the CloudFormation parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.{1,255}`
Required: Yes

 ** Value **   <a name="sagemaker-Type-CfnStackParameter-Value"></a>
 The value of the CloudFormation parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `.{0,4096}`
Required: No

## See Also
<a name="API_CfnStackParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CfnStackParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CfnStackParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CfnStackParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
