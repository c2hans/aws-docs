---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-greengrassv2-component.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Component
<a name="aws-resource-greengrassv2-component"></a>

<a name="aws-resource-greengrassv2-component-description"></a>The `AWS::GreengrassV2::Component` resource Property description not available. for GreengrassV2.

## Syntax
<a name="aws-resource-greengrassv2-component-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-greengrassv2-component-syntax.json"></a>

```
{
  "Type" : "AWS::GreengrassV2::Component",
  "Properties" : {
      "[ComponentName](#cfn-greengrassv2-component-componentname)" : {{String}},
      "[Tags](#cfn-greengrassv2-component-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-greengrassv2-component-syntax.yaml"></a>

```
Type: AWS::GreengrassV2::Component
Properties:
  [ComponentName](#cfn-greengrassv2-component-componentname): {{String}}
  [Tags](#cfn-greengrassv2-component-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-greengrassv2-component-properties"></a>

`ComponentName`  <a name="cfn-greengrassv2-component-componentname"></a>
The name of the component.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-greengrassv2-component-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-greengrassv2-component-tagsitems.md)
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-greengrassv2-component-return-values"></a>

### Ref
<a name="aws-resource-greengrassv2-component-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-greengrassv2-component-return-values-fn--getatt"></a>

####
<a name="aws-resource-greengrassv2-component-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.
