---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_OracleDataProviderSettings.html
---

# OracleDataProviderSettings
<a name="API_OracleDataProviderSettings"></a>

Provides information that defines an Oracle data provider.

## Contents
<a name="API_OracleDataProviderSettings_Contents"></a>

 ** AsmServer **   <a name="DMS-Type-OracleDataProviderSettings-AsmServer"></a>
The address of your Oracle Automatic Storage Management (ASM) server. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration).
Type: String
Required: No

 ** CertificateArn **   <a name="DMS-Type-OracleDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-OracleDataProviderSettings-DatabaseName"></a>
The database name on the Oracle data provider.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-OracleDataProviderSettings-Port"></a>
The port value for the Oracle data provider.
Type: Integer
Required: No

 ** S3AccessRoleArn **   <a name="DMS-Type-OracleDataProviderSettings-S3AccessRoleArn"></a>
The ARN for the role the application uses to access its Amazon S3 bucket.
Type: String
Required: No

 ** S3Path **   <a name="DMS-Type-OracleDataProviderSettings-S3Path"></a>
The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.
Type: String
Required: No

 ** SecretsManagerOracleAsmAccessRoleArn **   <a name="DMS-Type-OracleDataProviderSettings-SecretsManagerOracleAsmAccessRoleArn"></a>
The ARN of the IAM role that provides access to the secret in AWS Secrets Manager that contains the Oracle ASM connection details.
Type: String
Required: No

 ** SecretsManagerOracleAsmSecretId **   <a name="DMS-Type-OracleDataProviderSettings-SecretsManagerOracleAsmSecretId"></a>
The identifier of the secret in AWS Secrets Manager that contains the Oracle ASM connection details.
Required only if your data provider uses the Oracle ASM server.
Type: String
Required: No

 ** SecretsManagerSecurityDbEncryptionAccessRoleArn **   <a name="DMS-Type-OracleDataProviderSettings-SecretsManagerSecurityDbEncryptionAccessRoleArn"></a>
The ARN of the IAM role that provides access to the secret in AWS Secrets Manager that contains the TDE password.
Type: String
Required: No

 ** SecretsManagerSecurityDbEncryptionSecretId **   <a name="DMS-Type-OracleDataProviderSettings-SecretsManagerSecurityDbEncryptionSecretId"></a>
The identifier of the secret in AWS Secrets Manager that contains the transparent data encryption (TDE) password. AWS DMS requires this password to access Oracle redo logs encrypted by TDE using Binary Reader.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-OracleDataProviderSettings-ServerName"></a>
The name of the Oracle server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-OracleDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the Oracle data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_OracleDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/OracleDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/OracleDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/OracleDataProviderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
