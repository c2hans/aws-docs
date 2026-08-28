---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_Geometry.html
---

# Geometry
<a name="API_geospatial_Geometry"></a>

The structure representing a Geometry in terms of Type and Coordinates as per GeoJson spec.

## Contents
<a name="API_geospatial_Geometry_Contents"></a>

 ** Coordinates **   <a name="sagemaker-Type-geospatial_Geometry-Coordinates"></a>
The coordinates of the GeoJson Geometry.
Type: Array of arrays of arrays of doubles
Array Members: Minimum number of 1 item.
Array Members: Minimum number of 4 items.
Array Members: Fixed number of 2 items.
Required: Yes

 ** Type **   <a name="sagemaker-Type-geospatial_Geometry-Type"></a>
GeoJson Geometry types like Polygon and MultiPolygon.
Type: String
Required: Yes

## See Also
<a name="API_geospatial_Geometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/Geometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/Geometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/Geometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
