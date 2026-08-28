---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateWebAppConfiguration.html
---

# CreateWebAppConfiguration
<a name="API_CreateWebAppConfiguration"></a>

Input configuration for creating a web application. Used only in CreateDomain operation input.

## Contents
<a name="API_CreateWebAppConfiguration_Contents"></a>

 ** ehrRole **   <a name="connecthealth-Type-CreateWebAppConfiguration-ehrRole"></a>
ARN of the IAM role used for EHR operations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws:iam::[0-9]{12}:role/.+`
Required: Yes

 ** idcInstanceId **   <a name="connecthealth-Type-CreateWebAppConfiguration-idcInstanceId"></a>
The Identity Center instance ID to use for creating the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** idcRegion **   <a name="connecthealth-Type-CreateWebAppConfiguration-idcRegion"></a>
The AWS region where Identity Center is configured.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_CreateWebAppConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/CreateWebAppConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/CreateWebAppConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/CreateWebAppConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
