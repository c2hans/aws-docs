---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-databrickstablereference.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable DatabricksTableReference
<a name="aws-properties-cleanrooms-configuredtable-databrickstablereference"></a>

 A reference to a table within Databricks.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-databrickstablereference-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-databrickstablereference-syntax.json"></a>

```
{
  "[ConnectionType](#cfn-cleanrooms-configuredtable-databrickstablereference-connectiontype)" : {{DatabricksConnectionType}},
  "[SchemaName](#cfn-cleanrooms-configuredtable-databrickstablereference-schemaname)" : {{String}},
  "[TableName](#cfn-cleanrooms-configuredtable-databrickstablereference-tablename)" : {{String}},
  "[WorkspaceUrl](#cfn-cleanrooms-configuredtable-databrickstablereference-workspaceurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-databrickstablereference-syntax.yaml"></a>

```
  [ConnectionType](#cfn-cleanrooms-configuredtable-databrickstablereference-connectiontype): {{
    DatabricksConnectionType}}
  [SchemaName](#cfn-cleanrooms-configuredtable-databrickstablereference-schemaname): {{String}}
  [TableName](#cfn-cleanrooms-configuredtable-databrickstablereference-tablename): {{String}}
  [WorkspaceUrl](#cfn-cleanrooms-configuredtable-databrickstablereference-workspaceurl): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-databrickstablereference-properties"></a>

`ConnectionType`  <a name="cfn-cleanrooms-configuredtable-databrickstablereference-connectiontype"></a>
Type of the connector to be used for connecting to Databricks. Supported connector: Delta Sharing
*Required*: Yes
*Type*: [DatabricksConnectionType](aws-properties-cleanrooms-configuredtable-databricksconnectiontype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SchemaName`  <a name="cfn-cleanrooms-configuredtable-databrickstablereference-schemaname"></a>
Name of the Schema within Databricks.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-cleanrooms-configuredtable-databrickstablereference-tablename"></a>
Name of the Table within Databricks.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceUrl`  <a name="cfn-cleanrooms-configuredtable-databrickstablereference-workspaceurl"></a>
URL for the Databricks Workspace.
*Required*: Yes
*Type*: String
*Pattern*: `^https://[a-zA-Z0-9.-]+\.cloud\.databricks\.com/?$`
*Minimum*: `10`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
