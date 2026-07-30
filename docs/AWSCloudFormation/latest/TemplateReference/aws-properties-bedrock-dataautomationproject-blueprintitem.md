---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-blueprintitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject BlueprintItem
<a name="aws-properties-bedrock-dataautomationproject-blueprintitem"></a>

An abbreviated summary of a blueprint.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-blueprintitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-blueprintitem-syntax.json"></a>

```
{
  "[BlueprintArn](#cfn-bedrock-dataautomationproject-blueprintitem-blueprintarn)" : {{String}},
  "[BlueprintStage](#cfn-bedrock-dataautomationproject-blueprintitem-blueprintstage)" : {{String}},
  "[BlueprintVersion](#cfn-bedrock-dataautomationproject-blueprintitem-blueprintversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-blueprintitem-syntax.yaml"></a>

```
  [BlueprintArn](#cfn-bedrock-dataautomationproject-blueprintitem-blueprintarn): {{String}}
  [BlueprintStage](#cfn-bedrock-dataautomationproject-blueprintitem-blueprintstage): {{String}}
  [BlueprintVersion](#cfn-bedrock-dataautomationproject-blueprintitem-blueprintversion): {{String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-blueprintitem-properties"></a>

`BlueprintArn`  <a name="cfn-bedrock-dataautomationproject-blueprintitem-blueprintarn"></a>
The blueprint's ARN.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov|-iso|-iso-[a-z]):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlueprintStage`  <a name="cfn-bedrock-dataautomationproject-blueprintitem-blueprintstage"></a>
The blueprint's stage.
*Required*: No
*Type*: String
*Allowed values*: `DEVELOPMENT | LIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlueprintVersion`  <a name="cfn-bedrock-dataautomationproject-blueprintitem-blueprintversion"></a>
The blueprint's version.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
