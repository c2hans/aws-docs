---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceStatus.html
---

# InstanceStatus
<a name="API_InstanceStatus"></a>

The instance status details.

## Contents
<a name="API_InstanceStatus_Contents"></a>

 ** State **   <a name="EMR-Type-InstanceStatus-State"></a>
The current state of the instance.
Type: String
Valid Values: `AWAITING_FULFILLMENT | PROVISIONING | BOOTSTRAPPING | RUNNING | TERMINATED`
Required: No

 ** StateChangeReason **   <a name="EMR-Type-InstanceStatus-StateChangeReason"></a>
The details of the status change reason for the instance.
Type: [InstanceStateChangeReason](API_InstanceStateChangeReason.md) object
Required: No

 ** Timeline **   <a name="EMR-Type-InstanceStatus-Timeline"></a>
The timeline of the instance status over time.
Type: [InstanceTimeline](API_InstanceTimeline.md) object
Required: No

## See Also
<a name="API_InstanceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
