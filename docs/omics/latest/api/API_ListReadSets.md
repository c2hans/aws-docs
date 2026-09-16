---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListReadSets.html
---

# ListReadSets
<a name="API_ListReadSets"></a>

Retrieves a list of read sets from a sequence store ID and returns the metadata in JSON format.

## Request Syntax
<a name="API_ListReadSets_RequestSyntax"></a>

```
POST /sequencestore/{{sequenceStoreId}}/readsets?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "createdAfter": "{{string}}",
      "createdBefore": "{{string}}",
      "creationType": "{{string}}",
      "generatedFrom": "{{string}}",
      "name": "{{string}}",
      "referenceArn": "{{string}}",
      "sampleId": "{{string}}",
      "status": "{{string}}",
      "subjectId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListReadSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListReadSets_RequestSyntax) **   <a name="omics-ListReadSets-request-uri-maxResults"></a>
The maximum number of read sets to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListReadSets_RequestSyntax) **   <a name="omics-ListReadSets-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceStoreId](#API_ListReadSets_RequestSyntax) **   <a name="omics-ListReadSets-request-uri-sequenceStoreId"></a>
The jobs' sequence store ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_ListReadSets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListReadSets_RequestSyntax) **   <a name="omics-ListReadSets-request-filter"></a>
A filter to apply to the list.
Type: [ReadSetFilter](API_ReadSetFilter.md) object
Required: No

## Response Syntax
<a name="API_ListReadSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "readSets": [
      {
         "arn": "string",
         "creationTime": "string",
         "creationType": "string",
         "description": "string",
         "etag": {
            "algorithm": "string",
            "source1": "string",
            "source2": "string"
         },
         "fileType": "string",
         "id": "string",
         "name": "string",
         "referenceArn": "string",
         "sampleId": "string",
         "sequenceInformation": {
            "alignment": "string",
            "generatedFrom": "string",
            "totalBaseCount": number,
            "totalReadCount": number
         },
         "sequenceStoreId": "string",
         "status": "string",
         "statusMessage": "string",
         "subjectId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReadSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReadSets_ResponseSyntax) **   <a name="omics-ListReadSets-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [readSets](#API_ListReadSets_ResponseSyntax) **   <a name="omics-ListReadSets-response-readSets"></a>
A list of read sets.
Type: Array of [ReadSetListItem](API_ReadSetListItem.md) objects

## Errors
<a name="API_ListReadSets_Errors"></a>

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
<a name="API_ListReadSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListReadSets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListReadSets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListReadSets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListReadSets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListReadSets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListReadSets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListReadSets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListReadSets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListReadSets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListReadSets)
