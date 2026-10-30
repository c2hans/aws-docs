---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-databricksconnectiontype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable DatabricksConnectionType
<a name="aws-properties-cleanrooms-configuredtable-databricksconnectiontype"></a>

Type of the connector to be used for connecting to Databricks. Supported connector: Delta Sharing

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-databricksconnectiontype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-databricksconnectiontype-syntax.json"></a>

```
{
  "[DeltaSharing](#cfn-cleanrooms-configuredtable-databricksconnectiontype-deltasharing)" : {{DatabricksDeltaSharingConnection}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-databricksconnectiontype-syntax.yaml"></a>

```
  [DeltaSharing](#cfn-cleanrooms-configuredtable-databricksconnectiontype-deltasharing): {{
    DatabricksDeltaSharingConnection}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-databricksconnectiontype-properties"></a>

`DeltaSharing`  <a name="cfn-cleanrooms-configuredtable-databricksconnectiontype-deltasharing"></a>
Details about Connector for Databricks
*Required*: Yes
*Type*: [DatabricksDeltaSharingConnection](aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
