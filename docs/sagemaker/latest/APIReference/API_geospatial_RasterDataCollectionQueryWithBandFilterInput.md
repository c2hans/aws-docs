---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_RasterDataCollectionQueryWithBandFilterInput.html
---

# RasterDataCollectionQueryWithBandFilterInput
<a name="API_geospatial_RasterDataCollectionQueryWithBandFilterInput"></a>

This is a RasterDataCollectionQueryInput containing AreaOfInterest, Time Range filter and Property filters.

## Contents
<a name="API_geospatial_RasterDataCollectionQueryWithBandFilterInput_Contents"></a>

 ** TimeRangeFilter **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryWithBandFilterInput-TimeRangeFilter"></a>
The TimeRange Filter used in the search query.
Type: [TimeRangeFilterInput](API_geospatial_TimeRangeFilterInput.md) object
Required: Yes

 ** AreaOfInterest **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryWithBandFilterInput-AreaOfInterest"></a>
The Area of interest to be used in the search query.
Type: [AreaOfInterest](API_geospatial_AreaOfInterest.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** BandFilter **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryWithBandFilterInput-BandFilter"></a>
The list of Bands to be displayed in the result for each item.
Type: Array of strings
Array Members: Minimum number of 1 item.
Required: No

 ** PropertyFilters **   <a name="sagemaker-Type-geospatial_RasterDataCollectionQueryWithBandFilterInput-PropertyFilters"></a>
The Property Filters used in the search query.
Type: [PropertyFilters](API_geospatial_PropertyFilters.md) object
Required: No

## See Also
<a name="API_geospatial_RasterDataCollectionQueryWithBandFilterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryWithBandFilterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryWithBandFilterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/RasterDataCollectionQueryWithBandFilterInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
