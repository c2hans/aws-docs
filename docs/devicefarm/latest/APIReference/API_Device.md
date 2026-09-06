---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Device.html
---

# Device
<a name="API_Device"></a>

Represents a device type that an app is tested against.

## Contents
<a name="API_Device_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Device-arn"></a>
The device's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** availability **   <a name="devicefarm-Type-Device-availability"></a>
Indicates how likely a device is available for a test run. Currently available in the [ListDevices](API_ListDevices.md) and GetDevice API methods.
Type: String
Valid Values: `TEMPORARY_NOT_AVAILABLE | BUSY | AVAILABLE | HIGHLY_AVAILABLE`
Required: No

 ** carrier **   <a name="devicefarm-Type-Device-carrier"></a>
The device's carrier.
Type: String
Required: No

 ** cpu **   <a name="devicefarm-Type-Device-cpu"></a>
Information about the device's CPU.
Type: [CPU](API_CPU.md) object
Required: No

 ** fleetName **   <a name="devicefarm-Type-Device-fleetName"></a>
The name of the fleet to which this device belongs.
Type: String
Required: No

 ** fleetType **   <a name="devicefarm-Type-Device-fleetType"></a>
The type of fleet to which this device belongs. Possible values are PRIVATE and PUBLIC.
Type: String
Required: No

 ** formFactor **   <a name="devicefarm-Type-Device-formFactor"></a>
The device's form factor.
Allowed values include:
+ PHONE
+ TABLET
Type: String
Valid Values: `PHONE | TABLET`
Required: No

 ** heapSize **   <a name="devicefarm-Type-Device-heapSize"></a>
The device's heap size, expressed in bytes.
Type: Long
Required: No

 ** image **   <a name="devicefarm-Type-Device-image"></a>
The device's image name.
Type: String
Required: No

 ** instances **   <a name="devicefarm-Type-Device-instances"></a>
The instances that belong to this device.
Type: Array of [DeviceInstance](API_DeviceInstance.md) objects
Required: No

 ** manufacturer **   <a name="devicefarm-Type-Device-manufacturer"></a>
The device's manufacturer name.
Type: String
Required: No

 ** memory **   <a name="devicefarm-Type-Device-memory"></a>
The device's total memory size, expressed in bytes.
Type: Long
Required: No

 ** model **   <a name="devicefarm-Type-Device-model"></a>
The device's model name.
Type: String
Required: No

 ** modelId **   <a name="devicefarm-Type-Device-modelId"></a>
The device's model ID.
Type: String
Required: No

 ** name **   <a name="devicefarm-Type-Device-name"></a>
The device's display name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** os **   <a name="devicefarm-Type-Device-os"></a>
The device's operating system type.
Type: String
Required: No

 ** platform **   <a name="devicefarm-Type-Device-platform"></a>
The device's platform.
Allowed values include:
+ ANDROID
+ IOS
Type: String
Valid Values: `ANDROID | IOS`
Required: No

 ** radio **   <a name="devicefarm-Type-Device-radio"></a>
The device's radio.
Type: String
Required: No

 ** remoteAccessEnabled **   <a name="devicefarm-Type-Device-remoteAccessEnabled"></a>
Specifies whether remote access has been enabled for the specified device.
Type: Boolean
Required: No

 ** remoteDebugEnabled **   <a name="devicefarm-Type-Device-remoteDebugEnabled"></a>
 *This member has been deprecated.*
This flag is set to `true` if remote debugging is enabled for the device.
Remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html).
Type: Boolean
Required: No

 ** resolution **   <a name="devicefarm-Type-Device-resolution"></a>
The resolution of the device.
Type: [Resolution](API_Resolution.md) object
Required: No

## See Also
<a name="API_Device_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Device)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Device)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Device)
