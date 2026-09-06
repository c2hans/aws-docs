---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-dataqualityruleset-dataqualitytargettable.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::DataQualityRuleset DataQualityTargetTable
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable"></a>

An object representing an AWS Glue table.

## Syntax
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-glue-dataqualityruleset-dataqualitytargettable-databasename)" : {{String}},
  "[TableName](#cfn-glue-dataqualityruleset-dataqualitytargettable-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-syntax.yaml"></a>

```
  [DatabaseName](#cfn-glue-dataqualityruleset-dataqualitytargettable-databasename): {{String}}
  [TableName](#cfn-glue-dataqualityruleset-dataqualitytargettable-tablename): {{String}}
```

## Properties
<a name="aws-properties-glue-dataqualityruleset-dataqualitytargettable-properties"></a>

`DatabaseName`  <a name="cfn-glue-dataqualityruleset-dataqualitytargettable-databasename"></a>
The name of the database where the AWS Glue table exists.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-glue-dataqualityruleset-dataqualitytargettable-tablename"></a>
The name of the AWS Glue table.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
