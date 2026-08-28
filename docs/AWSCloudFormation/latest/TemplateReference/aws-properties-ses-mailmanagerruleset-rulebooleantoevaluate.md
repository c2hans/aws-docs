---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleBooleanToEvaluate
<a name="aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate"></a>

The union type representing the allowed types of operands for a boolean condition.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate-syntax.json"></a>

```
{
  "[Analysis](#cfn-ses-mailmanagerruleset-rulebooleantoevaluate-analysis)" : {{Analysis}},
  "[Attribute](#cfn-ses-mailmanagerruleset-rulebooleantoevaluate-attribute)" : {{String}},
  "[IsInAddressList](#cfn-ses-mailmanagerruleset-rulebooleantoevaluate-isinaddresslist)" : {{RuleIsInAddressList}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate-syntax.yaml"></a>

```
  [Analysis](#cfn-ses-mailmanagerruleset-rulebooleantoevaluate-analysis): {{
    Analysis}}
  [Attribute](#cfn-ses-mailmanagerruleset-rulebooleantoevaluate-attribute): {{String}}
  [IsInAddressList](#cfn-ses-mailmanagerruleset-rulebooleantoevaluate-isinaddresslist): {{
    RuleIsInAddressList}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate-properties"></a>

`Analysis`  <a name="cfn-ses-mailmanagerruleset-rulebooleantoevaluate-analysis"></a>
The Add On ARN and its returned value to evaluate in a boolean condition expression.
*Required*: No
*Type*: [Analysis](aws-properties-ses-mailmanagerruleset-analysis.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attribute`  <a name="cfn-ses-mailmanagerruleset-rulebooleantoevaluate-attribute"></a>
The boolean type representing the allowed attribute types for an email.
*Required*: No
*Type*: String
*Allowed values*: `READ_RECEIPT_REQUESTED | TLS | TLS_WRAPPED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsInAddressList`  <a name="cfn-ses-mailmanagerruleset-rulebooleantoevaluate-isinaddresslist"></a>
The structure representing the address lists and address list attribute that will be used in evaluation of boolean expression.
*Required*: No
*Type*: [RuleIsInAddressList](aws-properties-ses-mailmanagerruleset-ruleisinaddresslist.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
