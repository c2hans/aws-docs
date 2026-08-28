---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SchedulerStatus.html
---

# SchedulerStatus
<a name="API_SchedulerStatus"></a>

The current job-run counts for a virtual cluster, reflecting how much of the configured scheduler capacity is in use.

## Contents
<a name="API_SchedulerStatus_Contents"></a>

 ** currentConcurrentJobRuns **   <a name="emroneks-Type-SchedulerStatus-currentConcurrentJobRuns"></a>
The number of job runs currently in the `RUNNING` state for the virtual cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** currentInQueueJobRuns **   <a name="emroneks-Type-SchedulerStatus-currentInQueueJobRuns"></a>
The number of job runs currently waiting in the queue (`PENDING` or `SUBMITTED`) for the virtual cluster.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_SchedulerStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/SchedulerStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/SchedulerStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/SchedulerStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR on EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-on-eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
