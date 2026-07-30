---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-snowflaketableschemav1.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable SnowflakeTableSchemaV1
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschemav1"></a>

 The Snowflake table schema.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschemav1-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschemav1-syntax.json"></a>

```
{
  "[ColumnName](#cfn-cleanrooms-configuredtable-snowflaketableschemav1-columnname)" : {{String}},
  "[ColumnType](#cfn-cleanrooms-configuredtable-snowflaketableschemav1-columntype)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschemav1-syntax.yaml"></a>

```
  [ColumnName](#cfn-cleanrooms-configuredtable-snowflaketableschemav1-columnname): {{String}}
  [ColumnType](#cfn-cleanrooms-configuredtable-snowflaketableschemav1-columntype): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-snowflaketableschemav1-properties"></a>

`ColumnName`  <a name="cfn-cleanrooms-configuredtable-snowflaketableschemav1-columnname"></a>
 The column name.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnType`  <a name="cfn-cleanrooms-configuredtable-snowflaketableschemav1-columntype"></a>
 The column's data type. Supported data types: `ARRAY`, `BIGINT`, `BOOLEAN`, `CHAR`, `DATE`, `DECIMAL`, `DOUBLE`, `DOUBLE PRECISION`, `FLOAT`, `FLOAT4`, `INT`, `INTEGER`, `MAP`, `NUMERIC`, `NUMBER`, `REAL`, `SMALLINT`, `STRING`, `TIMESTAMP`, `TIMESTAMP_LTZ`, `TIMESTAMP_NTZ`, `DATETIME`, `TINYINT`, `VARCHAR`, `TEXT`, `CHARACTER`.
*Required*: Yes
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
