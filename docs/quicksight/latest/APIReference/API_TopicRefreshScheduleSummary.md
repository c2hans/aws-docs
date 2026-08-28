---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicRefreshScheduleSummary.html
---

# TopicRefreshScheduleSummary
<a name="API_TopicRefreshScheduleSummary"></a>

A summary of the refresh schedule details for a dataset.

## Contents
<a name="API_TopicRefreshScheduleSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DatasetArn **   <a name="QS-Type-TopicRefreshScheduleSummary-DatasetArn"></a>
The Amazon Resource Name (ARN) of the dataset.
Type: String
Required: No

 ** DatasetId **   <a name="QS-Type-TopicRefreshScheduleSummary-DatasetId"></a>
The ID of the dataset.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** DatasetName **   <a name="QS-Type-TopicRefreshScheduleSummary-DatasetName"></a>
The name of the dataset.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** RefreshSchedule **   <a name="QS-Type-TopicRefreshScheduleSummary-RefreshSchedule"></a>
The definition of a refresh schedule.
Type: [TopicRefreshSchedule](API_TopicRefreshSchedule.md) object
Required: No

## See Also
<a name="API_TopicRefreshScheduleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicRefreshScheduleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicRefreshScheduleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicRefreshScheduleSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
