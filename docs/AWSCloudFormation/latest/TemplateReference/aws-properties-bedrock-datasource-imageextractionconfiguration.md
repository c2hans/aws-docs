---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-imageextractionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ImageExtractionConfiguration
<a name="aws-properties-bedrock-datasource-imageextractionconfiguration"></a>

Configuration for image extraction.

## Syntax
<a name="aws-properties-bedrock-datasource-imageextractionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-imageextractionconfiguration-syntax.json"></a>

```
{
  "[ImageExtractionStatus](#cfn-bedrock-datasource-imageextractionconfiguration-imageextractionstatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-imageextractionconfiguration-syntax.yaml"></a>

```
  [ImageExtractionStatus](#cfn-bedrock-datasource-imageextractionconfiguration-imageextractionstatus): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-imageextractionconfiguration-properties"></a>

`ImageExtractionStatus`  <a name="cfn-bedrock-datasource-imageextractionconfiguration-imageextractionstatus"></a>
Whether image extraction is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
