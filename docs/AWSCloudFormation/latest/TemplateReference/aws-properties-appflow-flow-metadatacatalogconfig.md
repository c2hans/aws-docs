---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-flow-metadatacatalogconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::Flow MetadataCatalogConfig
<a name="aws-properties-appflow-flow-metadatacatalogconfig"></a>

Specifies the configuration that Amazon AppFlow uses when it catalogs your data. When Amazon AppFlow catalogs your data, it stores metadata in a data catalog.

## Syntax
<a name="aws-properties-appflow-flow-metadatacatalogconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-flow-metadatacatalogconfig-syntax.json"></a>

```
{
  "[GlueDataCatalog](#cfn-appflow-flow-metadatacatalogconfig-gluedatacatalog)" : {{GlueDataCatalog}}
}
```

### YAML
<a name="aws-properties-appflow-flow-metadatacatalogconfig-syntax.yaml"></a>

```
  [GlueDataCatalog](#cfn-appflow-flow-metadatacatalogconfig-gluedatacatalog): {{
    GlueDataCatalog}}
```

## Properties
<a name="aws-properties-appflow-flow-metadatacatalogconfig-properties"></a>

`GlueDataCatalog`  <a name="cfn-appflow-flow-metadatacatalogconfig-gluedatacatalog"></a>
Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the AWS Glue Data Catalog.
*Required*: No
*Type*: [GlueDataCatalog](aws-properties-appflow-flow-gluedatacatalog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
