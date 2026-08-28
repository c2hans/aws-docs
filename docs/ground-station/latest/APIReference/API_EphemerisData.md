---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_EphemerisData.html
---

# EphemerisData
<a name="API_EphemerisData"></a>

Ephemeris data.

## Contents
<a name="API_EphemerisData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azEl **   <a name="groundstation-Type-EphemerisData-azEl"></a>
Azimuth elevation ephemeris data.
 Use this ephemeris type to provide pointing angles directly, rather than satellite orbital elements. Use this when you need precise antenna pointing but have imprecise or unknown satellite trajectory information.
 The azimuth elevation data specifies the antenna pointing direction at specific times relative to a ground station location. AWS Ground Station uses 4th order Lagrange interpolation to compute pointing angles between the provided data points.
 AWS Ground Station automatically filters interpolated pointing angles, including only those that are above the site mask elevation of the specified ground station.
 For more detail about providing azimuth elevation ephemerides to AWS Ground Station, see the [azimuth elevation ephemeris section](https://docs.aws.amazon.com/ground-station/latest/ug/providing-azimuth-elevation-ephemeris-data.html) of the AWS Ground Station User Guide.
Type: [AzElEphemeris](API_AzElEphemeris.md) object
Required: No

 ** oem **   <a name="groundstation-Type-EphemerisData-oem"></a>
Ephemeris data in Orbit Ephemeris Message (OEM) format.
 AWS Ground Station processes OEM ephemerides according to the [CCSDS standard](https://ccsds.org/Pubs/502x0b3e1.pdf) with some extra restrictions. OEM files should be in KVN format. For more detail about the OEM format that AWS Ground Station supports, see [OEM ephemeris format](https://docs.aws.amazon.com/ground-station/latest/ug/providing-oem-ephemeris-data.html#oem-ephemeris-format) in the AWS Ground Station user guide.
Type: [OEMEphemeris](API_OEMEphemeris.md) object
Required: No

 ** tle **   <a name="groundstation-Type-EphemerisData-tle"></a>
Two-line element set (TLE) ephemeris.
 For more detail about providing Two-line element sets to AWS Ground Station, see the [TLE section](https://docs.aws.amazon.com/ground-station/latest/ug/providing-tle-ephemeris-data.html) of the AWS Ground Station user guide.
Type: [TLEEphemeris](API_TLEEphemeris.md) object
Required: No

## See Also
<a name="API_EphemerisData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/EphemerisData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/EphemerisData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/EphemerisData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
