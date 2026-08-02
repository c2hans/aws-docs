---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthParameters.html
---

# OAuthParameters
<a name="API_OAuthParameters"></a>

An object that contains information needed to create a data source connection that uses OAuth client credentials. This option is available for data source connections that are made with Snowflake and Starburst.

## Contents
<a name="API_OAuthParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TokenProviderUrl **   <a name="QS-Type-OAuthParameters-TokenProviderUrl"></a>
The token endpoint URL of the identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** IdentityProviderCACertificatesBundleS3Uri **   <a name="QS-Type-OAuthParameters-IdentityProviderCACertificatesBundleS3Uri"></a>
The S3 URI of the identity provider's CA certificates bundle in PEM format. Use this parameter to provide a custom CA certificate bundle for the identity provider when the default trust store does not include the required certificates.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^s3://.+/.+`
Required: No

 ** IdentityProviderResourceUri **   <a name="QS-Type-OAuthParameters-IdentityProviderResourceUri"></a>
The resource uri of the identity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** IdentityProviderVpcConnectionProperties **   <a name="QS-Type-OAuthParameters-IdentityProviderVpcConnectionProperties"></a>
VPC connection properties.
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object
Required: No

 ** OAuthScope **   <a name="QS-Type-OAuthParameters-OAuthScope"></a>
The OAuth scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_OAuthParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/OAuthParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/OAuthParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/OAuthParameters)
