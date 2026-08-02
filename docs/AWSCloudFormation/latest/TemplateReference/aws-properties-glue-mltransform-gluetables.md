---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-mltransform-gluetables.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::MLTransform GlueTables
<a name="aws-properties-glue-mltransform-gluetables"></a>

The database and table in the AWS Glue Data Catalog that is used for input or output data.

## Syntax
<a name="aws-properties-glue-mltransform-gluetables-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-mltransform-gluetables-syntax.json"></a>

```
{
  "[CatalogId](#cfn-glue-mltransform-gluetables-catalogid)" : {{String}},
  "[ConnectionName](#cfn-glue-mltransform-gluetables-connectionname)" : {{String}},
  "[DatabaseName](#cfn-glue-mltransform-gluetables-databasename)" : {{String}},
  "[TableName](#cfn-glue-mltransform-gluetables-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-mltransform-gluetables-syntax.yaml"></a>

```
  [CatalogId](#cfn-glue-mltransform-gluetables-catalogid): {{String}}
  [ConnectionName](#cfn-glue-mltransform-gluetables-connectionname): {{String}}
  [DatabaseName](#cfn-glue-mltransform-gluetables-databasename): {{String}}
  [TableName](#cfn-glue-mltransform-gluetables-tablename): {{String}}
```

## Properties
<a name="aws-properties-glue-mltransform-gluetables-properties"></a>

`CatalogId`  <a name="cfn-glue-mltransform-gluetables-catalogid"></a>
A unique identifier for the AWS Glue Data Catalog.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConnectionName`  <a name="cfn-glue-mltransform-gluetables-connectionname"></a>
The name of the connection to the AWS Glue Data Catalog.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-glue-mltransform-gluetables-databasename"></a>
A database name in the AWS Glue Data Catalog.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-glue-mltransform-gluetables-tablename"></a>
A table name in the AWS Glue Data Catalog.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
