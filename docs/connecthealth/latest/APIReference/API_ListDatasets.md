---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListDatasets.html
---

# ListDatasets
<a name="API_ListDatasets"></a>

Lists the Datasets in a Domain. You can list only the datasets of one type. The operation doesn't return datasets whose status is DELETED, and the order of the results isn't specified. We recommend using pagination to ensure that the operation returns quickly and successfully.

Datasets are in preview release and are subject to change.

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
GET /domains/{{domainId}}/datasets?maxResults={{maxResults}}&nextToken={{nextToken}}&type={{type}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_ListDatasets_RequestSyntax) **   <a name="connecthealth-ListDatasets-request-uri-domainId"></a>
The unique identifier of the parent Domain.
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `(hai-|dom-)[a-z0-9]+`
Required: Yes

 ** [maxResults](#API_ListDatasets_RequestSyntax) **   <a name="connecthealth-ListDatasets-request-uri-maxResults"></a>
The maximum number of datasets to return in one page. The default is 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListDatasets_RequestSyntax) **   <a name="connecthealth-ListDatasets-request-uri-nextToken"></a>
The token for the next page of results, from a previous ListDatasets response. If you don't specify a value, the operation returns the first page of results.

 ** [type](#API_ListDatasets_RequestSyntax) **   <a name="connecthealth-ListDatasets-request-uri-type"></a>
Returns only datasets of this type.
Valid Values: `MEDICAL_CODING`

## Request Body
<a name="API_ListDatasets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "createdAt": number,
         "datasetId": "string",
         "name": "string",
         "status": "string",
         "statusDetails": "string",
         "type": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDatasets_ResponseSyntax) **   <a name="connecthealth-ListDatasets-response-items"></a>
A list of dataset summaries.
Type: Array of [DatasetSummary](API_DatasetSummary.md) objects

 ** [nextToken](#API_ListDatasets_ResponseSyntax) **   <a name="connecthealth-ListDatasets-response-nextToken"></a>
The token for the next page of results. Not returned if there are no more results.
Type: String

## Errors
<a name="API_ListDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
This error is thrown when the client does not supply proper credentials to the API.
HTTP Status Code: 401

 ** InternalServerException **
This error is thrown when a transient error causes our API to fail.
HTTP Status Code: 500

 ** ResourceNotFoundException **
This error is thrown when the requested resource is not found.
HTTP Status Code: 404

 ** ThrottlingException **
This error is thrown when the client exceeds the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
This error is thrown when the client supplies invalid input to the API.
HTTP Status Code: 400

## See Also
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connecthealth-2025-01-29/ListDatasets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/ListDatasets)
