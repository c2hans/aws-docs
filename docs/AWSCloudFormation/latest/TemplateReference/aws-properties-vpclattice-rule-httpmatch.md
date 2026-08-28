---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-httpmatch.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule HttpMatch
<a name="aws-properties-vpclattice-rule-httpmatch"></a>

Describes criteria that can be applied to incoming requests.

## Syntax
<a name="aws-properties-vpclattice-rule-httpmatch-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-httpmatch-syntax.json"></a>

```
{
  "[HeaderMatches](#cfn-vpclattice-rule-httpmatch-headermatches)" : {{[ HeaderMatch, ... ]}},
  "[Method](#cfn-vpclattice-rule-httpmatch-method)" : {{String}},
  "[PathMatch](#cfn-vpclattice-rule-httpmatch-pathmatch)" : {{PathMatch}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-httpmatch-syntax.yaml"></a>

```
  [HeaderMatches](#cfn-vpclattice-rule-httpmatch-headermatches): {{
    - HeaderMatch}}
  [Method](#cfn-vpclattice-rule-httpmatch-method): {{String}}
  [PathMatch](#cfn-vpclattice-rule-httpmatch-pathmatch): {{
    PathMatch}}
```

## Properties
<a name="aws-properties-vpclattice-rule-httpmatch-properties"></a>

`HeaderMatches`  <a name="cfn-vpclattice-rule-httpmatch-headermatches"></a>
The header matches. Matches incoming requests with rule based on request header value before applying rule action.
*Required*: No
*Type*: Array of [HeaderMatch](aws-properties-vpclattice-rule-headermatch.md)
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Method`  <a name="cfn-vpclattice-rule-httpmatch-method"></a>
The HTTP method type.
*Required*: No
*Type*: String
*Allowed values*: `CONNECT | DELETE | GET | HEAD | OPTIONS | POST | PUT | TRACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PathMatch`  <a name="cfn-vpclattice-rule-httpmatch-pathmatch"></a>
The path match.
*Required*: No
*Type*: [PathMatch](aws-properties-vpclattice-rule-pathmatch.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
