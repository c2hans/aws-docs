---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_RasterDataCollectionQueryOutput.html
---

# RasterDataCollectionQueryOutput
<a name="API_geospatial_RasterDataCollectionQueryOutput"></a>

The output structure contains the Raster Data Collection Query input along with some additional metadata.

## Contents
<a name="API_geospatial_RasterDataCollectionQueryOutput_Contents"></a>

 ** RasterDataCollectionArn **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryOutput-RasterDataCollectionArn"></a>
The ARN of the Raster Data Collection against which the search is done.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}`
Required: Yes

 ** RasterDataCollectionName **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryOutput-RasterDataCollectionName"></a>
The name of the raster data collection.
Type: String
Required: Yes

 ** TimeRangeFilter **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryOutput-TimeRangeFilter"></a>
The TimeRange filter used in the search.
Type: [TimeRangeFilterOutput](API_geospatial_TimeRangeFilterOutput.md) object
Required: Yes

 ** AreaOfInterest **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryOutput-AreaOfInterest"></a>
The Area of Interest used in the search.
Type: [AreaOfInterest](API_geospatial_AreaOfInterest.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** PropertyFilters **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryOutput-PropertyFilters"></a>
Property filters used in the search.
Type: [PropertyFilters](API_geospatial_PropertyFilters.md) object
Required: No

## See Also
<a name="API_geospatial_RasterDataCollectionQueryOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
