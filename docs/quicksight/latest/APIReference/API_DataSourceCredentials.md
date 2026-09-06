---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceCredentials.html
---

# DataSourceCredentials
<a name="API_DataSourceCredentials"></a>

Data source credentials. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

## Contents
<a name="API_DataSourceCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CopySourceArn **   <a name="QS-Type-DataSourceCredentials-CopySourceArn"></a>
The Amazon Resource Name (ARN) of a data source that has the credential pair that you want to use. When `CopySourceArn` is not null, the credential pair from the data source in the ARN is used as the credentials for the `DataSourceCredentials` structure.
Type: String
Pattern: `^arn:[-a-z0-9]*:quicksight:[-a-z0-9]*:[0-9]{12}:datasource/.+`
Required: No

 ** CredentialPair **   <a name="QS-Type-DataSourceCredentials-CredentialPair"></a>
Credential pair. For more information, see ` [CredentialPair](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CredentialPair.html) `.
Type: [CredentialPair](API_CredentialPair.md) object
Required: No

 ** KeyPairCredentials **   <a name="QS-Type-DataSourceCredentials-KeyPairCredentials"></a>
The credentials for connecting using key-pair.
Type: [KeyPairCredentials](API_KeyPairCredentials.md) object
Required: No

 ** OAuthClientCredentials **   <a name="QS-Type-DataSourceCredentials-OAuthClientCredentials"></a>
The OAuth client credentials for connecting to a data source using OAuth 2.0 client credentials (2LO) authentication. For more information, see ` [OAuthClientCredentials](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_OAuthClientCredentials.html) `.
Type: [OAuthClientCredentials](API_OAuthClientCredentials.md) object
Required: No

 ** SecretArn **   <a name="QS-Type-DataSourceCredentials-SecretArn"></a>
The Amazon Resource Name (ARN) of the secret associated with the data source in Amazon Secrets Manager.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:[-a-z0-9]*:secretsmanager:[-a-z0-9]*:[0-9]{12}:secret:.+`
Required: No

 ** WebProxyCredentials **   <a name="QS-Type-DataSourceCredentials-WebProxyCredentials"></a>
The credentials for connecting through a web proxy server.
Type: [WebProxyCredentials](API_WebProxyCredentials.md) object
Required: No

## See Also
<a name="API_DataSourceCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DataSourceCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DataSourceCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DataSourceCredentials)
