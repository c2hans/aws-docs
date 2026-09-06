---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html
---

# AreaOfInterest
<a name="API_geospatial_AreaOfInterest"></a>

The geographic extent of the Earth Observation job.

## Contents
<a name="API_geospatial_AreaOfInterest_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AreaOfInterestGeometry **   <a name="sagemaker-Type-geospatial_AreaOfInterest-AreaOfInterestGeometry"></a>
A GeoJSON object representing the geographic extent in the coordinate space.
Type: [AreaOfInterestGeometry](API_geospatial_AreaOfInterestGeometry.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_geospatial_AreaOfInterest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/AreaOfInterest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/AreaOfInterest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/AreaOfInterest)
