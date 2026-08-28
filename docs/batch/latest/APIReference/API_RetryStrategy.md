---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_RetryStrategy.html
---

# RetryStrategy
<a name="API_RetryStrategy"></a>

The retry strategy that's associated with a job. For more information, see [Automated job retries](https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_RetryStrategy_Contents"></a>

 ** attempts **   <a name="Batch-Type-RetryStrategy-attempts"></a>
The number of times to move a job to the `RUNNABLE` status. You can specify between 1 and 10 attempts. If the value of `attempts` is greater than one, the job is retried on failure the same number of attempts as the value.
Type: Integer
Required: No

 ** evaluateOnExit **   <a name="Batch-Type-RetryStrategy-evaluateOnExit"></a>
Array of up to 5 objects that specify the conditions where jobs are retried or failed. If this parameter is specified, then the `attempts` parameter must also be specified. If none of the listed conditions match, then the job is retried.
Type: Array of [EvaluateOnExit](API_EvaluateOnExit.md) objects
Required: No

## See Also
<a name="API_RetryStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/RetryStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/RetryStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/RetryStrategy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
