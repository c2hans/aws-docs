---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_Property.html
---

# Property
<a name="API_geospatial_Property"></a>

Represents a single searchable property to search on.

## Contents
<a name="API_geospatial_Property_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EoCloudCover **   <a name="sagemaker-Type-geospatial_Property-EoCloudCover"></a>
The structure representing EoCloudCover property filter containing a lower bound and upper bound.
Type: [EoCloudCoverInput](API_geospatial_EoCloudCoverInput.md) object
Required: No

 ** LandsatCloudCoverLand **   <a name="sagemaker-Type-geospatial_Property-LandsatCloudCoverLand"></a>
The structure representing Land Cloud Cover property filter for Landsat collection containing a lower bound and upper bound.
Type: [LandsatCloudCoverLandInput](API_geospatial_LandsatCloudCoverLandInput.md) object
Required: No

 ** Platform **   <a name="sagemaker-Type-geospatial_Property-Platform"></a>
The structure representing Platform property filter consisting of value and comparison operator.
Type: [PlatformInput](API_geospatial_PlatformInput.md) object
Required: No

 ** ViewOffNadir **   <a name="sagemaker-Type-geospatial_Property-ViewOffNadir"></a>
The structure representing ViewOffNadir property filter containing a lower bound and upper bound.
Type: [ViewOffNadirInput](API_geospatial_ViewOffNadirInput.md) object
Required: No

 ** ViewSunAzimuth **   <a name="sagemaker-Type-geospatial_Property-ViewSunAzimuth"></a>
The structure representing ViewSunAzimuth property filter containing a lower bound and upper bound.
Type: [ViewSunAzimuthInput](API_geospatial_ViewSunAzimuthInput.md) object
Required: No

 ** ViewSunElevation **   <a name="sagemaker-Type-geospatial_Property-ViewSunElevation"></a>
The structure representing ViewSunElevation property filter containing a lower bound and upper bound.
Type: [ViewSunElevationInput](API_geospatial_ViewSunElevationInput.md) object
Required: No

## See Also
<a name="API_geospatial_Property_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/Property)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/Property)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/Property)
