---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer ConnectionDrainingPolicy
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy"></a>

Specifies the connection draining settings for your Classic Load Balancer.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-syntax.json"></a>

```
{
  "[Enabled](#cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-enabled)" : {{Boolean}},
  "[Timeout](#cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-timeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-syntax.yaml"></a>

```
  [Enabled](#cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-enabled): {{Boolean}}
  [Timeout](#cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-timeout): {{Integer}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-properties"></a>

`Enabled`  <a name="cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-enabled"></a>
Specifies whether connection draining is enabled for the load balancer.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-elasticloadbalancing-loadbalancer-connectiondrainingpolicy-timeout"></a>
The maximum time, in seconds, to keep the existing connections open before deregistering the instances.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectiondrainingpolicy--seealso"></a>
+ [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [Connection Draining](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html) in the *User Guide for Classic Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
