---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_IbmDb2LuwDataProviderSettings.html
---

# IbmDb2LuwDataProviderSettings
<a name="API_IbmDb2LuwDataProviderSettings"></a>

Provides information about an IBM DB2 LUW data provider.

## Contents
<a name="API_IbmDb2LuwDataProviderSettings_Contents"></a>

 ** CertificateArn **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-DatabaseName"></a>
The database name on the DB2 LUW data provider.
Type: String
Required: No

 ** EncryptionAlgorithm **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-EncryptionAlgorithm"></a>
 The encryption algorithm used for securing the connection to the IBM DB2 LUW database server. You can provide an integer value corresponding to a specific encryption algorithm, or leave this parameter empty to use the default behavior.
Type: Integer
Required: No

 ** Port **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-Port"></a>
The port value for the DB2 LUW data provider.
Type: Integer
Required: No

 ** S3AccessRoleArn **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-S3AccessRoleArn"></a>
The ARN for the role the application uses to access its Amazon S3 bucket.
Type: String
Required: No

 ** S3Path **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-S3Path"></a>
The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.
Type: String
Required: No

 ** SecurityMechanism **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-SecurityMechanism"></a>
 The security mechanism used for authenticating the connection to the IBM DB2 LUW database server. You can provide an integer value corresponding to a specific security mechanism, or leave this parameter empty to use the default behavior.
Type: Integer
Required: No

 ** ServerName **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-ServerName"></a>
The name of the DB2 LUW server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-IbmDb2LuwDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the DB2 LUW data provider. The default value is `none`. Valid Values: `none` and `verify-ca`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_IbmDb2LuwDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/IbmDb2LuwDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/IbmDb2LuwDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/IbmDb2LuwDataProviderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
