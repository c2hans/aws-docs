---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-scheduler.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster Scheduler
<a name="aws-properties-pcs-cluster-scheduler"></a>

The cluster management and job scheduling software associated with the cluster.

## Syntax
<a name="aws-properties-pcs-cluster-scheduler-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-scheduler-syntax.json"></a>

```
{
  "[Type](#cfn-pcs-cluster-scheduler-type)" : {{String}},
  "[Version](#cfn-pcs-cluster-scheduler-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-scheduler-syntax.yaml"></a>

```
  [Type](#cfn-pcs-cluster-scheduler-type): {{String}}
  [Version](#cfn-pcs-cluster-scheduler-version): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-scheduler-properties"></a>

`Type`  <a name="cfn-pcs-cluster-scheduler-type"></a>
The software AWS PCS uses to manage cluster scaling and job scheduling.
*Required*: Yes
*Type*: String
*Allowed values*: `SLURM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-pcs-cluster-scheduler-version"></a>
The version of the specified scheduling software that AWS PCS uses to manage cluster scaling and job scheduling. You can update this version using the `UpdateCluster` API action. For more information, see [Updating the scheduler version on a cluster](https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_version_update.html) and [Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html) in the *AWS PCS User Guide*.
Valid Values: `23.11 | 24.05 | 24.11 | 25.05 | 25.11`
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
