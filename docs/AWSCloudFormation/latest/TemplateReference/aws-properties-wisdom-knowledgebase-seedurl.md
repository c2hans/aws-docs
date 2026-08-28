---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-seedurl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase SeedUrl
<a name="aws-properties-wisdom-knowledgebase-seedurl"></a>

A URL for crawling.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-seedurl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-seedurl-syntax.json"></a>

```
{
  "[Url](#cfn-wisdom-knowledgebase-seedurl-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-seedurl-syntax.yaml"></a>

```
  [Url](#cfn-wisdom-knowledgebase-seedurl-url): {{String}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-seedurl-properties"></a>

`Url`  <a name="cfn-wisdom-knowledgebase-seedurl-url"></a>
URL for crawling
*Required*: No
*Type*: String
*Pattern*: `^https?://[A-Za-z0-9][^\s]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
