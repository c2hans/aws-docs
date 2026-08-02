---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_WirelessDeviceImportTask.html
---

# WirelessDeviceImportTask
<a name="API_WirelessDeviceImportTask"></a>

Information about an import task for wireless devices.

## Contents
<a name="API_WirelessDeviceImportTask_Contents"></a>

 ** Arn **   <a name="iotwireless-Type-WirelessDeviceImportTask-Arn"></a>
The ARN (Amazon Resource Name) of the wireless device import task.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** CreationTime **   <a name="iotwireless-Type-WirelessDeviceImportTask-CreationTime"></a>
The time at which the import task was created.
Type: Timestamp
Required: No

 ** DestinationName **   <a name="iotwireless-Type-WirelessDeviceImportTask-DestinationName"></a>
The name of the Sidewalk destination that that describes the IoT rule to route messages from the device in the import task that will be onboarded to AWS IoT Wireless
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** FailedImportedDeviceCount **   <a name="iotwireless-Type-WirelessDeviceImportTask-FailedImportedDeviceCount"></a>
The summary information of count of wireless devices in an import task that failed to onboarded to the import task.
Type: Long
Required: No

 ** Id **   <a name="iotwireless-Type-WirelessDeviceImportTask-Id"></a>
The ID of the wireless device import task.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** InitializedImportedDeviceCount **   <a name="iotwireless-Type-WirelessDeviceImportTask-InitializedImportedDeviceCount"></a>
The summary information of count of wireless devices that are waiting for the control log to be added to an import task.
Type: Long
Required: No

 ** OnboardedImportedDeviceCount **   <a name="iotwireless-Type-WirelessDeviceImportTask-OnboardedImportedDeviceCount"></a>
The summary information of count of wireless devices in an import task that have been onboarded to the import task.
Type: Long
Required: No

 ** PendingImportedDeviceCount **   <a name="iotwireless-Type-WirelessDeviceImportTask-PendingImportedDeviceCount"></a>
The summary information of count of wireless devices in an import task that are waiting in the queue to be onboarded.
Type: Long
Required: No

 ** Positioning **   <a name="iotwireless-Type-WirelessDeviceImportTask-Positioning"></a>
The integration status of the Device Location feature for Sidewalk devices.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** Sidewalk **   <a name="iotwireless-Type-WirelessDeviceImportTask-Sidewalk"></a>
The Sidewalk-related information of the wireless device import task.
Type: [SidewalkGetStartImportInfo](API_SidewalkGetStartImportInfo.md) object
Required: No

 ** Status **   <a name="iotwireless-Type-WirelessDeviceImportTask-Status"></a>
The status information of the wireless device import task.
Type: String
Valid Values: `INITIALIZING | INITIALIZED | PENDING | COMPLETE | FAILED | DELETING`
Required: No

 ** StatusReason **   <a name="iotwireless-Type-WirelessDeviceImportTask-StatusReason"></a>
The reason that provides additional information about the import task status.
Type: String
Required: No

## See Also
<a name="API_WirelessDeviceImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/WirelessDeviceImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/WirelessDeviceImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/WirelessDeviceImportTask)
