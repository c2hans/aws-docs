---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_TrustedTokenIssuerMetadata.html
---

# TrustedTokenIssuerMetadata
<a name="API_TrustedTokenIssuerMetadata"></a>

A structure that describes a trusted token issuer.

## Contents
<a name="API_TrustedTokenIssuerMetadata_Contents"></a>

 ** Name **   <a name="singlesignon-Type-TrustedTokenIssuerMetadata-Name"></a>
The name of the trusted token issuer configuration in the instance of IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w+=,.@-]+`
Required: No

 ** TrustedTokenIssuerArn **   <a name="singlesignon-Type-TrustedTokenIssuerMetadata-TrustedTokenIssuerArn"></a>
The ARN of the trusted token issuer configuration in the instance of IAM Identity Center.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** TrustedTokenIssuerType **   <a name="singlesignon-Type-TrustedTokenIssuerMetadata-TrustedTokenIssuerType"></a>
The type of trusted token issuer.
Type: String
Valid Values: `OIDC_JWT`
Required: No

## See Also
<a name="API_TrustedTokenIssuerMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/TrustedTokenIssuerMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/TrustedTokenIssuerMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/TrustedTokenIssuerMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Identity Center API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
