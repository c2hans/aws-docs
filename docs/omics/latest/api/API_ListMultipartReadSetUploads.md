---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListMultipartReadSetUploads.html
---

# ListMultipartReadSetUploads
<a name="API_ListMultipartReadSetUploads"></a>

Lists in-progress multipart read set uploads for a sequence store and returns it in a JSON formatted output. Multipart read set uploads are initiated by the `CreateMultipartReadSetUploads` API operation. This operation returns a response with no body when the upload is complete.

## Request Syntax
<a name="API_ListMultipartReadSetUploads_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/uploads?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMultipartReadSetUploads_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMultipartReadSetUploads_RequestSyntax) **   <a name="omics-ListMultipartReadSetUploads-request-uri-maxResults"></a>
The maximum number of multipart uploads returned in a page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListMultipartReadSetUploads_RequestSyntax) **   <a name="omics-ListMultipartReadSetUploads-request-uri-nextToken"></a>
Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceStoreId](#API_ListMultipartReadSetUploads_RequestSyntax) **   <a name="omics-ListMultipartReadSetUploads-request-uri-sequenceStoreId"></a>
The Sequence Store ID used for the multipart uploads.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_ListMultipartReadSetUploads_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMultipartReadSetUploads_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "uploads": [
      {
         "creationTime": "string",
         "description": "string",
         "generatedFrom": "string",
         "name": "string",
         "referenceArn": "string",
         "sampleId": "string",
         "sequenceStoreId": "string",
         "sourceFileType": "string",
         "subjectId": "string",
         "tags": {
            "string" : "string"
         },
         "uploadId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListMultipartReadSetUploads_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListMultipartReadSetUploads_ResponseSyntax) **   <a name="omics-ListMultipartReadSetUploads-response-nextToken"></a>
Next token returned in the response of a previous ListMultipartReadSetUploads call. Used to get the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [uploads](#API_ListMultipartReadSetUploads_ResponseSyntax) **   <a name="omics-ListMultipartReadSetUploads-response-uploads"></a>
An array of multipart uploads.
Type: Array of [MultipartReadSetUploadListItem](API_MultipartReadSetUploadListItem.md) objects

## Errors
<a name="API_ListMultipartReadSetUploads_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** NotSupportedOperationException **
 The operation is not supported by Amazon Omics, or the API does not exist.
HTTP Status Code: 405

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListMultipartReadSetUploads_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListMultipartReadSetUploads)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListMultipartReadSetUploads)
