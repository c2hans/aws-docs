---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-placementgroupconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster PlacementGroupConfig
<a name="aws-properties-emr-cluster-placementgroupconfig"></a>

Placement group configuration for an Amazon EMR cluster. The configuration specifies the placement strategy that can be applied to instance roles during cluster creation.

To use this configuration, consider attaching managed policy AmazonElasticMapReducePlacementGroupPolicy to the Amazon EMR role.

## Syntax
<a name="aws-properties-emr-cluster-placementgroupconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-placementgroupconfig-syntax.json"></a>

```
{
  "[InstanceRole](#cfn-emr-cluster-placementgroupconfig-instancerole)" : {{String}},
  "[PlacementStrategy](#cfn-emr-cluster-placementgroupconfig-placementstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-cluster-placementgroupconfig-syntax.yaml"></a>

```
  [InstanceRole](#cfn-emr-cluster-placementgroupconfig-instancerole): {{String}}
  [PlacementStrategy](#cfn-emr-cluster-placementgroupconfig-placementstrategy): {{String}}
```

## Properties
<a name="aws-properties-emr-cluster-placementgroupconfig-properties"></a>

`InstanceRole`  <a name="cfn-emr-cluster-placementgroupconfig-instancerole"></a>
Role of the instance in the cluster.
Starting with Amazon EMR release 5.23.0, the only supported instance role is `MASTER`.
*Required*: Yes
*Type*: String
*Allowed values*: `MASTER | CORE | TASK`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlacementStrategy`  <a name="cfn-emr-cluster-placementgroupconfig-placementstrategy"></a>
Amazon EC2 Placement Group strategy associated with instance role.
Starting with Amazon EMR release 5.23.0, the only supported placement strategy is `SPREAD` for the `MASTER` instance role.
*Required*: No
*Type*: String
*Allowed values*: `SPREAD | PARTITION | CLUSTER | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
