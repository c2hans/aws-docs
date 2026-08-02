---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ScheduledInstance.html
---

# ScheduledInstance
<a name="API_ScheduledInstance"></a>

Describes a Scheduled Instance.

## Contents
<a name="API_ScheduledInstance_Contents"></a>

 ** availabilityZone **
The Availability Zone.
Type: String
Required: No

 ** createDate **
The date when the Scheduled Instance was purchased.
Type: Timestamp
Required: No

 ** hourlyPrice **
The hourly price for a single instance.
Type: String
Required: No

 ** instanceCount **
The number of instances.
Type: Integer
Required: No

 ** instanceType **
The instance type.
Type: String
Required: No

 ** networkPlatform **
The network platform.
Type: String
Required: No

 ** nextSlotStartTime **
The time for the next schedule to start.
Type: Timestamp
Required: No

 ** platform **
The platform (`Linux/UNIX` or `Windows`).
Type: String
Required: No

 ** previousSlotEndTime **
The time that the previous schedule ended or will end.
Type: Timestamp
Required: No

 ** recurrence **
The schedule recurrence.
Type: [ScheduledInstanceRecurrence](API_ScheduledInstanceRecurrence.md) object
Required: No

 ** scheduledInstanceId **
The Scheduled Instance ID.
Type: String
Required: No

 ** slotDurationInHours **
The number of hours in the schedule.
Type: Integer
Required: No

 ** termEndDate **
The end date for the Scheduled Instance.
Type: Timestamp
Required: No

 ** termStartDate **
The start date for the Scheduled Instance.
Type: Timestamp
Required: No

 ** totalScheduledInstanceHours **
The total number of hours for a single instance for the entire term.
Type: Integer
Required: No

## See Also
<a name="API_ScheduledInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ScheduledInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ScheduledInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ScheduledInstance)
