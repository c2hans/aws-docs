---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_SecretsManagerAccessTokenConfiguration.html
---

# SecretsManagerAccessTokenConfiguration
<a name="API_SecretsManagerAccessTokenConfiguration"></a>

AWS Secrets Manager access token configuration parameters. For information about Secrets Manager access token authentication, see [Working with AWS Secrets Manager access token authentication](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-access-configuration-access-token.html).

## Contents
<a name="API_SecretsManagerAccessTokenConfiguration_Contents"></a>

 ** HeaderName **   <a name="mediatailor-Type-SecretsManagerAccessTokenConfiguration-HeaderName"></a>
The name of the HTTP header used to supply the access token in requests to the source location.
Type: String
Required: No

 ** SecretArn **   <a name="mediatailor-Type-SecretsManagerAccessTokenConfiguration-SecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the access token.
Type: String
Required: No

 ** SecretStringKey **   <a name="mediatailor-Type-SecretsManagerAccessTokenConfiguration-SecretStringKey"></a>
The AWS Secrets Manager [SecretString](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_CreateSecret.html#SecretsManager-CreateSecret-request-SecretString.html) key associated with the access token. MediaTailor uses the key to look up SecretString key and value pair containing the access token.
Type: String
Required: No

## See Also
<a name="API_SecretsManagerAccessTokenConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/SecretsManagerAccessTokenConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/SecretsManagerAccessTokenConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/SecretsManagerAccessTokenConfiguration)
