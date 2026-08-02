---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MySqlDataProviderSettings.html
---

# MySqlDataProviderSettings
<a name="API_MySqlDataProviderSettings"></a>

Provides information that defines a MySQL data provider.

## Contents
<a name="API_MySqlDataProviderSettings_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-MySqlDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MySqlDataProviderSettings-Port"></a>
The port value for the MySQL data provider.
Type: Integer
Required: No

 ** S3AccessRoleArn **   <a name="DMS-Type-MySqlDataProviderSettings-S3AccessRoleArn"></a>
The ARN for the role the application uses to access its Amazon S3 bucket.
Type: String
Required: No

 ** S3Path **   <a name="DMS-Type-MySqlDataProviderSettings-S3Path"></a>
The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-MySqlDataProviderSettings-ServerName"></a>
The name of the MySQL server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-MySqlDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the MySQL data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_MySqlDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MySqlDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MySqlDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MySqlDataProviderSettings)
