---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MicrosoftSQLServerSettings.html
---

# MicrosoftSQLServerSettings
<a name="API_MicrosoftSQLServerSettings"></a>

Provides information that defines a Microsoft SQL Server endpoint.

## Contents
<a name="API_MicrosoftSQLServerSettings_Contents"></a>

 ** AuthenticationMethod **   <a name="DMS-Type-MicrosoftSQLServerSettings-AuthenticationMethod"></a>
Specifies the authentication method to be used with Microsoft SQL Server.
Type: String
Valid Values: `password | kerberos`
Required: No

 ** BcpPacketSize **   <a name="DMS-Type-MicrosoftSQLServerSettings-BcpPacketSize"></a>
The maximum size of the packets (in bytes) used to transfer data using BCP.
Type: Integer
Required: No

 ** ControlTablesFileGroup **   <a name="DMS-Type-MicrosoftSQLServerSettings-ControlTablesFileGroup"></a>
Specifies a file group for the AWS DMS internal tables. When the replication task starts, all the internal AWS DMS control tables (awsdms\_ apply\_exception, awsdms\_apply, awsdms\_changes) are created for the specified file group.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-MicrosoftSQLServerSettings-DatabaseName"></a>
Database name for the endpoint.
Type: String
Required: No

 ** ForceLobLookup **   <a name="DMS-Type-MicrosoftSQLServerSettings-ForceLobLookup"></a>
Forces LOB lookup on inline LOB.
Type: Boolean
Required: No

 ** Password **   <a name="DMS-Type-MicrosoftSQLServerSettings-Password"></a>
Endpoint connection password.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MicrosoftSQLServerSettings-Port"></a>
Endpoint TCP port.
Type: Integer
Required: No

 ** QuerySingleAlwaysOnNode **   <a name="DMS-Type-MicrosoftSQLServerSettings-QuerySingleAlwaysOnNode"></a>
Cleans and recreates table metadata information on the replication instance when a mismatch occurs. An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.
Type: Boolean
Required: No

 ** ReadBackupOnly **   <a name="DMS-Type-MicrosoftSQLServerSettings-ReadBackupOnly"></a>
When this attribute is set to `Y`, AWS DMS only reads changes from transaction log backups and doesn't read from the active transaction log file during ongoing replication. Setting this parameter to `Y` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.
Type: Boolean
Required: No

 ** SafeguardPolicy **   <a name="DMS-Type-MicrosoftSQLServerSettings-SafeguardPolicy"></a>
Use this attribute to minimize the need to access the backup log and enable AWS DMS to prevent truncation using one of the following two methods.
 *Start transactions in the database:* This is the default method. When this method is used, AWS DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started aren't truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.
 *Exclusively use sp\_repldone within a single task*: When this method is used, AWS DMS reads the changes and then uses sp\_repldone to mark the TLOG transactions as ready for truncation. Although this method doesn't involve any transactional activities, it can only be used when Microsoft Replication isn't running. Also, when using this method, only one AWS DMS task can access the database at any given time. Therefore, if you need to run parallel AWS DMS tasks against the same database, use the default method.
Type: String
Valid Values: `rely-on-sql-server-replication-agent | exclusive-automatic-truncation | shared-automatic-truncation`
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-MicrosoftSQLServerSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the SQL Server endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-MicrosoftSQLServerSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the SQL Server endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-MicrosoftSQLServerSettings-ServerName"></a>
Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the ` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
Type: String
Required: No

 ** TlogAccessMode **   <a name="DMS-Type-MicrosoftSQLServerSettings-TlogAccessMode"></a>
Indicates the mode used to fetch CDC data.
Type: String
Valid Values: `BackupOnly | PreferBackup | PreferTlog | TlogOnly`
Required: No

 ** TrimSpaceInChar **   <a name="DMS-Type-MicrosoftSQLServerSettings-TrimSpaceInChar"></a>
Use the `TrimSpaceInChar` source endpoint setting to right-trim data on CHAR and NCHAR data types during migration. Setting `TrimSpaceInChar` does not left-trim data. The default value is `true`.
Type: Boolean
Required: No

 ** UseBcpFullLoad **   <a name="DMS-Type-MicrosoftSQLServerSettings-UseBcpFullLoad"></a>
Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.
Type: Boolean
Required: No

 ** Username **   <a name="DMS-Type-MicrosoftSQLServerSettings-Username"></a>
Endpoint connection user name.
Type: String
Required: No

 ** UseThirdPartyBackupDevice **   <a name="DMS-Type-MicrosoftSQLServerSettings-UseThirdPartyBackupDevice"></a>
When this attribute is set to `Y`, DMS processes third-party transaction log backups if they are created in native format.
Type: Boolean
Required: No

## See Also
<a name="API_MicrosoftSQLServerSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MicrosoftSQLServerSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MicrosoftSQLServerSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MicrosoftSQLServerSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
