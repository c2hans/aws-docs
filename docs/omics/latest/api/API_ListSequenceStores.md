---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListSequenceStores.html
---

# ListSequenceStores
<a name="API_ListSequenceStores"></a>

Retrieves a list of sequence stores and returns each sequence store's metadata.

For more information, see [Creating a HealthOmics sequence store](https://docs.aws.amazon.com/omics/latest/dev/create-sequence-store.html) in the * AWS HealthOmics User Guide*.

## Request Syntax
<a name="API_ListSequenceStores_RequestSyntax"></a>

```
POST /sequencestores?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "createdAfter": "{{string}}",
      "createdBefore": "{{string}}",
      "name": "{{string}}",
      "status": "{{string}}",
      "updatedAfter": "{{string}}",
      "updatedBefore": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListSequenceStores_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSequenceStores_RequestSyntax) **   <a name="omics-ListSequenceStores-request-uri-maxResults"></a>
The maximum number of stores to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSequenceStores_RequestSyntax) **   <a name="omics-ListSequenceStores-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Request Body
<a name="API_ListSequenceStores_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListSequenceStores_RequestSyntax) **   <a name="omics-ListSequenceStores-request-filter"></a>
A filter to apply to the list.
Type: [SequenceStoreFilter](API_SequenceStoreFilter.md) object
Required: No

## Response Syntax
<a name="API_ListSequenceStores_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sequenceStores": [
      {
         "arn": "string",
         "creationTime": "string",
         "description": "string",
         "eTagAlgorithmFamily": "string",
         "fallbackLocation": "string",
         "id": "string",
         "name": "string",
         "sseConfig": {
            "keyArn": "string",
            "type": "string"
         },
         "status": "string",
         "statusMessage": "string",
         "updateTime": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSequenceStores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSequenceStores_ResponseSyntax) **   <a name="omics-ListSequenceStores-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6144.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sequenceStores](#API_ListSequenceStores_ResponseSyntax) **   <a name="omics-ListSequenceStores-response-sequenceStores"></a>
A list of sequence stores.
Type: Array of [SequenceStoreDetail](API_SequenceStoreDetail.md) objects

## Errors
<a name="API_ListSequenceStores_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListSequenceStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListSequenceStores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListSequenceStores)
