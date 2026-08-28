---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftQueryEngineAwsDataCatalogStorageConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration"></a>

Contains configurations for storage in AWS Glue Data Catalog.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-syntax.json"></a>

```
{
  "[TableNames](#cfn-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-tablenames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-syntax.yaml"></a>

```
  [TableNames](#cfn-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-tablenames): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-properties"></a>

`TableNames`  <a name="cfn-bedrock-knowledgebase-redshiftqueryengineawsdatacatalogstorageconfiguration-tablenames"></a>
A list of names of the tables to use.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
