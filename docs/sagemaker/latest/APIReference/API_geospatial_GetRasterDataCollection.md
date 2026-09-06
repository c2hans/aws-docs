---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_GetRasterDataCollection.html
---

# GetRasterDataCollection
<a name="API_geospatial_GetRasterDataCollection"></a>

Use this operation to get details of a specific raster data collection.

## Request Syntax
<a name="API_geospatial_GetRasterDataCollection_RequestSyntax"></a>

```
GET /raster-data-collection/{{Arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geospatial_GetRasterDataCollection_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Arn](#API_geospatial_GetRasterDataCollection_RequestSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-request-uri-Arn"></a>
The Amazon Resource Name (ARN) of the raster data collection.
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}`
Required: Yes

## Request Body
<a name="API_geospatial_GetRasterDataCollection_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geospatial_GetRasterDataCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "Description": "string",
   "DescriptionPageUrl": "string",
   "ImageSourceBands": [ "string" ],
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
```

## Response Elements
<a name="API_geospatial_GetRasterDataCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-Arn"></a>
The Amazon Resource Name (ARN) of the raster data collection.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}`

 ** [Description](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-Description"></a>
A description of the raster data collection.
Type: String

 ** [DescriptionPageUrl](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-DescriptionPageUrl"></a>
The URL of the description page.
Type: String

 ** [ImageSourceBands](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-ImageSourceBands"></a>
The list of image source bands in the raster data collection.
Type: Array of strings

 ** [Name](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-Name"></a>
The name of the raster data collection.
Type: String

 ** [SupportedFilters](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-SupportedFilters"></a>
The filters supported by the raster data collection.
Type: Array of [Filter](API_geospatial_Filter.md) objects

 ** [Tags](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-Tags"></a>
Each tag consists of a key and a value.
Type: String to string map

 ** [Type](#API_geospatial_GetRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_GetRasterDataCollection-response-Type"></a>
The raster data collection type.
Type: String
Valid Values: `PUBLIC | PREMIUM | USER`

## Errors
<a name="API_geospatial_GetRasterDataCollection_Errors"></a>

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
<a name="API_geospatial_GetRasterDataCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/GetRasterDataCollection)
