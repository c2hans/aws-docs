---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_ScheduledOperationDetails.html
---

# ScheduledOperationDetails
<a name="API_ScheduledOperationDetails"></a>

The scheduled start and stop times for an Autonomous Database on a specific day of the week.

## Contents
<a name="API_ScheduledOperationDetails_Contents"></a>

 ** dayOfWeek **   <a name="odb-Type-ScheduledOperationDetails-dayOfWeek"></a>
The day of the week on which the scheduled operation occurs.
Type: [DayOfWeek](API_DayOfWeek.md) object
Required: Yes

 ** scheduledStartTime **   <a name="odb-Type-ScheduledOperationDetails-scheduledStartTime"></a>
The scheduled start time for the Autonomous Database, in UTC.
Type: String
Required: No

 ** scheduledStopTime **   <a name="odb-Type-ScheduledOperationDetails-scheduledStopTime"></a>
The scheduled stop time for the Autonomous Database, in UTC.
Type: String
Required: No

## See Also
<a name="API_ScheduledOperationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/ScheduledOperationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/ScheduledOperationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/ScheduledOperationDetails)
