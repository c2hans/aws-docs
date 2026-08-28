---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-enrichmentstrategyconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource EnrichmentStrategyConfiguration
<a name="aws-properties-bedrock-datasource-enrichmentstrategyconfiguration"></a>

The strategy used for performing context enrichment.

## Syntax
<a name="aws-properties-bedrock-datasource-enrichmentstrategyconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-enrichmentstrategyconfiguration-syntax.json"></a>

```
{
  "[Method](#cfn-bedrock-datasource-enrichmentstrategyconfiguration-method)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-enrichmentstrategyconfiguration-syntax.yaml"></a>

```
  [Method](#cfn-bedrock-datasource-enrichmentstrategyconfiguration-method): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-enrichmentstrategyconfiguration-properties"></a>

`Method`  <a name="cfn-bedrock-datasource-enrichmentstrategyconfiguration-method"></a>
The method used for the context enrichment strategy.
*Required*: Yes
*Type*: String
*Allowed values*: `CHUNK_ENTITY_EXTRACTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
