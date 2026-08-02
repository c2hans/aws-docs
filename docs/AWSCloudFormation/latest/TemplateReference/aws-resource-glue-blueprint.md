---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-blueprint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Blueprint
<a name="aws-resource-glue-blueprint"></a>

The details of a blueprint.

## Syntax
<a name="aws-resource-glue-blueprint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-blueprint-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::Blueprint",
  "Properties" : {
      "[BlueprintLocation](#cfn-glue-blueprint-blueprintlocation)" : {{String}},
      "[Description](#cfn-glue-blueprint-description)" : {{String}},
      "[Name](#cfn-glue-blueprint-name)" : {{String}},
      "[Tags](#cfn-glue-blueprint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-glue-blueprint-syntax.yaml"></a>

```
Type: AWS::Glue::Blueprint
Properties:
  [BlueprintLocation](#cfn-glue-blueprint-blueprintlocation): {{String}}
  [Description](#cfn-glue-blueprint-description): {{String}}
  [Name](#cfn-glue-blueprint-name): {{String}}
  [Tags](#cfn-glue-blueprint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-glue-blueprint-properties"></a>

`BlueprintLocation`  <a name="cfn-glue-blueprint-blueprintlocation"></a>
Specifies the path in Amazon S3 where the blueprint is published.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://([^/]+)/([^/]+/)*([^/]+)$`
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-glue-blueprint-description"></a>
The description of the blueprint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-blueprint-name"></a>
The name of the blueprint.
*Required*: Yes
*Type*: String
*Pattern*: `^[\.\-_A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-glue-blueprint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-blueprint-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-blueprint-return-values"></a>

### Ref
<a name="aws-resource-glue-blueprint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-blueprint-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-blueprint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedOn`  <a name="CreatedOn-fn::getatt"></a>
The date and time the blueprint was registered.

`LastModifiedOn`  <a name="LastModifiedOn-fn::getatt"></a>
The date and time the blueprint was last modified.

`ParameterSpec`  <a name="ParameterSpec-fn::getatt"></a>
A JSON string that indicates the list of parameter specifications for the blueprint.

`Status`  <a name="Status-fn::getatt"></a>
The status of the blueprint registration.
+ Creating — The blueprint registration is in progress.
+ Active — The blueprint has been successfully registered.
+ Updating — An update to the blueprint registration is in progress.
+ Failed — The blueprint registration failed.
