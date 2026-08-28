---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_PostgreSQLSettings.html
---

# PostgreSQLSettings
<a name="API_PostgreSQLSettings"></a>

Provides information that defines a PostgreSQL endpoint.

## Contents
<a name="API_PostgreSQLSettings_Contents"></a>

 ** AfterConnectScript **   <a name="DMS-Type-PostgreSQLSettings-AfterConnectScript"></a>
For use with change data capture (CDC) only, this attribute has AWS DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data.
Example: `afterConnectScript=SET session_replication_role='replica'`
Type: String
Required: No

 ** AuthenticationMethod **   <a name="DMS-Type-PostgreSQLSettings-AuthenticationMethod"></a>
This attribute allows you to specify the authentication method as "iam auth".
Type: String
Valid Values: `password | iam`
Required: No

 ** BabelfishDatabaseName **   <a name="DMS-Type-PostgreSQLSettings-BabelfishDatabaseName"></a>
The Babelfish for Aurora PostgreSQL database name for the endpoint.
Type: String
Required: No

 ** CaptureDdls **   <a name="DMS-Type-PostgreSQLSettings-CaptureDdls"></a>
To capture DDL events, AWS DMS creates various artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts.
The default value is `true`.
If this value is set to `N`, you don't have to create tables or triggers on the source database.
Type: Boolean
Required: No

 ** DatabaseMode **   <a name="DMS-Type-PostgreSQLSettings-DatabaseMode"></a>
Specifies the default behavior of the replication's handling of PostgreSQL- compatible endpoints that require some additional configuration, such as Babelfish endpoints.
Type: String
Valid Values: `default | babelfish`
Required: No

 ** DatabaseName **   <a name="DMS-Type-PostgreSQLSettings-DatabaseName"></a>
Database name for the endpoint.
Type: String
Required: No

 ** DdlArtifactsSchema **   <a name="DMS-Type-PostgreSQLSettings-DdlArtifactsSchema"></a>
The schema in which the operational DDL database artifacts are created.
The default value is `public`.
Example: `ddlArtifactsSchema=xyzddlschema;`
Type: String
Required: No

 ** DisableUnicodeSourceFilter **   <a name="DMS-Type-PostgreSQLSettings-DisableUnicodeSourceFilter"></a>
Disables the Unicode source filter with PostgreSQL, for values passed into the Selection rule filter on Source Endpoint column values. By default DMS performs source filter comparisons using a Unicode string which can cause look ups to ignore the indexes in the text columns and slow down migrations.
Unicode support should only be disabled when using a selection rule filter is on a text column in the Source database that is indexed.
Type: Boolean
Required: No

 ** ExecuteTimeout **   <a name="DMS-Type-PostgreSQLSettings-ExecuteTimeout"></a>
Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds.
Example: `executeTimeout=100;`
Type: Integer
Required: No

 ** FailTasksOnLobTruncation **   <a name="DMS-Type-PostgreSQLSettings-FailTasksOnLobTruncation"></a>
When set to `true`, this value causes a task to fail if the actual size of a LOB column is greater than the specified `LobMaxSize`.
The default value is `false`.
If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.
Type: Boolean
Required: No

 ** HeartbeatEnable **   <a name="DMS-Type-PostgreSQLSettings-HeartbeatEnable"></a>
The write-ahead log (WAL) heartbeat feature mimics a dummy transaction. By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps `restart_lsn` moving and prevents storage full scenarios.
The default value is `false`.
Type: Boolean
Required: No

 ** HeartbeatFrequency **   <a name="DMS-Type-PostgreSQLSettings-HeartbeatFrequency"></a>
Sets the WAL heartbeat frequency (in minutes).
The default value is 5 minutes.
Type: Integer
Required: No

 ** HeartbeatSchema **   <a name="DMS-Type-PostgreSQLSettings-HeartbeatSchema"></a>
Sets the schema in which the heartbeat artifacts are created.
The default value is `public`.
Type: String
Required: No

 ** MapBooleanAsBoolean **   <a name="DMS-Type-PostgreSQLSettings-MapBooleanAsBoolean"></a>
When true, lets PostgreSQL migrate the boolean type as boolean. By default, PostgreSQL migrates booleans as `varchar(5)`. You must set this setting on both the source and target endpoints for it to take effect.
The default value is `false`.
Type: Boolean
Required: No

 ** MapJsonbAsClob **   <a name="DMS-Type-PostgreSQLSettings-MapJsonbAsClob"></a>
When true, AWS DMS migrates JSONB values as CLOB.
The default value is `false`.
Type: Boolean
Required: No

 ** MapLongVarcharAs **   <a name="DMS-Type-PostgreSQLSettings-MapLongVarcharAs"></a>
Sets what datatype to map LONG values as.
The default value is `wstring`.
Type: String
Valid Values: `wstring | clob | nclob`
Required: No

 ** MaxFileSize **   <a name="DMS-Type-PostgreSQLSettings-MaxFileSize"></a>
Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL.
The default value is 32,768 KB (32 MB).
Example: `maxFileSize=512`
Type: Integer
Required: No

 ** Password **   <a name="DMS-Type-PostgreSQLSettings-Password"></a>
Endpoint connection password.
Type: String
Required: No

 ** PluginName **   <a name="DMS-Type-PostgreSQLSettings-PluginName"></a>
Specifies the plugin to use to create a replication slot.
The default value is `pglogical`.
Type: String
Valid Values: `no-preference | test-decoding | pglogical`
Required: No

 ** Port **   <a name="DMS-Type-PostgreSQLSettings-Port"></a>
Endpoint TCP port. The default is 5432.
Type: Integer
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-PostgreSQLSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the PostgreSQL endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-PostgreSQLSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the PostgreSQL endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-PostgreSQLSettings-ServerName"></a>
The host name of the endpoint database.
For an Amazon RDS PostgreSQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the ` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
For an Aurora PostgreSQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html), in the `Endpoint` field.
Type: String
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-PostgreSQLSettings-ServiceAccessRoleArn"></a>
The IAM role arn you can use to authenticate the connection to your endpoint. Ensure to include `iam:PassRole` and `rds-db:connect` actions in permission policy.
Type: String
Required: No

 ** SlotName **   <a name="DMS-Type-PostgreSQLSettings-SlotName"></a>
Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance.
When used with the `CdcStartPosition` request parameter for the AWS DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of `CdcStartPosition`. If the specified slot doesn't exist or the task doesn't have a valid `CdcStartPosition` setting, DMS raises an error.
For more information about setting the `CdcStartPosition` request parameter, see [Determining a CDC native start point](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native) in the * AWS Database Migration Service User Guide*. For more information about using `CdcStartPosition`, see [CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html), [StartReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html), and [ModifyReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html).
Type: String
Required: No

 ** TrimSpaceInChar **   <a name="DMS-Type-PostgreSQLSettings-TrimSpaceInChar"></a>
Use the `TrimSpaceInChar` source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is `true`.
Type: Boolean
Required: No

 ** Username **   <a name="DMS-Type-PostgreSQLSettings-Username"></a>
Endpoint connection user name.
Type: String
Required: No

## See Also
<a name="API_PostgreSQLSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/PostgreSQLSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/PostgreSQLSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/PostgreSQLSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
