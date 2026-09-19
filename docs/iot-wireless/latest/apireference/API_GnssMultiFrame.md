---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GnssMultiFrame.html
---

# GnssMultiFrame
<a name="API_GnssMultiFrame"></a>

Global navigation satellite system (GNSS) multi-frame object used for positioning. Contains multiple GNSS scan captures that are combined by the solver.

## Contents
<a name="API_GnssMultiFrame_Contents"></a>

 ** Captures **   <a name="iotwireless-Type-GnssMultiFrame-Captures"></a>
List of GNSS scan captures. Each capture contains a payload from a single GNSS scan. The number of captures must be 2, 4, 8, 16, or 32.
Type: Array of [GnssCapture](API_GnssCapture.md) objects
Array Members: Minimum number of 2 items. Maximum number of 32 items.
Required: Yes

 ** AssistAltitude **   <a name="iotwireless-Type-GnssMultiFrame-AssistAltitude"></a>
Optional assistance altitude, which is the altitude of the device at capture time, specified in meters above the WGS84 reference ellipsoid. This parameter is required when Use2DSolver is enabled.
Type: Float
Required: No

 ** AssistPosition **   <a name="iotwireless-Type-GnssMultiFrame-AssistPosition"></a>
Optional assistance position information, specified using latitude and longitude values in degrees. The coordinates are inside the WGS84 reference frame.
Type: Array of floats
Array Members: Fixed number of 2 items.
Required: No

 ** CaptureTimeAccuracy **   <a name="iotwireless-Type-GnssMultiFrame-CaptureTimeAccuracy"></a>
Optional value that gives the capture time estimate accuracy, in seconds. If capture time accuracy is not specified, default value of 300 is used.
Type: Float
Required: No

 ** Use2DSolver **   <a name="iotwireless-Type-GnssMultiFrame-Use2DSolver"></a>
Optional parameter that forces 2D solve, which modifies the positioning algorithm to a 2D solution problem. When this parameter is specified, the assistance altitude should have an accuracy of at least 10 meters.
Type: Boolean
Required: No

## See Also
<a name="API_GnssMultiFrame_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GnssMultiFrame)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GnssMultiFrame)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GnssMultiFrame)
