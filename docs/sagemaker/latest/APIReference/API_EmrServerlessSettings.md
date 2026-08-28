---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EmrServerlessSettings.html
---

# EmrServerlessSettings
<a name="API_EmrServerlessSettings"></a>

The settings for running Amazon EMR Serverless jobs in SageMaker Canvas.

## Contents
<a name="API_EmrServerlessSettings_Contents"></a>

 ** ExecutionRoleArn **   <a name="sagemaker-Type-EmrServerlessSettings-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS IAM role that is assumed for running Amazon EMR Serverless jobs in SageMaker Canvas. This role should have the necessary permissions to read and write data attached and a trust relationship with EMR Serverless.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Status **   <a name="sagemaker-Type-EmrServerlessSettings-Status"></a>
Describes whether Amazon EMR Serverless job capabilities are enabled or disabled in the SageMaker Canvas application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_EmrServerlessSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EmrServerlessSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EmrServerlessSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EmrServerlessSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
