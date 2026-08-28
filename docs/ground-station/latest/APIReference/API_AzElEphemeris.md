---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElEphemeris.html
---

# AzElEphemeris
<a name="API_AzElEphemeris"></a>

Azimuth elevation ephemeris data.

 Use this ephemeris type to provide pointing angles directly, rather than satellite orbital elements. Use this when you need precise antenna pointing but have imprecise or unknown satellite trajectory information.

 The azimuth elevation data specifies the antenna pointing direction at specific times relative to a ground station location. AWS Ground Station uses 4th order Lagrange interpolation to compute pointing angles between the provided data points.

 AWS Ground Station automatically filters interpolated pointing angles, including only those that are above the site mask elevation of the specified ground station.

 For more detail about providing azimuth elevation ephemerides to AWS Ground Station, see the [azimuth elevation ephemeris section](https://docs.aws.amazon.com/ground-station/latest/ug/providing-azimuth-elevation-ephemeris-data.html) of the AWS Ground Station User Guide.

## Contents
<a name="API_AzElEphemeris_Contents"></a>

 ** data **   <a name="groundstation-Type-AzElEphemeris-data"></a>
Azimuth elevation segment data.
You can provide data inline in the request or through an Amazon S3 object reference.
Type: [AzElSegmentsData](API_AzElSegmentsData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** groundStation **   <a name="groundstation-Type-AzElEphemeris-groundStation"></a>
The ground station name for which you're providing azimuth elevation data.
This ephemeris is specific to this ground station and can't be used at other locations.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 97.
Pattern: `[ a-zA-Z0-9-._:=]{4,97}`
Required: Yes

## See Also
<a name="API_AzElEphemeris_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AzElEphemeris)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AzElEphemeris)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AzElEphemeris)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
