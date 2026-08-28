---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-connectionsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer ConnectionSettings
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectionsettings"></a>

Specifies the idle timeout value for your Classic Load Balancer.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectionsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectionsettings-syntax.json"></a>

```
{
  "[IdleTimeout](#cfn-elasticloadbalancing-loadbalancer-connectionsettings-idletimeout)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectionsettings-syntax.yaml"></a>

```
  [IdleTimeout](#cfn-elasticloadbalancing-loadbalancer-connectionsettings-idletimeout): {{Integer}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectionsettings-properties"></a>

`IdleTimeout`  <a name="cfn-elasticloadbalancing-loadbalancer-connectionsettings-idletimeout"></a>
The time, in seconds, that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-connectionsettings--seealso"></a>
+ [ModifyLoadBalancerAttributes](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_ModifyLoadBalancerAttributes.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [Idle Connection Timeout](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-idle-timeout.html) in the *User Guide for Classic Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
