---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_InputConfigInput.html
---

# InputConfigInput
<a name="API_geospatial_InputConfigInput"></a>

Input configuration information.

## Contents
<a name="API_geospatial_InputConfigInput_Contents"></a>

 ** PreviousEarthObservationJobArn **   <a name="sagemaker-Type-geospatial_InputConfigInput-PreviousEarthObservationJobArn"></a>
The Amazon Resource Name (ARN) of the previous Earth Observation job.
Type: String
Pattern: `arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}`
Required: No

 ** RasterDataCollectionQuery **   <a name="sagemaker-Type-geospatial_InputConfigInput-RasterDataCollectionQuery"></a>
The structure representing the RasterDataCollection Query consisting of the Area of Interest, RasterDataCollectionArn,TimeRange and Property Filters.
Type: [RasterDataCollectionQueryInput](API_geospatial_RasterDataCollectionQueryInput.md) object
Required: No

## See Also
<a name="API_geospatial_InputConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/InputConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/InputConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/InputConfigInput)
