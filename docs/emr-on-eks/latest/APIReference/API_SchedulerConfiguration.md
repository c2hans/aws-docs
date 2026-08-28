---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SchedulerConfiguration.html
---

# SchedulerConfiguration
<a name="API_SchedulerConfiguration"></a>

The scheduler configuration for a virtual cluster on Amazon EMR on EKS. It controls how many job runs can run concurrently and how many can wait in the queue. When not set, no concurrency or queue limits are applied.

## Contents
<a name="API_SchedulerConfiguration_Contents"></a>

 ** maxConcurrentJobRuns **   <a name="emroneks-Type-SchedulerConfiguration-maxConcurrentJobRuns"></a>
The maximum number of job runs that can be in the `RUNNING` state at any time for the virtual cluster. As running slots free up, queued job runs start automatically. If you omit this field, the service applies no concurrency limit.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** maxInQueueJobRuns **   <a name="emroneks-Type-SchedulerConfiguration-maxInQueueJobRuns"></a>
The maximum number of job runs that can be in the `PENDING` or `SUBMITTED` state at any time for the virtual cluster. When the queue is full, the service rejects `StartJobRun` requests with a `ValidationException`. If you omit this field, the service applies no queue-depth limit.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## See Also
<a name="API_SchedulerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/SchedulerConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/SchedulerConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/SchedulerConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
