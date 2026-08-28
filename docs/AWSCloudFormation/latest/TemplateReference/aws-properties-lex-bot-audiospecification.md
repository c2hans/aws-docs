---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-audiospecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot AudioSpecification
<a name="aws-properties-lex-bot-audiospecification"></a>

Specifies the audio input specifications.

## Syntax
<a name="aws-properties-lex-bot-audiospecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-audiospecification-syntax.json"></a>

```
{
  "[EndTimeoutMs](#cfn-lex-bot-audiospecification-endtimeoutms)" : {{Integer}},
  "[MaxLengthMs](#cfn-lex-bot-audiospecification-maxlengthms)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lex-bot-audiospecification-syntax.yaml"></a>

```
  [EndTimeoutMs](#cfn-lex-bot-audiospecification-endtimeoutms): {{Integer}}
  [MaxLengthMs](#cfn-lex-bot-audiospecification-maxlengthms): {{Integer}}
```

## Properties
<a name="aws-properties-lex-bot-audiospecification-properties"></a>

`EndTimeoutMs`  <a name="cfn-lex-bot-audiospecification-endtimeoutms"></a>
Time for which a bot waits after the customer stops speaking to assume the utterance is finished.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxLengthMs`  <a name="cfn-lex-bot-audiospecification-maxlengthms"></a>
Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
