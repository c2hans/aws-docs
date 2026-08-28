---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-jobdefinition-multinodeecsproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::JobDefinition MultiNodeEcsProperties
<a name="aws-properties-batch-jobdefinition-multinodeecsproperties"></a>

An object that contains the properties for the Amazon ECS resources of a job.

## Syntax
<a name="aws-properties-batch-jobdefinition-multinodeecsproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-jobdefinition-multinodeecsproperties-syntax.json"></a>

```
{
  "[TaskProperties](#cfn-batch-jobdefinition-multinodeecsproperties-taskproperties)" : {{[ MultiNodeEcsTaskProperties, ... ]}}
}
```

### YAML
<a name="aws-properties-batch-jobdefinition-multinodeecsproperties-syntax.yaml"></a>

```
  [TaskProperties](#cfn-batch-jobdefinition-multinodeecsproperties-taskproperties): {{
    - MultiNodeEcsTaskProperties}}
```

## Properties
<a name="aws-properties-batch-jobdefinition-multinodeecsproperties-properties"></a>

`TaskProperties`  <a name="cfn-batch-jobdefinition-multinodeecsproperties-taskproperties"></a>
An object that contains the properties for the Amazon ECS task definition of a job.
This object is currently limited to one task element. However, the task element can run up to 10 containers.
*Required*: Yes
*Type*: Array of [MultiNodeEcsTaskProperties](aws-properties-batch-jobdefinition-multinodeecstaskproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
