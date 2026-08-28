---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kendra::DataSource SalesforceKnowledgeArticleConfiguration
<a name="aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration"></a>

Provides the configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both

## Syntax
<a name="aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration-syntax.json"></a>

```
{
  "[CustomKnowledgeArticleTypeConfigurations](#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-customknowledgearticletypeconfigurations)" : {{[ SalesforceCustomKnowledgeArticleTypeConfiguration, ... ]}},
  "[IncludedStates](#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-includedstates)" : {{[ String, ... ]}},
  "[StandardKnowledgeArticleTypeConfiguration](#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-standardknowledgearticletypeconfiguration)" : {{SalesforceStandardKnowledgeArticleTypeConfiguration}}
}
```

### YAML
<a name="aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration-syntax.yaml"></a>

```
  [CustomKnowledgeArticleTypeConfigurations](#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-customknowledgearticletypeconfigurations): {{
    - SalesforceCustomKnowledgeArticleTypeConfiguration}}
  [IncludedStates](#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-includedstates): {{
    - String}}
  [StandardKnowledgeArticleTypeConfiguration](#cfn-kendra-datasource-salesforceknowledgearticleconfiguration-standardknowledgearticletypeconfiguration): {{
    SalesforceStandardKnowledgeArticleTypeConfiguration}}
```

## Properties
<a name="aws-properties-kendra-datasource-salesforceknowledgearticleconfiguration-properties"></a>

`CustomKnowledgeArticleTypeConfigurations`  <a name="cfn-kendra-datasource-salesforceknowledgearticleconfiguration-customknowledgearticletypeconfigurations"></a>
Configuration information for custom Salesforce knowledge articles.
*Required*: No
*Type*: Array of [SalesforceCustomKnowledgeArticleTypeConfiguration](aws-properties-kendra-datasource-salesforcecustomknowledgearticletypeconfiguration.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedStates`  <a name="cfn-kendra-datasource-salesforceknowledgearticleconfiguration-includedstates"></a>
Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StandardKnowledgeArticleTypeConfiguration`  <a name="cfn-kendra-datasource-salesforceknowledgearticleconfiguration-standardknowledgearticletypeconfiguration"></a>
Configuration information for standard Salesforce knowledge articles.
*Required*: No
*Type*: [SalesforceStandardKnowledgeArticleTypeConfiguration](aws-properties-kendra-datasource-salesforcestandardknowledgearticletypeconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
