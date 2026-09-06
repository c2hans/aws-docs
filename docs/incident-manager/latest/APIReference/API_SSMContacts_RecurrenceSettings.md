---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_RecurrenceSettings.html
---

# RecurrenceSettings
<a name="API_SSMContacts_RecurrenceSettings"></a>

Information about when an on-call rotation is in effect and how long the rotation period lasts.

## Contents
<a name="API_SSMContacts_RecurrenceSettings_Contents"></a>

 ** NumberOfOnCalls **   <a name="IncidentManager-Type-SSMContacts_RecurrenceSettings-NumberOfOnCalls"></a>
The number of contacts, or shift team members designated to be on call concurrently during a shift. For example, in an on-call schedule that contains ten contacts, a value of `2` designates that two of them are on call at any given time.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** RecurrenceMultiplier **   <a name="IncidentManager-Type-SSMContacts_RecurrenceSettings-RecurrenceMultiplier"></a>
The number of days, weeks, or months a single rotation lasts.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** DailySettings **   <a name="IncidentManager-Type-SSMContacts_RecurrenceSettings-DailySettings"></a>
Information about on-call rotations that recur daily.
Type: Array of [HandOffTime](API_SSMContacts_HandOffTime.md) objects
Required: No

 ** MonthlySettings **   <a name="IncidentManager-Type-SSMContacts_RecurrenceSettings-MonthlySettings"></a>
Information about on-call rotations that recur monthly.
Type: Array of [MonthlySetting](API_SSMContacts_MonthlySetting.md) objects
Required: No

 ** ShiftCoverages **   <a name="IncidentManager-Type-SSMContacts_RecurrenceSettings-ShiftCoverages"></a>
Information about the days of the week that the on-call rotation coverage includes.
Type: String to array of [CoverageTime](API_SSMContacts_CoverageTime.md) objects map
Valid Keys: `MON | TUE | WED | THU | FRI | SAT | SUN`
Required: No

 ** WeeklySettings **   <a name="IncidentManager-Type-SSMContacts_RecurrenceSettings-WeeklySettings"></a>
Information about on-call rotations that recur weekly.
Type: Array of [WeeklySetting](API_SSMContacts_WeeklySetting.md) objects
Required: No

## See Also
<a name="API_SSMContacts_RecurrenceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-contacts-2021-05-03/RecurrenceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-contacts-2021-05-03/RecurrenceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-contacts-2021-05-03/RecurrenceSettings)
