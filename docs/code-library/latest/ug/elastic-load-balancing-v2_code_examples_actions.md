---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/elastic-load-balancing-v2_code_examples_actions.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Actions for Elastic Load Balancing - Version 2 using AWS SDKs
<a name="elastic-load-balancing-v2_code_examples_actions"></a>

The following code examples demonstrate how to perform individual Elastic Load Balancing - Version 2 actions with AWS SDKs. Each example includes a link to GitHub, where you can find instructions for setting up and running the code.

These excerpts call the Elastic Load Balancing - Version 2 API and are code excerpts from larger programs that must be run in context. You can see actions in context in [Scenarios for Elastic Load Balancing - Version 2 using AWS SDKs](elastic-load-balancing-v2_code_examples_scenarios.md).

 The following examples include only the most commonly used actions. For a complete list, see the [Elastic Load Balancing - Version 2 API Reference](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/Welcome.html).

**Topics**
+ [`AddListenerCertificates`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_AddListenerCertificates_section.md)
+ [`AddTags`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_AddTags_section.md)
+ [`CreateListener`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_CreateListener_section.md)
+ [`CreateLoadBalancer`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_CreateLoadBalancer_section.md)
+ [`CreateRule`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_CreateRule_section.md)
+ [`CreateTargetGroup`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_CreateTargetGroup_section.md)
+ [`DeleteListener`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DeleteListener_section.md)
+ [`DeleteLoadBalancer`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DeleteLoadBalancer_section.md)
+ [`DeleteRule`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DeleteRule_section.md)
+ [`DeleteTargetGroup`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DeleteTargetGroup_section.md)
+ [`DeregisterTargets`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DeregisterTargets_section.md)
+ [`DescribeAccountLimits`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeAccountLimits_section.md)
+ [`DescribeListenerCertificates`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeListenerCertificates_section.md)
+ [`DescribeListeners`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeListeners_section.md)
+ [`DescribeLoadBalancerAttributes`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeLoadBalancerAttributes_section.md)
+ [`DescribeLoadBalancers`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeLoadBalancers_section.md)
+ [`DescribeRules`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeRules_section.md)
+ [`DescribeSslPolicies`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeSslPolicies_section.md)
+ [`DescribeTags`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeTags_section.md)
+ [`DescribeTargetGroupAttributes`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeTargetGroupAttributes_section.md)
+ [`DescribeTargetGroups`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeTargetGroups_section.md)
+ [`DescribeTargetHealth`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_DescribeTargetHealth_section.md)
+ [`ModifyListener`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyListener_section.md)
+ [`ModifyLoadBalancerAttributes`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyLoadBalancerAttributes_section.md)
+ [`ModifyRule`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyRule_section.md)
+ [`ModifyTargetGroup`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyTargetGroup_section.md)
+ [`ModifyTargetGroupAttributes`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_ModifyTargetGroupAttributes_section.md)
+ [`RegisterTargets`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_RegisterTargets_section.md)
+ [`RemoveListenerCertificates`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_RemoveListenerCertificates_section.md)
+ [`RemoveTags`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_RemoveTags_section.md)
+ [`SetIpAddressType`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetIpAddressType_section.md)
+ [`SetRulePriorities`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetRulePriorities_section.md)
+ [`SetSecurityGroups`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetSecurityGroups_section.md)
+ [`SetSubnets`](elastic-load-balancing-v2_example_elastic-load-balancing-v2_SetSubnets_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
