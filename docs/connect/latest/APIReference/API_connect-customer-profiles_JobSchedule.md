---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_JobSchedule.html
---

# JobSchedule
<a name="API_connect-customer-profiles_JobSchedule"></a>

The day and time when do you want to start the Identity Resolution Job every week.

## Contents
<a name="API_connect-customer-profiles_JobSchedule_Contents"></a>

 ** DayOfTheWeek **   <a name="connect-Type-connect-customer-profiles_JobSchedule-DayOfTheWeek"></a>
The day when the Identity Resolution Job should run every week.
Type: String
Valid Values: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
Required: Yes

 ** Time **   <a name="connect-Type-connect-customer-profiles_JobSchedule-Time"></a>
The time when the Identity Resolution Job should run every week.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 5.
Pattern: `^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_JobSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/JobSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/JobSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/JobSchedule)
