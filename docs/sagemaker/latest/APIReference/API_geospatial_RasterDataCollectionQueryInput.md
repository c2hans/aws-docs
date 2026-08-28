---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_RasterDataCollectionQueryInput.html
---

# RasterDataCollectionQueryInput
<a name="API_geospatial_RasterDataCollectionQueryInput"></a>

The input structure for Raster Data Collection Query containing the Area of Interest, TimeRange Filters, and Property Filters.

## Contents
<a name="API_geospatial_RasterDataCollectionQueryInput_Contents"></a>

 ** RasterDataCollectionArn **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryInput-RasterDataCollectionArn"></a>
The Amazon Resource Name (ARN) of the raster data collection.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}`
Required: Yes

 ** TimeRangeFilter **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryInput-TimeRangeFilter"></a>
The TimeRange Filter used in the RasterDataCollection Query.
Type: [TimeRangeFilterInput](API_geospatial_TimeRangeFilterInput.md) object
Required: Yes

 ** AreaOfInterest **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryInput-AreaOfInterest"></a>
The area of interest being queried for the raster data collection.
Type: [AreaOfInterest](API_geospatial_AreaOfInterest.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** PropertyFilters **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryInput-PropertyFilters"></a>
The list of Property filters used in the Raster Data Collection Query.
Type: [PropertyFilters](API_geospatial_PropertyFilters.md) object
Required: No

## See Also
<a name="API_geospatial_RasterDataCollectionQueryInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
