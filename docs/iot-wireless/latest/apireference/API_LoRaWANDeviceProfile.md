---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANDeviceProfile.html
---

# LoRaWANDeviceProfile
<a name="API_LoRaWANDeviceProfile"></a>

LoRaWANDeviceProfile object.

## Contents
<a name="API_LoRaWANDeviceProfile_Contents"></a>

 ** ClassBTimeout **   <a name="iotwireless-Type-LoRaWANDeviceProfile-ClassBTimeout"></a>
The ClassBTimeout value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** ClassCTimeout **   <a name="iotwireless-Type-LoRaWANDeviceProfile-ClassCTimeout"></a>
The ClassCTimeout value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** FactoryPresetFreqsList **   <a name="iotwireless-Type-LoRaWANDeviceProfile-FactoryPresetFreqsList"></a>
The list of values that make up the FactoryPresetFreqs value.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Valid Range: Minimum value of 1000000. Maximum value of 16700000.
Required: No

 ** MacVersion **   <a name="iotwireless-Type-LoRaWANDeviceProfile-MacVersion"></a>
The MAC version (such as OTAA 1.1 or OTAA 1.0.3) to use with this device profile.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** MaxDutyCycle **   <a name="iotwireless-Type-LoRaWANDeviceProfile-MaxDutyCycle"></a>
The MaxDutyCycle value. It ranges from 0 to 15.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** MaxEirp **   <a name="iotwireless-Type-LoRaWANDeviceProfile-MaxEirp"></a>
The MaxEIRP value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** PingSlotDr **   <a name="iotwireless-Type-LoRaWANDeviceProfile-PingSlotDr"></a>
The PingSlotDR value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** PingSlotFreq **   <a name="iotwireless-Type-LoRaWANDeviceProfile-PingSlotFreq"></a>
The PingSlotFreq value.
Type: Integer
Valid Range: Minimum value of 1000000. Maximum value of 16700000.
Required: No

 ** PingSlotPeriod **   <a name="iotwireless-Type-LoRaWANDeviceProfile-PingSlotPeriod"></a>
The PingSlotPeriod value.
Type: Integer
Valid Range: Minimum value of 32. Maximum value of 4096.
Required: No

 ** RegParamsRevision **   <a name="iotwireless-Type-LoRaWANDeviceProfile-RegParamsRevision"></a>
The version of regional parameters.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** RfRegion **   <a name="iotwireless-Type-LoRaWANDeviceProfile-RfRegion"></a>
The frequency band (RFRegion) value.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** RxDataRate2 **   <a name="iotwireless-Type-LoRaWANDeviceProfile-RxDataRate2"></a>
The RXDataRate2 value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** RxDelay1 **   <a name="iotwireless-Type-LoRaWANDeviceProfile-RxDelay1"></a>
The RXDelay1 value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** RxDrOffset1 **   <a name="iotwireless-Type-LoRaWANDeviceProfile-RxDrOffset1"></a>
The RXDROffset1 value.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 7.
Required: No

 ** RxFreq2 **   <a name="iotwireless-Type-LoRaWANDeviceProfile-RxFreq2"></a>
The RXFreq2 value.
Type: Integer
Valid Range: Minimum value of 1000000. Maximum value of 16700000.
Required: No

 ** Supports32BitFCnt **   <a name="iotwireless-Type-LoRaWANDeviceProfile-Supports32BitFCnt"></a>
The Supports32BitFCnt value.
Type: Boolean
Required: No

 ** SupportsClassB **   <a name="iotwireless-Type-LoRaWANDeviceProfile-SupportsClassB"></a>
The SupportsClassB value.
Type: Boolean
Required: No

 ** SupportsClassC **   <a name="iotwireless-Type-LoRaWANDeviceProfile-SupportsClassC"></a>
The SupportsClassC value.
Type: Boolean
Required: No

 ** SupportsJoin **   <a name="iotwireless-Type-LoRaWANDeviceProfile-SupportsJoin"></a>
The SupportsJoin value.
Type: Boolean
Required: No

## See Also
<a name="API_LoRaWANDeviceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANDeviceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANDeviceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANDeviceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
