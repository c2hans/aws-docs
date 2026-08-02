---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-usageprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::UsageProfile
<a name="aws-resource-glue-usageprofile"></a>

Creates an AWS Glue usage profile.

## Syntax
<a name="aws-resource-glue-usageprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-glue-usageprofile-syntax.json"></a>

```
{
  "Type" : "AWS::Glue::UsageProfile",
  "Properties" : {
      "[Configuration](#cfn-glue-usageprofile-configuration)" : {{ProfileConfiguration}},
      "[Description](#cfn-glue-usageprofile-description)" : {{String}},
      "[Name](#cfn-glue-usageprofile-name)" : {{String}},
      "[Tags](#cfn-glue-usageprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-glue-usageprofile-syntax.yaml"></a>

```
Type: AWS::Glue::UsageProfile
Properties:
  [Configuration](#cfn-glue-usageprofile-configuration): {{
    ProfileConfiguration}}
  [Description](#cfn-glue-usageprofile-description): {{String}}
  [Name](#cfn-glue-usageprofile-name): {{String}}
  [Tags](#cfn-glue-usageprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-glue-usageprofile-properties"></a>

`Configuration`  <a name="cfn-glue-usageprofile-configuration"></a>
Property description not available.
*Required*: No
*Type*: [ProfileConfiguration](aws-properties-glue-usageprofile-profileconfiguration.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-glue-usageprofile-description"></a>
A description of the usage profile.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9\-\:\_]{1,64}`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-glue-usageprofile-name"></a>
The name of the usage profile.
*Required*: Yes
*Type*: String
*Minimum*: `5`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-glue-usageprofile-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-glue-usageprofile-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-glue-usageprofile-return-values"></a>

### Ref
<a name="aws-resource-glue-usageprofile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-glue-usageprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-glue-usageprofile-return-values-fn--getatt-fn--getatt"></a>

`CreatedOn`  <a name="CreatedOn-fn::getatt"></a>
The date and time when the usage profile was created.
