---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-match.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule Match
<a name="aws-properties-vpclattice-rule-match"></a>

Describes a rule match.

## Syntax
<a name="aws-properties-vpclattice-rule-match-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-match-syntax.json"></a>

```
{
  "[HttpMatch](#cfn-vpclattice-rule-match-httpmatch)" : {{HttpMatch}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-match-syntax.yaml"></a>

```
  [HttpMatch](#cfn-vpclattice-rule-match-httpmatch): {{
    HttpMatch}}
```

## Properties
<a name="aws-properties-vpclattice-rule-match-properties"></a>

`HttpMatch`  <a name="cfn-vpclattice-rule-match-httpmatch"></a>
The HTTP criteria that a rule must match.
*Required*: Yes
*Type*: [HttpMatch](aws-properties-vpclattice-rule-httpmatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
