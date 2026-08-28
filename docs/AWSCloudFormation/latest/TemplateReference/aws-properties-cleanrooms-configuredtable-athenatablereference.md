---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-athenatablereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable AthenaTableReference
<a name="aws-properties-cleanrooms-configuredtable-athenatablereference"></a>

 A reference to a table within Athena.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-athenatablereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-athenatablereference-syntax.json"></a>

```
{
  "[CatalogName](#cfn-cleanrooms-configuredtable-athenatablereference-catalogname)" : {{String}},
  "[DatabaseName](#cfn-cleanrooms-configuredtable-athenatablereference-databasename)" : {{String}},
  "[OutputLocation](#cfn-cleanrooms-configuredtable-athenatablereference-outputlocation)" : {{String}},
  "[Region](#cfn-cleanrooms-configuredtable-athenatablereference-region)" : {{String}},
  "[TableName](#cfn-cleanrooms-configuredtable-athenatablereference-tablename)" : {{String}},
  "[WorkGroup](#cfn-cleanrooms-configuredtable-athenatablereference-workgroup)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-athenatablereference-syntax.yaml"></a>

```
  [CatalogName](#cfn-cleanrooms-configuredtable-athenatablereference-catalogname): {{String}}
  [DatabaseName](#cfn-cleanrooms-configuredtable-athenatablereference-databasename): {{String}}
  [OutputLocation](#cfn-cleanrooms-configuredtable-athenatablereference-outputlocation): {{String}}
  [Region](#cfn-cleanrooms-configuredtable-athenatablereference-region): {{String}}
  [TableName](#cfn-cleanrooms-configuredtable-athenatablereference-tablename): {{String}}
  [WorkGroup](#cfn-cleanrooms-configuredtable-athenatablereference-workgroup): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-athenatablereference-properties"></a>

`CatalogName`  <a name="cfn-cleanrooms-configuredtable-athenatablereference-catalogname"></a>
 The catalog name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-cleanrooms-configuredtable-athenatablereference-databasename"></a>
 The database name.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputLocation`  <a name="cfn-cleanrooms-configuredtable-athenatablereference-outputlocation"></a>
 The output location for the Athena table.
*Required*: No
*Type*: String
*Minimum*: `8`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-cleanrooms-configuredtable-athenatablereference-region"></a>
The AWS Region where the Athena table is located. This parameter is required to uniquely identify and access tables across different Regions.
*Required*: No
*Type*: String
*Allowed values*: `us-west-1 | us-west-2 | us-east-1 | us-east-2 | af-south-1 | ap-east-1 | ap-south-2 | ap-southeast-1 | ap-southeast-2 | ap-southeast-5 | ap-southeast-4 | ap-southeast-7 | ap-south-1 | ap-northeast-3 | ap-northeast-1 | ap-northeast-2 | ca-central-1 | ca-west-1 | eu-south-1 | eu-west-3 | eu-south-2 | eu-central-2 | eu-central-1 | eu-north-1 | eu-west-1 | eu-west-2 | me-south-1 | me-central-1 | il-central-1 | sa-east-1 | mx-central-1 | ap-east-2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-cleanrooms-configuredtable-athenatablereference-tablename"></a>
 The table reference.
*Required*: Yes
*Type*: String
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkGroup`  <a name="cfn-cleanrooms-configuredtable-athenatablereference-workgroup"></a>
 The workgroup of the Athena table reference.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
