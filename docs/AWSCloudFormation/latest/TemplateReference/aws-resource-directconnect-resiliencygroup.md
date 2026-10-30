---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directconnect-resiliencygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::ResiliencyGroup
<a name="aws-resource-directconnect-resiliencygroup"></a>

Information about a resiliency group.

## Syntax
<a name="aws-resource-directconnect-resiliencygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-directconnect-resiliencygroup-syntax.json"></a>

```
{
  "Type" : "AWS::DirectConnect::ResiliencyGroup",
  "Properties" : {
      "[ConnectionArns](#cfn-directconnect-resiliencygroup-connectionarns)" : {{[ String, ... ]}},
      "[IntendedResiliencyModel](#cfn-directconnect-resiliencygroup-intendedresiliencymodel)" : {{String}},
      "[ResiliencyGroupName](#cfn-directconnect-resiliencygroup-resiliencygroupname)" : {{String}},
      "[Tags](#cfn-directconnect-resiliencygroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-directconnect-resiliencygroup-syntax.yaml"></a>

```
Type: AWS::DirectConnect::ResiliencyGroup
Properties:
  [ConnectionArns](#cfn-directconnect-resiliencygroup-connectionarns): {{
    - String}}
  [IntendedResiliencyModel](#cfn-directconnect-resiliencygroup-intendedresiliencymodel): {{String}}
  [ResiliencyGroupName](#cfn-directconnect-resiliencygroup-resiliencygroupname): {{String}}
  [Tags](#cfn-directconnect-resiliencygroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-directconnect-resiliencygroup-properties"></a>

`ConnectionArns`  <a name="cfn-directconnect-resiliencygroup-connectionarns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntendedResiliencyModel`  <a name="cfn-directconnect-resiliencygroup-intendedresiliencymodel"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `maximum-resiliency | high-resiliency | basic-resiliency`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResiliencyGroupName`  <a name="cfn-directconnect-resiliencygroup-resiliencygroupname"></a>
The name of the resiliency group.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-directconnect-resiliencygroup-tags"></a>
The tags associated with the resiliency group.
*Required*: No
*Type*: Array of [Tag](aws-properties-directconnect-resiliencygroup-tag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-directconnect-resiliencygroup-return-values"></a>

### Ref
<a name="aws-resource-directconnect-resiliencygroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-directconnect-resiliencygroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-directconnect-resiliencygroup-return-values-fn--getatt-fn--getatt"></a>

`ResiliencyGroupArn`  <a name="ResiliencyGroupArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resiliency group.

`ResiliencyGroupId`  <a name="ResiliencyGroupId-fn::getatt"></a>
The ID of the resiliency group.
