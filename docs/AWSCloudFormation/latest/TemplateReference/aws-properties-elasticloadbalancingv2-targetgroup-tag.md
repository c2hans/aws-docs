---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-targetgroup-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::TargetGroup Tag
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag"></a>

Information about a tag.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag-syntax.json"></a>

```
{
  "[Key](#cfn-elasticloadbalancingv2-targetgroup-tag-key)" : {{String}},
  "[Value](#cfn-elasticloadbalancingv2-targetgroup-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag-syntax.yaml"></a>

```
  [Key](#cfn-elasticloadbalancingv2-targetgroup-tag-key): {{String}}
  [Value](#cfn-elasticloadbalancingv2-targetgroup-tag-value): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag-properties"></a>

`Key`  <a name="cfn-elasticloadbalancingv2-targetgroup-tag-key"></a>
The key of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-elasticloadbalancingv2-targetgroup-tag-value"></a>
The value of the tag.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag--examples"></a>

###
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag--examples--"></a>

The following example creates a target group with two tags.

#### YAML
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag--examples----yaml"></a>

```
myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: instance
      VpcId: !Ref myVPC
      Tags:
        - Key: "department"
          Value: "123"
        - Key: "project"
          Value: "lima"
```

#### JSON
<a name="aws-properties-elasticloadbalancingv2-targetgroup-tag--examples----json"></a>

```
{
    "myTargetGroup": {
        "Type": "AWS::ElasticLoadBalancingV2::TargetGroup",
        "Properties": {
            "Name": "my-target-group",
            "Protocol": "HTTP",
            "Port": 80,
            "TargetType": "instance",
            "VpcId": {
                "Ref": "myVPC"
            },
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
