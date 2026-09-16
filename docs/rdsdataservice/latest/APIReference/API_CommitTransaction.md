---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_CommitTransaction.html
---

# CommitTransaction
<a name="API_CommitTransaction"></a>

Ends a SQL transaction started with the `BeginTransaction` operation and commits the changes.

## Request Syntax
<a name="API_CommitTransaction_RequestSyntax"></a>

```
POST /CommitTransaction HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
   "secretArn": "{{string}}",
   "transactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CommitTransaction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CommitTransaction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceArn](#API_CommitTransaction_RequestSyntax) **   <a name="rdsdtataservice-CommitTransaction-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [secretArn](#API_CommitTransaction_RequestSyntax) **   <a name="rdsdtataservice-CommitTransaction-request-secretArn"></a>
The name or ARN of the secret that enables access to the DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [transactionId](#API_CommitTransaction_RequestSyntax) **   <a name="rdsdtataservice-CommitTransaction-request-transactionId"></a>
The identifier of the transaction to end and commit.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: Yes

## Response Syntax
<a name="API_CommitTransaction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "transactionStatus": "string"
}
```

## Response Elements
<a name="API_CommitTransaction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [transactionStatus](#API_CommitTransaction_ResponseSyntax) **   <a name="rdsdtataservice-CommitTransaction-response-transactionStatus"></a>
The status of the commit operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

## Errors
<a name="API_CommitTransaction_Errors"></a>

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

 ** NotFoundException **
The `resourceArn`, `secretArn`, or `transactionId` value can't be found.
 ** message **
The error message returned by this `NotFoundException` error.
HTTP Status Code: 404

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
<a name="API_CommitTransaction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-data-2018-08-01/CommitTransaction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/CommitTransaction)
