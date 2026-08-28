---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListReadSetUploadParts.html
---

# ListReadSetUploadParts
<a name="API_ListReadSetUploadParts"></a>

Lists all parts in a multipart read set upload for a sequence store and returns the metadata in a JSON formatted output.

## Request Syntax
<a name="API_ListReadSetUploadParts_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/upload/{{uploadId}}/parts?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "createdAfter": "{{string}}",
      "createdBefore": "{{string}}"
   },
   "partSource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListReadSetUploadParts_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListReadSetUploadParts_RequestSyntax) **   <a name="omics-ListReadSetUploadParts-request-uri-maxResults"></a>
The maximum number of read set upload parts returned in a page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListReadSetUploadParts_RequestSyntax) **   <a name="omics-ListReadSetUploadParts-request-uri-nextToken"></a>
Next token returned in the response of a previous ListReadSetUploadPartsRequest call. Used to get the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceStoreId](#API_ListReadSetUploadParts_RequestSyntax) **   <a name="omics-ListReadSetUploadParts-request-uri-sequenceStoreId"></a>
The Sequence Store ID used for the multipart uploads.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

 ** [uploadId](#API_ListReadSetUploadParts_RequestSyntax) **   <a name="omics-ListReadSetUploadParts-request-uri-uploadId"></a>
The ID for the initiated multipart upload.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_ListReadSetUploadParts_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListReadSetUploadParts_RequestSyntax) **   <a name="omics-ListReadSetUploadParts-request-filter"></a>
Attributes used to filter for a specific subset of read set part uploads.
Type: [ReadSetUploadPartListFilter](API_ReadSetUploadPartListFilter.md) object
Required: No

 ** [partSource](#API_ListReadSetUploadParts_RequestSyntax) **   <a name="omics-ListReadSetUploadParts-request-partSource"></a>
The source file for the upload part.
Type: String
Valid Values: `SOURCE1 | SOURCE2`
Required: Yes

## Response Syntax
<a name="API_ListReadSetUploadParts_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "parts": [
      {
         "checksum": "string",
         "creationTime": "string",
         "lastUpdatedTime": "string",
         "partNumber": number,
         "partSize": number,
         "partSource": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReadSetUploadParts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReadSetUploadParts_ResponseSyntax) **   <a name="omics-ListReadSetUploadParts-response-nextToken"></a>
Next token returned in the response of a previous ListReadSetUploadParts call. Used to get the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [parts](#API_ListReadSetUploadParts_ResponseSyntax) **   <a name="omics-ListReadSetUploadParts-response-parts"></a>
An array of upload parts.
Type: Array of [ReadSetUploadPartListItem](API_ReadSetUploadPartListItem.md) objects

## Errors
<a name="API_ListReadSetUploadParts_Errors"></a>

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
<a name="API_ListReadSetUploadParts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListReadSetUploadParts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListReadSetUploadParts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
