---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-documentenrichmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource DocumentEnrichmentConfiguration
<a name="aws-properties-qbusiness-datasource-documentenrichmentconfiguration"></a>

Provides the configuration information for altering document metadata and content during the document ingestion process.

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).

## Syntax
<a name="aws-properties-qbusiness-datasource-documentenrichmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-documentenrichmentconfiguration-syntax.json"></a>

```
{
  "[InlineConfigurations](#cfn-qbusiness-datasource-documentenrichmentconfiguration-inlineconfigurations)" : {{[ InlineDocumentEnrichmentConfiguration, ... ]}},
  "[PostExtractionHookConfiguration](#cfn-qbusiness-datasource-documentenrichmentconfiguration-postextractionhookconfiguration)" : {{HookConfiguration}},
  "[PreExtractionHookConfiguration](#cfn-qbusiness-datasource-documentenrichmentconfiguration-preextractionhookconfiguration)" : {{HookConfiguration}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-documentenrichmentconfiguration-syntax.yaml"></a>

```
  [InlineConfigurations](#cfn-qbusiness-datasource-documentenrichmentconfiguration-inlineconfigurations): {{
    - InlineDocumentEnrichmentConfiguration}}
  [PostExtractionHookConfiguration](#cfn-qbusiness-datasource-documentenrichmentconfiguration-postextractionhookconfiguration): {{
    HookConfiguration}}
  [PreExtractionHookConfiguration](#cfn-qbusiness-datasource-documentenrichmentconfiguration-preextractionhookconfiguration): {{
    HookConfiguration}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-documentenrichmentconfiguration-properties"></a>

`InlineConfigurations`  <a name="cfn-qbusiness-datasource-documentenrichmentconfiguration-inlineconfigurations"></a>
Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Q Business.
*Required*: No
*Type*: Array of [InlineDocumentEnrichmentConfiguration](aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.md)
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostExtractionHookConfiguration`  <a name="cfn-qbusiness-datasource-documentenrichmentconfiguration-postextractionhookconfiguration"></a>
Configuration information for invoking a Lambda function in AWS Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see [Using Lambda functions](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html).
*Required*: No
*Type*: [HookConfiguration](aws-properties-qbusiness-datasource-hookconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreExtractionHookConfiguration`  <a name="cfn-qbusiness-datasource-documentenrichmentconfiguration-preextractionhookconfiguration"></a>
Configuration information for invoking a Lambda function in AWS Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see [Using Lambda functions](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html).
*Required*: No
*Type*: [HookConfiguration](aws-properties-qbusiness-datasource-hookconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
