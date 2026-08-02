---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-entityresolution-matchingworkflow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow
<a name="aws-resource-entityresolution-matchingworkflow"></a>

Creates a matching workflow that defines the configuration for a data processing job. The workflow name must be unique. To modify an existing workflow, use `UpdateMatchingWorkflow`.

**Important**
For workflows where `resolutionType` is `PROVIDER`, incremental processing is not supported.

## Syntax
<a name="aws-resource-entityresolution-matchingworkflow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-entityresolution-matchingworkflow-syntax.json"></a>

```
{
  "Type" : "AWS::EntityResolution::MatchingWorkflow",
  "Properties" : {
      "[Description](#cfn-entityresolution-matchingworkflow-description)" : {{String}},
      "[IncrementalRunConfig](#cfn-entityresolution-matchingworkflow-incrementalrunconfig)" : {{IncrementalRunConfig}},
      "[InputSourceConfig](#cfn-entityresolution-matchingworkflow-inputsourceconfig)" : {{[ InputSource, ... ]}},
      "[OutputSourceConfig](#cfn-entityresolution-matchingworkflow-outputsourceconfig)" : {{[ OutputSource, ... ]}},
      "[ResolutionTechniques](#cfn-entityresolution-matchingworkflow-resolutiontechniques)" : {{ResolutionTechniques}},
      "[RoleArn](#cfn-entityresolution-matchingworkflow-rolearn)" : {{String}},
      "[Tags](#cfn-entityresolution-matchingworkflow-tags)" : {{[ Tag, ... ]}},
      "[WorkflowName](#cfn-entityresolution-matchingworkflow-workflowname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-entityresolution-matchingworkflow-syntax.yaml"></a>

```
Type: AWS::EntityResolution::MatchingWorkflow
Properties:
  [Description](#cfn-entityresolution-matchingworkflow-description): {{String}}
  [IncrementalRunConfig](#cfn-entityresolution-matchingworkflow-incrementalrunconfig): {{
    IncrementalRunConfig}}
  [InputSourceConfig](#cfn-entityresolution-matchingworkflow-inputsourceconfig): {{
    - InputSource}}
  [OutputSourceConfig](#cfn-entityresolution-matchingworkflow-outputsourceconfig): {{
    - OutputSource}}
  [ResolutionTechniques](#cfn-entityresolution-matchingworkflow-resolutiontechniques): {{
    ResolutionTechniques}}
  [RoleArn](#cfn-entityresolution-matchingworkflow-rolearn): {{String}}
  [Tags](#cfn-entityresolution-matchingworkflow-tags): {{
    - Tag}}
  [WorkflowName](#cfn-entityresolution-matchingworkflow-workflowname): {{String}}
```

## Properties
<a name="aws-resource-entityresolution-matchingworkflow-properties"></a>

`Description`  <a name="cfn-entityresolution-matchingworkflow-description"></a>
A description of the workflow.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncrementalRunConfig`  <a name="cfn-entityresolution-matchingworkflow-incrementalrunconfig"></a>
Optional. An object that defines the incremental run type. This object contains only the `incrementalRunType` field, which appears as "Automatic" in the console.
For workflows where `resolutionType` is `PROVIDER`, incremental processing is not supported.
*Required*: No
*Type*: [IncrementalRunConfig](aws-properties-entityresolution-matchingworkflow-incrementalrunconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputSourceConfig`  <a name="cfn-entityresolution-matchingworkflow-inputsourceconfig"></a>
A list of `InputSource` objects, which have the fields `InputSourceARN` and `SchemaName`.
*Required*: Yes
*Type*: Array of [InputSource](aws-properties-entityresolution-matchingworkflow-inputsource.md)
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputSourceConfig`  <a name="cfn-entityresolution-matchingworkflow-outputsourceconfig"></a>
A list of `OutputSource` objects, each of which contains fields `outputS3Path`, `applyNormalization`, `KMSArn`, and `output`.
*Required*: Yes
*Type*: Array of [OutputSource](aws-properties-entityresolution-matchingworkflow-outputsource.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResolutionTechniques`  <a name="cfn-entityresolution-matchingworkflow-resolutiontechniques"></a>
An object which defines the `resolutionType` and the `ruleBasedProperties`.
*Required*: Yes
*Type*: [ResolutionTechniques](aws-properties-entityresolution-matchingworkflow-resolutiontechniques.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-entityresolution-matchingworkflow-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-entityresolution-matchingworkflow-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-entityresolution-matchingworkflow-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowName`  <a name="cfn-entityresolution-matchingworkflow-workflowname"></a>
The name of the workflow. There can't be multiple `MatchingWorkflows` with the same name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_0-9-]*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
