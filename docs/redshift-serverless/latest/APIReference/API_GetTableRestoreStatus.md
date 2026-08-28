---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_GetTableRestoreStatus.html
---

# GetTableRestoreStatus
<a name="API_GetTableRestoreStatus"></a>

Returns information about a `TableRestoreStatus` object.

## Request Syntax
<a name="API_GetTableRestoreStatus_RequestSyntax"></a>

```
{
   "tableRestoreRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetTableRestoreStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [tableRestoreRequestId](#API_GetTableRestoreStatus_RequestSyntax) **   <a name="redshiftserverless-GetTableRestoreStatus-request-tableRestoreRequestId"></a>
The ID of the `RestoreTableFromSnapshot` request to return status for.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetTableRestoreStatus_ResponseSyntax"></a>

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
<a name="API_GetTableRestoreStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tableRestoreStatus](#API_GetTableRestoreStatus_ResponseSyntax) **   <a name="redshiftserverless-GetTableRestoreStatus-response-tableRestoreStatus"></a>
The returned `TableRestoreStatus` object that contains information about the status of your `RestoreTableFromSnapshot` request.
Type: [TableRestoreStatus](API_TableRestoreStatus.md) object

## Errors
<a name="API_GetTableRestoreStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetTableRestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/GetTableRestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/GetTableRestoreStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
