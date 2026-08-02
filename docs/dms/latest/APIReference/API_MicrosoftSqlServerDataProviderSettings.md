---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MicrosoftSqlServerDataProviderSettings.html
---

# MicrosoftSqlServerDataProviderSettings
<a name="API_MicrosoftSqlServerDataProviderSettings"></a>

Provides information that defines a Microsoft SQL Server data provider.

## Contents
<a name="API_MicrosoftSqlServerDataProviderSettings_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-DatabaseName"></a>
The database name on the Microsoft SQL Server data provider.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-Port"></a>
The port value for the Microsoft SQL Server data provider.
Type: Integer
Required: No

 ** S3AccessRoleArn **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-S3AccessRoleArn"></a>
The ARN for the role the application uses to access its Amazon S3 bucket.
Type: String
Required: No

 ** S3Path **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-S3Path"></a>
The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-ServerName"></a>
The name of the Microsoft SQL Server server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-MicrosoftSqlServerDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the Microsoft SQL Server data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_MicrosoftSqlServerDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MicrosoftSqlServerDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MicrosoftSqlServerDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MicrosoftSqlServerDataProviderSettings)
