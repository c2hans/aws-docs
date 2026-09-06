---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-gluetablereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable GlueTableReference
<a name="aws-properties-cleanrooms-configuredtable-gluetablereference"></a>

A reference to a table within an AWS Glue data catalog.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-gluetablereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-gluetablereference-syntax.json"></a>

```
{
  "[DatabaseName](#cfn-cleanrooms-configuredtable-gluetablereference-databasename)" : {{String}},
  "[Region](#cfn-cleanrooms-configuredtable-gluetablereference-region)" : {{String}},
  "[TableName](#cfn-cleanrooms-configuredtable-gluetablereference-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-gluetablereference-syntax.yaml"></a>

```
  [DatabaseName](#cfn-cleanrooms-configuredtable-gluetablereference-databasename): {{String}}
  [Region](#cfn-cleanrooms-configuredtable-gluetablereference-region): {{String}}
  [TableName](#cfn-cleanrooms-configuredtable-gluetablereference-tablename): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-gluetablereference-properties"></a>

`DatabaseName`  <a name="cfn-cleanrooms-configuredtable-gluetablereference-databasename"></a>
The name of the database the AWS Glue table belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-cleanrooms-configuredtable-gluetablereference-region"></a>
The AWS Region where the AWS Glue table is located. This parameter is required to uniquely identify and access tables across different Regions.
*Required*: No
*Type*: String
*Allowed values*: `us-west-1 | us-west-2 | us-east-1 | us-east-2 | af-south-1 | ap-east-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-5 | ap-southeast-4 | ap-southeast-7 | ap-south-1 | ap-northeast-3 | ap-northeast-1 | ap-northeast-2 | ca-central-1 | ca-west-1 | eu-south-1 | eu-west-3 | eu-south-2 | eu-central-2 | eu-central-1 | eu-north-1 | eu-west-1 | eu-west-2 | me-south-1 | me-central-1 | il-central-1 | sa-east-1 | mx-central-1 | ap-east-2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-cleanrooms-configuredtable-gluetablereference-tablename"></a>
The name of the AWS Glue table.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
