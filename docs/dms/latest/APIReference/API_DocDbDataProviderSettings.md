---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DocDbDataProviderSettings.html
---

# DocDbDataProviderSettings
<a name="API_DocDbDataProviderSettings"></a>

Provides information that defines a DocumentDB data provider.

## Contents
<a name="API_DocDbDataProviderSettings_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-DocDbDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-DocDbDataProviderSettings-DatabaseName"></a>
The database name on the DocumentDB data provider.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-DocDbDataProviderSettings-Port"></a>
The port value for the DocumentDB data provider.
Type: Integer
Required: No

 ** ServerName **   <a name="DMS-Type-DocDbDataProviderSettings-ServerName"></a>
The name of the source DocumentDB server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-DocDbDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the DocumentDB data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_DocDbDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DocDbDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DocDbDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DocDbDataProviderSettings)
