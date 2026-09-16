---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_ListRasterDataCollections.html
---

# ListRasterDataCollections
<a name="API_geospatial_ListRasterDataCollections"></a>

Use this operation to get raster data collections.

## Request Syntax
<a name="API_geospatial_ListRasterDataCollections_RequestSyntax"></a>

```
GET /raster-data-collections?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geospatial_ListRasterDataCollections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_geospatial_ListRasterDataCollections_RequestSyntax) **   <a name="sagemaker-geospatial_ListRasterDataCollections-request-uri-MaxResults"></a>
The total number of items to return.
Valid Range: Minimum value of 1. Maximum value of 20.

 ** [NextToken](#API_geospatial_ListRasterDataCollections_RequestSyntax) **   <a name="sagemaker-geospatial_ListRasterDataCollections-request-uri-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Length Constraints: Minimum length of 0. Maximum length of 8192.

## Request Body
<a name="API_geospatial_ListRasterDataCollections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geospatial_ListRasterDataCollections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "RasterDataCollectionSummaries": [
      {
         "Arn": "string",
         "Description": "string",
         "DescriptionPageUrl": "string",
         "Name": "string",
         "SupportedFilters": [
            {
               "Maximum": number,
               "Minimum": number,
               "Name": "string",
               "Type": "string"
            }
         ],
         "Tags": {
            "string" : "string"
         },
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_geospatial_ListRasterDataCollections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_geospatial_ListRasterDataCollections_ResponseSyntax) **   <a name="sagemaker-geospatial_ListRasterDataCollections-response-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.

 ** [RasterDataCollectionSummaries](#API_geospatial_ListRasterDataCollections_ResponseSyntax) **   <a name="sagemaker-geospatial_ListRasterDataCollections-response-RasterDataCollectionSummaries"></a>
Contains summary information about the raster data collection.
Type: Array of [RasterDataCollectionMetadata](API_geospatial_RasterDataCollectionMetadata.md) objects

## Errors
<a name="API_geospatial_ListRasterDataCollections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
 ** ResourceId **

HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
 ** ResourceId **
Identifier of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** ResourceId **

HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** ResourceId **

HTTP Status Code: 400

## See Also
<a name="API_geospatial_ListRasterDataCollections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/ListRasterDataCollections)
