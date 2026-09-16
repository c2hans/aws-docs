---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListTables.html
---

# ListTables
<a name="API_ListTables"></a>

List the tables in a database. If neither `SchemaPattern` nor `TablePattern` are specified, then all tables in the database are returned. A token is returned to page through the table list. Depending on the authorization method, use one of the following combinations of request parameters:
+  AWS Secrets Manager - when connecting to a cluster, provide the `secret-arn` of a secret stored in AWS Secrets Manager which has `username` and `password`. The specified secret contains credentials to connect to the `database` you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (`dbClusterIdentifier`), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.
+ Temporary credentials - when connecting to your data warehouse, choose one of the following options:
  + When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo`. Also, permission to call the `redshift-serverless:GetCredentials` operation is required.
  + When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo`. Also, permission to call the `redshift:GetClusterCredentialsWithIAM` operation is required.
  + When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the `redshift:GetClusterCredentials` operation is required.

For more information about the Amazon Redshift Data API and AWS CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide*.

## Request Syntax
<a name="API_ListTables_RequestSyntax"></a>

```
{
   "ClusterIdentifier": "{{string}}",
   "ConnectedDatabase": "{{string}}",
   "Database": "{{string}}",
   "DbUser": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SchemaPattern": "{{string}}",
   "SecretArn": "{{string}}",
   "TablePattern": "{{string}}",
   "WorkgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTables_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Database](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-Database"></a>
The name of the database that contains the tables to list. If `ConnectedDatabase` is not specified, this is also the database to connect to with your authentication credentials.
Type: String
Required: Yes

 ** [ClusterIdentifier](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-ClusterIdentifier"></a>
The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: No

 ** [ConnectedDatabase](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-ConnectedDatabase"></a>
A database name. The connected database is specified when you connect with your authentication credentials.
Type: String
Required: No

 ** [DbUser](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-DbUser"></a>
The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials.
Type: String
Required: No

 ** [MaxResults](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-MaxResults"></a>
The maximum number of tables to return in the response. If more tables exist than fit in one response, then `NextToken` is returned to page through the results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [NextToken](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-NextToken"></a>
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.
Type: String
Required: No

 ** [SchemaPattern](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-SchemaPattern"></a>
A pattern to filter results by schema name. Within a schema pattern, "%" means match any substring of 0 or more characters and "\_" means match any one character. Only schema name entries matching the search pattern are returned. If `SchemaPattern` is not specified, then all tables that match `TablePattern` are returned. If neither `SchemaPattern` or `TablePattern` are specified, then all tables are returned.
Type: String
Required: No

 ** [SecretArn](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-SecretArn"></a>
The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using AWS Secrets Manager.
Type: String
Required: No

 ** [TablePattern](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-TablePattern"></a>
A pattern to filter results by table name. Within a table pattern, "%" means match any substring of 0 or more characters and "\_" means match any one character. Only table name entries matching the search pattern are returned. If `TablePattern` is not specified, then all tables that match `SchemaPattern`are returned. If neither `SchemaPattern` or `TablePattern` are specified, then all tables are returned.
Type: String
Required: No

 ** [WorkgroupName](#API_ListTables_RequestSyntax) **   <a name="redshiftdata-ListTables-request-WorkgroupName"></a>
The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either AWS Secrets Manager or temporary credentials.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `([a-z0-9-]{3,63}|arn:(aws(-[a-z]+)*):redshift-serverless:([a-z]{2}(-gov|(-iso[a-z]?))?|eusc-[a-z]+)-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

## Response Syntax
<a name="API_ListTables_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tables": [
      {
         "name": "string",
         "schema": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTables_ResponseSyntax) **   <a name="redshiftdata-ListTables-response-NextToken"></a>
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.
Type: String

 ** [Tables](#API_ListTables_ResponseSyntax) **   <a name="redshiftdata-ListTables-response-Tables"></a>
The tables that match the request pattern.
Type: Array of [TableMember](API_TableMember.md) objects

## Errors
<a name="API_ListTables_Errors"></a>

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
<a name="API_ListTables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-data-2019-12-20/ListTables)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/ListTables)
