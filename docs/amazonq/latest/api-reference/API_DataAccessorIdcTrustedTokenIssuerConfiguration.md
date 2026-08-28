---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataAccessorIdcTrustedTokenIssuerConfiguration.html
---

# DataAccessorIdcTrustedTokenIssuerConfiguration
<a name="API_DataAccessorIdcTrustedTokenIssuerConfiguration"></a>

Configuration details for IAM Identity Center Trusted Token Issuer (TTI) authentication.

## Contents
<a name="API_DataAccessorIdcTrustedTokenIssuerConfiguration_Contents"></a>

 ** idcTrustedTokenIssuerArn **   <a name="qbusiness-Type-DataAccessorIdcTrustedTokenIssuerConfiguration-idcTrustedTokenIssuerArn"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center Trusted Token Issuer that will be used for authentication.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:aws:sso::[0-9]{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## See Also
<a name="API_DataAccessorIdcTrustedTokenIssuerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataAccessorIdcTrustedTokenIssuerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataAccessorIdcTrustedTokenIssuerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataAccessorIdcTrustedTokenIssuerConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
