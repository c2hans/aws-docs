---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_DeviceFilter.html
---

# DeviceFilter
<a name="API_DeviceFilter"></a>

Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the `deviceSelectionConfiguration` parameter to `ScheduleRun`. For an example of the JSON request syntax, see [ScheduleRun](API_ScheduleRun.md).

It is also passed in as the `filters` parameter to `ListDevices`. For an example of the JSON request syntax, see [ListDevices](API_ListDevices.md).

## Contents
<a name="API_DeviceFilter_Contents"></a>

 ** attribute **   <a name="devicefarm-Type-DeviceFilter-attribute"></a>
The aspect of a device such as platform or model used as the selection criteria in a device filter.
The supported operators for each attribute are provided in the following list.
ARN
The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example`).
Supported operators: `EQUALS`, `IN`, `NOT_IN`
PLATFORM
The device platform. Valid values are ANDROID or IOS.
Supported operators: `EQUALS`
OS\_VERSION
The operating system version (for example, 10.3.2).
Supported operators: `EQUALS`, `GREATER_THAN`, `GREATER_THAN_OR_EQUALS`, `IN`, `LESS_THAN`, `LESS_THAN_OR_EQUALS`, `NOT_IN`
MODEL
The device model (for example, iPad 5th Gen).
Supported operators: `CONTAINS`, `EQUALS`, `IN`, `NOT_IN`
AVAILABILITY
The current availability of the device. Valid values are AVAILABLE, HIGHLY\_AVAILABLE, BUSY, or TEMPORARY\_NOT\_AVAILABLE.
Supported operators: `EQUALS`
FORM\_FACTOR
The device form factor. Valid values are PHONE or TABLET.
Supported operators: `EQUALS`
MANUFACTURER
The device manufacturer (for example, Apple).
Supported operators: `EQUALS`, `IN`, `NOT_IN`
REMOTE\_ACCESS\_ENABLED
Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: `EQUALS`
REMOTE\_DEBUG\_ENABLED
Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: `EQUALS`
Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html), this filter is ignored.
INSTANCE\_ARN
The Amazon Resource Name (ARN) of the device instance.
Supported operators: `EQUALS`, `IN`, `NOT_IN`
INSTANCE\_LABELS
The label of the device instance.
Supported operators: `CONTAINS`
FLEET\_TYPE
The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: `EQUALS`
Type: String
Valid Values: `ARN | PLATFORM | OS_VERSION | MODEL | AVAILABILITY | FORM_FACTOR | MANUFACTURER | REMOTE_ACCESS_ENABLED | REMOTE_DEBUG_ENABLED | INSTANCE_ARN | INSTANCE_LABELS | FLEET_TYPE`
Required: Yes

 ** operator **   <a name="devicefarm-Type-DeviceFilter-operator"></a>
Specifies how Device Farm compares the filter's attribute to the value. See the attribute descriptions.
Type: String
Valid Values: `EQUALS | LESS_THAN | LESS_THAN_OR_EQUALS | GREATER_THAN | GREATER_THAN_OR_EQUALS | IN | NOT_IN | CONTAINS`
Required: Yes

 ** values **   <a name="devicefarm-Type-DeviceFilter-values"></a>
An array of one or more filter values used in a device filter.

**Operator Values**
+ The IN and NOT\_IN operators can take a values array that has more than one element.
+ The other operators require an array with a single element.

**Attribute Values**
+ The PLATFORM attribute can be set to ANDROID or IOS.
+ The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY\_AVAILABLE, BUSY, or TEMPORARY\_NOT\_AVAILABLE.
+ The FORM\_FACTOR attribute can be set to PHONE or TABLET.
+ The FLEET\_TYPE attribute can be set to PUBLIC or PRIVATE.
Type: Array of strings
Required: Yes

## See Also
<a name="API_DeviceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/DeviceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/DeviceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/DeviceFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
