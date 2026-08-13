---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionstate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecycleExecution LifecycleExecutionState
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionstate"></a>

The current state of the runtime instance of the lifecycle policy.

## Syntax
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionstate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionstate-syntax.json"></a>

```
{
  "[Status](#cfn-imagebuilder-lifecycleexecution-lifecycleexecutionstate-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionstate-syntax.yaml"></a>

```
  [Status](#cfn-imagebuilder-lifecycleexecution-lifecycleexecutionstate-status): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecycleexecution-lifecycleexecutionstate-properties"></a>

`Status`  <a name="cfn-imagebuilder-lifecycleexecution-lifecycleexecutionstate-status"></a>
The runtime status of the lifecycle execution.
*Required*: No
*Type*: String
*Allowed values*: `IN_PROGRESS | CANCELLED | CANCELLING | FAILED | SUCCESS | PENDING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
