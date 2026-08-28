---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-buildtimesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BuildtimeSettings
<a name="aws-properties-lex-bot-buildtimesettings"></a>

Contains specifications about the Amazon Lex build time generative AI capabilities from Amazon Bedrock that you can turn on for your bot.

## Syntax
<a name="aws-properties-lex-bot-buildtimesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-buildtimesettings-syntax.json"></a>

```
{
  "[DescriptiveBotBuilderSpecification](#cfn-lex-bot-buildtimesettings-descriptivebotbuilderspecification)" : {{DescriptiveBotBuilderSpecification}},
  "[SampleUtteranceGenerationSpecification](#cfn-lex-bot-buildtimesettings-sampleutterancegenerationspecification)" : {{SampleUtteranceGenerationSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-buildtimesettings-syntax.yaml"></a>

```
  [DescriptiveBotBuilderSpecification](#cfn-lex-bot-buildtimesettings-descriptivebotbuilderspecification): {{
    DescriptiveBotBuilderSpecification}}
  [SampleUtteranceGenerationSpecification](#cfn-lex-bot-buildtimesettings-sampleutterancegenerationspecification): {{
    SampleUtteranceGenerationSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-buildtimesettings-properties"></a>

`DescriptiveBotBuilderSpecification`  <a name="cfn-lex-bot-buildtimesettings-descriptivebotbuilderspecification"></a>
Property description not available.
*Required*: No
*Type*: [DescriptiveBotBuilderSpecification](aws-properties-lex-bot-descriptivebotbuilderspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleUtteranceGenerationSpecification`  <a name="cfn-lex-bot-buildtimesettings-sampleutterancegenerationspecification"></a>
Property description not available.
*Required*: No
*Type*: [SampleUtteranceGenerationSpecification](aws-properties-lex-bot-sampleutterancegenerationspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
