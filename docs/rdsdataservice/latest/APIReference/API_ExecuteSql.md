---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ExecuteSql.html
---

# ExecuteSql
<a name="API_ExecuteSql"></a>

Runs one or more SQL statements.

**Note**
This operation isn't supported for Aurora Serverless v2 and provisioned DB clusters. For Aurora Serverless v1 DB clusters, the operation is deprecated. Use the `BatchExecuteStatement` or `ExecuteStatement` operation.

## Request Syntax
<a name="API_ExecuteSql_RequestSyntax"></a>

```
POST /ExecuteSql HTTP/1.1
Content-type: application/json

{
   "awsSecretStoreArn": "{{string}}",
   "database": "{{string}}",
   "dbClusterOrInstanceArn": "{{string}}",
   "schema": "{{string}}",
   "sqlStatements": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExecuteSql_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ExecuteSql_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [awsSecretStoreArn](#API_ExecuteSql_RequestSyntax) **   <a name="rdsdtataservice-ExecuteSql-request-awsSecretStoreArn"></a>
The Amazon Resource Name (ARN) of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.
For information about creating the secret, see [Create a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html).
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [database](#API_ExecuteSql_RequestSyntax) **   <a name="rdsdtataservice-ExecuteSql-request-database"></a>
The name of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [dbClusterOrInstanceArn](#API_ExecuteSql_RequestSyntax) **   <a name="rdsdtataservice-ExecuteSql-request-dbClusterOrInstanceArn"></a>
The ARN of the Aurora Serverless DB cluster.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 100.
Required: Yes

 ** [schema](#API_ExecuteSql_RequestSyntax) **   <a name="rdsdtataservice-ExecuteSql-request-schema"></a>
The name of the database schema.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** [sqlStatements](#API_ExecuteSql_RequestSyntax) **   <a name="rdsdtataservice-ExecuteSql-request-sqlStatements"></a>
One or more SQL statements to run on the DB cluster.
You can separate SQL statements from each other with a semicolon (;). Any valid SQL statement is permitted, including data definition, data manipulation, and commit statements.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: Yes

## Response Syntax
<a name="API_ExecuteSql_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "sqlStatementResults": [
      {
         "numberOfRecordsUpdated": number,
         "resultFrame": {
            "records": [
               {
                  "values": [
                     { ... }
                  ]
               }
            ],
            "resultSetMetadata": {
               "columnCount": number,
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
               ]
            }
         }
      }
   ]
}
```

## Response Elements
<a name="API_ExecuteSql_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [sqlStatementResults](#API_ExecuteSql_ResponseSyntax) **   <a name="rdsdtataservice-ExecuteSql-response-sqlStatementResults"></a>
The results of the SQL statement or statements.
Type: Array of [SqlStatementResult](API_SqlStatementResult.md) objects

## Errors
<a name="API_ExecuteSql_Errors"></a>

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
There is an error in the call or in a SQL statement. (This error only appears in calls from Aurora Serverless v1 databases.)
 ** message **
The error message returned by this `BadRequestException` error.
HTTP Status Code: 400

 ** ForbiddenException **
There are insufficient privileges to make the call.
 ** message **
The error message returned by this `ForbiddenException` error.
HTTP Status Code: 403

 ** InternalServerErrorException **
An internal error occurred.
HTTP Status Code: 500

 ** ServiceUnavailableError **
The service specified by the `resourceArn` parameter isn't available.
HTTP Status Code: 503

## See Also
<a name="API_ExecuteSql_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-data-2018-08-01/ExecuteSql)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/ExecuteSql)
