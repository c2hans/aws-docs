---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroupStickinessConfig.html
---

# TargetGroupStickinessConfig
<a name="API_TargetGroupStickinessConfig"></a>

Information about the target group stickiness for a rule.

## Contents
<a name="API_TargetGroupStickinessConfig_Contents"></a>

 ** DurationSeconds **
[Application Load Balancers] The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days). You must specify this value when enabling target group stickiness.
Type: Integer
Required: No

 ** Enabled **
Indicates whether target group stickiness is enabled.
Type: Boolean
Required: No

## See Also
<a name="API_TargetGroupStickinessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TargetGroupStickinessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TargetGroupStickinessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TargetGroupStickinessConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
