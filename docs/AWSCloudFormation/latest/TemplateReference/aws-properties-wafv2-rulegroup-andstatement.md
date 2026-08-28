---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wafv2-rulegroup-andstatement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WAFv2::RuleGroup AndStatement
<a name="aws-properties-wafv2-rulegroup-andstatement"></a>

A logical rule statement used to combine other rule statements with AND logic. You provide more than one `Statement` within the `AndStatement`.

## Syntax
<a name="aws-properties-wafv2-rulegroup-andstatement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wafv2-rulegroup-andstatement-syntax.json"></a>

```
{
  "[Statements](#cfn-wafv2-rulegroup-andstatement-statements)" : {{[ Statement, ... ]}}
}
```

### YAML
<a name="aws-properties-wafv2-rulegroup-andstatement-syntax.yaml"></a>

```
  [Statements](#cfn-wafv2-rulegroup-andstatement-statements): {{
    - Statement}}
```

## Properties
<a name="aws-properties-wafv2-rulegroup-andstatement-properties"></a>

`Statements`  <a name="cfn-wafv2-rulegroup-andstatement-statements"></a>
The statements to combine with AND logic. You can use any statements that can be nested.
*Required*: Yes
*Type*: Array of [Statement](aws-properties-wafv2-rulegroup-statement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
