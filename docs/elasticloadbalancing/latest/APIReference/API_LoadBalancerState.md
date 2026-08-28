---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_LoadBalancerState.html
---

# LoadBalancerState
<a name="API_LoadBalancerState"></a>

Information about the state of the load balancer.

## Contents
<a name="API_LoadBalancerState_Contents"></a>

 ** Code **
The state code. The initial state of the load balancer is `provisioning`. After the load balancer is fully set up and ready to route traffic, its state is `active`. If load balancer is routing traffic but does not have the resources it needs to scale, its state is`active_impaired`. If the load balancer could not be set up, its state is `failed`.
Type: String
Valid Values: `active | provisioning | active_impaired | failed`
Required: No

 ** Reason **
A description of the state.
Type: String
Required: No

## See Also
<a name="API_LoadBalancerState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/LoadBalancerState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/LoadBalancerState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/LoadBalancerState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
