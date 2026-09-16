---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ListStatements.html
---

# ListStatements
<a name="API_ListStatements"></a>

List of SQL statements. By default, only finished statements are shown. A token is returned to page through the statement list.

When you use identity-enhanced role sessions to list statements, you must provide either the `cluster-identifier` or `workgroup-name` parameter. This ensures that the IdC user can only access the Amazon Redshift IdC applications they are assigned. For more information, see [ Trusted identity propagation overview](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html).

For more information about the Amazon Redshift Data API and AWS CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide*.

## Request Syntax
<a name="API_ListStatements_RequestSyntax"></a>

```
{
   "ClusterIdentifier": "{{string}}",
   "Database": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "RoleLevel": {{boolean}},
   "StatementName": "{{string}}",
   "Status": "{{string}}",
   "WorkgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStatements_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ClusterIdentifier](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-ClusterIdentifier"></a>
The cluster identifier. Only statements that ran on this cluster are returned. When providing `ClusterIdentifier`, then `WorkgroupName` can't be specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: No

 ** [Database](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-Database"></a>
The name of the database when listing statements run against a `ClusterIdentifier` or `WorkgroupName`.
Type: String
Required: No

 ** [MaxResults](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-MaxResults"></a>
The maximum number of SQL statements to return in the response. If more SQL statements exist than fit in one response, then `NextToken` is returned to page through the results.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-NextToken"></a>
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.
Type: String
Required: No

 ** [RoleLevel](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-RoleLevel"></a>
A value that filters which statements to return in the response. If true, all statements run by the caller's IAM role are returned. If false, only statements run by the caller's IAM role in the current IAM session are returned. The default is true.
Type: Boolean
Required: No

 ** [StatementName](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-StatementName"></a>
The name of the SQL statement specified as input to `BatchExecuteStatement` or `ExecuteStatement` to identify the query. You can list multiple statements by providing a prefix that matches the beginning of the statement name. For example, to list myStatement1, myStatement2, myStatement3, and so on, then provide the a value of `myStatement`. Data API does a case-sensitive match of SQL statement names to the prefix value you provide.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** [Status](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-Status"></a>
The status of the SQL statement to list. Status values are defined as follows:
+ ABORTED - The query run was stopped by the user.
+ ALL - A status value that includes all query statuses. This value can be used to filter results.
+ FAILED - The query run failed.
+ FINISHED - The query has finished running.
+ PICKED - The query has been chosen to be run.
+ STARTED - The query run has started.
+ SUBMITTED - The query was submitted, but not yet processed.
Type: String
Valid Values: `SUBMITTED | PICKED | STARTED | FINISHED | ABORTED | FAILED | ALL`
Required: No

 ** [WorkgroupName](#API_ListStatements_RequestSyntax) **   <a name="redshiftdata-ListStatements-request-WorkgroupName"></a>
The serverless workgroup name or Amazon Resource Name (ARN). Only statements that ran on this workgroup are returned. When providing `WorkgroupName`, then `ClusterIdentifier` can't be specified.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `([a-z0-9-]{3,63}|arn:(aws(-[a-z]+)*):redshift-serverless:([a-z]{2}(-gov|(-iso[a-z]?))?|eusc-[a-z]+)-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})`
Required: No

## Response Syntax
<a name="API_ListStatements_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Statements": [
      {
         "CreatedAt": number,
         "Id": "string",
         "IsBatchStatement": boolean,
         "QueryParameters": [
            {
               "name": "string",
               "value": "string"
            }
         ],
         "QueryString": "string",
         "QueryStrings": [ "string" ],
         "ResultFormat": "string",
         "SecretArn": "string",
         "SessionId": "string",
         "StatementName": "string",
         "Status": "string",
         "UpdatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_ListStatements_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Statements](#API_ListStatements_ResponseSyntax) **   <a name="redshiftdata-ListStatements-response-Statements"></a>
The SQL statements.
Type: Array of [StatementData](API_StatementData.md) objects

 ** [NextToken](#API_ListStatements_ResponseSyntax) **   <a name="redshiftdata-ListStatements-response-NextToken"></a>
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request.
Type: String

## Errors
<a name="API_ListStatements_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_ListStatements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/redshift-data-2019-12-20/ListStatements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/ListStatements)
