---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-actiontarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ActionTarget
<a name="aws-resource-securityhub-actiontarget"></a>

Creates a custom action target in Security Hub CSPM.

You can use custom actions on findings and insights in Security Hub CSPM to trigger target actions in Amazon CloudWatch Events.

## Syntax
<a name="aws-resource-securityhub-actiontarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-actiontarget-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::ActionTarget",
  "Properties" : {
      "[Description](#cfn-securityhub-actiontarget-description)" : {{String}},
      "[Id](#cfn-securityhub-actiontarget-id)" : {{String}},
      "[Name](#cfn-securityhub-actiontarget-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-actiontarget-syntax.yaml"></a>

```
Type: AWS::SecurityHub::ActionTarget
Properties:
  [Description](#cfn-securityhub-actiontarget-description): {{String}}
  [Id](#cfn-securityhub-actiontarget-id): {{String}}
  [Name](#cfn-securityhub-actiontarget-name): {{String}}
```

## Properties
<a name="aws-resource-securityhub-actiontarget-properties"></a>

`Description`  <a name="cfn-securityhub-actiontarget-description"></a>
The description of the target action.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-securityhub-actiontarget-id"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-securityhub-actiontarget-name"></a>
The name of the action target.
*Required*: Yes
*Type*: String
*Pattern*: `\S`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-actiontarget-return-values"></a>

### Ref
<a name="aws-resource-securityhub-actiontarget-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-securityhub-actiontarget-return-values-fn--getatt"></a>

####
<a name="aws-resource-securityhub-actiontarget-return-values-fn--getatt-fn--getatt"></a>

`ActionTargetArn`  <a name="ActionTargetArn-fn::getatt"></a>
The ARN for the target action.
