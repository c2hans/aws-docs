---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-omnidashboard.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::OmniDashboard
<a name="aws-resource-cloudwatch-omnidashboard"></a>

<a name="aws-resource-cloudwatch-omnidashboard-description"></a>The `AWS::CloudWatch::OmniDashboard` resource Property description not available. for CloudWatch.

## Syntax
<a name="aws-resource-cloudwatch-omnidashboard-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-omnidashboard-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::OmniDashboard",
  "Properties" : {
      "[Body](#cfn-cloudwatch-omnidashboard-body)" : {{String}},
      "[Description](#cfn-cloudwatch-omnidashboard-description)" : {{String}},
      "[Name](#cfn-cloudwatch-omnidashboard-name)" : {{String}},
      "[SpaceId](#cfn-cloudwatch-omnidashboard-spaceid)" : {{String}},
      "[Tags](#cfn-cloudwatch-omnidashboard-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-omnidashboard-syntax.yaml"></a>

```
Type: AWS::CloudWatch::OmniDashboard
Properties:
  [Body](#cfn-cloudwatch-omnidashboard-body): {{String}}
  [Description](#cfn-cloudwatch-omnidashboard-description): {{String}}
  [Name](#cfn-cloudwatch-omnidashboard-name): {{String}}
  [SpaceId](#cfn-cloudwatch-omnidashboard-spaceid): {{String}}
  [Tags](#cfn-cloudwatch-omnidashboard-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-omnidashboard-properties"></a>

`Body`  <a name="cfn-cloudwatch-omnidashboard-body"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1048576`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cloudwatch-omnidashboard-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-omnidashboard-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.@~()-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceId`  <a name="cfn-cloudwatch-omnidashboard-spaceid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-omnidashboard-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-omnidashboard-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-omnidashboard-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-omnidashboard-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-omnidashboard-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-omnidashboard-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Property description not available.

`DashboardId`  <a name="DashboardId-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
