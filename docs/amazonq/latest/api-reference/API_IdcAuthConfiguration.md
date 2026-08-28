---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_IdcAuthConfiguration.html
---

# IdcAuthConfiguration
<a name="API_IdcAuthConfiguration"></a>

Information about the AWS IAM Identity Center Application used to configure authentication for a plugin.

## Contents
<a name="API_IdcAuthConfiguration_Contents"></a>

 ** idcApplicationArn **   <a name="qbusiness-Type-IdcAuthConfiguration-idcApplicationArn"></a>
The Amazon Resource Name (ARN) of the AWS IAM Identity Center Application used to configure authentication.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: Yes

 ** roleArn **   <a name="qbusiness-Type-IdcAuthConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role with permissions to perform actions on AWS services on your behalf.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## See Also
<a name="API_IdcAuthConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/IdcAuthConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/IdcAuthConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/IdcAuthConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
