---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-replicaspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table ReplicaSpecification
<a name="aws-properties-cassandra-table-replicaspecification"></a>

The AWS Region specific settings of a multi-Region table.

For a multi-Region table, you can configure the table's read capacity differently per AWS Region. You can do this by configuring the following parameters.
+ `region`: The Region where these settings are applied. (Required)
+ `readCapacityUnits`: The provisioned read capacity units. (Optional)
+ `readCapacityAutoScaling`: The read capacity auto scaling settings for the table. (Optional)

## Syntax
<a name="aws-properties-cassandra-table-replicaspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-replicaspecification-syntax.json"></a>

```
{
  "[ReadCapacityAutoScaling](#cfn-cassandra-table-replicaspecification-readcapacityautoscaling)" : {{AutoScalingSetting}},
  "[ReadCapacityUnits](#cfn-cassandra-table-replicaspecification-readcapacityunits)" : {{Integer}},
  "[Region](#cfn-cassandra-table-replicaspecification-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-table-replicaspecification-syntax.yaml"></a>

```
  [ReadCapacityAutoScaling](#cfn-cassandra-table-replicaspecification-readcapacityautoscaling): {{
    AutoScalingSetting}}
  [ReadCapacityUnits](#cfn-cassandra-table-replicaspecification-readcapacityunits): {{Integer}}
  [Region](#cfn-cassandra-table-replicaspecification-region): {{String}}
```

## Properties
<a name="aws-properties-cassandra-table-replicaspecification-properties"></a>

`ReadCapacityAutoScaling`  <a name="cfn-cassandra-table-replicaspecification-readcapacityautoscaling"></a>
The read capacity auto scaling settings for the multi-Region table in the specified AWS Region.
*Required*: No
*Type*: [AutoScalingSetting](aws-properties-cassandra-table-autoscalingsetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadCapacityUnits`  <a name="cfn-cassandra-table-replicaspecification-readcapacityunits"></a>
The provisioned read capacity units for the multi-Region table in the specified AWS Region.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-cassandra-table-replicaspecification-region"></a>
The AWS Region.
*Required*: Yes
*Type*: String
*Minimum*: `2`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
