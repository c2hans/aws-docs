---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-insight-keywordfilter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Insight KeywordFilter
<a name="aws-properties-securityhub-insight-keywordfilter"></a>

A keyword filter for querying findings.

## Syntax
<a name="aws-properties-securityhub-insight-keywordfilter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-insight-keywordfilter-syntax.json"></a>

```
{
  "[Value](#cfn-securityhub-insight-keywordfilter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityhub-insight-keywordfilter-syntax.yaml"></a>

```
  [Value](#cfn-securityhub-insight-keywordfilter-value): {{String}}
```

## Properties
<a name="aws-properties-securityhub-insight-keywordfilter-properties"></a>

`Value`  <a name="cfn-securityhub-insight-keywordfilter-value"></a>
A value for the keyword.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
