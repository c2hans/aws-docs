---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot ElicitationCodeHookInvocationSetting
<a name="aws-properties-lex-bot-elicitationcodehookinvocationsetting"></a>

Settings that specify the dialog code hook that is called by Amazon Lex between eliciting slot values.

## Syntax
<a name="aws-properties-lex-bot-elicitationcodehookinvocationsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-elicitationcodehookinvocationsetting-syntax.json"></a>

```
{
  "[EnableCodeHookInvocation](#cfn-lex-bot-elicitationcodehookinvocationsetting-enablecodehookinvocation)" : {{Boolean}},
  "[InvocationLabel](#cfn-lex-bot-elicitationcodehookinvocationsetting-invocationlabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-elicitationcodehookinvocationsetting-syntax.yaml"></a>

```
  [EnableCodeHookInvocation](#cfn-lex-bot-elicitationcodehookinvocationsetting-enablecodehookinvocation): {{Boolean}}
  [InvocationLabel](#cfn-lex-bot-elicitationcodehookinvocationsetting-invocationlabel): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-elicitationcodehookinvocationsetting-properties"></a>

`EnableCodeHookInvocation`  <a name="cfn-lex-bot-elicitationcodehookinvocationsetting-enablecodehookinvocation"></a>
Indicates whether a Lambda function should be invoked for the dialog.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InvocationLabel`  <a name="cfn-lex-bot-elicitationcodehookinvocationsetting-invocationlabel"></a>
A label that indicates the dialog step from which the dialog code hook is happening.
*Required*: No
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
