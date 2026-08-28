---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ServerStatusSummary.html
---

# ServerStatusSummary
<a name="API_ServerStatusSummary"></a>

The status summary of the server analysis.

## Contents
<a name="API_ServerStatusSummary_Contents"></a>

 ** count **   <a name="migrationhubstrategy-Type-ServerStatusSummary-count"></a>
The number of servers successfully analyzed, partially successful or failed analysis.
Type: Integer
Required: No

 ** runTimeAssessmentStatus **   <a name="migrationhubstrategy-Type-ServerStatusSummary-runTimeAssessmentStatus"></a>
The status of the run time.
Type: String
Valid Values: `dataCollectionTaskToBeScheduled | dataCollectionTaskScheduled | dataCollectionTaskStarted | dataCollectionTaskStopped | dataCollectionTaskSuccess | dataCollectionTaskFailed | dataCollectionTaskPartialSuccess`
Required: No

## See Also
<a name="API_ServerStatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/ServerStatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/ServerStatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/ServerStatusSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Strategy Recommendations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-strategy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
