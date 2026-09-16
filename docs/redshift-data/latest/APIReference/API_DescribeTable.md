---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_DescribeTable.html
---

# DescribeTable
<a name="API_DescribeTable"></a>

Describes the detailed information about a table from metadata in the cluster. The information includes its columns. A token is returned to page through the column list. Depending on the authorization method, use one of the following combinations of request parameters:
+  AWS Secrets Manager - when connecting to a cluster, provide the `secret-arn` of a secret stored in AWS Secrets Manager which has `username` and `password`. The specified secret contains credentials to connect to the `database` you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (`dbClusterIdentifier`), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.
+ Temporary credentials - when connecting to your data warehouse, choose one of the following options:
  + When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo`. Also, permission to call the `redshift-serverless:GetCredentials` operation is required.
  + When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo`. Also, permission to call the `redshift:GetClusterCredentialsWithIAM` operation is required.
  + When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the `redshift:GetClusterCredentials` operation is required.

For more information about the Amazon Redshift Data API and AWS CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide*.

## Request Syntax
<a name="API_DescribeTable_RequestSyntax"></a>

```
{
   "ClusterIdentifier": "{{string}}",
   "ConnectedDatabase": "{{string}}",
   "Database": "{{string}}",
   "DbUser": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Schema": "{{string}}",
   "SecretArn": "{{string}}",
   "Table": "{{string}}",
   "WorkgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTable_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Database](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-Database"></a>
The name of the database that contains the tables to be described. If `ConnectedDatabase` is not specified, this is also the database to connect to with your authentication credentials.
Type: String
Required: Yes

 ** [ClusterIdentifier](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-ClusterIdentifier"></a>
The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: No

 ** [ConnectedDatabase](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-ConnectedDatabase"></a>
A database name. The connected database is specified when you connect with your authentication credentials.
Type: String
Required: No

 ** [DbUser](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-DbUser"></a>
The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials.
Type: String
Required: No

 ** [MaxResults](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-MaxResults"></a>
The maximum number of tables to return in the response. If more tables exist than fit in one response, then `NextToken` is returned to page through the results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [NextToken](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-NextToken"></a>
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.
Type: String
Required: No

 ** [Schema](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-Schema"></a>
The schema that contains the table. If no schema is specified, then matching tables for all schemas are returned.
Type: String
Required: No

 ** [SecretArn](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-SecretArn"></a>
The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using AWS Secrets Manager.
Type: String
Required: No

 ** [Table](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-Table"></a>
The table name. If no table is specified, then all tables for all matching schemas are returned. If no table and no schema is specified, then all tables for all schemas in the database are returned
Type: String
Required: No

 ** [WorkgroupName](#API_DescribeTable_RequestSyntax) **   <a name="redshiftdata-DescribeTable-request-WorkgroupName"></a>
The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `([a-z0-9-]{3,63}|arn:(aws(-[a-z]+)*):redshift-serverless:([a-z]{2}(-gov|(-iso[a-z]?))?|eusc-[a-z]+)-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

## Response Syntax
<a name="API_DescribeTable_ResponseSyntax"></a>

```
{
   "ColumnList": [
      {
         "columnDefault": "string",
         "isCaseSensitive": boolean,
         "isCurrency": boolean,
         "isSigned": boolean,
         "label": "string",
         "length": number,
         "name": "string",
         "nullable": number,
         "precision": number,
         "scale": number,
         "schemaName": "string",
         "tableName": "string",
         "typeName": "string"
      }
   ],
   "NextToken": "string",
   "TableName": "string"
}
```

## Response Elements
<a name="API_DescribeTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ColumnList](#API_DescribeTable_ResponseSyntax) **   <a name="redshiftdata-DescribeTable-response-ColumnList"></a>
A list of columns in the table.
Type: Array of [ColumnMetadata](API_ColumnMetadata.md) objects

 ** [NextToken](#API_DescribeTable_ResponseSyntax) **   <a name="redshiftdata-DescribeTable-response-NextToken"></a>
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.
Type: String

 ** [TableName](#API_DescribeTable_ResponseSyntax) **   <a name="redshiftdata-DescribeTable-response-TableName"></a>
The table name.
Type: String

## Errors
<a name="API_DescribeTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DatabaseConnectionException **
Connection to a database failed.
HTTP Status Code: 500

 ** InternalServerException **
The Amazon Redshift Data API operation failed due to invalid input.
 ** Message **
The exception message.
HTTP Status Code: 500

 ** QueryTimeoutException **
The Amazon Redshift Data API operation failed due to timeout.
HTTP Status Code: 400

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
<a name="API_DescribeTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-data-2019-12-20/DescribeTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/DescribeTable)
