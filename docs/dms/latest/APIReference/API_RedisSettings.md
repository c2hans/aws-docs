---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RedisSettings.html
---

# RedisSettings
<a name="API_RedisSettings"></a>

Provides information that defines a Redis target endpoint.

## Contents
<a name="API_RedisSettings_Contents"></a>

 ** Port **   <a name="DMS-Type-RedisSettings-Port"></a>
Transmission Control Protocol (TCP) port for the endpoint.
Type: Integer
Required: Yes

 ** ServerName **   <a name="DMS-Type-RedisSettings-ServerName"></a>
Fully qualified domain name of the endpoint.
Type: String
Required: Yes

 ** AuthPassword **   <a name="DMS-Type-RedisSettings-AuthPassword"></a>
The password provided with the `auth-role` and `auth-token` options of the `AuthType` setting for a Redis target endpoint.
Type: String
Required: No

 ** AuthType **   <a name="DMS-Type-RedisSettings-AuthType"></a>
The type of authentication to perform when connecting to a Redis target. Options include `none`, `auth-token`, and `auth-role`. The `auth-token` option requires an `AuthPassword` value to be provided. The `auth-role` option requires `AuthUserName` and `AuthPassword` values to be provided.
Type: String
Valid Values: `none | auth-role | auth-token`
Required: No

 ** AuthUserName **   <a name="DMS-Type-RedisSettings-AuthUserName"></a>
The user name provided with the `auth-role` option of the `AuthType` setting for a Redis target endpoint.
Type: String
Required: No

 ** SslCaCertificateArn **   <a name="DMS-Type-RedisSettings-SslCaCertificateArn"></a>
The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.
Type: String
Required: No

 ** SslSecurityProtocol **   <a name="DMS-Type-RedisSettings-SslSecurityProtocol"></a>
The connection to a Redis target endpoint using Transport Layer Security (TLS). Valid values include `plaintext` and `ssl-encryption`. The default is `ssl-encryption`. The `ssl-encryption` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the `SslCaCertificateArn `setting. If an ARN isn't given for a CA, DMS uses the Amazon root CA.
The `plaintext` option doesn't provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.
Type: String
Valid Values: `plaintext | ssl-encryption`
Required: No

## See Also
<a name="API_RedisSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RedisSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RedisSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RedisSettings)
