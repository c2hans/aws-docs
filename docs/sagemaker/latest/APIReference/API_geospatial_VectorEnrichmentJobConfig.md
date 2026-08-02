---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_VectorEnrichmentJobConfig.html
---

# VectorEnrichmentJobConfig
<a name="API_geospatial_VectorEnrichmentJobConfig"></a>

It contains configs such as ReverseGeocodingConfig and MapMatchingConfig.

## Contents
<a name="API_geospatial_VectorEnrichmentJobConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** MapMatchingConfig **   <a name="sagemaker-Type-geospatial_VectorEnrichmentJobConfig-MapMatchingConfig"></a>
The input structure for Map Matching operation type.
Type: [MapMatchingConfig](API_geospatial_MapMatchingConfig.md) object
Required: No

 ** ReverseGeocodingConfig **   <a name="sagemaker-Type-geospatial_VectorEnrichmentJobConfig-ReverseGeocodingConfig"></a>
The input structure for Reverse Geocoding operation type.
Type: [ReverseGeocodingConfig](API_geospatial_ReverseGeocodingConfig.md) object
Required: No

## See Also
<a name="API_geospatial_VectorEnrichmentJobConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/VectorEnrichmentJobConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/VectorEnrichmentJobConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/VectorEnrichmentJobConfig)
