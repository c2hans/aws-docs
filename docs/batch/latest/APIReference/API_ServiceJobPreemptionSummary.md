---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ServiceJobPreemptionSummary.html
---

# ServiceJobPreemptionSummary
<a name="API_ServiceJobPreemptionSummary"></a>

Summarizes the preemptions of the service job. This field appears on a service job when it has been preempted.

## Contents
<a name="API_ServiceJobPreemptionSummary_Contents"></a>

 ** preemptedAttemptCount **   <a name="Batch-Type-ServiceJobPreemptionSummary-preemptedAttemptCount"></a>
The total number of times the service job has been preempted.
Type: Integer
Required: No

 ** recentPreemptedAttempts **   <a name="Batch-Type-ServiceJobPreemptionSummary-recentPreemptedAttempts"></a>
A list of the most recent preemption attempts for the service job.
Type: Array of [ServiceJobPreemptedAttempt](API_ServiceJobPreemptedAttempt.md) objects
Required: No

## See Also
<a name="API_ServiceJobPreemptionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobPreemptionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobPreemptionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobPreemptionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
