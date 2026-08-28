---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-rule-assignslaaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Rule AssignSlaAction
<a name="aws-properties-connect-rule-assignslaaction"></a>

<a name="aws-properties-connect-rule-assignslaaction-description"></a>The `AssignSlaAction` property type specifies Property description not available. for an [AWS::Connect::Rule](aws-resource-connect-rule.md).

## Syntax
<a name="aws-properties-connect-rule-assignslaaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-rule-assignslaaction-syntax.json"></a>

```
{
  "[CaseSlaConfiguration](#cfn-connect-rule-assignslaaction-caseslaconfiguration)" : {{CaseSlaConfiguration}},
  "[SlaAssignmentType](#cfn-connect-rule-assignslaaction-slaassignmenttype)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-rule-assignslaaction-syntax.yaml"></a>

```
  [CaseSlaConfiguration](#cfn-connect-rule-assignslaaction-caseslaconfiguration): {{
    CaseSlaConfiguration}}
  [SlaAssignmentType](#cfn-connect-rule-assignslaaction-slaassignmenttype): {{String}}
```

## Properties
<a name="aws-properties-connect-rule-assignslaaction-properties"></a>

`CaseSlaConfiguration`  <a name="cfn-connect-rule-assignslaaction-caseslaconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [CaseSlaConfiguration](aws-properties-connect-rule-caseslaconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SlaAssignmentType`  <a name="cfn-connect-rule-assignslaaction-slaassignmenttype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `CASES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
