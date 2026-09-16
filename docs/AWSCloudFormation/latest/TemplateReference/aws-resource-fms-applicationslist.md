---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fms-applicationslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::ApplicationsList
<a name="aws-resource-fms-applicationslist"></a>

<a name="aws-resource-fms-applicationslist-description"></a>The `AWS::FMS::ApplicationsList` resource Property description not available. for FMS.

## Syntax
<a name="aws-resource-fms-applicationslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fms-applicationslist-syntax.json"></a>

```
{
  "Type" : "AWS::FMS::ApplicationsList",
  "Properties" : {
      "[AppsList](#cfn-fms-applicationslist-appslist)" : {{[ App, ... ]}},
      "[ListName](#cfn-fms-applicationslist-listname)" : {{String}},
      "[Tags](#cfn-fms-applicationslist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fms-applicationslist-syntax.yaml"></a>

```
Type: AWS::FMS::ApplicationsList
Properties:
  [AppsList](#cfn-fms-applicationslist-appslist): {{
    - App}}
  [ListName](#cfn-fms-applicationslist-listname): {{String}}
  [Tags](#cfn-fms-applicationslist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fms-applicationslist-properties"></a>

`AppsList`  <a name="cfn-fms-applicationslist-appslist"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [App](aws-properties-fms-applicationslist-app.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListName`  <a name="cfn-fms-applicationslist-listname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-fms-applicationslist-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-fms-applicationslist-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fms-applicationslist-return-values"></a>

### Ref
<a name="aws-resource-fms-applicationslist-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fms-applicationslist-return-values-fn--getatt"></a>

####
<a name="aws-resource-fms-applicationslist-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
Property description not available.

`LastUpdateTime`  <a name="LastUpdateTime-fn::getatt"></a>
Property description not available.

`ListId`  <a name="ListId-fn::getatt"></a>
Property description not available.
