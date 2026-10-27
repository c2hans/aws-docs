---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SecretsManagerEndpointEncryptionConfiguration.html
---

# SecretsManagerEndpointEncryptionConfiguration
<a name="API_SecretsManagerEndpointEncryptionConfiguration"></a>

The endpoint encryption configuration for connections that use a key or passphrase that you store in AWS Secrets Manager.

## Contents
<a name="API_SecretsManagerEndpointEncryptionConfiguration_Contents"></a>

 ** encryptionSecret **   <a name="mediaconnect-Type-SecretsManagerEndpointEncryptionConfiguration-encryptionSecret"></a>
The AWS Secrets Manager secret that holds the key or passphrase used to encrypt the connection.
Type: [EndpointEncryptionSecretConfiguration](API_EndpointEncryptionSecretConfiguration.md) object
Required: Yes

 ** encryptionSecretType **   <a name="mediaconnect-Type-SecretsManagerEndpointEncryptionConfiguration-encryptionSecretType"></a>
The type of secret used to encrypt the connection. Valid values include the following:
+  `AES_128_KEY` – A 128-bit AES encryption key.
+  `AES_192_KEY` – A 192-bit AES encryption key.
+  `AES_256_KEY` – A 256-bit AES encryption key.
+  `SRT_PASSPHRASE` – An SRT passphrase.
Type: String
Valid Values: `AES_128_KEY | AES_192_KEY | AES_256_KEY | SRT_PASSPHRASE`
Required: No

## See Also
<a name="API_SecretsManagerEndpointEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SecretsManagerEndpointEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SecretsManagerEndpointEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SecretsManagerEndpointEncryptionConfiguration)
