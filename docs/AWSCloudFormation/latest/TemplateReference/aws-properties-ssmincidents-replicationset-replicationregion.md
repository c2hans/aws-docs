---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssmincidents-replicationset-replicationregion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMIncidents::ReplicationSet ReplicationRegion
<a name="aws-properties-ssmincidents-replicationset-replicationregion"></a>

The `ReplicationRegion` property type specifies the Region and AWS Key Management Service key to add to the replication set.

## Syntax
<a name="aws-properties-ssmincidents-replicationset-replicationregion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssmincidents-replicationset-replicationregion-syntax.json"></a>

```
{
  "[RegionConfiguration](#cfn-ssmincidents-replicationset-replicationregion-regionconfiguration)" : {{RegionConfiguration}},
  "[RegionName](#cfn-ssmincidents-replicationset-replicationregion-regionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssmincidents-replicationset-replicationregion-syntax.yaml"></a>

```
  [RegionConfiguration](#cfn-ssmincidents-replicationset-replicationregion-regionconfiguration): {{
    RegionConfiguration}}
  [RegionName](#cfn-ssmincidents-replicationset-replicationregion-regionname): {{String}}
```

## Properties
<a name="aws-properties-ssmincidents-replicationset-replicationregion-properties"></a>

`RegionConfiguration`  <a name="cfn-ssmincidents-replicationset-replicationregion-regionconfiguration"></a>
Specifies the Region configuration.
*Required*: No
*Type*: [RegionConfiguration](aws-properties-ssmincidents-replicationset-regionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RegionName`  <a name="cfn-ssmincidents-replicationset-replicationregion-regionname"></a>
Specifies the region name to add to the replication set.
*Required*: No
*Type*: String
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
