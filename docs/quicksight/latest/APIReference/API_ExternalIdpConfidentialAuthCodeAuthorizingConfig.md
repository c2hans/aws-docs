---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ExternalIdpConfidentialAuthCodeAuthorizingConfig.html
---

# ExternalIdpConfidentialAuthCodeAuthorizingConfig

The configuration for an external OpenID Connect IdP that uses the authorization code flow with a confidential client. Client secret values are never included.

## Contents
<a name="API_ExternalIdpConfidentialAuthCodeAuthorizingConfig_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ClientId **   <a name="QS-Type-ExternalIdpConfidentialAuthCodeAuthorizingConfig-ClientId"></a>
The OAuth 2.0 client ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** IssuerUrl **   <a name="QS-Type-ExternalIdpConfidentialAuthCodeAuthorizingConfig-IssuerUrl"></a>
The issuer URL of the external OpenID Connect IdP.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://[-a-zA-Z0-9+&@/%=~_|!:,.;]*[-a-zA-Z0-9+&@/%=~_|]`
Required: Yes

 ** ClientSecrets **   <a name="QS-Type-ExternalIdpConfidentialAuthCodeAuthorizingConfig-ClientSecrets"></a>
The client secrets of the confidential client, with the AWS Secrets Manager ARN for each Region. Secret values are never included.
Type: Array of [ExternalIdpConfidentialClientSecret](API_ExternalIdpConfidentialClientSecret.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_ExternalIdpConfidentialAuthCodeAuthorizingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ExternalIdpConfidentialAuthCodeAuthorizingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ExternalIdpConfidentialAuthCodeAuthorizingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ExternalIdpConfidentialAuthCodeAuthorizingConfig)
