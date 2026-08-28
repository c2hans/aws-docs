---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::ListenerRule SourceIpConfig
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig"></a>

Information about a source IP condition.

You can use this condition to route based on the IP address of the source that connects to the load balancer. If a client is behind a proxy, this is the IP address of the proxy not the IP address of the client.

For Application Load Balancers, use `Values` to specify CIDR ranges. For Network Load Balancers, use `IpAddressType` to match on the IP address type of the source traffic.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig-syntax.json"></a>

```
{
  "[IpAddressType](#cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-ipaddresstype)" : {{String}},
  "[Values](#cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig-syntax.yaml"></a>

```
  [IpAddressType](#cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-ipaddresstype): {{String}}
  [Values](#cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-values): {{
    - String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig-properties"></a>

`IpAddressType`  <a name="cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-ipaddresstype"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-elasticloadbalancingv2-listenerrule-sourceipconfig-values"></a>
The source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.
If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig--examples--"></a>

The following example creates a listener rule with an action that forwards traffic to the specified target group when the specified source IP condition is met. You can create the target group using [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html).

#### YAML
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig--examples----yaml"></a>

```
myListenerRule:
  Type: 'AWS::ElasticLoadBalancingV2::ListenerRule'
  Properties:
    Actions:
     - Type: forward
       TargetGroupArn: !Ref myTargetGroup
    Conditions:
     - Field: source-ip
       SourceIpConfig:
        Values:
         - 192.168.0.0/16
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-listenerrule-sourceipconfig--examples----json"></a>

```
{
    "myListenerRule": {
        "Type": "AWS::ElasticLoadBalancingV2::ListenerRule",
        "Properties": {
            "Actions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": {
                        "Ref": "myTargetGroup"
                    }
                }
            ],
            "Conditions": [
                {
                    "Field": "source-ip",
                    "SourceIpConfig": {
                        "Values": [
                            "192.168.0.0/24"
                        ]
                    }
                }
            ]
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
