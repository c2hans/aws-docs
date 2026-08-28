---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_AzElSegment.html
---

# AzElSegment
<a name="API_AzElSegment"></a>

A time segment containing azimuth elevation pointing data.

 Each segment defines a continuous time period with pointing angle data points. AWS Ground Station uses 4th order Lagrange interpolation between the provided points, so each segment must contain at least five data points.

## Contents
<a name="API_AzElSegment_Contents"></a>

 ** azElList **   <a name="groundstation-Type-AzElSegment-azElList"></a>
List of time-tagged azimuth elevation data points.
 Must contain at least five points to support 4th order Lagrange interpolation. Points must be in chronological order with no duplicates.
Type: Array of [TimeAzEl](API_TimeAzEl.md) objects
Array Members: Minimum number of 5 items.
Required: Yes

 ** referenceEpoch **   <a name="groundstation-Type-AzElSegment-referenceEpoch"></a>
The reference time for this segment in ISO 8601 format in Coordinated Universal Time (UTC).
All time values within the segment's [AzElSegment:azElList](#groundstation-Type-AzElSegment-azElList) are specified as offsets in atomic seconds from this reference epoch.
Example: `2024-01-15T12:00:00.000Z`
Type: Timestamp
Required: Yes

 ** validTimeRange **   <a name="groundstation-Type-AzElSegment-validTimeRange"></a>
The valid time range for this segment.
 Specifies the start and end timestamps in ISO 8601 format in Coordinated Universal Time (UTC). The segment's pointing data must cover this entire time range.
Type: [ISO8601TimeRange](API_ISO8601TimeRange.md) object
Required: Yes

## See Also
<a name="API_AzElSegment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/AzElSegment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/AzElSegment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/AzElSegment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
