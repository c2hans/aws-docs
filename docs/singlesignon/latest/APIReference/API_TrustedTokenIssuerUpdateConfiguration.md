---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TrustedTokenIssuerUpdateConfiguration.html
---

# TrustedTokenIssuerUpdateConfiguration
<a name="API_TrustedTokenIssuerUpdateConfiguration"></a>

A structure that contains details to be updated for a trusted token issuer configuration. The structure and settings that you can include depend on the type of the trusted token issuer being updated.

## Contents
<a name="API_TrustedTokenIssuerUpdateConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** OidcJwtConfiguration **   <a name="singlesignon-Type-TrustedTokenIssuerUpdateConfiguration-OidcJwtConfiguration"></a>
A structure that describes an updated configuration for a trusted token issuer that uses OpenID Connect (OIDC) with JSON web tokens (JWT).
Type: [OidcJwtUpdateConfiguration](API_OidcJwtUpdateConfiguration.md) object
Required: No

## See Also
<a name="API_TrustedTokenIssuerUpdateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/TrustedTokenIssuerUpdateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/TrustedTokenIssuerUpdateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/TrustedTokenIssuerUpdateConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
