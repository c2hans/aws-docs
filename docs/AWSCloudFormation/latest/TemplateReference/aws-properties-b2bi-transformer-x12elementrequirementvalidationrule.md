---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12elementrequirementvalidationrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12ElementRequirementValidationRule
<a name="aws-properties-b2bi-transformer-x12elementrequirementvalidationrule"></a>

Defines a validation rule that modifies the requirement status of a specific X12 element within a segment. This rule allows you to make optional elements mandatory or mandatory elements optional, providing flexibility to accommodate different trading partner requirements and business rules. The rule targets a specific element position within a segment and sets its requirement status to either OPTIONAL or MANDATORY.

## Syntax
<a name="aws-properties-b2bi-transformer-x12elementrequirementvalidationrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12elementrequirementvalidationrule-syntax.json"></a>

```
{
  "[ElementPosition](#cfn-b2bi-transformer-x12elementrequirementvalidationrule-elementposition)" : {{String}},
  "[Requirement](#cfn-b2bi-transformer-x12elementrequirementvalidationrule-requirement)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12elementrequirementvalidationrule-syntax.yaml"></a>

```
  [ElementPosition](#cfn-b2bi-transformer-x12elementrequirementvalidationrule-elementposition): {{String}}
  [Requirement](#cfn-b2bi-transformer-x12elementrequirementvalidationrule-requirement): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12elementrequirementvalidationrule-properties"></a>

`ElementPosition`  <a name="cfn-b2bi-transformer-x12elementrequirementvalidationrule-elementposition"></a>
Specifies the position of the element within an X12 segment for which the requirement status will be modified. The format follows the pattern of segment identifier followed by element position (e.g., "ST-01" for the first element of the ST segment).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+(?:-\d{2})(?:-\d{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Requirement`  <a name="cfn-b2bi-transformer-x12elementrequirementvalidationrule-requirement"></a>
Specifies the requirement status for the element at the specified position. Valid values are OPTIONAL (the element may be omitted) or MANDATORY (the element must be present).
*Required*: Yes
*Type*: String
*Allowed values*: `OPTIONAL | MANDATORY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
