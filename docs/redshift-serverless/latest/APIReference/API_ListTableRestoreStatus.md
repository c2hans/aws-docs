---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListTableRestoreStatus.html
---

# ListTableRestoreStatus
<a name="API_ListTableRestoreStatus"></a>

Returns information about an array of `TableRestoreStatus` objects.

## Request Syntax
<a name="API_ListTableRestoreStatus_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "namespaceName": "{{string}}",
   "nextToken": "{{string}}",
   "workgroupName": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTableRestoreStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTableRestoreStatus_RequestSyntax) **   <a name="redshiftserverless-ListTableRestoreStatus-request-maxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use nextToken to display the next page of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [namespaceName](#API_ListTableRestoreStatus_RequestSyntax) **   <a name="redshiftserverless-ListTableRestoreStatus-request-namespaceName"></a>
The namespace from which to list all of the statuses of `RestoreTableFromSnapshot` operations .
Type: String
Required: No

 ** [nextToken](#API_ListTableRestoreStatus_RequestSyntax) **   <a name="redshiftserverless-ListTableRestoreStatus-request-nextToken"></a>
If your initial `ListTableRestoreStatus` operation returns a nextToken, you can include the returned `nextToken` in following `ListTableRestoreStatus` operations. This will return results on the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

 ** [workgroupName](#API_ListTableRestoreStatus_RequestSyntax) **   <a name="redshiftserverless-ListTableRestoreStatus-request-workgroupName"></a>
The workgroup from which to list all of the statuses of `RestoreTableFromSnapshot` operations.
Type: String
Required: No

## Response Syntax
<a name="API_ListTableRestoreStatus_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tableRestoreStatuses": [
      {
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
   ]
}
```

## Response Elements
<a name="API_ListTableRestoreStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTableRestoreStatus_ResponseSyntax) **   <a name="redshiftserverless-ListTableRestoreStatus-response-nextToken"></a>
If your initial `ListTableRestoreStatus` operation returns a `nextToken`, you can include the returned `nextToken` in following `ListTableRestoreStatus` operations. This will returns results on the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [tableRestoreStatuses](#API_ListTableRestoreStatus_ResponseSyntax) **   <a name="redshiftserverless-ListTableRestoreStatus-response-tableRestoreStatuses"></a>
The array of returned `TableRestoreStatus` objects.
Type: Array of [TableRestoreStatus](API_TableRestoreStatus.md) objects

## Errors
<a name="API_ListTableRestoreStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPaginationException **
The provided pagination token is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The name of the resource that could not be found.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListTableRestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListTableRestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListTableRestoreStatus)
