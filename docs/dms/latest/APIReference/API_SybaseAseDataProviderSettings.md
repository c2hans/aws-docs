---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_SybaseAseDataProviderSettings.html
---

# SybaseAseDataProviderSettings
<a name="API_SybaseAseDataProviderSettings"></a>

Provides information that defines an SAP ASE data provider.

## Contents
<a name="API_SybaseAseDataProviderSettings_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-SybaseAseDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-SybaseAseDataProviderSettings-DatabaseName"></a>
The database name on the SAP ASE data provider.
Type: String
Required: No

 ** EncryptPassword **   <a name="DMS-Type-SybaseAseDataProviderSettings-EncryptPassword"></a>
Specifies whether to encrypt the password when connecting to the Sybase ASE database. When set to true, the connection password is encrypted during transmission. Default is true.
Type: Boolean
Required: No

 ** Port **   <a name="DMS-Type-SybaseAseDataProviderSettings-Port"></a>
The port value for the SAP ASE data provider.
Type: Integer
Required: No

 ** ServerName **   <a name="DMS-Type-SybaseAseDataProviderSettings-ServerName"></a>
The name of the SAP ASE server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-SybaseAseDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the SAP ASE data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_SybaseAseDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/SybaseAseDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/SybaseAseDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/SybaseAseDataProviderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
