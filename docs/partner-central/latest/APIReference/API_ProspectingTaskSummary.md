---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProspectingTaskSummary.html
---

# ProspectingTaskSummary
<a name="API_ProspectingTaskSummary"></a>

A summary of a single prospecting task, returned by `ListProspectingFromEngagementTasks`. Contains key metrics and status information without the full per-engagement detail available from `GetProspectingFromEngagementTask`.

## Contents
<a name="API_ProspectingTaskSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CompletedEngagementCount **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-CompletedEngagementCount"></a>
The number of engagements that have been successfully converted into prospecting leads.
Type: Integer
Required: Yes

 ** FailedEngagementCount **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-FailedEngagementCount"></a>
The number of engagements that failed to be converted. Retrieve the full task details using `GetProspectingFromEngagementTask` for per-engagement error information.
Type: Integer
Required: Yes

 ** StartTime **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-StartTime"></a>
The timestamp indicating when the task was initiated. The format follows ISO 8601 date-time notation.
Type: Timestamp
Required: Yes

 ** TaskArn **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-TaskArn"></a>
The Amazon Resource Name (ARN) of the task.
Type: String
Pattern: `arn:aws:partnercentral-selling:.*:.*:catalog/.*/prospecting-from-engagement-task/task-[0-9a-z]{14}`
Required: Yes

 ** TaskId **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-TaskId"></a>
The unique identifier of the task. Use this value with `GetProspectingFromEngagementTask` to retrieve full task details.
Type: String
Pattern: `task-[0-9a-z]{14}`
Required: Yes

 ** TaskName **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-TaskName"></a>
The descriptive name of the task provided when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** TotalEngagementCount **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-TotalEngagementCount"></a>
The total number of engagements included in the task.
Type: Integer
Required: Yes

 ** EndTime **   <a name="AWSPartnerCentral-Type-ProspectingTaskSummary-EndTime"></a>
The timestamp indicating when the task finished processing. This field is absent if the task is still in progress. The format follows ISO 8601 date-time notation.
Type: Timestamp
Required: No

## See Also
<a name="API_ProspectingTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProspectingTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProspectingTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProspectingTaskSummary)
