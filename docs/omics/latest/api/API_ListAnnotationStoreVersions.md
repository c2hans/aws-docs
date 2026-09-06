---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListAnnotationStoreVersions.html
---

# ListAnnotationStoreVersions
<a name="API_ListAnnotationStoreVersions"></a>

 Lists the versions of an annotation store.

## Request Syntax
<a name="API_ListAnnotationStoreVersions_RequestSyntax"></a>

```
POST /annotationStore/{{name}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filter": {
      "status": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_ListAnnotationStoreVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAnnotationStoreVersions_RequestSyntax) **   <a name="omics-ListAnnotationStoreVersions-request-uri-maxResults"></a>
 The maximum number of annotation store versions to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [name](#API_ListAnnotationStoreVersions_RequestSyntax) **   <a name="omics-ListAnnotationStoreVersions-request-uri-name"></a>
 The name of an annotation store.
Required: Yes

 ** [nextToken](#API_ListAnnotationStoreVersions_RequestSyntax) **   <a name="omics-ListAnnotationStoreVersions-request-uri-nextToken"></a>
 Specifies the pagination token from a previous request to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10000.

## Request Body
<a name="API_ListAnnotationStoreVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListAnnotationStoreVersions_RequestSyntax) **   <a name="omics-ListAnnotationStoreVersions-request-filter"></a>
 A filter to apply to the list of annotation store versions.
Type: [ListAnnotationStoreVersionsFilter](API_ListAnnotationStoreVersionsFilter.md) object
Required: No

## Response Syntax
<a name="API_ListAnnotationStoreVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "annotationStoreVersions": [
      {
         "creationTime": "string",
         "description": "string",
         "id": "string",
         "name": "string",
         "status": "string",
         "statusMessage": "string",
         "storeId": "string",
         "updateTime": "string",
         "versionArn": "string",
         "versionName": "string",
         "versionSizeBytes": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnnotationStoreVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [annotationStoreVersions](#API_ListAnnotationStoreVersions_ResponseSyntax) **   <a name="omics-ListAnnotationStoreVersions-response-annotationStoreVersions"></a>
 Lists all versions of an annotation store.
Type: Array of [AnnotationStoreVersionItem](API_AnnotationStoreVersionItem.md) objects

 ** [nextToken](#API_ListAnnotationStoreVersions_ResponseSyntax) **   <a name="omics-ListAnnotationStoreVersions-response-nextToken"></a>
 Specifies the pagination token from a previous request to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListAnnotationStoreVersions_Errors"></a>

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
<a name="API_ListAnnotationStoreVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListAnnotationStoreVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListAnnotationStoreVersions)
