---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBaseRefreshScheduleSummary.html
---

# KnowledgeBaseRefreshScheduleSummary

A summary of a knowledge base refresh schedule, including its identifier, frequency, start time, and state. The `DescribeKnowledgeBaseRefreshSchedule` and `ListKnowledgeBaseRefreshSchedules` operations return this summary.

## Contents
<a name="API_KnowledgeBaseRefreshScheduleSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ScheduleFrequency **   <a name="QS-Type-KnowledgeBaseRefreshScheduleSummary-ScheduleFrequency"></a>
The frequency configuration for the refresh schedule. The frequency configuration specifies how often the schedule runs and, for weekly or monthly schedules, the day on which it runs.
Type: [KnowledgeBaseRefreshFrequency](API_KnowledgeBaseRefreshFrequency.md) object
Required: Yes

 ** ScheduleId **   <a name="QS-Type-KnowledgeBaseRefreshScheduleSummary-ScheduleId"></a>
The unique identifier for the refresh schedule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z_=-][0-9a-zA-Z_=.-]*`
Required: Yes

 ** StartTime **   <a name="QS-Type-KnowledgeBaseRefreshScheduleSummary-StartTime"></a>
The date and time, in ISO 8601 format, after which the schedule can start refreshing the knowledge base.
Type: Timestamp
Required: No

 ** State **   <a name="QS-Type-KnowledgeBaseRefreshScheduleSummary-State"></a>
The current state of the refresh schedule. A schedule that isn't `ENABLED` doesn't run refreshes.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_KnowledgeBaseRefreshScheduleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBaseRefreshScheduleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBaseRefreshScheduleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBaseRefreshScheduleSummary)
