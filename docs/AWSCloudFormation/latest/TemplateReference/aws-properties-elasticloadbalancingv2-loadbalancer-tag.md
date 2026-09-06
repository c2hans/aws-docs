---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-loadbalancer-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::LoadBalancer Tag
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag"></a>

Information about a tag.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag-syntax.json"></a>

```
{
  "[Key](#cfn-elasticloadbalancingv2-loadbalancer-tag-key)" : {{String}},
  "[Value](#cfn-elasticloadbalancingv2-loadbalancer-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag-syntax.yaml"></a>

```
  [Key](#cfn-elasticloadbalancingv2-loadbalancer-tag-key): {{String}}
  [Value](#cfn-elasticloadbalancingv2-loadbalancer-tag-value): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag-properties"></a>

`Key`  <a name="cfn-elasticloadbalancingv2-loadbalancer-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticloadbalancingv2-loadbalancer-tag-value"></a>
The value of the tag.
*Required*: No
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag--examples--"></a>

The following example creates a Network Load Balancer with two tags.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag--examples----yaml"></a>

```
myLoadBalancer:
    Type: AWS::ElasticLoadBalancingV2::LoadBalancer
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      Tags:
        - Key: "department"
          Value: "123"
        - Key: "project"
          Value: "lima"
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-tag--examples----json"></a>

```
{
    "myLoadBalancer": {
        "Type": "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "Properties": {
            "Name": "my-alb",
            "Type": "network",
            "Scheme": "internal",
            "Subnets": [
                {
                    "Ref": "subnet-AZ1"
                },
                {
                    "Ref": "subnet-AZ2"
                }
            ],
            "SecurityGroups": [
                {
                    "Ref": "mySecurityGroup"
                }
            ],
            "Tags": [
                {
                    "Key": "department",
                    "Value": "123"
                },
                {
                    "Key": "project",
                    "Value": "lima"
                }
            ]
        }
    }
}
```
