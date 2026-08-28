---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-catalog-targetredshiftcatalog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Catalog TargetRedshiftCatalog
<a name="aws-properties-glue-catalog-targetredshiftcatalog"></a>

A structure that describes a target catalog for resource linking.

## Syntax
<a name="aws-properties-glue-catalog-targetredshiftcatalog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-catalog-targetredshiftcatalog-syntax.json"></a>

```
{
  "[CatalogArn](#cfn-glue-catalog-targetredshiftcatalog-catalogarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-catalog-targetredshiftcatalog-syntax.yaml"></a>

```
  [CatalogArn](#cfn-glue-catalog-targetredshiftcatalog-catalogarn): {{String}}
```

## Properties
<a name="aws-properties-glue-catalog-targetredshiftcatalog-properties"></a>

`CatalogArn`  <a name="cfn-glue-catalog-targetredshiftcatalog-catalogarn"></a>
The Amazon Resource Name (ARN) of the catalog resource.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
