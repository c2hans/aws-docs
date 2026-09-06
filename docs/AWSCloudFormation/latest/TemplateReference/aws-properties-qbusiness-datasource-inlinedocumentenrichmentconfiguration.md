---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::DataSource InlineDocumentEnrichmentConfiguration
<a name="aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration"></a>

Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Q Business.

To apply advanced logic, to go beyond what you can do with basic logic, see [`HookConfiguration`](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_HookConfiguration.html).

For more information, see [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/custom-document-enrichment.html).

## Syntax
<a name="aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration-syntax.json"></a>

```
{
  "[Condition](#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-condition)" : {{DocumentAttributeCondition}},
  "[DocumentContentOperator](#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-documentcontentoperator)" : {{String}},
  "[Target](#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-target)" : {{DocumentAttributeTarget}}
}
```

### YAML
<a name="aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration-syntax.yaml"></a>

```
  [Condition](#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-condition): {{
    DocumentAttributeCondition}}
  [DocumentContentOperator](#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-documentcontentoperator): {{String}}
  [Target](#cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-target): {{
    DocumentAttributeTarget}}
```

## Properties
<a name="aws-properties-qbusiness-datasource-inlinedocumentenrichmentconfiguration-properties"></a>

`Condition`  <a name="cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-condition"></a>
Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Q Business.
*Required*: No
*Type*: [DocumentAttributeCondition](aws-properties-qbusiness-datasource-documentattributecondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DocumentContentOperator`  <a name="cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-documentcontentoperator"></a>
`TRUE` to delete content if the condition used for the target attribute is met.
*Required*: No
*Type*: String
*Allowed values*: `DELETE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Target`  <a name="cfn-qbusiness-datasource-inlinedocumentenrichmentconfiguration-target"></a>
Configuration of the target document attribute or metadata field when ingesting documents into Amazon Q Business. You can also include a value.
*Required*: No
*Type*: [DocumentAttributeTarget](aws-properties-qbusiness-datasource-documentattributetarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
