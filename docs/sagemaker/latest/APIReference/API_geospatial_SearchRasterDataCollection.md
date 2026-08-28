---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html
---

# SearchRasterDataCollection
<a name="API_geospatial_SearchRasterDataCollection"></a>

Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.

## Request Syntax
<a name="API_geospatial_SearchRasterDataCollection_RequestSyntax"></a>

```
POST /search-raster-data-collection HTTP/1.1
Content-type: application/json

{
   "Arn": "{{string}}",
   "NextToken": "{{string}}",
   "RasterDataCollectionQuery": {
      "AreaOfInterest": { ... },
      "BandFilter": [ "{{string}}" ],
      "PropertyFilters": {
         "LogicalOperator": "{{string}}",
         "Properties": [
            {
               "Property": { ... }
            }
         ]
      },
      "TimeRangeFilter": {
         "EndTime": {{number}},
         "StartTime": {{number}}
      }
   }
}
```

## URI Request Parameters
<a name="API_geospatial_SearchRasterDataCollection_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_geospatial_SearchRasterDataCollection_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Arn](#API_geospatial_SearchRasterDataCollection_RequestSyntax) **   <a name="sagemaker-geospatial_SearchRasterDataCollection-request-Arn"></a>
The Amazon Resource Name (ARN) of the raster data collection.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}`
Required: Yes

 ** [NextToken](#API_geospatial_SearchRasterDataCollection_RequestSyntax) **   <a name="sagemaker-geospatial_SearchRasterDataCollection-request-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** [RasterDataCollectionQuery](#API_geospatial_SearchRasterDataCollection_RequestSyntax) **   <a name="sagemaker-geospatial_SearchRasterDataCollection-request-RasterDataCollectionQuery"></a>
RasterDataCollectionQuery consisting of [AreaOfInterest(AOI)](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html), [PropertyFilters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html) and [TimeRangeFilterInput](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html) used in [SearchRasterDataCollection](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html).
Type: [RasterDataCollectionQueryWithBandFilterInput](API_geospatial_RasterDataCollectionQueryWithBandFilterInput.md) object
Required: Yes

## Response Syntax
<a name="API_geospatial_SearchRasterDataCollection_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateResultCount": number,
   "Items": [
      {
         "Assets": {
            "string" : {
               "Href": "string"
            }
         },
         "DateTime": number,
         "Geometry": {
            "Coordinates": [
               [
                  [ number ]
               ]
            ],
            "Type": "string"
         },
         "Id": "string",
         "Properties": {
            "EoCloudCover": number,
            "LandsatCloudCoverLand": number,
            "Platform": "string",
            "ViewOffNadir": number,
            "ViewSunAzimuth": number,
            "ViewSunElevation": number
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_geospatial_SearchRasterDataCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateResultCount](#API_geospatial_SearchRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_SearchRasterDataCollection-response-ApproximateResultCount"></a>
Approximate number of results in the response.
Type: Integer

 ** [Items](#API_geospatial_SearchRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_SearchRasterDataCollection-response-Items"></a>
List of items matching the Raster DataCollectionQuery.
Type: Array of [ItemSource](API_geospatial_ItemSource.md) objects

 ** [NextToken](#API_geospatial_SearchRasterDataCollection_ResponseSyntax) **   <a name="sagemaker-geospatial_SearchRasterDataCollection-response-NextToken"></a>
If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.

## Errors
<a name="API_geospatial_SearchRasterDataCollection_Errors"></a>

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
<a name="API_geospatial_SearchRasterDataCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/SearchRasterDataCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
