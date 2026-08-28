---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-taskcontainerdependency.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition TaskContainerDependency
<a name="aws-properties-batch-jobdefinition-taskcontainerdependency"></a>

A list of containers that this task depends on.

## Syntax
<a name="aws-properties-batch-jobdefinition-taskcontainerdependency-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-taskcontainerdependency-syntax.json"></a>

```
{
  "[Condition](#cfn-batch-jobdefinition-taskcontainerdependency-condition)" : {{String}},
  "[ContainerName](#cfn-batch-jobdefinition-taskcontainerdependency-containername)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-taskcontainerdependency-syntax.yaml"></a>

```
  [Condition](#cfn-batch-jobdefinition-taskcontainerdependency-condition): {{String}}
  [ContainerName](#cfn-batch-jobdefinition-taskcontainerdependency-containername): {{String}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-taskcontainerdependency-properties"></a>

`Condition`  <a name="cfn-batch-jobdefinition-taskcontainerdependency-condition"></a>
The dependency condition of the container. The following are the available conditions and their behavior:
+ `START` - This condition emulates the behavior of links and volumes today. It validates that a dependent container is started before permitting other containers to start.
+ `COMPLETE` - This condition validates that a dependent container runs to completion (exits) before permitting other containers to start. This can be useful for nonessential containers that run a script and then exit. This condition can't be set on an essential container.
+ `SUCCESS` - This condition is the same as `COMPLETE`, but it also requires that the container exits with a zero status. This condition can't be set on an essential container.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerName`  <a name="cfn-batch-jobdefinition-taskcontainerdependency-containername"></a>
A unique identifier for the container.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
