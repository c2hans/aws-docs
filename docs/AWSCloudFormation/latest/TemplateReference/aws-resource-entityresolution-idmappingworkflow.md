---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-entityresolution-idmappingworkflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow
<a name="aws-resource-entityresolution-idmappingworkflow"></a>

Creates an `IdMappingWorkflow` object which stores the configuration of the data processing job to be run. Each `IdMappingWorkflow` must have a unique workflow name. To modify an existing workflow, use the UpdateIdMappingWorkflow API.

**Important**
Incremental processing is not supported for ID mapping workflows.

## Syntax
<a name="aws-resource-entityresolution-idmappingworkflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-entityresolution-idmappingworkflow-syntax.json"></a>

```
{
  "Type" : "AWS::EntityResolution::IdMappingWorkflow",
  "Properties" : {
      "[Description](#cfn-entityresolution-idmappingworkflow-description)" : {{String}},
      "[IdMappingIncrementalRunConfig](#cfn-entityresolution-idmappingworkflow-idmappingincrementalrunconfig)" : {{IdMappingIncrementalRunConfig}},
      "[IdMappingTechniques](#cfn-entityresolution-idmappingworkflow-idmappingtechniques)" : {{IdMappingTechniques}},
      "[InputSourceConfig](#cfn-entityresolution-idmappingworkflow-inputsourceconfig)" : {{[ IdMappingWorkflowInputSource, ... ]}},
      "[OutputSourceConfig](#cfn-entityresolution-idmappingworkflow-outputsourceconfig)" : {{[ IdMappingWorkflowOutputSource, ... ]}},
      "[RoleArn](#cfn-entityresolution-idmappingworkflow-rolearn)" : {{String}},
      "[Tags](#cfn-entityresolution-idmappingworkflow-tags)" : {{[ Tag, ... ]}},
      "[WorkflowName](#cfn-entityresolution-idmappingworkflow-workflowname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-entityresolution-idmappingworkflow-syntax.yaml"></a>

```
Type: AWS::EntityResolution::IdMappingWorkflow
Properties:
  [Description](#cfn-entityresolution-idmappingworkflow-description): {{String}}
  [IdMappingIncrementalRunConfig](#cfn-entityresolution-idmappingworkflow-idmappingincrementalrunconfig): {{
    IdMappingIncrementalRunConfig}}
  [IdMappingTechniques](#cfn-entityresolution-idmappingworkflow-idmappingtechniques): {{
    IdMappingTechniques}}
  [InputSourceConfig](#cfn-entityresolution-idmappingworkflow-inputsourceconfig): {{
    - IdMappingWorkflowInputSource}}
  [OutputSourceConfig](#cfn-entityresolution-idmappingworkflow-outputsourceconfig): {{
    - IdMappingWorkflowOutputSource}}
  [RoleArn](#cfn-entityresolution-idmappingworkflow-rolearn): {{String}}
  [Tags](#cfn-entityresolution-idmappingworkflow-tags): {{
    - Tag}}
  [WorkflowName](#cfn-entityresolution-idmappingworkflow-workflowname): {{String}}
```

## Properties
<a name="aws-resource-entityresolution-idmappingworkflow-properties"></a>

`Description`  <a name="cfn-entityresolution-idmappingworkflow-description"></a>
A description of the workflow.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdMappingIncrementalRunConfig`  <a name="cfn-entityresolution-idmappingworkflow-idmappingincrementalrunconfig"></a>
 The incremental run configuration for the ID mapping workflow.
*Required*: No
*Type*: [IdMappingIncrementalRunConfig](aws-properties-entityresolution-idmappingworkflow-idmappingincrementalrunconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdMappingTechniques`  <a name="cfn-entityresolution-idmappingworkflow-idmappingtechniques"></a>
An object which defines the ID mapping technique and any additional configurations.
*Required*: Yes
*Type*: [IdMappingTechniques](aws-properties-entityresolution-idmappingworkflow-idmappingtechniques.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSourceConfig`  <a name="cfn-entityresolution-idmappingworkflow-inputsourceconfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
*Required*: Yes
*Type*: Array of [IdMappingWorkflowInputSource](aws-properties-entityresolution-idmappingworkflow-idmappingworkflowinputsource.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputSourceConfig`  <a name="cfn-entityresolution-idmappingworkflow-outputsourceconfig"></a>
A list of `IdMappingWorkflowOutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.
*Required*: No
*Type*: Array of [IdMappingWorkflowOutputSource](aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-entityresolution-idmappingworkflow-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-entityresolution-idmappingworkflow-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-entityresolution-idmappingworkflow-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowName`  <a name="cfn-entityresolution-idmappingworkflow-workflowname"></a>
The name of the workflow. There can't be multiple `IdMappingWorkflows` with the same name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_0-9-]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
