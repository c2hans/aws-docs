---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule Action
<a name="aws-properties-vpclattice-rule-action"></a>

Describes the action for a rule.

## Syntax
<a name="aws-properties-vpclattice-rule-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-action-syntax.json"></a>

```
{
  "[FixedResponse](#cfn-vpclattice-rule-action-fixedresponse)" : {{FixedResponse}},
  "[Forward](#cfn-vpclattice-rule-action-forward)" : {{Forward}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-action-syntax.yaml"></a>

```
  [FixedResponse](#cfn-vpclattice-rule-action-fixedresponse): {{
    FixedResponse}}
  [Forward](#cfn-vpclattice-rule-action-forward): {{
    Forward}}
```

## Properties
<a name="aws-properties-vpclattice-rule-action-properties"></a>

`FixedResponse`  <a name="cfn-vpclattice-rule-action-fixedresponse"></a>
The fixed response action. The rule returns a custom HTTP response.
*Required*: No
*Type*: [FixedResponse](aws-properties-vpclattice-rule-fixedresponse.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Forward`  <a name="cfn-vpclattice-rule-action-forward"></a>
The forward action. Traffic that matches the rule is forwarded to the specified target groups.
*Required*: No
*Type*: [Forward](aws-properties-vpclattice-rule-forward.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
