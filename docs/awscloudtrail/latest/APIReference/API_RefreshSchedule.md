---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RefreshSchedule.html
---

# RefreshSchedule
<a name="API_RefreshSchedule"></a>

 The schedule for a dashboard refresh.

## Contents
<a name="API_RefreshSchedule_Contents"></a>

 ** Frequency **   <a name="awscloudtrail-Type-RefreshSchedule-Frequency"></a>
 The frequency at which you want the dashboard refreshed.
Type: [RefreshScheduleFrequency](API_RefreshScheduleFrequency.md) object
Required: No

 ** Status **   <a name="awscloudtrail-Type-RefreshSchedule-Status"></a>
 Specifies whether the refresh schedule is enabled. Set the value to `ENABLED` to enable the refresh schedule, or to `DISABLED` to turn off the refresh schedule.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** TimeOfDay **   <a name="awscloudtrail-Type-RefreshSchedule-TimeOfDay"></a>
 The time of day in UTC to run the schedule; for hourly only refer to minutes; default is 00:00.
Type: String
Pattern: `^[0-9]{2}:[0-9]{2}`
Required: No

## See Also
<a name="API_RefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/RefreshSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/RefreshSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/RefreshSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
