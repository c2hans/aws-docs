---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-textinputspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot TextInputSpecification
<a name="aws-properties-lex-bot-textinputspecification"></a>

Specifies the text input specifications.

## Syntax
<a name="aws-properties-lex-bot-textinputspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-textinputspecification-syntax.json"></a>

```
{
  "[StartTimeoutMs](#cfn-lex-bot-textinputspecification-starttimeoutms)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lex-bot-textinputspecification-syntax.yaml"></a>

```
  [StartTimeoutMs](#cfn-lex-bot-textinputspecification-starttimeoutms): {{Integer}}
```

## Properties
<a name="aws-properties-lex-bot-textinputspecification-properties"></a>

`StartTimeoutMs`  <a name="cfn-lex-bot-textinputspecification-starttimeoutms"></a>
Time for which a bot waits before re-prompting a customer for text input.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
