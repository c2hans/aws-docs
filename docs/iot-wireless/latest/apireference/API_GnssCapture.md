---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GnssCapture.html
---

# GnssCapture
<a name="API_GnssCapture"></a>

A single GNSS scan capture containing the scan payload and optional capture time.

## Contents
<a name="API_GnssCapture_Contents"></a>

 ** Payload **   <a name="iotwireless-Type-GnssCapture-Payload"></a>
Payload that contains the GNSS scan result, or NAV message, in hexadecimal notation.
Type: String
Length Constraints: Maximum length of 2048.
Required: Yes

 ** CaptureTime **   <a name="iotwireless-Type-GnssCapture-CaptureTime"></a>
Optional parameter that gives an estimate of the time when the GNSS scan information is taken, in seconds GPS time (GPST). If capture time is not specified, the local server time is used.
Type: Float
Required: No

## See Also
<a name="API_GnssCapture_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GnssCapture)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GnssCapture)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GnssCapture)
