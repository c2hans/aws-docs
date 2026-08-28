---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MySQLSettings.html
---

# MySQLSettings
<a name="API_MySQLSettings"></a>

Provides information that defines a MySQL endpoint.

## Contents
<a name="API_MySQLSettings_Contents"></a>

 ** AfterConnectScript **   <a name="DMS-Type-MySQLSettings-AfterConnectScript"></a>
Specifies a script to run immediately after AWS DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails.
For this parameter, provide the code of the script itself, not the name of a file containing the script.
Type: String
Required: No

 ** AuthenticationMethod **   <a name="DMS-Type-MySQLSettings-AuthenticationMethod"></a>
This attribute allows you to specify the authentication method as "iam auth".
Type: String
Valid Values: `password | iam`
Required: No

 ** CleanSourceMetadataOnMismatch **   <a name="DMS-Type-MySQLSettings-CleanSourceMetadataOnMismatch"></a>
Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.
Type: Boolean
Required: No

 ** DatabaseName **   <a name="DMS-Type-MySQLSettings-DatabaseName"></a>
Database name for the endpoint. For a MySQL source or target endpoint, don't explicitly specify the database using the `DatabaseName` request parameter on either the `CreateEndpoint` or `ModifyEndpoint` API call. Specifying `DatabaseName` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.
Type: String
Required: No

 ** EventsPollInterval **   <a name="DMS-Type-MySQLSettings-EventsPollInterval"></a>
Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds.
Example: `eventsPollInterval=5;`
In the example, AWS DMS checks for changes in the binary logs every five seconds.
Type: Integer
Required: No

 ** ExecuteTimeout **   <a name="DMS-Type-MySQLSettings-ExecuteTimeout"></a>
Sets the client statement timeout (in seconds) for a MySQL source endpoint.
Type: Integer
Required: No

 ** MaxFileSize **   <a name="DMS-Type-MySQLSettings-MaxFileSize"></a>
Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.
Example: `maxFileSize=512`
Type: Integer
Required: No

 ** ParallelLoadThreads **   <a name="DMS-Type-MySQLSettings-ParallelLoadThreads"></a>
Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.
Example: `parallelLoadThreads=1`
Type: Integer
Required: No

 ** Password **   <a name="DMS-Type-MySQLSettings-Password"></a>
Endpoint connection password.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MySQLSettings-Port"></a>
Endpoint TCP port.
Type: Integer
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-MySQLSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-MySQLSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MySQL endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-MySQLSettings-ServerName"></a>
The host name of the endpoint database.
For an Amazon RDS MySQL instance, this is the output of [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html), in the ` [Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html).Address` field.
For an Aurora MySQL instance, this is the output of [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html), in the `Endpoint` field.
Type: String
Required: No

 ** ServerTimezone **   <a name="DMS-Type-MySQLSettings-ServerTimezone"></a>
Specifies the time zone for the source MySQL database.
Example: `serverTimezone=US/Pacific;`
Note: Do not enclose time zones in single quotes.
Type: String
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-MySQLSettings-ServiceAccessRoleArn"></a>
The IAM role you can use to authenticate when connecting to your endpoint. Ensure to include `iam:PassRole` and `rds-db:connect` actions in permission policy.
Type: String
Required: No

 ** TargetDbType **   <a name="DMS-Type-MySQLSettings-TargetDbType"></a>
Specifies where to migrate source tables on the target, either to a single database or multiple databases. If you specify `SPECIFIC_DATABASE`, specify the database name using the `DatabaseName` parameter of the `Endpoint` object.
Example: `targetDbType=MULTIPLE_DATABASES`
Type: String
Valid Values: `specific-database | multiple-databases`
Required: No

 ** Username **   <a name="DMS-Type-MySQLSettings-Username"></a>
Endpoint connection user name.
Type: String
Required: No

## See Also
<a name="API_MySQLSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MySQLSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MySQLSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MySQLSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
