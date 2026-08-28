---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-placementstrategy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule PlacementStrategy
<a name="aws-properties-scheduler-schedule-placementstrategy"></a>

The task placement strategy for a task or service.

## Syntax
<a name="aws-properties-scheduler-schedule-placementstrategy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-placementstrategy-syntax.json"></a>

```
{
  "[Field](#cfn-scheduler-schedule-placementstrategy-field)" : {{String}},
  "[Type](#cfn-scheduler-schedule-placementstrategy-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-placementstrategy-syntax.yaml"></a>

```
  [Field](#cfn-scheduler-schedule-placementstrategy-field): {{String}}
  [Type](#cfn-scheduler-schedule-placementstrategy-type): {{String}}
```

## Properties
<a name="aws-properties-scheduler-schedule-placementstrategy-properties"></a>

`Field`  <a name="cfn-scheduler-schedule-placementstrategy-field"></a>
The field to apply the placement strategy against. For the spread placement strategy, valid values are `instanceId` (or `instanceId`, which has the same effect), or any platform or custom attribute that is applied to a container instance, such as `attribute:ecs.availability-zone`. For the binpack placement strategy, valid values are `cpu` and `memory`. For the random placement strategy, this field is not used.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-scheduler-schedule-placementstrategy-type"></a>
The type of placement strategy. The random placement strategy randomly places tasks on available candidates. The spread placement strategy spreads placement across available candidates evenly based on the field parameter. The binpack strategy places tasks on available candidates that have the least available amount of the resource that is specified with the field parameter. For example, if you binpack on memory, a task is placed on the instance with the least amount of remaining memory (but still enough to run the task).
*Required*: No
*Type*: String
*Allowed values*: `random | spread | binpack`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
