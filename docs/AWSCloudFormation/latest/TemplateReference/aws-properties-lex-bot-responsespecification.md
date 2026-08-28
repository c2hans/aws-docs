---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-responsespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ResponseSpecification
<a name="aws-properties-lex-bot-responsespecification"></a>

Specifies a list of message groups that Amazon Lex uses to respond the user input.

## Syntax
<a name="aws-properties-lex-bot-responsespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-responsespecification-syntax.json"></a>

```
{
  "[AllowInterrupt](#cfn-lex-bot-responsespecification-allowinterrupt)" : {{Boolean}},
  "[MessageGroupsList](#cfn-lex-bot-responsespecification-messagegroupslist)" : {{[ MessageGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-lex-bot-responsespecification-syntax.yaml"></a>

```
  [AllowInterrupt](#cfn-lex-bot-responsespecification-allowinterrupt): {{Boolean}}
  [MessageGroupsList](#cfn-lex-bot-responsespecification-messagegroupslist): {{
    - MessageGroup}}
```

## Properties
<a name="aws-properties-lex-bot-responsespecification-properties"></a>

`AllowInterrupt`  <a name="cfn-lex-bot-responsespecification-allowinterrupt"></a>
Indicates whether the user can interrupt a speech response from Amazon Lex.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MessageGroupsList`  <a name="cfn-lex-bot-responsespecification-messagegroupslist"></a>
A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.
*Required*: Yes
*Type*: Array of [MessageGroup](aws-properties-lex-bot-messagegroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
