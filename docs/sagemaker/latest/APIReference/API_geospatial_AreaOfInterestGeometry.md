---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterestGeometry.html
---

# AreaOfInterestGeometry
<a name="API_geospatial_AreaOfInterestGeometry"></a>

A GeoJSON object representing the geographic extent in the coordinate space.

## Contents
<a name="API_geospatial_AreaOfInterestGeometry_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** MultiPolygonGeometry **   <a name="sagemaker-Type-geospatial_AreaOfInterestGeometry-MultiPolygonGeometry"></a>
The structure representing the MultiPolygon Geometry.
Type: [MultiPolygonGeometryInput](API_geospatial_MultiPolygonGeometryInput.md) object
Required: No

 ** PolygonGeometry **   <a name="sagemaker-Type-geospatial_AreaOfInterestGeometry-PolygonGeometry"></a>
The structure representing Polygon Geometry.
Type: [PolygonGeometryInput](API_geospatial_PolygonGeometryInput.md) object
Required: No

## See Also
<a name="API_geospatial_AreaOfInterestGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-geospatial-2020-05-27/AreaOfInterestGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-geospatial-2020-05-27/AreaOfInterestGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-geospatial-2020-05-27/AreaOfInterestGeometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
