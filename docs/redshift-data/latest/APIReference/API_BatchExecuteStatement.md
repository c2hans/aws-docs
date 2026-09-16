---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_BatchExecuteStatement.html
---

# BatchExecuteStatement
<a name="API_BatchExecuteStatement"></a>

Runs one or more SQL statements, which can be data manipulation language (DML) or data definition language (DDL). Depending on the authorization method, use one of the following combinations of request parameters:
+  AWS Secrets Manager - when connecting to a cluster, provide the `secret-arn` of a secret stored in AWS Secrets Manager which has `username` and `password`. The specified secret contains credentials to connect to the `database` you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (`dbClusterIdentifier`), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.
+ Temporary credentials - when connecting to your data warehouse, choose one of the following options:
  + When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo`. Also, permission to call the `redshift-serverless:GetCredentials` operation is required.
  + When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo`. Also, permission to call the `redshift:GetClusterCredentialsWithIAM` operation is required.
  + When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the `redshift:GetClusterCredentials` operation is required.

For more information about the Amazon Redshift Data API and AWS CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide*.

## Request Syntax
<a name="API_BatchExecuteStatement_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "ClusterIdentifier": "{{string}}",
   "Database": "{{string}}",
   "DbUser": "{{string}}",
   "ExecutionMode": "{{string}}",
   "Parameters": [
      {
         "name": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "ResultFormat": "{{string}}",
   "SecretArn": "{{string}}",
   "SessionId": "{{string}}",
   "SessionKeepAliveSeconds": {{number}},
   "Sqls": [ "{{string}}" ],
   "StatementName": "{{string}}",
   "WaitTimeSeconds": {{number}},
   "WithEvent": {{boolean}},
   "WorkgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchExecuteStatement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Sqls](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-Sqls"></a>
One or more SQL statements to run. The SQL statements run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. By default, the SQL statements are run as a single transaction. If any SQL statement fails, all work is rolled back. To change this behavior, see the `ExecutionMode` parameter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 40 items.
Required: Yes

 ** [ClientToken](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [ClusterIdentifier](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-ClusterIdentifier"></a>
The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: No

 ** [Database](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-Database"></a>
The name of the database. This parameter is required when authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Required: No

 ** [DbUser](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-DbUser"></a>
The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials.
Type: String
Required: No

 ** [ExecutionMode](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-ExecutionMode"></a>
Determines how the SQL statements in the batch are run. If set to `TRANSACTION` (the default), all SQL statements are run as a single transaction and they are committed or rolled back together. If set to `AUTO_COMMIT`, each SQL statement is committed individually, and a failure of one statement does not affect the others.
Type: String
Valid Values: `TRANSACTION | AUTO_COMMIT`
Required: No

 ** [Parameters](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-Parameters"></a>
The parameters for the SQL statements. The parameters are available to all SQL statements in the batch. Each statement can reference any subset of the provided parameters. Each provided parameter must be referenced by at least one SQL statement in the batch.
Type: Array of [SqlParameter](API_SqlParameter.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** [ResultFormat](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-ResultFormat"></a>
The data format of the result of the SQL statement. If no format is specified, the default is JSON.
Type: String
Valid Values: `JSON | CSV`
Required: No

 ** [SecretArn](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-SecretArn"></a>
The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using AWS Secrets Manager.
Type: String
Required: No

 ** [SessionId](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-SessionId"></a>
The session identifier of the query.
Type: String
Pattern: `[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d{0,2})?`
Required: No

 ** [SessionKeepAliveSeconds](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-SessionKeepAliveSeconds"></a>
The number of seconds to keep the session alive after the query finishes. The maximum time a session can keep alive is 24 hours. After 24 hours, the session is forced closed and the query is terminated.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 86400.
Required: No

 ** [StatementName](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-StatementName"></a>
The name of the SQL statements. You can name the SQL statements when you create them to identify the query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [WaitTimeSeconds](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-WaitTimeSeconds"></a>
The number of seconds to wait for all SQL statements in the batch to complete execution before returning the response. If the SQL statements do not complete within the specified time, the response returns the current status. The maximum value is 30 seconds.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: No

 ** [WithEvent](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-WithEvent"></a>
A value that indicates whether to send an event to the Amazon EventBridge event bus after the SQL statements run.
Type: Boolean
Required: No

 ** [WorkgroupName](#API_BatchExecuteStatement_RequestSyntax) **   <a name="redshiftdata-BatchExecuteStatement-request-WorkgroupName"></a>
The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `([a-z0-9-]{3,63}|arn:(aws(-[a-z]+)*):redshift-serverless:([a-z]{2}(-gov|(-iso[a-z]?))?|eusc-[a-z]+)-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

## Response Syntax
<a name="API_BatchExecuteStatement_ResponseSyntax"></a>

```
{
   "ClusterIdentifier": "string",
   "CreatedAt": number,
   "Database": "string",
   "DbGroups": [ "string" ],
   "DbUser": "string",
   "HasResultSet": boolean,
   "Id": "string",
   "RedshiftPid": number,
   "SecretArn": "string",
   "SessionId": "string",
   "Status": "string",
   "WorkgroupName": "string"
}
```

## Response Elements
<a name="API_BatchExecuteStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ClusterIdentifier](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-ClusterIdentifier"></a>
The cluster identifier. This element is not returned when connecting to a serverless workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [CreatedAt](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-CreatedAt"></a>
The date and time (UTC) the statement was created.
Type: Timestamp

 ** [Database](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-Database"></a>
The name of the database.
Type: String

 ** [DbGroups](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-DbGroups"></a>
A list of colon (:) separated names of database groups.
Type: Array of strings

 ** [DbUser](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-DbUser"></a>
The database user name.
Type: String

 ** [HasResultSet](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-HasResultSet"></a>
A value that indicates whether the statement has a result set. The result set can be empty. The value is true for an empty result set. The value is true if any substatement returns a result set.
Type: Boolean

 ** [Id](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-Id"></a>
The identifier of the SQL statement whose results are to be fetched. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. This identifier is returned by `BatchExecuteStatment`.
Type: String
Pattern: `[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d{0,2})?`

 ** [RedshiftPid](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-RedshiftPid"></a>
The process identifier from Amazon Redshift.
Type: Long

 ** [SecretArn](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-SecretArn"></a>
The name or ARN of the secret that enables access to the database.
Type: String

 ** [SessionId](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-SessionId"></a>
The session identifier of the query.
Type: String
Pattern: `[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}(:\d{0,2})?`

 ** [Status](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-Status"></a>
The status of the SQL statement. Status values are defined as follows:
+ ABORTED - The query run was stopped by the user.
+ FAILED - The query run failed.
+ FINISHED - The query has finished running.
+ PICKED - The query has been chosen to be run.
+ STARTED - The query run has started.
+ SUBMITTED - The query was submitted, but not yet processed.
Type: String
Valid Values: `SUBMITTED | PICKED | STARTED | FINISHED | ABORTED | FAILED`

 ** [WorkgroupName](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="redshiftdata-BatchExecuteStatement-response-WorkgroupName"></a>
The serverless workgroup name or Amazon Resource Name (ARN). This element is not returned when connecting to a provisioned cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `([a-z0-9-]{3,63}|arn:(aws(-[a-z]+)*):redshift-serverless:([a-z]{2}(-gov|(-iso[a-z]?))?|eusc-[a-z]+)-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`

## Errors
<a name="API_BatchExecuteStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActiveSessionsExceededException **
The Amazon Redshift Data API operation failed because the maximum number of active sessions exceeded.
HTTP Status Code: 400

 ** ActiveStatementsExceededException **
The number of active statements exceeds the limit.
HTTP Status Code: 400

 ** BatchExecuteStatementException **
An SQL statement encountered an environmental error while running.
 ** StatementId **
Statement identifier of the exception.
HTTP Status Code: 500

 ** InternalServerException **
The Amazon Redshift Data API operation failed due to invalid input.
 ** Message **
The exception message.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The Amazon Redshift Data API operation failed due to a missing resource.
 ** Message **
The exception message.
 ** ResourceId **
Resource identifier associated with the exception.
HTTP Status Code: 400

 ** ValidationException **
The Amazon Redshift Data API operation failed due to invalid input.
 ** Message **
The exception message.
HTTP Status Code: 400

## See Also
<a name="API_BatchExecuteStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-data-2019-12-20/BatchExecuteStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/BatchExecuteStatement)
