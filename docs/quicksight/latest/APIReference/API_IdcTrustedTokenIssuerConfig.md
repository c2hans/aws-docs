---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_IdcTrustedTokenIssuerConfig.html
---

# IdcTrustedTokenIssuerConfig

A trusted token issuer configuration. When you provide it, Quick Sight authenticates the user with the external IdP and then exchanges the token with IAM Identity Center through the specified trusted token issuer.

## Contents
<a name="API_IdcTrustedTokenIssuerConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IdcTrustedTokenIssuerArn **   <a name="QS-Type-IdcTrustedTokenIssuerConfig-IdcTrustedTokenIssuerArn"></a>
The ARN of the trusted token issuer in IAM Identity Center.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1284.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):sso::\d{12}:trustedTokenIssuer/(sso)?ins-[a-zA-Z0-9-.]{16}/tti-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_IdcTrustedTokenIssuerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/IdcTrustedTokenIssuerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/IdcTrustedTokenIssuerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/IdcTrustedTokenIssuerConfig)
