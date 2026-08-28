---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANMulticastSession.html
---

# LoRaWANMulticastSession
<a name="API_LoRaWANMulticastSession"></a>

The LoRaWAN information used with the multicast session.

## Contents
<a name="API_LoRaWANMulticastSession_Contents"></a>

 ** DlDr **   <a name="iotwireless-Type-LoRaWANMulticastSession-DlDr"></a>
Downlink data rate.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** DlFreq **   <a name="iotwireless-Type-LoRaWANMulticastSession-DlFreq"></a>
Downlink frequency.
Type: Integer
Valid Range: Minimum value of 100000000. Maximum value of 1000000000.
Required: No

 ** PingSlotPeriod **   <a name="iotwireless-Type-LoRaWANMulticastSession-PingSlotPeriod"></a>
The PingSlotPeriod value.
Type: Integer
Valid Range: Minimum value of 32. Maximum value of 4096.
Required: No

 ** SessionStartTime **   <a name="iotwireless-Type-LoRaWANMulticastSession-SessionStartTime"></a>
Timestamp of when the multicast group session is to start.
Type: Timestamp
Required: No

 ** SessionTimeout **   <a name="iotwireless-Type-LoRaWANMulticastSession-SessionTimeout"></a>
How long before a multicast group session is to timeout.
We recommend that you provide a timeout value that is a power-of-two (such as 64, 128, 256). If a non-power-of-two value is provided, it will automatically be rounded up to the next supported power-of-two within the allowed range.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 172800.
Required: No

## See Also
<a name="API_LoRaWANMulticastSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANMulticastSession)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANMulticastSession)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANMulticastSession)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
