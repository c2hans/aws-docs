---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-x12splitoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer X12SplitOptions
<a name="aws-properties-b2bi-transformer-x12splitoptions"></a>

Contains options for splitting X12 EDI files into smaller units. This is useful for processing large EDI files more efficiently.

## Syntax
<a name="aws-properties-b2bi-transformer-x12splitoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-x12splitoptions-syntax.json"></a>

```
{
  "[SplitBy](#cfn-b2bi-transformer-x12splitoptions-splitby)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-x12splitoptions-syntax.yaml"></a>

```
  [SplitBy](#cfn-b2bi-transformer-x12splitoptions-splitby): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-x12splitoptions-properties"></a>

`SplitBy`  <a name="cfn-b2bi-transformer-x12splitoptions-splitby"></a>
Specifies the method used to split X12 EDI files. Valid values include `TRANSACTION` (split by individual transaction sets), or `NONE` (no splitting).
*Required*: No
*Type*: String
*Allowed values*: `NONE | TRANSACTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
