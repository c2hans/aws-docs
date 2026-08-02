---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dsql-cluster-multiregionproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DSQL::Cluster MultiRegionProperties
<a name="aws-properties-dsql-cluster-multiregionproperties"></a>

Defines the structure for multi-Region cluster configurations, containing the witness Region and peered cluster settings.

## Syntax
<a name="aws-properties-dsql-cluster-multiregionproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dsql-cluster-multiregionproperties-syntax.json"></a>

```
{
  "[Clusters](#cfn-dsql-cluster-multiregionproperties-clusters)" : {{[ String, ... ]}},
  "[WitnessRegion](#cfn-dsql-cluster-multiregionproperties-witnessregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-dsql-cluster-multiregionproperties-syntax.yaml"></a>

```
  [Clusters](#cfn-dsql-cluster-multiregionproperties-clusters): {{
    - String}}
  [WitnessRegion](#cfn-dsql-cluster-multiregionproperties-witnessregion): {{String}}
```

## Properties
<a name="aws-properties-dsql-cluster-multiregionproperties-properties"></a>

`Clusters`  <a name="cfn-dsql-cluster-multiregionproperties-clusters"></a>
The set of peered clusters that form the multi-Region cluster configuration. Each peered cluster represents a database instance in a different Region.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WitnessRegion`  <a name="cfn-dsql-cluster-multiregionproperties-witnessregion"></a>
The Region that serves as the witness Region for a multi-Region cluster. The witness Region helps maintain cluster consistency and quorum.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
