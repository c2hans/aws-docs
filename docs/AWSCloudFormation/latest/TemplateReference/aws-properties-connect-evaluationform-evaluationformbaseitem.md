---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-evaluationform-evaluationformbaseitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EvaluationForm EvaluationFormBaseItem
<a name="aws-properties-connect-evaluationform-evaluationformbaseitem"></a>

An item at the root level. All items must be sections.

## Syntax
<a name="aws-properties-connect-evaluationform-evaluationformbaseitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-evaluationform-evaluationformbaseitem-syntax.json"></a>

```
{
  "[Section](#cfn-connect-evaluationform-evaluationformbaseitem-section)" : {{EvaluationFormSection}}
}
```

### YAML
<a name="aws-properties-connect-evaluationform-evaluationformbaseitem-syntax.yaml"></a>

```
  [Section](#cfn-connect-evaluationform-evaluationformbaseitem-section): {{
    EvaluationFormSection}}
```

## Properties
<a name="aws-properties-connect-evaluationform-evaluationformbaseitem-properties"></a>

`Section`  <a name="cfn-connect-evaluationform-evaluationformbaseitem-section"></a>
A subsection or inner section of an item.
*Required*: Yes
*Type*: [EvaluationFormSection](aws-properties-connect-evaluationform-evaluationformsection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
