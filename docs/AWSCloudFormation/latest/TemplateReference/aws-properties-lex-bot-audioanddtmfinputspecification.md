---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-audioanddtmfinputspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot AudioAndDTMFInputSpecification
<a name="aws-properties-lex-bot-audioanddtmfinputspecification"></a>

Specifies the audio and DTMF input specification.

## Syntax
<a name="aws-properties-lex-bot-audioanddtmfinputspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-audioanddtmfinputspecification-syntax.json"></a>

```
{
  "[AudioSpecification](#cfn-lex-bot-audioanddtmfinputspecification-audiospecification)" : {{AudioSpecification}},
  "[DTMFSpecification](#cfn-lex-bot-audioanddtmfinputspecification-dtmfspecification)" : {{DTMFSpecification}},
  "[StartTimeoutMs](#cfn-lex-bot-audioanddtmfinputspecification-starttimeoutms)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lex-bot-audioanddtmfinputspecification-syntax.yaml"></a>

```
  [AudioSpecification](#cfn-lex-bot-audioanddtmfinputspecification-audiospecification): {{
    AudioSpecification}}
  [DTMFSpecification](#cfn-lex-bot-audioanddtmfinputspecification-dtmfspecification): {{
    DTMFSpecification}}
  [StartTimeoutMs](#cfn-lex-bot-audioanddtmfinputspecification-starttimeoutms): {{Integer}}
```

## Properties
<a name="aws-properties-lex-bot-audioanddtmfinputspecification-properties"></a>

`AudioSpecification`  <a name="cfn-lex-bot-audioanddtmfinputspecification-audiospecification"></a>
Specifies the settings on audio input.
*Required*: No
*Type*: [AudioSpecification](aws-properties-lex-bot-audiospecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DTMFSpecification`  <a name="cfn-lex-bot-audioanddtmfinputspecification-dtmfspecification"></a>
Specifies the settings on DTMF input.
*Required*: No
*Type*: [DTMFSpecification](aws-properties-lex-bot-dtmfspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTimeoutMs`  <a name="cfn-lex-bot-audioanddtmfinputspecification-starttimeoutms"></a>
Time for which a bot waits before assuming that the customer isn't going to speak or press a key. This timeout is shared between Audio and DTMF inputs.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
