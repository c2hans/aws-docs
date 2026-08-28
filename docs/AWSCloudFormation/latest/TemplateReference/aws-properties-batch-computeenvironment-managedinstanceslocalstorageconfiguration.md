---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment ManagedInstancesLocalStorageConfiguration
<a name="aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration"></a>

The local storage configuration for Amazon ECS Managed Instances.

## Syntax
<a name="aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration-syntax.json"></a>

```
{
  "[UseLocalStorage](#cfn-batch-computeenvironment-managedinstanceslocalstorageconfiguration-uselocalstorage)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration-syntax.yaml"></a>

```
  [UseLocalStorage](#cfn-batch-computeenvironment-managedinstanceslocalstorageconfiguration-uselocalstorage): {{Boolean}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-managedinstanceslocalstorageconfiguration-properties"></a>

`UseLocalStorage`  <a name="cfn-batch-computeenvironment-managedinstanceslocalstorageconfiguration-uselocalstorage"></a>
Specifies whether instance store volumes (local NVMe SSDs) are available to containers. When enabled, containers can use the instance store for high-performance temporary storage.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
