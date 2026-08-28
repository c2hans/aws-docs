---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer AppCookieStickinessPolicy
<a name="aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy"></a>

Specifies a policy for application-controlled session stickiness for your Classic Load Balancer.

To associate a policy with a listener, use the [PolicyNames](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-policynames) property for the listener.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-syntax.json"></a>

```
{
  "[CookieName](#cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-cookiename)" : {{String}},
  "[PolicyName](#cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-policyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-syntax.yaml"></a>

```
  [CookieName](#cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-cookiename): {{String}}
  [PolicyName](#cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-policyname): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-properties"></a>

`CookieName`  <a name="cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-cookiename"></a>
The name of the application cookie used for stickiness.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy-policyname"></a>
The mnemonic name for the policy being created. The name must be unique within a set of policies for this load balancer.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-appcookiestickinesspolicy--seealso"></a>
+ [CreateAppCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateAppCookieStickinessPolicy.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [Sticky Sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html) in the *User Guide for Classic Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
