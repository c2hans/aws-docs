---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstanceAvailability.html
---

# ScheduledInstanceAvailability
<a name="API_ScheduledInstanceAvailability"></a>

Describes a schedule that is available for your Scheduled Instances.

## Contents
<a name="API_ScheduledInstanceAvailability_Contents"></a>

 ** availabilityZone **
The Availability Zone.
Type: String
Required: No

 ** availableInstanceCount **
The number of available instances.
Type: Integer
Required: No

 ** firstSlotStartTime **
The time period for the first schedule to start.
Type: Timestamp
Required: No

 ** hourlyPrice **
The hourly price for a single instance.
Type: String
Required: No

 ** instanceType **
The instance type. You can specify one of the C3, C4, M4, or R3 instance types.
Type: String
Required: No

 ** maxTermDurationInDays **
The maximum term. The only possible value is 365 days.
Type: Integer
Required: No

 ** minTermDurationInDays **
The minimum term. The only possible value is 365 days.
Type: Integer
Required: No

 ** networkPlatform **
The network platform.
Type: String
Required: No

 ** platform **
The platform (`Linux/UNIX` or `Windows`).
Type: String
Required: No

 ** purchaseToken **
The purchase token. This token expires in two hours.
Type: String
Required: No

 ** recurrence **
The schedule recurrence.
Type: [ScheduledInstanceRecurrence](API_ScheduledInstanceRecurrence.md) object
Required: No

 ** slotDurationInHours **
The number of hours in the schedule.
Type: Integer
Required: No

 ** totalScheduledInstanceHours **
The total number of hours for a single instance for the entire term.
Type: Integer
Required: No

## See Also
<a name="API_ScheduledInstanceAvailability_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstanceAvailability)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstanceAvailability)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstanceAvailability)
