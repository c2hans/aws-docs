---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_JobConfigInput.html
---

# JobConfigInput
<a name="API_geospatial_JobConfigInput"></a>

The input structure for the JobConfig in an EarthObservationJob.

## Contents
<a name="API_geospatial_JobConfigInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** BandMathConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-BandMathConfig"></a>
An object containing information about the job configuration for BandMath.
Type: [BandMathConfigInput](API_geospatial_BandMathConfigInput.md) object
Required: No

 ** CloudMaskingConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-CloudMaskingConfig"></a>
An object containing information about the job configuration for cloud masking.
Type: [CloudMaskingConfigInput](API_geospatial_CloudMaskingConfigInput.md) object
Required: No

 ** CloudRemovalConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-CloudRemovalConfig"></a>
An object containing information about the job configuration for cloud removal.
Type: [CloudRemovalConfigInput](API_geospatial_CloudRemovalConfigInput.md) object
Required: No

 ** GeoMosaicConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-GeoMosaicConfig"></a>
An object containing information about the job configuration for geomosaic.
Type: [GeoMosaicConfigInput](API_geospatial_GeoMosaicConfigInput.md) object
Required: No

 ** LandCoverSegmentationConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-LandCoverSegmentationConfig"></a>
An object containing information about the job configuration for land cover segmentation.
Type: [LandCoverSegmentationConfigInput](API_geospatial_LandCoverSegmentationConfigInput.md) object
Required: No

 ** ResamplingConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-ResamplingConfig"></a>
An object containing information about the job configuration for resampling.
Type: [ResamplingConfigInput](API_geospatial_ResamplingConfigInput.md) object
Required: No

 ** StackConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-StackConfig"></a>
An object containing information about the job configuration for a Stacking Earth Observation job.
Type: [StackConfigInput](API_geospatial_StackConfigInput.md) object
Required: No

 ** TemporalStatisticsConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-TemporalStatisticsConfig"></a>
An object containing information about the job configuration for temporal statistics.
Type: [TemporalStatisticsConfigInput](API_geospatial_TemporalStatisticsConfigInput.md) object
Required: No

 ** ZonalStatisticsConfig **   <a name="sagemaker-Type-geospatial_JobConfigInput-ZonalStatisticsConfig"></a>
An object containing information about the job configuration for zonal statistics.
Type: [ZonalStatisticsConfigInput](API_geospatial_ZonalStatisticsConfigInput.md) object
Required: No

## See Also
<a name="API_geospatial_JobConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/JobConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/JobConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/JobConfigInput)
