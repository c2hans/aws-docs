---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer LBCookieStickinessPolicy
<a name="aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy"></a>

Specifies a policy for duration-based session stickiness for your Classic Load Balancer.

To associate a policy with a listener, use the [PolicyNames](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-policynames) property for the listener.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-syntax.json"></a>

```
{
  "[CookieExpirationPeriod](#cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-cookieexpirationperiod)" : {{String}},
  "[PolicyName](#cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-policyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-syntax.yaml"></a>

```
  [CookieExpirationPeriod](#cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-cookieexpirationperiod): {{String}}
  [PolicyName](#cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-policyname): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-properties"></a>

`CookieExpirationPeriod`  <a name="cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-cookieexpirationperiod"></a>
The time period, in seconds, after which the cookie should be considered stale. If this parameter is not specified, the stickiness session lasts for the duration of the browser session.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy-policyname"></a>
The name of the policy. This name must be unique within the set of policies for this load balancer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-lbcookiestickinesspolicy--seealso"></a>
+ [CreateLBCookieStickinessPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLBCookieStickinessPolicy.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [Sticky Sessions](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-sticky-sessions.html) in the *User Guide for Classic Load Balancers*
