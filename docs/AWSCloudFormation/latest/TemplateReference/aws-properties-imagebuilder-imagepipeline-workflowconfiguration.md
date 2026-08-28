---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-workflowconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline WorkflowConfiguration
<a name="aws-properties-imagebuilder-imagepipeline-workflowconfiguration"></a>

Contains control settings and configurable inputs for a workflow resource.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-workflowconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-workflowconfiguration-syntax.json"></a>

```
{
  "[OnFailure](#cfn-imagebuilder-imagepipeline-workflowconfiguration-onfailure)" : {{String}},
  "[ParallelGroup](#cfn-imagebuilder-imagepipeline-workflowconfiguration-parallelgroup)" : {{String}},
  "[Parameters](#cfn-imagebuilder-imagepipeline-workflowconfiguration-parameters)" : {{[ WorkflowParameter, ... ]}},
  "[WorkflowArn](#cfn-imagebuilder-imagepipeline-workflowconfiguration-workflowarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-workflowconfiguration-syntax.yaml"></a>

```
  [OnFailure](#cfn-imagebuilder-imagepipeline-workflowconfiguration-onfailure): {{String}}
  [ParallelGroup](#cfn-imagebuilder-imagepipeline-workflowconfiguration-parallelgroup): {{String}}
  [Parameters](#cfn-imagebuilder-imagepipeline-workflowconfiguration-parameters): {{
    - WorkflowParameter}}
  [WorkflowArn](#cfn-imagebuilder-imagepipeline-workflowconfiguration-workflowarn): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-workflowconfiguration-properties"></a>

`OnFailure`  <a name="cfn-imagebuilder-imagepipeline-workflowconfiguration-onfailure"></a>
The action to take if the workflow fails.
*Required*: No
*Type*: String
*Allowed values*: `CONTINUE | ABORT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParallelGroup`  <a name="cfn-imagebuilder-imagepipeline-workflowconfiguration-parallelgroup"></a>
Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9-_+#]{0,99}$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-imagebuilder-imagepipeline-workflowconfiguration-parameters"></a>
Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.
*Required*: No
*Type*: Array of [WorkflowParameter](aws-properties-imagebuilder-imagepipeline-workflowparameter.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowArn`  <a name="cfn-imagebuilder-imagepipeline-workflowconfiguration-workflowarn"></a>
The Amazon Resource Name (ARN) of the workflow resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
