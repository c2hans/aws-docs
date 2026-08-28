---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetAccountConfiguration.html
---

# TargetAccountConfiguration
<a name="API_TargetAccountConfiguration"></a>

Describes a target account configuration.

## Contents
<a name="API_TargetAccountConfiguration_Contents"></a>

 ** accountId **   <a name="fis-Type-TargetAccountConfiguration-accountId"></a>
The AWS account ID of the target account.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 48.
Pattern: `[\S]+`
Required: No

 ** description **   <a name="fis-Type-TargetAccountConfiguration-description"></a>
The description of the target account.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]*`
Required: No

 ** roleArn **   <a name="fis-Type-TargetAccountConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role for the target account.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_TargetAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/TargetAccountConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/TargetAccountConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/TargetAccountConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
