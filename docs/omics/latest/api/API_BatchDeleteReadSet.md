---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_BatchDeleteReadSet.html
---

# BatchDeleteReadSet
<a name="API_BatchDeleteReadSet"></a>

Deletes one or more read sets. If the operation is successful, it returns a response with no body. If there is an error with deleting one of the read sets, the operation returns an error list. If the operation successfully deletes only a subset of files, it will return an error list for the remaining files that fail to be deleted. There is a limit of 100 read sets that can be deleted in each `BatchDeleteReadSet` API call.

## Request Syntax
<a name="API_BatchDeleteReadSet_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/readset/batch/delete HTTP/1.1
Content-type: application/json

{
   "ids": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteReadSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sequenceStoreId](#API_BatchDeleteReadSet_RequestSyntax) **   <a name="omics-BatchDeleteReadSet-request-uri-sequenceStoreId"></a>
The read sets' sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_BatchDeleteReadSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ids](#API_BatchDeleteReadSet_RequestSyntax) **   <a name="omics-BatchDeleteReadSet-request-ids"></a>
The read sets' IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteReadSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "code": "string",
         "id": "string",
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteReadSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchDeleteReadSet_ResponseSyntax) **   <a name="omics-BatchDeleteReadSet-response-errors"></a>
Errors returned by individual delete operations.
Type: Array of [ReadSetBatchError](API_ReadSetBatchError.md) objects

## Errors
<a name="API_BatchDeleteReadSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_BatchDeleteReadSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/BatchDeleteReadSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/BatchDeleteReadSet)
