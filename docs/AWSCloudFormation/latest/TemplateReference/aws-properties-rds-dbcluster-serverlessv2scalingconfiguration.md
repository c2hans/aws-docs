---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-dbcluster-serverlessv2scalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::DBCluster ServerlessV2ScalingConfiguration
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration"></a>

The `ServerlessV2ScalingConfiguration` property type specifies the scaling configuration of an Aurora Serverless V2 DB cluster. For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.

If you have an Aurora cluster, you must set this attribute before you add a DB instance that uses the `db.serverless` DB instance class. For more information, see [Clusters that use Aurora Serverless v2 must have a capacity range specified](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html#aurora-serverless-v2.requirements.capacity-range) in the *Amazon Aurora User Guide*.

This property is only supported for Aurora Serverless v2. For Aurora Serverless v1, use the `ScalingConfiguration` property.

Valid for: Aurora Serverless v2 DB clusters

## Syntax
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration-syntax.json"></a>

```
{
  "[MaxCapacity](#cfn-rds-dbcluster-serverlessv2scalingconfiguration-maxcapacity)" : {{Number}},
  "[MinCapacity](#cfn-rds-dbcluster-serverlessv2scalingconfiguration-mincapacity)" : {{Number}},
  "[SecondsUntilAutoPause](#cfn-rds-dbcluster-serverlessv2scalingconfiguration-secondsuntilautopause)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration-syntax.yaml"></a>

```
  [MaxCapacity](#cfn-rds-dbcluster-serverlessv2scalingconfiguration-maxcapacity): {{Number}}
  [MinCapacity](#cfn-rds-dbcluster-serverlessv2scalingconfiguration-mincapacity): {{Number}}
  [SecondsUntilAutoPause](#cfn-rds-dbcluster-serverlessv2scalingconfiguration-secondsuntilautopause): {{Integer}}
```

## Properties
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration-properties"></a>

`MaxCapacity`  <a name="cfn-rds-dbcluster-serverlessv2scalingconfiguration-maxcapacity"></a>
The maximum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 40, 40.5, 41, and so on. The largest value that you can use is 128.
The maximum capacity must be higher than 0.5 ACUs. For more information, see [ Choosing the maximum Aurora Serverless v2 capacity setting for a cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.setting-capacity.html#aurora-serverless-v2.max_capacity_considerations) in the *Amazon Aurora User Guide*.
Aurora automatically sets certain parameters for Aurora Serverless V2 DB instances to values that depend on the maximum ACU value in the capacity range. When you update the maximum capacity value, the `ParameterApplyStatus` value for the DB instance changes to `pending-reboot`. You can update the parameter values by rebooting the DB instance after changing the capacity range.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinCapacity`  <a name="cfn-rds-dbcluster-serverlessv2scalingconfiguration-mincapacity"></a>
The minimum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 8, 8.5, 9, and so on. For Aurora versions that support the Aurora Serverless v2 auto-pause feature, the smallest value that you can use is 0. For versions that don't support Aurora Serverless v2 auto-pause, the smallest value that you can use is 0.5.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondsUntilAutoPause`  <a name="cfn-rds-dbcluster-serverlessv2scalingconfiguration-secondsuntilautopause"></a>
Specifies the number of seconds an Aurora Serverless v2 DB instance must be idle before Aurora attempts to automatically pause it.
Specify a value between 300 seconds (five minutes) and 86,400 seconds (one day). The default is 300 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration--examples"></a>

The following example specifies a scaling configuration for an Aurora Serverless v2 DB cluster.

### Specifying a scaling configuration for a Serverless v2 DB cluster
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration--examples--Specifying_a_scaling_configuration_for_a_Serverless_v2_DB_cluster"></a>

#### JSON
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration--examples--Specifying_a_scaling_configuration_for_a_Serverless_v2_DB_cluster--json"></a>

```
"ServerlessV2ScalingConfiguration":{
   "MinCapacity": 9,
   "MaxCapacity": 42
}
```

#### YAML
<a name="aws-properties-rds-dbcluster-serverlessv2scalingconfiguration--examples--Specifying_a_scaling_configuration_for_a_Serverless_v2_DB_cluster--yaml"></a>

```
ServerlessV2ScalingConfiguration:
  MinCapacity: 9
  MaxCapacity: 42
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
