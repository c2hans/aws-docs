---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-custompayload.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot CustomPayload
<a name="aws-properties-lex-bot-custompayload"></a>

A custom response string that Amazon Lex sends to your application. You define the content and structure the string.

## Syntax
<a name="aws-properties-lex-bot-custompayload-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-custompayload-syntax.json"></a>

```
{
  "[Value](#cfn-lex-bot-custompayload-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-custompayload-syntax.yaml"></a>

```
  [Value](#cfn-lex-bot-custompayload-value): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-custompayload-properties"></a>

`Value`  <a name="cfn-lex-bot-custompayload-value"></a>
The string that is sent to your application.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
