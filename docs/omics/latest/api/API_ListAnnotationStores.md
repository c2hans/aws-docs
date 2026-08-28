---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListAnnotationStores.html
---

# ListAnnotationStores
<a name="API_ListAnnotationStores"></a>

**Important**
 AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html).

Retrieves a list of annotation stores.

## Request Syntax
<a name="API_ListAnnotationStores_RequestSyntax"></a>

```
POST /annotationStores?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "status": "{{string}}"
   },
   "ids": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListAnnotationStores_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAnnotationStores_RequestSyntax) **   <a name="omics-ListAnnotationStores-request-uri-maxResults"></a>
The maximum number of stores to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAnnotationStores_RequestSyntax) **   <a name="omics-ListAnnotationStores-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10000.

## Request Body
<a name="API_ListAnnotationStores_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListAnnotationStores_RequestSyntax) **   <a name="omics-ListAnnotationStores-request-filter"></a>
A filter to apply to the list.
Type: [ListAnnotationStoresFilter](API_ListAnnotationStoresFilter.md) object
Required: No

 ** [ids](#API_ListAnnotationStores_RequestSyntax) **   <a name="omics-ListAnnotationStores-request-ids"></a>
IDs of stores to list.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

## Response Syntax
<a name="API_ListAnnotationStores_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "annotationStores": [
      {
         "creationTime": "string",
         "description": "string",
         "id": "string",
         "name": "string",
         "reference": { ... },
         "sseConfig": {
            "keyArn": "string",
            "type": "string"
         },
         "status": "string",
         "statusMessage": "string",
         "storeArn": "string",
         "storeFormat": "string",
         "storeSizeBytes": number,
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnnotationStores_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [annotationStores](#API_ListAnnotationStores_ResponseSyntax) **   <a name="omics-ListAnnotationStores-response-annotationStores"></a>
A list of stores.
Type: Array of [AnnotationStoreItem](API_AnnotationStoreItem.md) objects

 ** [nextToken](#API_ListAnnotationStores_ResponseSyntax) **   <a name="omics-ListAnnotationStores-response-nextToken"></a>
A pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListAnnotationStores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

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
<a name="API_ListAnnotationStores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListAnnotationStores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListAnnotationStores)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
