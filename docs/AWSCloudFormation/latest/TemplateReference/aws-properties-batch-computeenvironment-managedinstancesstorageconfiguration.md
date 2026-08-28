---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment ManagedInstancesStorageConfiguration
<a name="aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration"></a>

The storage configuration for Amazon ECS Managed Instances.

## Syntax
<a name="aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration-syntax.json"></a>

```
{
  "[StorageSizeGiB](#cfn-batch-computeenvironment-managedinstancesstorageconfiguration-storagesizegib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration-syntax.yaml"></a>

```
  [StorageSizeGiB](#cfn-batch-computeenvironment-managedinstancesstorageconfiguration-storagesizegib): {{Integer}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-managedinstancesstorageconfiguration-properties"></a>

`StorageSizeGiB`  <a name="cfn-batch-computeenvironment-managedinstancesstorageconfiguration-storagesizegib"></a>
The size of the root EBS volume in GiB for the managed instances.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
