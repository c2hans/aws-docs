---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_JobTimeout.html
---

# JobTimeout
<a name="API_JobTimeout"></a>

An object that represents a job timeout configuration.

## Contents
<a name="API_JobTimeout_Contents"></a>

 ** attemptDurationSeconds **   <a name="Batch-Type-JobTimeout-attemptDurationSeconds"></a>
The job timeout time (in seconds) that's measured from the job attempt's `startedAt` timestamp. After this time passes, AWS Batch terminates your jobs if they aren't finished. The minimum value for the timeout is 60 seconds.
For array jobs, the timeout applies to the child jobs, not to the parent array job.
For multi-node parallel (MNP) jobs, the timeout applies to the whole job, not to the individual nodes.
Type: Integer
Required: No

## See Also
<a name="API_JobTimeout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/JobTimeout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/JobTimeout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/JobTimeout)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
