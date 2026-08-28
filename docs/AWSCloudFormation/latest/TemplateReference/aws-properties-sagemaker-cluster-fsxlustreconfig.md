---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-fsxlustreconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster FSxLustreConfig
<a name="aws-properties-sagemaker-cluster-fsxlustreconfig"></a>

Configuration settings for an Amazon FSx for Lustre file system to be used with the cluster.

## Syntax
<a name="aws-properties-sagemaker-cluster-fsxlustreconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-fsxlustreconfig-syntax.json"></a>

```
{
  "[PerUnitStorageThroughput](#cfn-sagemaker-cluster-fsxlustreconfig-perunitstoragethroughput)" : {{Integer}},
  "[SizeInGiB](#cfn-sagemaker-cluster-fsxlustreconfig-sizeingib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-fsxlustreconfig-syntax.yaml"></a>

```
  [PerUnitStorageThroughput](#cfn-sagemaker-cluster-fsxlustreconfig-perunitstoragethroughput): {{Integer}}
  [SizeInGiB](#cfn-sagemaker-cluster-fsxlustreconfig-sizeingib): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-fsxlustreconfig-properties"></a>

`PerUnitStorageThroughput`  <a name="cfn-sagemaker-cluster-fsxlustreconfig-perunitstoragethroughput"></a>
The throughput capacity of the Amazon FSx for Lustre file system, measured in MB/s per TiB of storage.
*Required*: Yes
*Type*: Integer
*Minimum*: `125`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeInGiB`  <a name="cfn-sagemaker-cluster-fsxlustreconfig-sizeingib"></a>
The storage capacity of the Amazon FSx for Lustre file system, specified in gibibytes (GiB).
*Required*: Yes
*Type*: Integer
*Minimum*: `1200`
*Maximum*: `100800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
