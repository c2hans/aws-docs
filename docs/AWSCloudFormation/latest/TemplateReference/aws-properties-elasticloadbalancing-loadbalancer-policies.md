---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancing-loadbalancer-policies.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancing::LoadBalancer Policies
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies"></a>

Specifies policies for your Classic Load Balancer.

To associate policies with a listener, use the [PolicyNames](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-policynames) property for the listener.

## Syntax
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies-syntax.json"></a>

```
{
  "[Attributes](#cfn-elasticloadbalancing-loadbalancer-policies-attributes)" : {{[ {{{Key}}: {{Value}}, ...}, ... ]}},
  "[InstancePorts](#cfn-elasticloadbalancing-loadbalancer-policies-instanceports)" : {{[ String, ... ]}},
  "[LoadBalancerPorts](#cfn-elasticloadbalancing-loadbalancer-policies-loadbalancerports)" : {{[ String, ... ]}},
  "[PolicyName](#cfn-elasticloadbalancing-loadbalancer-policies-policyname)" : {{String}},
  "[PolicyType](#cfn-elasticloadbalancing-loadbalancer-policies-policytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies-syntax.yaml"></a>

```
  [Attributes](#cfn-elasticloadbalancing-loadbalancer-policies-attributes): {{
    -
    {{Key}}: {{Value}}}}
  [InstancePorts](#cfn-elasticloadbalancing-loadbalancer-policies-instanceports): {{
    - String}}
  [LoadBalancerPorts](#cfn-elasticloadbalancing-loadbalancer-policies-loadbalancerports): {{
    - String}}
  [PolicyName](#cfn-elasticloadbalancing-loadbalancer-policies-policyname): {{String}}
  [PolicyType](#cfn-elasticloadbalancing-loadbalancer-policies-policytype): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies-properties"></a>

`Attributes`  <a name="cfn-elasticloadbalancing-loadbalancer-policies-attributes"></a>
The policy attributes.
*Required*: Yes
*Type*: Array of Object
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstancePorts`  <a name="cfn-elasticloadbalancing-loadbalancer-policies-instanceports"></a>
The instance ports for the policy. Required only for some policy types.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadBalancerPorts`  <a name="cfn-elasticloadbalancing-loadbalancer-policies-loadbalancerports"></a>
The load balancer ports for the policy. Required only for some policy types.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-elasticloadbalancing-loadbalancer-policies-policyname"></a>
The name of the policy.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyType`  <a name="cfn-elasticloadbalancing-loadbalancer-policies-policytype"></a>
The name of the policy type.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies--examples"></a>

###
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies--examples--"></a>

#### JSON
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies--examples----json"></a>

```
"Policies": [{
    "PolicyName": "My-SSLNegotiation-Policy",
    "PolicyType": "SSLNegotiationPolicyType",
    "Attributes": [{
        "Name": "Reference-Security-Policy",
        "Value": "ELBSecurityPolicy-TLS-1-2-2017-01"
    }]
}]
```

#### YAML
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies--examples----yaml"></a>

```
Policies:
    - PolicyName: My-SSLNegotiation-Policy
      PolicyType: SSLNegotiationPolicyType
      Attributes:
      - Name: Reference-Security-Policy
        Value: ELBSecurityPolicy-TLS-1-2-2017-01
```

## See also
<a name="aws-properties-elasticloadbalancing-loadbalancer-policies--seealso"></a>
+ [CreateLoadBalancerPolicy](https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_CreateLoadBalancerPolicy.html) in the *Elastic Load Balancing API Reference (version 2012-06-01)*
