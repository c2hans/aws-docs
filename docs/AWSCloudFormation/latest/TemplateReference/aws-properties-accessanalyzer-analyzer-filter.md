---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-accessanalyzer-analyzer-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AccessAnalyzer::Analyzer Filter
<a name="aws-properties-accessanalyzer-analyzer-filter"></a>

The criteria that defines the archive rule.

To learn about filter keys that you can use to create an archive rule, see [AWS Identity and Access Management Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html) in the *AWS Identity and Access Management User Guide*.

## Syntax
<a name="aws-properties-accessanalyzer-analyzer-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-accessanalyzer-analyzer-filter-syntax.json"></a>

```
{
  "[Contains](#cfn-accessanalyzer-analyzer-filter-contains)" : {{[ String, ... ]}},
  "[Eq](#cfn-accessanalyzer-analyzer-filter-eq)" : {{[ String, ... ]}},
  "[Exists](#cfn-accessanalyzer-analyzer-filter-exists)" : {{Boolean}},
  "[Neq](#cfn-accessanalyzer-analyzer-filter-neq)" : {{[ String, ... ]}},
  "[Property](#cfn-accessanalyzer-analyzer-filter-property)" : {{String}}
}
```

### YAML
<a name="aws-properties-accessanalyzer-analyzer-filter-syntax.yaml"></a>

```
  [Contains](#cfn-accessanalyzer-analyzer-filter-contains): {{
    - String}}
  [Eq](#cfn-accessanalyzer-analyzer-filter-eq): {{
    - String}}
  [Exists](#cfn-accessanalyzer-analyzer-filter-exists): {{Boolean}}
  [Neq](#cfn-accessanalyzer-analyzer-filter-neq): {{
    - String}}
  [Property](#cfn-accessanalyzer-analyzer-filter-property): {{String}}
```

## Properties
<a name="aws-properties-accessanalyzer-analyzer-filter-properties"></a>

`Contains`  <a name="cfn-accessanalyzer-analyzer-filter-contains"></a>
A "contains" condition to match for the rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Eq`  <a name="cfn-accessanalyzer-analyzer-filter-eq"></a>
An "equals" condition to match for the rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Exists`  <a name="cfn-accessanalyzer-analyzer-filter-exists"></a>
An "exists" condition to match for the rule.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Neq`  <a name="cfn-accessanalyzer-analyzer-filter-neq"></a>
A "not equal" condition to match for the rule.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Property`  <a name="cfn-accessanalyzer-analyzer-filter-property"></a>
The property used to define the criteria in the filter for the rule.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
