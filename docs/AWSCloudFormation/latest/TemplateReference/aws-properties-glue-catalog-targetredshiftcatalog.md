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
