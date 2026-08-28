---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_SamlConfiguration.html
---

# SamlConfiguration
<a name="API_SamlConfiguration"></a>

Provides the SAML 2.0 compliant identity provider (IdP) configuration information Amazon Q Business needs to deploy a Amazon Q Business web experience.

## Contents
<a name="API_SamlConfiguration_Contents"></a>

 ** metadataXML **   <a name="qbusiness-Type-SamlConfiguration-metadataXML"></a>
The metadata XML that your IdP generated.
Type: String
Length Constraints: Minimum length of 1000. Maximum length of 10000000.
Pattern: `.*`
Required: Yes

 ** roleArn **   <a name="qbusiness-Type-SamlConfiguration-roleArn"></a>
The Amazon Resource Name (ARN) of an IAM role assumed by users when they authenticate into their Amazon Q Business web experience, containing the relevant Amazon Q Business permissions for conversing with Amazon Q Business.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** userIdAttribute **   <a name="qbusiness-Type-SamlConfiguration-userIdAttribute"></a>
The user attribute name in your IdP that maps to the user email.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** userGroupAttribute **   <a name="qbusiness-Type-SamlConfiguration-userGroupAttribute"></a>
The group attribute name in your IdP that maps to user groups.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_SamlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/SamlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/SamlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/SamlConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
