---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-mltransform-inputrecordtables.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::MLTransform InputRecordTables
<a name="aws-properties-glue-mltransform-inputrecordtables"></a>

A list of AWS Glue table definitions used by the transform.

## Syntax
<a name="aws-properties-glue-mltransform-inputrecordtables-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-mltransform-inputrecordtables-syntax.json"></a>

```
{
  "[GlueTables](#cfn-glue-mltransform-inputrecordtables-gluetables)" : {{[ GlueTables, ... ]}}
}
```

### YAML
<a name="aws-properties-glue-mltransform-inputrecordtables-syntax.yaml"></a>

```
  [GlueTables](#cfn-glue-mltransform-inputrecordtables-gluetables): {{
    - GlueTables}}
```

## Properties
<a name="aws-properties-glue-mltransform-inputrecordtables-properties"></a>

`GlueTables`  <a name="cfn-glue-mltransform-inputrecordtables-gluetables"></a>
The database and table in the AWS Glue Data Catalog that is used for input or output data.
*Required*: No
*Type*: [Array](aws-properties-glue-mltransform-gluetables.md) of [GlueTables](aws-properties-glue-mltransform-gluetables.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
