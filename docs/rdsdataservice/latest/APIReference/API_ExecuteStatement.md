---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteStatement.html
---

# ExecuteStatement
<a name="API_ExecuteStatement"></a>

Runs a SQL statement against a database.

**Note**
If a call isn't part of a transaction because it doesn't include the `transactionID` parameter, changes that result from the call are committed automatically.
If the binary response data from the database is more than 1 MB, the call is terminated.

## Request Syntax
<a name="API_ExecuteStatement_RequestSyntax"></a>

```
POST /Execute HTTP/1.1
Content-type: application/json

{
   "continueAfterTimeout": {{boolean}},
   "database": "{{string}}",
   "formatRecordsAs": "{{string}}",
   "includeResultMetadata": {{boolean}},
   "parameters": [
      {
         "name": "{{string}}",
         "typeHint": "{{string}}",
         "value": { ... }
      }
   ],
   "resourceArn": "{{string}}",
   "resultSetOptions": {
      "decimalReturnType": "{{string}}",
      "longReturnType": "{{string}}"
   },
   "schema": "{{string}}",
   "secretArn": "{{string}}",
   "sql": "{{string}}",
   "transactionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExecuteStatement_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExecuteStatement_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [continueAfterTimeout](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-continueAfterTimeout"></a>
A value that indicates whether to continue running the statement after the call times out. By default, the statement stops running when the call times out.
For DDL statements, we recommend continuing to run the statement after the call times out. When a DDL statement terminates before it is finished running, it can result in errors and possibly corrupted data structures.
Type: Boolean
Required: No

 ** [database](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-database"></a>
The name of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [formatRecordsAs](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-formatRecordsAs"></a>
A value that indicates whether to format the result set as a single JSON string. This parameter only applies to `SELECT` statements and is ignored for other types of statements. Allowed values are `NONE` and `JSON`. The default value is `NONE`. The result is returned in the `formattedRecords` field.
For usage information about the JSON format for result sets, see [Using the Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon Aurora User Guide*.
Type: String
Valid Values: `NONE | JSON`
Required: No

 ** [includeResultMetadata](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-includeResultMetadata"></a>
A value that indicates whether to include metadata in the results.
Type: Boolean
Required: No

 ** [parameters](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-parameters"></a>
The parameters for the SQL statement.
Array parameters are not supported.
Type: Array of [SqlParameter](API_SqlParameter.md) objects
Required: No

 ** [resourceArn](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [resultSetOptions](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-resultSetOptions"></a>
Options that control how the result set is returned.
Type: [ResultSetOptions](API_ResultSetOptions.md) object
Required: No

 ** [schema](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-schema"></a>
The name of the database schema.
Currently, the `schema` parameter isn't supported.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [secretArn](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-secretArn"></a>
The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.
For information about creating the secret, see [Create a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html).
When you use the CLI on Linux to reference a secret created in the RDS console, the ARN might include special characters like `rds!cluster`. If you enclose the ARN in double quotes, the `!` character might trigger a shell expansion error, such as `-bash: !cluster: event not found`. To avoid this, escape the exclamation mark (\\\!) in the ARN or enclose the entire ARN in single quotes (') instead of double quotes.
Alternatively, disable shell history expansion by running `set +H` before you execute the command.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [sql](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-sql"></a>
The SQL statement to run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: Yes

 ** [transactionId](#API_ExecuteStatement_RequestSyntax) **   <a name="rdsdtataservice-ExecuteStatement-request-transactionId"></a>
The identifier of a transaction that was started by using the `BeginTransaction` operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.
If the SQL statement is not part of a transaction, don't set this parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 192.
Required: No

## Response Syntax
<a name="API_ExecuteStatement_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "columnMetadata": [
      {
         "arrayBaseColumnType": number,
         "isAutoIncrement": boolean,
         "isCaseSensitive": boolean,
         "isCurrency": boolean,
         "isSigned": boolean,
         "label": "string",
         "name": "string",
         "nullable": number,
         "precision": number,
         "scale": number,
         "schemaName": "string",
         "tableName": "string",
         "type": number,
         "typeName": "string"
      }
   ],
   "formattedRecords": "string",
   "generatedFields": [
      { ... }
   ],
   "numberOfRecordsUpdated": number,
   "records": [
      [
         { ... }
      ]
   ]
}
```

## Response Elements
<a name="API_ExecuteStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [columnMetadata](#API_ExecuteStatement_ResponseSyntax) **   <a name="rdsdtataservice-ExecuteStatement-response-columnMetadata"></a>
Metadata for the columns included in the results. This field is blank if the `formatRecordsAs` parameter is set to `JSON`.
Type: Array of [ColumnMetadata](API_ColumnMetadata.md) objects

 ** [formattedRecords](#API_ExecuteStatement_ResponseSyntax) **   <a name="rdsdtataservice-ExecuteStatement-response-formattedRecords"></a>
A string value that represents the result set of a `SELECT` statement in JSON format. This value is only present when the `formatRecordsAs` parameter is set to `JSON`.
The size limit for this field is currently 10 MB. If the JSON-formatted string representing the result set requires more than 10 MB, the call returns an error.
Type: String

 ** [generatedFields](#API_ExecuteStatement_ResponseSyntax) **   <a name="rdsdtataservice-ExecuteStatement-response-generatedFields"></a>
Values for fields generated during a DML request.
The `generatedFields` data isn't supported by Aurora PostgreSQL. To get the values of generated fields, use the `RETURNING` clause. For more information, see [Returning Data From Modified Rows](https://www.postgresql.org/docs/10/dml-returning.html) in the PostgreSQL documentation.
Type: Array of [Field](API_Field.md) objects

 ** [numberOfRecordsUpdated](#API_ExecuteStatement_ResponseSyntax) **   <a name="rdsdtataservice-ExecuteStatement-response-numberOfRecordsUpdated"></a>
The number of records updated by the request.
Type: Long

 ** [records](#API_ExecuteStatement_ResponseSyntax) **   <a name="rdsdtataservice-ExecuteStatement-response-records"></a>
The records returned by the SQL statement. This field is blank if the `formatRecordsAs` parameter is set to `JSON`.
Type: Array of arrays of [Field](API_Field.md) objects

## Errors
<a name="API_ExecuteStatement_Errors"></a>

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

 ** UnsupportedResultException **
There was a problem with the result because of one of the following conditions:
+ It contained an unsupported data type.
+ It contained a multidimensional array.
+ The size was too large.
HTTP Status Code: 400

## See Also
<a name="API_ExecuteStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rds-data-2018-08-01/ExecuteStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/ExecuteStatement)
