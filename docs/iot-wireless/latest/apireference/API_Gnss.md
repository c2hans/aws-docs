---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_Gnss.html
---

# Gnss
<a name="API_Gnss"></a>

Global navigation satellite system (GNSS) object used for positioning.

## Contents
<a name="API_Gnss_Contents"></a>

 ** Payload **   <a name="iotwireless-Type-Gnss-Payload"></a>
Payload that contains the GNSS scan result, or NAV message, in hexadecimal notation.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

 ** AssistAltitude **   <a name="iotwireless-Type-Gnss-AssistAltitude"></a>
Optional assistance altitude, which is the altitude of the device at capture time, specified in meters above the WGS84 reference ellipsoid.
Type: Float
Required: No

 ** AssistPosition **   <a name="iotwireless-Type-Gnss-AssistPosition"></a>
Optional assistance position information, specified using latitude and longitude values in degrees. The coordinates are inside the WGS84 reference frame.
Type: Array of floats
Array Members: Fixed number of 2 items.
Required: No

 ** CaptureTime **   <a name="iotwireless-Type-Gnss-CaptureTime"></a>
Optional parameter that gives an estimate of the time when the GNSS scan information is taken, in seconds GPS time (GPST). If capture time is not specified, the local server time is used.
Type: Float
Required: No

 ** CaptureTimeAccuracy **   <a name="iotwireless-Type-Gnss-CaptureTimeAccuracy"></a>
Optional value that gives the capture time estimate accuracy, in seconds. If capture time accuracy is not specified, default value of 300 is used.
Type: Float
Required: No

 ** Use2DSolver **   <a name="iotwireless-Type-Gnss-Use2DSolver"></a>
Optional parameter that forces 2D solve, which modifies the positioning algorithm to a 2D solution problem. When this parameter is specified, the assistance altitude should have an accuracy of at least 10 meters.
Type: Boolean
Required: No

## See Also
<a name="API_Gnss_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/Gnss)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/Gnss)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/Gnss)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
