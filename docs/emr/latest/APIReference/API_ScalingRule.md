---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ScalingRule.html
---

# ScalingRule
<a name="API_ScalingRule"></a>

A scale-in or scale-out rule that defines scaling activity, including the CloudWatch metric alarm that triggers activity, how Amazon EC2 instances are added or removed, and the periodicity of adjustments. The automatic scaling policy for an instance group can comprise one or more automatic scaling rules.

## Contents
<a name="API_ScalingRule_Contents"></a>

 ** Action **   <a name="EMR-Type-ScalingRule-Action"></a>
The conditions that trigger an automatic scaling activity.
Type: [ScalingAction](API_ScalingAction.md) object
Required: Yes

 ** Name **   <a name="EMR-Type-ScalingRule-Name"></a>
The name used to identify an automatic scaling rule. Rule names must be unique within a scaling policy.
Type: String
Required: Yes

 ** Trigger **   <a name="EMR-Type-ScalingRule-Trigger"></a>
The CloudWatch alarm definition that determines when automatic scaling activity is triggered.
Type: [ScalingTrigger](API_ScalingTrigger.md) object
Required: Yes

 ** Description **   <a name="EMR-Type-ScalingRule-Description"></a>
A friendly, more verbose description of the automatic scaling rule.
Type: String
Required: No

## See Also
<a name="API_ScalingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ScalingRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ScalingRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ScalingRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
