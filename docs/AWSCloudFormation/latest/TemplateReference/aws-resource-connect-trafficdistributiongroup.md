---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-trafficdistributiongroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TrafficDistributionGroup
<a name="aws-resource-connect-trafficdistributiongroup"></a>

Information about a traffic distribution group.

## Syntax
<a name="aws-resource-connect-trafficdistributiongroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-trafficdistributiongroup-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::TrafficDistributionGroup",
  "Properties" : {
      "[Description](#cfn-connect-trafficdistributiongroup-description)" : {{String}},
      "[InstanceArn](#cfn-connect-trafficdistributiongroup-instancearn)" : {{String}},
      "[Name](#cfn-connect-trafficdistributiongroup-name)" : {{String}},
      "[Tags](#cfn-connect-trafficdistributiongroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-trafficdistributiongroup-syntax.yaml"></a>

```
Type: AWS::Connect::TrafficDistributionGroup
Properties:
  [Description](#cfn-connect-trafficdistributiongroup-description): {{String}}
  [InstanceArn](#cfn-connect-trafficdistributiongroup-instancearn): {{String}}
  [Name](#cfn-connect-trafficdistributiongroup-name): {{String}}
  [Tags](#cfn-connect-trafficdistributiongroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-trafficdistributiongroup-properties"></a>

`Description`  <a name="cfn-connect-trafficdistributiongroup-description"></a>
The description of the traffic distribution group.
*Required*: No
*Type*: String
*Pattern*: `(^[\S].*[\S]$)|(^[\S]$)`
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceArn`  <a name="cfn-connect-trafficdistributiongroup-instancearn"></a>
The Amazon Resource Name (ARN).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-connect-trafficdistributiongroup-name"></a>
The name of the traffic distribution group.
*Required*: Yes
*Type*: String
*Pattern*: `(^[\S].*[\S]$)|(^[\S]$)`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-trafficdistributiongroup-tags"></a>
The tags used to organize, track, or control access for this resource. For example, {"tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-trafficdistributiongroup-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-trafficdistributiongroup-return-values"></a>

### Ref
<a name="aws-resource-connect-trafficdistributiongroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the traffic distribution group name. For example:

 `{ "Ref": "myTrafficDistributionGroupName" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-trafficdistributiongroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-trafficdistributiongroup-return-values-fn--getatt-fn--getatt"></a>

`IsDefault`  <a name="IsDefault-fn::getatt"></a>
Describes whether this is the default traffic distribution group.

`Status`  <a name="Status-fn::getatt"></a>
The status of the traffic distribution group.

`TrafficDistributionGroupArn`  <a name="TrafficDistributionGroupArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the traffic distribution group.
