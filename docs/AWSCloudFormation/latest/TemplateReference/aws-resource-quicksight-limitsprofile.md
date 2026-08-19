---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-limitsprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::LimitsProfile
<a name="aws-resource-quicksight-limitsprofile"></a>

<a name="aws-resource-quicksight-limitsprofile-description"></a>The `AWS::QuickSight::LimitsProfile` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-limitsprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-limitsprofile-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::LimitsProfile",
  "Properties" : {
      "[AccountId](#cfn-quicksight-limitsprofile-accountid)" : {{String}},
      "[Description](#cfn-quicksight-limitsprofile-description)" : {{String}},
      "[ProfileName](#cfn-quicksight-limitsprofile-profilename)" : {{String}},
      "[ResourceLimits](#cfn-quicksight-limitsprofile-resourcelimits)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-limitsprofile-syntax.yaml"></a>

```
Type: AWS::QuickSight::LimitsProfile
Properties:
  [AccountId](#cfn-quicksight-limitsprofile-accountid): {{String}}
  [Description](#cfn-quicksight-limitsprofile-description): {{String}}
  [ProfileName](#cfn-quicksight-limitsprofile-profilename): {{String}}
  [ResourceLimits](#cfn-quicksight-limitsprofile-resourcelimits): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-quicksight-limitsprofile-properties"></a>

`AccountId`  <a name="cfn-quicksight-limitsprofile-accountid"></a>
The ID of the AWS account that contains the limits profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-quicksight-limitsprofile-description"></a>
The description of the limits profile.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileName`  <a name="cfn-quicksight-limitsprofile-profilename"></a>
The display name of the limits profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceLimits`  <a name="cfn-quicksight-limitsprofile-resourcelimits"></a>
A map of resource types to their limit values.
*Required*: Yes
*Type*: Object of [ProfileLimitValue](aws-properties-quicksight-limitsprofile-profilelimitvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-limitsprofile-return-values"></a>

### Ref
<a name="aws-resource-quicksight-limitsprofile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-limitsprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-limitsprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the limits profile.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the limits profile was created.

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
The unique identifier for the limits profile.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time that the limits profile was last updated.
