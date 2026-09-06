---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_OpenIDConnectProviderConfiguration.html
---

# OpenIDConnectProviderConfiguration
<a name="API_OpenIDConnectProviderConfiguration"></a>

Information about the OIDC-compliant identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.

## Contents
<a name="API_OpenIDConnectProviderConfiguration_Contents"></a>

 ** secretsArn **   <a name="qbusiness-Type-OpenIDConnectProviderConfiguration-secretsArn"></a>
The Amazon Resource Name (ARN) of a Secrets Manager secret containing the OIDC client secret.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

 ** secretsRole **   <a name="qbusiness-Type-OpenIDConnectProviderConfiguration-secretsRole"></a>
An IAM role with permissions to access AWS KMS to decrypt the Secrets Manager secret containing your OIDC client secret.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: Yes

## See Also
<a name="API_OpenIDConnectProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/OpenIDConnectProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/OpenIDConnectProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/OpenIDConnectProviderConfiguration)
