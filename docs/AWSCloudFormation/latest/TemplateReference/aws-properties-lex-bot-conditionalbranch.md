---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-conditionalbranch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ConditionalBranch
<a name="aws-properties-lex-bot-conditionalbranch"></a>

A set of actions that Amazon Lex should run if the condition is matched.

## Syntax
<a name="aws-properties-lex-bot-conditionalbranch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-conditionalbranch-syntax.json"></a>

```
{
  "[Condition](#cfn-lex-bot-conditionalbranch-condition)" : {{Condition}},
  "[Name](#cfn-lex-bot-conditionalbranch-name)" : {{String}},
  "[NextStep](#cfn-lex-bot-conditionalbranch-nextstep)" : {{DialogState}},
  "[Response](#cfn-lex-bot-conditionalbranch-response)" : {{ResponseSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-conditionalbranch-syntax.yaml"></a>

```
  [Condition](#cfn-lex-bot-conditionalbranch-condition): {{
    Condition}}
  [Name](#cfn-lex-bot-conditionalbranch-name): {{String}}
  [NextStep](#cfn-lex-bot-conditionalbranch-nextstep): {{
    DialogState}}
  [Response](#cfn-lex-bot-conditionalbranch-response): {{
    ResponseSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-conditionalbranch-properties"></a>

`Condition`  <a name="cfn-lex-bot-conditionalbranch-condition"></a>
Contains the expression to evaluate. If the condition is true, the branch's actions are taken.
*Required*: Yes
*Type*: [Condition](aws-properties-lex-bot-condition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lex-bot-conditionalbranch-name"></a>
The name of the branch.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NextStep`  <a name="cfn-lex-bot-conditionalbranch-nextstep"></a>
The next step in the conversation.
*Required*: Yes
*Type*: [DialogState](aws-properties-lex-bot-dialogstate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Response`  <a name="cfn-lex-bot-conditionalbranch-response"></a>
Specifies a list of message groups that Amazon Lex uses to respond the user input.
*Required*: No
*Type*: [ResponseSpecification](aws-properties-lex-bot-responsespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
