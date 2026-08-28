---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_TopicsDetectionJobFilter.html
---

# TopicsDetectionJobFilter
<a name="API_TopicsDetectionJobFilter"></a>

**Important**
Service availability notice: Amazon Comprehend topic modeling, event detection, and prompt safety classification features will no longer be available to new customers, effective April 30, 2026. For more information, see [Amazon Comprehend feature availability change](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-availability-change.html).

Provides information for filtering topic detection jobs. For more information, see [ListTopicsDetectionJobs](API_ListTopicsDetectionJobs.md).

## Contents
<a name="API_TopicsDetectionJobFilter_Contents"></a>

 ** JobName **   <a name="comprehend-Type-TopicsDetectionJobFilter-JobName"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: No

 ** JobStatus **   <a name="comprehend-Type-TopicsDetectionJobFilter-JobStatus"></a>
Filters the list of topic detection jobs based on job status. Returns only jobs with the specified status.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | COMPLETED | FAILED | STOP_REQUESTED | STOPPED`
Required: No

 ** SubmitTimeAfter **   <a name="comprehend-Type-TopicsDetectionJobFilter-SubmitTimeAfter"></a>
Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted after the specified time. Jobs are returned in ascending order, oldest to newest.
Type: Timestamp
Required: No

 ** SubmitTimeBefore **   <a name="comprehend-Type-TopicsDetectionJobFilter-SubmitTimeBefore"></a>
Filters the list of jobs based on the time that the job was submitted for processing. Only returns jobs submitted before the specified time. Jobs are returned in descending order, newest to oldest.
Type: Timestamp
Required: No

## See Also
<a name="API_TopicsDetectionJobFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/TopicsDetectionJobFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/TopicsDetectionJobFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/TopicsDetectionJobFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
