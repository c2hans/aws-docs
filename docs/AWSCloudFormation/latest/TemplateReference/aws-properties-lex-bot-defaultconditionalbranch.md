---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-defaultconditionalbranch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot DefaultConditionalBranch
<a name="aws-properties-lex-bot-defaultconditionalbranch"></a>

A set of actions that Amazon Lex should run if none of the other conditions are met.

## Syntax
<a name="aws-properties-lex-bot-defaultconditionalbranch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-defaultconditionalbranch-syntax.json"></a>

```
{
  "[NextStep](#cfn-lex-bot-defaultconditionalbranch-nextstep)" : {{DialogState}},
  "[Response](#cfn-lex-bot-defaultconditionalbranch-response)" : {{ResponseSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-defaultconditionalbranch-syntax.yaml"></a>

```
  [NextStep](#cfn-lex-bot-defaultconditionalbranch-nextstep): {{
    DialogState}}
  [Response](#cfn-lex-bot-defaultconditionalbranch-response): {{
    ResponseSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-defaultconditionalbranch-properties"></a>

`NextStep`  <a name="cfn-lex-bot-defaultconditionalbranch-nextstep"></a>
The next step in the conversation.
*Required*: No
*Type*: [DialogState](aws-properties-lex-bot-dialogstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Response`  <a name="cfn-lex-bot-defaultconditionalbranch-response"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
*Required*: No
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
