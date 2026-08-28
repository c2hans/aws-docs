---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-descriptivebotbuilderspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot DescriptiveBotBuilderSpecification
<a name="aws-properties-lex-bot-descriptivebotbuilderspecification"></a>

Contains specifications for the descriptive bot building feature.

## Syntax
<a name="aws-properties-lex-bot-descriptivebotbuilderspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-descriptivebotbuilderspecification-syntax.json"></a>

```
{
  "[BedrockModelSpecification](#cfn-lex-bot-descriptivebotbuilderspecification-bedrockmodelspecification)" : {{BedrockModelSpecification}},
  "[Enabled](#cfn-lex-bot-descriptivebotbuilderspecification-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-descriptivebotbuilderspecification-syntax.yaml"></a>

```
  [BedrockModelSpecification](#cfn-lex-bot-descriptivebotbuilderspecification-bedrockmodelspecification): {{
    BedrockModelSpecification}}
  [Enabled](#cfn-lex-bot-descriptivebotbuilderspecification-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-descriptivebotbuilderspecification-properties"></a>

`BedrockModelSpecification`  <a name="cfn-lex-bot-descriptivebotbuilderspecification-bedrockmodelspecification"></a>
An object containing information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.
*Required*: No
*Type*: [BedrockModelSpecification](aws-properties-lex-bot-bedrockmodelspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lex-bot-descriptivebotbuilderspecification-enabled"></a>
Specifies whether the descriptive bot building feature is activated or not.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
