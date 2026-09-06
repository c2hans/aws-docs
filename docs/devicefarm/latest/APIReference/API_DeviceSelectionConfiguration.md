---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceSelectionConfiguration.html
---

# DeviceSelectionConfiguration
<a name="API_DeviceSelectionConfiguration"></a>

Represents the device filters used in a test run and the maximum number of devices to be included in the run. It is passed in as the `deviceSelectionConfiguration` request parameter in [ScheduleRun](API_ScheduleRun.md).

## Contents
<a name="API_DeviceSelectionConfiguration_Contents"></a>

 ** filters **   <a name="devicefarm-Type-DeviceSelectionConfiguration-filters"></a>
Used to dynamically select a set of devices for a test run. A filter is made up of an attribute, an operator, and one or more values.
+  **Attribute**

  The aspect of a device such as platform or model used as the selection criteria in a device filter.

  Allowed values include:
  + ARN: The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example`).
  + PLATFORM: The device platform. Valid values are ANDROID or IOS.
  + OS\_VERSION: The operating system version (for example, 10.3.2).
  + MODEL: The device model (for example, iPad 5th Gen).
  + AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY\_AVAILABLE, BUSY, or TEMPORARY\_NOT\_AVAILABLE.
  + FORM\_FACTOR: The device form factor. Valid values are PHONE or TABLET.
  + MANUFACTURER: The device manufacturer (for example, Apple).
  + REMOTE\_ACCESS\_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
  + REMOTE\_DEBUG\_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html), this filter is ignored.
  + INSTANCE\_ARN: The Amazon Resource Name (ARN) of the device instance.
  + INSTANCE\_LABELS: The label of the device instance.
  + FLEET\_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.
+  **Operator**

  The filter operator.
  + The EQUALS operator is available for every attribute except INSTANCE\_LABELS.
  + The CONTAINS operator is available for the INSTANCE\_LABELS and MODEL attributes.
  + The IN and NOT\_IN operators are available for the ARN, OS\_VERSION, MODEL, MANUFACTURER, and INSTANCE\_ARN attributes.
  + The LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUALS, and GREATER\_THAN\_OR\_EQUALS operators are also available for the OS\_VERSION attribute.
+  **Values**

  An array of one or more filter values.

**Operator Values**
  + The IN and NOT\_IN operators can take a values array that has more than one element.
  + The other operators require an array with a single element.

**Attribute Values**
  + The PLATFORM attribute can be set to ANDROID or IOS.
  + The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY\_AVAILABLE, BUSY, or TEMPORARY\_NOT\_AVAILABLE.
  + The FORM\_FACTOR attribute can be set to PHONE or TABLET.
  + The FLEET\_TYPE attribute can be set to PUBLIC or PRIVATE.
Type: Array of [DeviceFilter](API_DeviceFilter.md) objects
Required: Yes

 ** maxDevices **   <a name="devicefarm-Type-DeviceSelectionConfiguration-maxDevices"></a>
The maximum number of devices to be included in a test run.
Type: Integer
Required: Yes

## See Also
<a name="API_DeviceSelectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeviceSelectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeviceSelectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeviceSelectionConfiguration)
