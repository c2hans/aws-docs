---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-schedulingpolicy-quotasharepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::SchedulingPolicy QuotaSharePolicy
<a name="aws-properties-batch-schedulingpolicy-quotasharepolicy"></a>

The quota share scheduling policy details for a job queue.

## Syntax
<a name="aws-properties-batch-schedulingpolicy-quotasharepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-schedulingpolicy-quotasharepolicy-syntax.json"></a>

```
{
  "[IdleResourceAssignmentStrategy](#cfn-batch-schedulingpolicy-quotasharepolicy-idleresourceassignmentstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-schedulingpolicy-quotasharepolicy-syntax.yaml"></a>

```
  [IdleResourceAssignmentStrategy](#cfn-batch-schedulingpolicy-quotasharepolicy-idleresourceassignmentstrategy): {{String}}
```

## Properties
<a name="aws-properties-batch-schedulingpolicy-quotasharepolicy-properties"></a>

`IdleResourceAssignmentStrategy`  <a name="cfn-batch-schedulingpolicy-quotasharepolicy-idleresourceassignmentstrategy"></a>
The strategy that determines how idle resources are assigned to quota shares that are borrowing capacity. Currently, only `FIFO` is supported.
*Required*: No
*Type*: String
*Allowed values*: `FIFO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
