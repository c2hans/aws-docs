---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ForwardActionConfig.html
---

# ForwardActionConfig
<a name="API_ForwardActionConfig"></a>

Information about a forward action.

## Contents
<a name="API_ForwardActionConfig_Contents"></a>

 ** TargetGroups.member.N **
The target groups.
Type: Array of [TargetGroupTuple](API_TargetGroupTuple.md) objects
Required: No

 ** TargetGroupStickinessConfig **
The target group stickiness for the rule.
Type: [TargetGroupStickinessConfig](API_TargetGroupStickinessConfig.md) object
Required: No

## See Also
<a name="API_ForwardActionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ForwardActionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ForwardActionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ForwardActionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
