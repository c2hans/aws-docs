---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IdcConfigInput.html
---

# IdcConfigInput
<a name="API_IdcConfigInput"></a>

Specifies the AWS IAM Identity Center configuration to use for a SageMaker Partner AI App that uses `IDC` authorization.

## Contents
<a name="API_IdcConfigInput_Contents"></a>

 ** InstanceArn **   <a name="sagemaker-Type-IdcConfigInput-InstanceArn"></a>
The ARN of the AWS IAM Identity Center instance that the SageMaker Partner AI App uses to authenticate users.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sso:::instance/(sso)?ins-[a-zA-Z0-9.-]{16}`
Required: Yes

## See Also
<a name="API_IdcConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IdcConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IdcConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IdcConfigInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
