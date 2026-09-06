---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_TimeAzEl.html
---

# TimeAzEl
<a name="API_TimeAzEl"></a>

Time-tagged azimuth elevation pointing data.

Specifies the antenna pointing direction at a specific time offset from the segment's reference epoch.

## Contents
<a name="API_TimeAzEl_Contents"></a>

 ** az **   <a name="groundstation-Type-TimeAzEl-az"></a>
Azimuth angle at the specified time.
Valid ranges by unit:
+  `DEGREE_ANGLE`: -180 to 360 degrees, measured clockwise from true north
+  `RADIAN`: -π to 2π radians, measured clockwise from true north
Type: Double
Required: Yes

 ** dt **   <a name="groundstation-Type-TimeAzEl-dt"></a>
Time offset in atomic seconds from the segment's reference epoch.
All `dt` values within a segment must be in ascending order with no duplicates.
 `dt` values may be:
+ negative
+ expressed as fractions of a second
+ expressed in scientific notation
Type: Double
Required: Yes

 ** el **   <a name="groundstation-Type-TimeAzEl-el"></a>
Elevation angle at the specified time.
Valid ranges by unit:
+  `DEGREE_ANGLE`: -90 to 90 degrees, where 0 is the horizon, 90 is zenith, and negative values are below the horizon
+  `RADIAN`: -π/2 to π/2 radians, where 0 is the horizon, π/2 is zenith, and negative values are below the horizon
Type: Double
Required: Yes

## See Also
<a name="API_TimeAzEl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/TimeAzEl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/TimeAzEl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/TimeAzEl)
