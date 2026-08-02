---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceSelectionResult.html
---

# DeviceSelectionResult
<a name="API_DeviceSelectionResult"></a>

Contains the run results requested by the device selection configuration and how many devices were returned. For an example of the JSON response syntax, see [ScheduleRun](API_ScheduleRun.md).

## Contents
<a name="API_DeviceSelectionResult_Contents"></a>

 ** filters **   <a name="devicefarm-Type-DeviceSelectionResult-filters"></a>
The filters in a device selection result.
Type: Array of [DeviceFilter](API_DeviceFilter.md) objects
Required: No

 ** matchedDevicesCount **   <a name="devicefarm-Type-DeviceSelectionResult-matchedDevicesCount"></a>
The number of devices that matched the device filter selection criteria.
Type: Integer
Required: No

 ** maxDevices **   <a name="devicefarm-Type-DeviceSelectionResult-maxDevices"></a>
The maximum number of devices to be selected by a device filter and included in a test run.
Type: Integer
Required: No

## See Also
<a name="API_DeviceSelectionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeviceSelectionResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeviceSelectionResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeviceSelectionResult)
