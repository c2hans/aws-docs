---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_RestoreTableFromSnapshot.html
---

# RestoreTableFromSnapshot
<a name="API_RestoreTableFromSnapshot"></a>

Restores a table from a snapshot to your Amazon Redshift Serverless instance. You can't use this operation to restore tables with [interleaved sort keys](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html#t_Sorting_data-interleaved).

## Request Syntax
<a name="API_RestoreTableFromSnapshot_RequestSyntax"></a>

```
{
   "activateCaseSensitiveIdentifier": {{boolean}},
   "namespaceName": "{{string}}",
   "newTableName": "{{string}}",
   "snapshotName": "{{string}}",
   "sourceDatabaseName": "{{string}}",
   "sourceSchemaName": "{{string}}",
   "sourceTableName": "{{string}}",
   "targetDatabaseName": "{{string}}",
   "targetSchemaName": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_RestoreTableFromSnapshot_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [activateCaseSensitiveIdentifier](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-activateCaseSensitiveIdentifier"></a>
Indicates whether name identifiers for database, schema, and table are case sensitive. If true, the names are case sensitive. If false, the names are not case sensitive. The default is false.
Type: Boolean
Required: No

 ** [namespaceName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-namespaceName"></a>
The namespace of the snapshot to restore from.
Type: String
Required: Yes

 ** [newTableName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-newTableName"></a>
The name of the table to create from the restore operation.
Type: String
Required: Yes

 ** [snapshotName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-snapshotName"></a>
The name of the snapshot to restore the table from.
Type: String
Required: Yes

 ** [sourceDatabaseName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-sourceDatabaseName"></a>
The name of the source database that contains the table being restored.
Type: String
Required: Yes

 ** [sourceSchemaName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-sourceSchemaName"></a>
The name of the source schema that contains the table being restored.
Type: String
Required: No

 ** [sourceTableName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-sourceTableName"></a>
The name of the source table being restored.
Type: String
Required: Yes

 ** [targetDatabaseName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-targetDatabaseName"></a>
The name of the database to restore the table to.
Type: String
Required: No

 ** [targetSchemaName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-targetSchemaName"></a>
The name of the schema to restore the table to.
Type: String
Required: No

 ** [workgroupName](#API_RestoreTableFromSnapshot_RequestSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-request-workgroupName"></a>
The workgroup to restore the table to.
Type: String
Required: Yes

## Response Syntax
<a name="API_RestoreTableFromSnapshot_ResponseSyntax"></a>

```
{
   "tableRestoreStatus": {
      "message": "string",
      "namespaceName": "string",
      "newTableName": "string",
      "progressInMegaBytes": number,
      "recoveryPointId": "string",
      "requestTime": number,
      "snapshotName": "string",
      "sourceDatabaseName": "string",
      "sourceSchemaName": "string",
      "sourceTableName": "string",
      "status": "string",
      "tableRestoreRequestId": "string",
      "targetDatabaseName": "string",
      "targetSchemaName": "string",
      "totalDataInMegaBytes": number,
      "workgroupName": "string"
   }
}
```

## Response Elements
<a name="API_RestoreTableFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tableRestoreStatus](#API_RestoreTableFromSnapshot_ResponseSyntax) **   <a name="redshiftserverless-RestoreTableFromSnapshot-response-tableRestoreStatus"></a>
The TableRestoreStatus object that contains the status of the restore operation.
Type: [TableRestoreStatus](API_TableRestoreStatus.md) object

## Errors
<a name="API_RestoreTableFromSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The submitted action has conflicts.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RestoreTableFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/RestoreTableFromSnapshot)
