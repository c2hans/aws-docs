---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DocDB::DBCluster ServerlessV2ScalingConfiguration
<a name="aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration"></a>

Sets the scaling configuration of an Amazon DocumentDB Serverless cluster.

## Syntax
<a name="aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration-syntax.json"></a>

```
{
  "[MaxCapacity](#cfn-docdb-dbcluster-serverlessv2scalingconfiguration-maxcapacity)" : {{Number}},
  "[MinCapacity](#cfn-docdb-dbcluster-serverlessv2scalingconfiguration-mincapacity)" : {{Number}}
}
```

### YAML
<a name="aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration-syntax.yaml"></a>

```
  [MaxCapacity](#cfn-docdb-dbcluster-serverlessv2scalingconfiguration-maxcapacity): {{Number}}
  [MinCapacity](#cfn-docdb-dbcluster-serverlessv2scalingconfiguration-mincapacity): {{Number}}
```

## Properties
<a name="aws-properties-docdb-dbcluster-serverlessv2scalingconfiguration-properties"></a>

`MaxCapacity`  <a name="cfn-docdb-dbcluster-serverlessv2scalingconfiguration-maxcapacity"></a>
The maximum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 32, 32.5, 33, and so on.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinCapacity`  <a name="cfn-docdb-dbcluster-serverlessv2scalingconfiguration-mincapacity"></a>
The minimum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 8, 8.5, 9, and so on.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
