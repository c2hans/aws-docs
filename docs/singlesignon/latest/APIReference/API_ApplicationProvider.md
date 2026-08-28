---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ApplicationProvider.html
---

# ApplicationProvider
<a name="API_ApplicationProvider"></a>

A structure that describes a provider that can be used to connect an AWS managed application or customer managed application to IAM Identity Center.

## Contents
<a name="API_ApplicationProvider_Contents"></a>

 ** ApplicationProviderArn **   <a name="singlesignon-Type-ApplicationProvider-ApplicationProviderArn"></a>
The ARN of the application provider.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`
Required: Yes

 ** DisplayData **   <a name="singlesignon-Type-ApplicationProvider-DisplayData"></a>
A structure that describes how IAM Identity Center represents the application provider in the portal.
Type: [DisplayData](API_DisplayData.md) object
Required: No

 ** FederationProtocol **   <a name="singlesignon-Type-ApplicationProvider-FederationProtocol"></a>
The protocol that the application provider uses to perform federation.
Type: String
Valid Values: `SAML | OAUTH`
Required: No

 ** ResourceServerConfig **   <a name="singlesignon-Type-ApplicationProvider-ResourceServerConfig"></a>
A structure that describes the application provider's resource server.
Type: [ResourceServerConfig](API_ResourceServerConfig.md) object
Required: No

## See Also
<a name="API_ApplicationProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ApplicationProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ApplicationProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ApplicationProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
