---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_Properties.html
---

# Properties
<a name="API_geospatial_Properties"></a>

Properties associated with the Item.

## Contents
<a name="API_geospatial_Properties_Contents"></a>

 ** EoCloudCover **   <a name="sagemaker-Type-geospatial_Properties-EoCloudCover"></a>
Estimate of cloud cover.
Type: Float
Required: No

 ** LandsatCloudCoverLand **   <a name="sagemaker-Type-geospatial_Properties-LandsatCloudCoverLand"></a>
Land cloud cover for Landsat Data Collection.
Type: Float
Required: No

 ** Platform **   <a name="sagemaker-Type-geospatial_Properties-Platform"></a>
Platform property. Platform refers to the unique name of the specific platform the instrument is attached to. For satellites it is the name of the satellite, eg. landsat-8 (Landsat-8), sentinel-2a.
Type: String
Required: No

 ** ViewOffNadir **   <a name="sagemaker-Type-geospatial_Properties-ViewOffNadir"></a>
The angle from the sensor between nadir (straight down) and the scene center. Measured in degrees (0-90).
Type: Float
Required: No

 ** ViewSunAzimuth **   <a name="sagemaker-Type-geospatial_Properties-ViewSunAzimuth"></a>
The sun azimuth angle. From the scene center point on the ground, this is the angle between truth north and the sun. Measured clockwise in degrees (0-360).
Type: Float
Required: No

 ** ViewSunElevation **   <a name="sagemaker-Type-geospatial_Properties-ViewSunElevation"></a>
The sun elevation angle. The angle from the tangent of the scene center point to the sun. Measured from the horizon in degrees (-90-90). Negative values indicate the sun is below the horizon, e.g. sun elevation of -10° means the data was captured during [nautical twilight](https://www.timeanddate.com/astronomy/different-types-twilight.html).
Type: Float
Required: No

## See Also
<a name="API_geospatial_Properties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/Properties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/Properties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/Properties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
