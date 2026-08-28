---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-topic-topicconfigoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Topic TopicConfigOptions
<a name="aws-properties-quicksight-topic-topicconfigoptions"></a>

Configuration options for a `Topic`.

## Syntax
<a name="aws-properties-quicksight-topic-topicconfigoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-topic-topicconfigoptions-syntax.json"></a>

```
{
  "[QBusinessInsightsEnabled](#cfn-quicksight-topic-topicconfigoptions-qbusinessinsightsenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-topic-topicconfigoptions-syntax.yaml"></a>

```
  [QBusinessInsightsEnabled](#cfn-quicksight-topic-topicconfigoptions-qbusinessinsightsenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-topic-topicconfigoptions-properties"></a>

`QBusinessInsightsEnabled`  <a name="cfn-quicksight-topic-topicconfigoptions-qbusinessinsightsenabled"></a>
Enables Amazon Q Business Insights for a `Topic`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
