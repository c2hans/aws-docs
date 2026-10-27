---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-accessprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AccessProfile
<a name="aws-resource-cloudwatch-accessprofile"></a>

<a name="aws-resource-cloudwatch-accessprofile-description"></a>The `AWS::CloudWatch::AccessProfile` resource Property description not available. for CloudWatch.

## Syntax
<a name="aws-resource-cloudwatch-accessprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-accessprofile-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::AccessProfile",
  "Properties" : {
      "[Description](#cfn-cloudwatch-accessprofile-description)" : {{String}},
      "[Name](#cfn-cloudwatch-accessprofile-name)" : {{String}},
      "[SpaceId](#cfn-cloudwatch-accessprofile-spaceid)" : {{String}},
      "[Tags](#cfn-cloudwatch-accessprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-accessprofile-syntax.yaml"></a>

```
Type: AWS::CloudWatch::AccessProfile
Properties:
  [Description](#cfn-cloudwatch-accessprofile-description): {{String}}
  [Name](#cfn-cloudwatch-accessprofile-name): {{String}}
  [SpaceId](#cfn-cloudwatch-accessprofile-spaceid): {{String}}
  [Tags](#cfn-cloudwatch-accessprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-accessprofile-properties"></a>

`Description`  <a name="cfn-cloudwatch-accessprofile-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-accessprofile-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _.:/=+@-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceId`  <a name="cfn-cloudwatch-accessprofile-spaceid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-accessprofile-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-accessprofile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-accessprofile-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-accessprofile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-accessprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-accessprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`AssumeStatus`  <a name="AssumeStatus-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
Property description not available.

`ProfileType`  <a name="ProfileType-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
