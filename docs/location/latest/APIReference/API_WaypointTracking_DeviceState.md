---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointTracking_DeviceState.html
---

# DeviceState
<a name="API_WaypointTracking_DeviceState"></a>

The device's position, IP address, and Wi-Fi access points.

## Contents
<a name="API_WaypointTracking_DeviceState_Contents"></a>

 ** DeviceId **   <a name="location-Type-WaypointTracking_DeviceState-DeviceId"></a>
The device identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\p{L}\p{N}]+`
Required: Yes

 ** Position **   <a name="location-Type-WaypointTracking_DeviceState-Position"></a>
The last known device position.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** SampleTime **   <a name="location-Type-WaypointTracking_DeviceState-SampleTime"></a>
The timestamp at which the device's position was determined. Uses [ ISO 8601 ](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
Type: Timestamp
Required: Yes

 ** Accuracy **   <a name="location-Type-WaypointTracking_DeviceState-Accuracy"></a>

Type: [PositionalAccuracy](API_WaypointTracking_PositionalAccuracy.md) object
Required: No

 ** CellSignals **   <a name="location-Type-WaypointTracking_DeviceState-CellSignals"></a>
The cellular network infrastructure that the device is connected to.
Type: [CellSignals](API_WaypointTracking_CellSignals.md) object
Required: No

 ** Ipv4Address **   <a name="location-Type-WaypointTracking_DeviceState-Ipv4Address"></a>
The device's Ipv4 address.
Type: String
Pattern: `(?:(?:25[0-5]|(?:2[0-4]|1\d|[0-9]|)\d)\.?\b){4}`
Required: No

 ** WiFiAccessPoints **   <a name="location-Type-WaypointTracking_DeviceState-WiFiAccessPoints"></a>
The Wi-Fi access points the device is using.
Type: Array of [WiFiAccessPoint](API_WaypointTracking_WiFiAccessPoint.md) objects
Required: No

## See Also
<a name="API_WaypointTracking_DeviceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waypointtracking-2020-11-19/DeviceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waypointtracking-2020-11-19/DeviceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waypointtracking-2020-11-19/DeviceState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
