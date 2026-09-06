---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stackset-managedexecution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet ManagedExecution
<a name="aws-properties-cloudformation-stackset-managedexecution"></a>

Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.

## Syntax
<a name="aws-properties-cloudformation-stackset-managedexecution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stackset-managedexecution-syntax.json"></a>

```
{
  "[Active](#cfn-cloudformation-stackset-managedexecution-active)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cloudformation-stackset-managedexecution-syntax.yaml"></a>

```
  [Active](#cfn-cloudformation-stackset-managedexecution-active): {{Boolean}}
```

## Properties
<a name="aws-properties-cloudformation-stackset-managedexecution-properties"></a>

`Active`  <a name="cfn-cloudformation-stackset-managedexecution-active"></a>
When `true`, CloudFormation performs non-conflicting operations concurrently and queues conflicting operations. After conflicting operations finish, CloudFormation starts queued operations in request order.
If there are already running or queued operations, CloudFormation queues all incoming operations even if they are non-conflicting.
You can't modify your StackSet's execution configuration while there are running or queued operations for that StackSet.
When `false` (default), StackSets performs one operation at a time in request order.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
