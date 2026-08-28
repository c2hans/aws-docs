---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-custompermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::CustomPermissions
<a name="aws-resource-quicksight-custompermissions"></a>

Creates a custom permissions profile.

## Syntax
<a name="aws-resource-quicksight-custompermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-custompermissions-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::CustomPermissions",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-custompermissions-awsaccountid)" : {{String}},
      "[Capabilities](#cfn-quicksight-custompermissions-capabilities)" : {{Capabilities}},
      "[CustomPermissionsName](#cfn-quicksight-custompermissions-custompermissionsname)" : {{String}},
      "[Tags](#cfn-quicksight-custompermissions-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-custompermissions-syntax.yaml"></a>

```
Type: AWS::QuickSight::CustomPermissions
Properties:
  [AwsAccountId](#cfn-quicksight-custompermissions-awsaccountid): {{String}}
  [Capabilities](#cfn-quicksight-custompermissions-capabilities): {{
    Capabilities}}
  [CustomPermissionsName](#cfn-quicksight-custompermissions-custompermissionsname): {{String}}
  [Tags](#cfn-quicksight-custompermissions-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-quicksight-custompermissions-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-custompermissions-awsaccountid"></a>
The ID of the AWS account that contains the custom permission configuration that you want to update.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Capabilities`  <a name="cfn-quicksight-custompermissions-capabilities"></a>
A set of actions in the custom permissions profile.
*Required*: No
*Type*: [Capabilities](aws-properties-quicksight-custompermissions-capabilities.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomPermissionsName`  <a name="cfn-quicksight-custompermissions-custompermissionsname"></a>
The name of the custom permissions profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9+=,.@_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-quicksight-custompermissions-tags"></a>
The tags to associate with the custom permissions profile.
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-custompermissions-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-custompermissions-return-values"></a>

### Ref
<a name="aws-resource-quicksight-custompermissions-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-custompermissions-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-custompermissions-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the custom permissions profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
