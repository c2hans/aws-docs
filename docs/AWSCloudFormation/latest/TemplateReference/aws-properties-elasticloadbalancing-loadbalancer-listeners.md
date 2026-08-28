---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-listeners.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer Listeners
<a name="aws-properties-elasticloadbalancing-loadbalancer-listeners"></a>

Specifies a listener for your Classic Load Balancer.

Modifying any property replaces the listener.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-listeners-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-listeners-syntax.json"></a>

```
{
  "[InstancePort](#cfn-elasticloadbalancing-loadbalancer-listeners-instanceport)" : {{String}},
  "[InstanceProtocol](#cfn-elasticloadbalancing-loadbalancer-listeners-instanceprotocol)" : {{String}},
  "[LoadBalancerPort](#cfn-elasticloadbalancing-loadbalancer-listeners-loadbalancerport)" : {{String}},
  "[PolicyNames](#cfn-elasticloadbalancing-loadbalancer-listeners-policynames)" : {{[ String, ... ]}},
  "[Protocol](#cfn-elasticloadbalancing-loadbalancer-listeners-protocol)" : {{String}},
  "[SSLCertificateId](#cfn-elasticloadbalancing-loadbalancer-listeners-sslcertificateid)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-listeners-syntax.yaml"></a>

```
  [InstancePort](#cfn-elasticloadbalancing-loadbalancer-listeners-instanceport): {{String}}
  [InstanceProtocol](#cfn-elasticloadbalancing-loadbalancer-listeners-instanceprotocol): {{String}}
  [LoadBalancerPort](#cfn-elasticloadbalancing-loadbalancer-listeners-loadbalancerport): {{String}}
  [PolicyNames](#cfn-elasticloadbalancing-loadbalancer-listeners-policynames): {{
    - String}}
  [Protocol](#cfn-elasticloadbalancing-loadbalancer-listeners-protocol): {{String}}
  [SSLCertificateId](#cfn-elasticloadbalancing-loadbalancer-listeners-sslcertificateid): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-listeners-properties"></a>

`InstancePort`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners-instanceport"></a>
The port on which the instance is listening.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`InstanceProtocol`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners-instanceprotocol"></a>
The protocol to use for routing traffic to instances: HTTP, HTTPS, TCP, or SSL.
If the front-end protocol is TCP or SSL, the back-end protocol must be TCP or SSL. If the front-end protocol is HTTP or HTTPS, the back-end protocol must be HTTP or HTTPS.
If there is another listener with the same `InstancePort` whose `InstanceProtocol` is secure, (HTTPS or SSL), the listener's `InstanceProtocol` must also be secure.
If there is another listener with the same `InstancePort` whose `InstanceProtocol` is HTTP or TCP, the listener's `InstanceProtocol` must be HTTP or TCP.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LoadBalancerPort`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners-loadbalancerport"></a>
The port on which the load balancer is listening. On EC2-VPC, you can specify any port from the range 1-65535. On EC2-Classic, you can specify any port from the following list: 25, 80, 443, 465, 587, 1024-65535.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`PolicyNames`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners-policynames"></a>
The names of the policies to associate with the listener.
*Required*: No
*Type*: Array of String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Protocol`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners-protocol"></a>
The load balancer transport protocol to use for routing: HTTP, HTTPS, TCP, or SSL.
*Required*: Yes
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SSLCertificateId`  <a name="cfn-elasticloadbalancing-loadbalancer-listeners-sslcertificateid"></a>
The Amazon Resource Name (ARN) of the server certificate.
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-listeners--seealso"></a>
+ [CreateLoadBalancerListeners](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerListeners.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
+ [Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html) in the *User Guide for Classic Load Balancers*
+ [HTTPS Listeners](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-https-load-balancers.html) in the *User Guide for Classic Load Balancers*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
