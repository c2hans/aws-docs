---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_StepStatus.html
---

# StepStatus
<a name="API_StepStatus"></a>

The execution status details of the cluster step.

## Contents
<a name="API_StepStatus_Contents"></a>

 ** FailureDetails **   <a name="EMR-Type-StepStatus-FailureDetails"></a>
The details for the step failure including reason, message, and log file path where the root cause was identified.
Type: [FailureDetails](API_FailureDetails.md) object
Required: No

 ** State **   <a name="EMR-Type-StepStatus-State"></a>
The execution state of the cluster step.
Type: String
Valid Values: `PENDING | CANCEL_PENDING | RUNNING | COMPLETED | CANCELLED | FAILED | INTERRUPTED`
Required: No

 ** StateChangeReason **   <a name="EMR-Type-StepStatus-StateChangeReason"></a>
The reason for the step execution status change.
Type: [StepStateChangeReason](API_StepStateChangeReason.md) object
Required: No

 ** Timeline **   <a name="EMR-Type-StepStatus-Timeline"></a>
The timeline of the cluster step status over time.
Type: [StepTimeline](API_StepTimeline.md) object
Required: No

## See Also
<a name="API_StepStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
