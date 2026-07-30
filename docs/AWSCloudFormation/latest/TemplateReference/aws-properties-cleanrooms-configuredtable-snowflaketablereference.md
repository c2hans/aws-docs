---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-snowflaketablereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable SnowflakeTableReference
<a name="aws-properties-cleanrooms-configuredtable-snowflaketablereference"></a>

 A reference to a table within Snowflake.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-snowflaketablereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-snowflaketablereference-syntax.json"></a>

```
{
  "[AccountIdentifier](#cfn-cleanrooms-configuredtable-snowflaketablereference-accountidentifier)" : {{String}},
  "[DatabaseName](#cfn-cleanrooms-configuredtable-snowflaketablereference-databasename)" : {{String}},
  "[SchemaName](#cfn-cleanrooms-configuredtable-snowflaketablereference-schemaname)" : {{String}},
  "[SecretArn](#cfn-cleanrooms-configuredtable-snowflaketablereference-secretarn)" : {{String}},
  "[TableName](#cfn-cleanrooms-configuredtable-snowflaketablereference-tablename)" : {{String}},
  "[TableSchema](#cfn-cleanrooms-configuredtable-snowflaketablereference-tableschema)" : {{SnowflakeTableSchema}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-snowflaketablereference-syntax.yaml"></a>

```
  [AccountIdentifier](#cfn-cleanrooms-configuredtable-snowflaketablereference-accountidentifier): {{String}}
  [DatabaseName](#cfn-cleanrooms-configuredtable-snowflaketablereference-databasename): {{String}}
  [SchemaName](#cfn-cleanrooms-configuredtable-snowflaketablereference-schemaname): {{String}}
  [SecretArn](#cfn-cleanrooms-configuredtable-snowflaketablereference-secretarn): {{String}}
  [TableName](#cfn-cleanrooms-configuredtable-snowflaketablereference-tablename): {{String}}
  [TableSchema](#cfn-cleanrooms-configuredtable-snowflaketablereference-tableschema): {{
    SnowflakeTableSchema}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-snowflaketablereference-properties"></a>

`AccountIdentifier`  <a name="cfn-cleanrooms-configuredtable-snowflaketablereference-accountidentifier"></a>
 The account identifier for the Snowflake table reference.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-cleanrooms-configuredtable-snowflaketablereference-databasename"></a>
 The name of the database the Snowflake table belongs to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaName`  <a name="cfn-cleanrooms-configuredtable-snowflaketablereference-schemaname"></a>
 The schema name of the Snowflake table reference.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-cleanrooms-configuredtable-snowflaketablereference-secretarn"></a>
 The secret ARN of the Snowflake table reference.
*Required*: Yes
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-cleanrooms-configuredtable-snowflaketablereference-tablename"></a>
 The name of the Snowflake table.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableSchema`  <a name="cfn-cleanrooms-configuredtable-snowflaketablereference-tableschema"></a>
 The schema of the Snowflake table.
*Required*: Yes
*Type*: [SnowflakeTableSchema](aws-properties-cleanrooms-configuredtable-snowflaketableschema.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
