---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-headermatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule HeaderMatch
<a name="aws-properties-vpclattice-rule-headermatch"></a>

Describes the constraints for a header match. Matches incoming requests with rule based on request header value before applying rule action.

## Syntax
<a name="aws-properties-vpclattice-rule-headermatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-headermatch-syntax.json"></a>

```
{
  "[CaseSensitive](#cfn-vpclattice-rule-headermatch-casesensitive)" : {{Boolean}},
  "[Match](#cfn-vpclattice-rule-headermatch-match)" : {{HeaderMatchType}},
  "[Name](#cfn-vpclattice-rule-headermatch-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-headermatch-syntax.yaml"></a>

```
  [CaseSensitive](#cfn-vpclattice-rule-headermatch-casesensitive): {{Boolean}}
  [Match](#cfn-vpclattice-rule-headermatch-match): {{
    HeaderMatchType}}
  [Name](#cfn-vpclattice-rule-headermatch-name): {{String}}
```

## Properties
<a name="aws-properties-vpclattice-rule-headermatch-properties"></a>

`CaseSensitive`  <a name="cfn-vpclattice-rule-headermatch-casesensitive"></a>
Indicates whether the match is case sensitive.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Match`  <a name="cfn-vpclattice-rule-headermatch-match"></a>
The header match type.
*Required*: Yes
*Type*: [HeaderMatchType](aws-properties-vpclattice-rule-headermatchtype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-vpclattice-rule-headermatch-name"></a>
The name of the header.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
