---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MariaDbDataProviderSettings.html
---

# MariaDbDataProviderSettings
<a name="API_MariaDbDataProviderSettings"></a>

Provides information that defines a MariaDB data provider.

## Contents
<a name="API_MariaDbDataProviderSettings_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-MariaDbDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MariaDbDataProviderSettings-Port"></a>
The port value for the MariaDB data provider
Type: Integer
Required: No

 ** S3AccessRoleArn **   <a name="DMS-Type-MariaDbDataProviderSettings-S3AccessRoleArn"></a>
The ARN for the role the application uses to access its Amazon S3 bucket.
Type: String
Required: No

 ** S3Path **   <a name="DMS-Type-MariaDbDataProviderSettings-S3Path"></a>
The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-MariaDbDataProviderSettings-ServerName"></a>
The name of the MariaDB server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-MariaDbDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the MariaDB data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_MariaDbDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MariaDbDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MariaDbDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MariaDbDataProviderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
