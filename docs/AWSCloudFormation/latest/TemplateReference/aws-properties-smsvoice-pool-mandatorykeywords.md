---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-pool-mandatorykeywords.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::Pool MandatoryKeywords
<a name="aws-properties-smsvoice-pool-mandatorykeywords"></a>

The manadatory keywords, `HELP` and `STOP` to add to the pool. For more information, see [Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html) in the AWS End User Messaging SMS User Guide.

## Syntax
<a name="aws-properties-smsvoice-pool-mandatorykeywords-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-pool-mandatorykeywords-syntax.json"></a>

```
{
  "[HELP](#cfn-smsvoice-pool-mandatorykeywords-help)" : {{MandatoryKeyword}},
  "[STOP](#cfn-smsvoice-pool-mandatorykeywords-stop)" : {{MandatoryKeyword}}
}
```

### YAML
<a name="aws-properties-smsvoice-pool-mandatorykeywords-syntax.yaml"></a>

```
  [HELP](#cfn-smsvoice-pool-mandatorykeywords-help): {{
    MandatoryKeyword}}
  [STOP](#cfn-smsvoice-pool-mandatorykeywords-stop): {{
    MandatoryKeyword}}
```

## Properties
<a name="aws-properties-smsvoice-pool-mandatorykeywords-properties"></a>

`HELP`  <a name="cfn-smsvoice-pool-mandatorykeywords-help"></a>
Specifies the pool's `HELP` keyword. For more information, see [Opt out list required keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html) in the AWS End User Messaging SMS User Guide.
*Required*: Yes
*Type*: [MandatoryKeyword](aws-properties-smsvoice-pool-mandatorykeyword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`STOP`  <a name="cfn-smsvoice-pool-mandatorykeywords-stop"></a>
Specifies the pool's opt-out keyword. For more information, see [Required opt-out keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html) in the AWS End User Messaging SMS User Guide.
*Required*: Yes
*Type*: [MandatoryKeyword](aws-properties-smsvoice-pool-mandatorykeyword.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
