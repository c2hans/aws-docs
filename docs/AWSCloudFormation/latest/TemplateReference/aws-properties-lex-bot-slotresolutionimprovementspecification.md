---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-slotresolutionimprovementspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SlotResolutionImprovementSpecification
<a name="aws-properties-lex-bot-slotresolutionimprovementspecification"></a>

Contains specifications for the assisted slot resolution feature.

## Syntax
<a name="aws-properties-lex-bot-slotresolutionimprovementspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-slotresolutionimprovementspecification-syntax.json"></a>

```
{
  "[BedrockModelSpecification](#cfn-lex-bot-slotresolutionimprovementspecification-bedrockmodelspecification)" : {{BedrockModelSpecification}},
  "[Enabled](#cfn-lex-bot-slotresolutionimprovementspecification-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-slotresolutionimprovementspecification-syntax.yaml"></a>

```
  [BedrockModelSpecification](#cfn-lex-bot-slotresolutionimprovementspecification-bedrockmodelspecification): {{
    BedrockModelSpecification}}
  [Enabled](#cfn-lex-bot-slotresolutionimprovementspecification-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-slotresolutionimprovementspecification-properties"></a>

`BedrockModelSpecification`  <a name="cfn-lex-bot-slotresolutionimprovementspecification-bedrockmodelspecification"></a>
An object containing information about the Amazon Bedrock model used to assist slot resolution.
*Required*: No
*Type*: [BedrockModelSpecification](aws-properties-lex-bot-bedrockmodelspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lex-bot-slotresolutionimprovementspecification-enabled"></a>
Specifies whether assisted slot resolution is turned on or off.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
