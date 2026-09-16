---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_BatchExecuteStatement.html
---

# BatchExecuteStatement
<a name="API_BatchExecuteStatement"></a>

Runs a batch SQL statement over an array of data.

You can run bulk update and insert operations for multiple records using a DML statement with different parameter sets. Bulk operations can provide a significant performance improvement over individual insert and update operations.

**Note**
If a call isn't part of a transaction because it doesn't include the `transactionID` parameter, changes that result from the call are committed automatically.
There isn't a fixed upper limit on the number of parameter sets. However, the maximum size of the HTTP request submitted through the Data API is 4 MiB. If the request exceeds this limit, the Data API returns an error and doesn't process the request. This 4-MiB limit includes the size of the HTTP headers and the JSON notation in the request. Thus, the number of parameter sets that you can include depends on a combination of factors, such as the size of the SQL statement and the size of each parameter set.
The response size limit is 1 MiB. If the call returns more than 1 MiB of response data, the call is terminated.

## Request Syntax
<a name="API_BatchExecuteStatement_RequestSyntax"></a>

```
POST /BatchExecute HTTP/1.1
Content-type: application/json

{
   "database": "{{string}}",
   "parameterSets": [
      [
         {
            "name": "{{string}}",
            "typeHint": "{{string}}",
            "value": { ... }
         }
      ]
   ],
   "resourceArn": "{{string}}",
   "schema": "{{string}}",
   "secretArn": "{{string}}",
   "sql": "{{string}}",
   "transactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_BatchExecuteStatement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchExecuteStatement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [database](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-database"></a>
The name of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [parameterSets](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-parameterSets"></a>
The parameter set for the batch operation.
The SQL statement is executed as many times as the number of parameter sets provided. To execute a SQL statement with no parameters, use one of the following options:
+ Specify one or more empty parameter sets.
+ Use the `ExecuteStatement` operation instead of the `BatchExecuteStatement` operation.
Array parameters are not supported.
Type: Array of arrays of [SqlParameter](API_SqlParameter.md) objects
Required: No

 ** [resourceArn](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [schema](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-schema"></a>
The name of the database schema.
Currently, the `schema` parameter isn't supported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [secretArn](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-secretArn"></a>
The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.
For information about creating the secret, see [Create a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html).
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [sql](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-sql"></a>
The SQL statement to run. Don't include a semicolon (;) at the end of the SQL statement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: Yes

 ** [transactionId](#API_BatchExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-request-transactionId"></a>
The identifier of a transaction that was started by using the `BeginTransaction` operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.
If the SQL statement is not part of a transaction, don't set this parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: No

## Response Syntax
<a name="API_BatchExecuteStatement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "updateResults": [
      {
         "generatedFields": [
            { ... }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchExecuteStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [updateResults](#API_BatchExecuteStatement_ResponseSyntax) **   <a name="rdsdtataservice-BatchExecuteStatement-response-updateResults"></a>
The execution results of each batch entry.
Type: Array of [UpdateResult](API_UpdateResult.md) objects

## Errors
<a name="API_BatchExecuteStatement_Errors"></a>

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora Serverless v1 databases.)
 ** message **
The error message returned by this `BadRequestException` error.
HTTP Status Code: 400

 ** DatabaseErrorException **
There was an error in processing the SQL statement.
HTTP Status Code: 400

 ** DatabaseNotFoundException **
The DB cluster doesn't have a DB instance.
HTTP Status Code: 404

 ** DatabaseResumingException **
A request was cancelled because the Aurora Serverless v2 DB instance was paused. The Data API request automatically resumes the DB instance. Wait a few seconds and try again.
HTTP Status Code: 400

 ** DatabaseUnavailableException **
The writer instance in the DB cluster isn't available.
HTTP Status Code: 504

 ** ForbiddenException **
There are insufficient privileges to make the call.
 ** message **
The error message returned by this `ForbiddenException` error.
HTTP Status Code: 403

 ** HttpEndpointNotEnabledException **
The HTTP endpoint for using RDS Data API isn't enabled for the DB cluster.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal error occurred.
HTTP Status Code: 500

 ** InvalidResourceStateException **
The resource is in an invalid state.
HTTP Status Code: 400

 ** InvalidSecretException **
The Secrets Manager secret used with the request isn't valid.
HTTP Status Code: 400

 ** SecretsErrorException **
There was a problem with the Secrets Manager secret used with the request, caused by one of the following conditions:
+ RDS Data API timed out retrieving the secret.
+ The secret provided wasn't found.
+ The secret couldn't be decrypted.
HTTP Status Code: 400

 ** ServiceUnavailableError **
The service specified by the `resourceArn` parameter isn't available.
HTTP Status Code: 503

 ** StatementTimeoutException **
The execution of the SQL statement timed out.
 ** dbConnectionId **
The database connection ID that executed the SQL statement.
 ** message **
The error message returned by this `StatementTimeoutException` error.
HTTP Status Code: 400

 ** TransactionNotFoundException **
The transaction ID wasn't found.
HTTP Status Code: 404

## See Also
<a name="API_BatchExecuteStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-data-2018-08-01/BatchExecuteStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/BatchExecuteStatement)
