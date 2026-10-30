---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable DatabricksDeltaSharingConnection
<a name="aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection"></a>

Details about Delta Sharing Connector for Databricks

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection-syntax.json"></a>

```
{
  "[DeltaShareEndpoint](#cfn-cleanrooms-configuredtable-databricksdeltasharingconnection-deltashareendpoint)" : {{String}},
  "[ShareName](#cfn-cleanrooms-configuredtable-databricksdeltasharingconnection-sharename)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection-syntax.yaml"></a>

```
  [DeltaShareEndpoint](#cfn-cleanrooms-configuredtable-databricksdeltasharingconnection-deltashareendpoint): {{String}}
  [ShareName](#cfn-cleanrooms-configuredtable-databricksdeltasharingconnection-sharename): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-databricksdeltasharingconnection-properties"></a>

`DeltaShareEndpoint`  <a name="cfn-cleanrooms-configuredtable-databricksdeltasharingconnection-deltashareendpoint"></a>
The base URL of a Delta Sharing server that hosts shared datasets.
*Required*: Yes
*Type*: String
*Pattern*: `^https://(?:[a-zA-Z0-9.-]+\.cloud\.databricks\.com/api/2\.0/delta-sharing|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.opensharing\.[a-z0-9-]+\.cloud\.databricks\.com/api/2\.0/opensharing)/metastores/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/recipients/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `10`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShareName`  <a name="cfn-cleanrooms-configuredtable-databricksdeltasharingconnection-sharename"></a>
Name of the Share used for OpenSharing (Delta Sharing) the Databricks Table.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
