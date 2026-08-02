---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_OracleSettings.html
---

# OracleSettings
<a name="API_OracleSettings"></a>

Provides information that defines an Oracle endpoint.

## Contents
<a name="API_OracleSettings_Contents"></a>

 ** AccessAlternateDirectly **   <a name="DMS-Type-OracleSettings-AccessAlternateDirectly"></a>
Set this attribute to `false` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.
Type: Boolean
Required: No

 ** AdditionalArchivedLogDestId **   <a name="DMS-Type-OracleSettings-AdditionalArchivedLogDestId"></a>
Set this attribute with `ArchivedLogDestId` in a primary/ standby setup. This attribute is useful in the case of a switchover. In this case, AWS DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover.
Although AWS DMS supports the use of the Oracle `RESETLOGS` option to open the database, never use `RESETLOGS` unless necessary. For additional information about `RESETLOGS`, see [RMAN Data Repair Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B) in the *Oracle Database Backup and Recovery User's Guide*.
Type: Integer
Required: No

 ** AddSupplementalLogging **   <a name="DMS-Type-OracleSettings-AddSupplementalLogging"></a>
Set this attribute to set up table-level supplemental logging for the Oracle database. This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task.
If you use this option, you still need to enable database-level supplemental logging.
Type: Boolean
Required: No

 ** AllowSelectNestedTables **   <a name="DMS-Type-OracleSettings-AllowSelectNestedTables"></a>
Set this attribute to `true` to enable replication of Oracle tables containing columns that are nested tables or defined types.
Type: Boolean
Required: No

 ** ArchivedLogDestId **   <a name="DMS-Type-OracleSettings-ArchivedLogDestId"></a>
Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest\_id column of the v$archived\_log view. If you work with an additional redo log destination, use the `AdditionalArchivedLogDestId` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.
Type: Integer
Required: No

 ** ArchivedLogsOnly **   <a name="DMS-Type-OracleSettings-ArchivedLogsOnly"></a>
When this field is set to `True`, AWS DMS only accesses the archived redo logs. If the archived redo logs are stored on Automatic Storage Management (ASM) only, the AWS DMS user account needs to be granted ASM privileges.
Type: Boolean
Required: No

 ** AsmPassword **   <a name="DMS-Type-OracleSettings-AsmPassword"></a>
For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password. You can set this value from the ` asm_user_password ` value. You set this value as part of the comma-separated value that you set to the `Password` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration).
Type: String
Required: No

 ** AsmServer **   <a name="DMS-Type-OracleSettings-AsmServer"></a>
For an Oracle source endpoint, your ASM server address. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration).
Type: String
Required: No

 ** AsmUser **   <a name="DMS-Type-OracleSettings-AsmUser"></a>
For an Oracle source endpoint, your ASM user name. You can set this value from the `asm_user` value. You set `asm_user` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration).
Type: String
Required: No

 ** AuthenticationMethod **   <a name="DMS-Type-OracleSettings-AuthenticationMethod"></a>
Specifies the authentication method to be used with Oracle.
Type: String
Valid Values: `password | kerberos`
Required: No

 ** CharLengthSemantics **   <a name="DMS-Type-OracleSettings-CharLengthSemantics"></a>
Specifies whether the length of a character column is in bytes or in characters. To indicate that the character column length is in characters, set this attribute to `CHAR`. Otherwise, the character column length is in bytes.
Example: `charLengthSemantics=CHAR;`
Type: String
Valid Values: `default | char | byte`
Required: No

 ** ConvertTimestampWithZoneToUTC **   <a name="DMS-Type-OracleSettings-ConvertTimestampWithZoneToUTC"></a>
When true, converts timestamps with the `timezone` datatype to their UTC value.
Type: Boolean
Required: No

 ** DatabaseName **   <a name="DMS-Type-OracleSettings-DatabaseName"></a>
Database name for the endpoint.
Type: String
Required: No

 ** DirectPathNoLog **   <a name="DMS-Type-OracleSettings-DirectPathNoLog"></a>
When set to `true`, this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.
Type: Boolean
Required: No

 ** DirectPathParallelLoad **   <a name="DMS-Type-OracleSettings-DirectPathParallelLoad"></a>
When set to `true`, this attribute specifies a parallel load when `useDirectPathFullLoad` is set to `Y`. This attribute also only applies when you use the AWS DMS parallel load feature. Note that the target table cannot have any constraints or indexes.
Type: Boolean
Required: No

 ** EnableHomogenousTablespace **   <a name="DMS-Type-OracleSettings-EnableHomogenousTablespace"></a>
Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.
Type: Boolean
Required: No

 ** ExtraArchivedLogDestIds **   <a name="DMS-Type-OracleSettings-ExtraArchivedLogDestIds"></a>
Specifies the IDs of one more destinations for one or more archived redo logs. These IDs are the values of the `dest_id` column in the `v$archived_log` view. Use this setting with the `archivedLogDestId` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup.
This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, AWS DMS needs information about what destination to get archive redo logs from to read changes. AWS DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings.
 `archivedLogDestId=1; ExtraArchivedLogDestIds=[2]`
In a primary-to-multiple-standby setup, you might apply the following settings.
 `archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]`
Although AWS DMS supports the use of the Oracle `RESETLOGS` option to open the database, never use `RESETLOGS` unless it's necessary. For more information about `RESETLOGS`, see [ RMAN Data Repair Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B) in the *Oracle Database Backup and Recovery User's Guide*.
Type: Array of integers
Required: No

 ** FailTasksOnLobTruncation **   <a name="DMS-Type-OracleSettings-FailTasksOnLobTruncation"></a>
When set to `true`, this attribute causes a task to fail if the actual size of an LOB column is greater than the specified `LobMaxSize`.
If a task is set to limited LOB mode and this option is set to `true`, the task fails instead of truncating the LOB data.
Type: Boolean
Required: No

 ** NumberDatatypeScale **   <a name="DMS-Type-OracleSettings-NumberDatatypeScale"></a>
Specifies the number scale. You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10.
Example: `numberDataTypeScale=12`
Type: Integer
Required: No

 ** OpenTransactionWindow **   <a name="DMS-Type-OracleSettings-OpenTransactionWindow"></a>
The timeframe in minutes to check for open transactions for a CDC-only task.
You can specify an integer value between 0 (the default) and 240 (the maximum).
This parameter is only valid in AWS DMS version 3.5.0 and later.
Type: Integer
Required: No

 ** OraclePathPrefix **   <a name="DMS-Type-OracleSettings-OraclePathPrefix"></a>
Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the default Oracle root used to access the redo logs.
Type: String
Required: No

 ** ParallelAsmReadThreads **   <a name="DMS-Type-OracleSettings-ParallelAsmReadThreads"></a>
Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the `readAheadBlocks` attribute.
Type: Integer
Required: No

 ** Password **   <a name="DMS-Type-OracleSettings-Password"></a>
Endpoint connection password.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-OracleSettings-Port"></a>
Endpoint TCP port.
Type: Integer
Required: No

 ** ReadAheadBlocks **   <a name="DMS-Type-OracleSettings-ReadAheadBlocks"></a>
Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 1000 (the default) and 200,000 (the maximum).
Type: Integer
Required: No

 ** ReadTableSpaceName **   <a name="DMS-Type-OracleSettings-ReadTableSpaceName"></a>
When set to `true`, this attribute supports tablespace replication.
Type: Boolean
Required: No

 ** ReplacePathPrefix **   <a name="DMS-Type-OracleSettings-ReplacePathPrefix"></a>
Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This setting tells DMS instance to replace the default Oracle root with the specified `usePathPrefix` setting to access the redo logs.
Type: Boolean
Required: No

 ** RetryInterval **   <a name="DMS-Type-OracleSettings-RetryInterval"></a>
Specifies the number of seconds that the system waits before resending a query.
Example: `retryInterval=6;`
Type: Integer
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-OracleSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the Oracle endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerOracleAsmAccessRoleArn **   <a name="DMS-Type-OracleSettings-SecretsManagerOracleAsmAccessRoleArn"></a>
Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the `SecretsManagerOracleAsmSecret`. This `SecretsManagerOracleAsmSecret` has the secret value that allows access to the Oracle ASM of the endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerOracleAsmSecretId`. Or you can specify clear-text values for `AsmUser`, `AsmPassword`, and `AsmServerName`. You can't specify both. For more information on creating this `SecretsManagerOracleAsmSecret` and the `SecretsManagerOracleAsmAccessRoleArn` and `SecretsManagerOracleAsmSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerOracleAsmSecretId **   <a name="DMS-Type-OracleSettings-SecretsManagerOracleAsmSecretId"></a>
Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the `SecretsManagerOracleAsmSecret` that contains the Oracle ASM connection details for the Oracle endpoint.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-OracleSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Oracle endpoint connection details.
Type: String
Required: No

 ** SecurityDbEncryption **   <a name="DMS-Type-OracleSettings-SecurityDbEncryption"></a>
For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWS DMS to access Oracle redo logs encrypted by TDE using Binary Reader. It is also the ` TDE_Password ` part of the comma-separated value you set to the `Password` request parameter when you create the endpoint. The `SecurityDbEncryption` setting is related to this `SecurityDbEncryptionName` setting. For more information, see [ Supported encryption methods for using Oracle as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecurityDbEncryptionName **   <a name="DMS-Type-OracleSettings-SecurityDbEncryptionName"></a>
For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE. The key value is the value of the `SecurityDbEncryption` setting. For more information on setting the key name value of `SecurityDbEncryptionName`, see the information and example for setting the `securityDbEncryptionName` extra connection attribute in [ Supported encryption methods for using Oracle as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-OracleSettings-ServerName"></a>
Fully qualified domain name of the endpoint.
For an Amazon RDS Oracle instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the ` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
Type: String
Required: No

 ** SpatialDataOptionToGeoJsonFunctionName **   <a name="DMS-Type-OracleSettings-SpatialDataOptionToGeoJsonFunctionName"></a>
Use this attribute to convert `SDO_GEOMETRY` to `GEOJSON` format. By default, DMS calls the `SDO2GEOJSON` custom function if present and accessible. Or you can create your own custom function that mimics the operation of `SDOGEOJSON` and set `SpatialDataOptionToGeoJsonFunctionName` to call it instead.
Type: String
Required: No

 ** StandbyDelayTime **   <a name="DMS-Type-OracleSettings-StandbyDelayTime"></a>
Use this attribute to specify a time in minutes for the delay in standby sync. If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases.
In AWS DMS, you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.
Type: Integer
Required: No

 ** TrimSpaceInChar **   <a name="DMS-Type-OracleSettings-TrimSpaceInChar"></a>
Use the `TrimSpaceInChar` source endpoint setting to trim data on CHAR and NCHAR data types during migration. The default value is `true`.
Type: Boolean
Required: No

 ** UseAlternateFolderForOnline **   <a name="DMS-Type-OracleSettings-UseAlternateFolderForOnline"></a>
Set this attribute to `true` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to use any specified prefix replacement to access all online redo logs.
Type: Boolean
Required: No

 ** UseBFile **   <a name="DMS-Type-OracleSettings-UseBFile"></a>
Set this attribute to True to capture change data using the Binary Reader utility. Set `UseLogminerReader` to False to set this attribute to True. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see [ Using Oracle LogMiner or AWS DMS Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC).
Type: Boolean
Required: No

 ** UseDirectPathFullLoad **   <a name="DMS-Type-OracleSettings-UseDirectPathFullLoad"></a>
Set this attribute to True to have AWS DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.
Type: Boolean
Required: No

 ** UseLogminerReader **   <a name="DMS-Type-OracleSettings-UseLogminerReader"></a>
Set this attribute to True to capture change data using the Oracle LogMiner utility (the default). Set this attribute to False if you want to access the redo logs as a binary file. When you set `UseLogminerReader` to False, also set `UseBfile` to True. For more information on this setting and using Oracle ASM, see [ Using Oracle LogMiner or AWS DMS Binary Reader for CDC](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC) in the * AWS DMS User Guide*.
Type: Boolean
Required: No

 ** UsePathPrefix **   <a name="DMS-Type-OracleSettings-UsePathPrefix"></a>
Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the path prefix used to replace the default Oracle root to access the redo logs.
Type: String
Required: No

 ** Username **   <a name="DMS-Type-OracleSettings-Username"></a>
Endpoint connection user name.
Type: String
Required: No

## See Also
<a name="API_OracleSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/OracleSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/OracleSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/OracleSettings)
