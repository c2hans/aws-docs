---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_FrontOfQueueDetail.html
---

# FrontOfQueueDetail
<a name="API_FrontOfQueueDetail"></a>

Contains a list of the first 100 `RUNNABLE` jobs associated to a single job queue.

## Contents
<a name="API_FrontOfQueueDetail_Contents"></a>

 ** jobs **   <a name="Batch-Type-FrontOfQueueDetail-jobs"></a>
The Amazon Resource Names (ARNs) of the first 100 `RUNNABLE` jobs in a named job queue. For first-in-first-out (FIFO) job queues, jobs are ordered based on their submission time. For fair-share scheduling (FSS) job queues, jobs are ordered based on their job priority and share usage.
Type: Array of [FrontOfQueueJobSummary](API_FrontOfQueueJobSummary.md) objects
Required: No

 ** lastUpdatedAt **   <a name="Batch-Type-FrontOfQueueDetail-lastUpdatedAt"></a>
The Unix timestamp (in milliseconds) for when each of the first 100 `RUNNABLE` jobs were last updated.
Type: Long
Required: No

## See Also
<a name="API_FrontOfQueueDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/FrontOfQueueDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/FrontOfQueueDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/FrontOfQueueDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
