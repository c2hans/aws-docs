---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-experiment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Experiment
<a name="aws-resource-sagemaker-experiment"></a>

The properties of an experiment as returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API. For information about experiments, see the [CreateExperiment](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateExperiment.html) API.

## Syntax
<a name="aws-resource-sagemaker-experiment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-experiment-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Experiment",
  "Properties" : {
      "[Description](#cfn-sagemaker-experiment-description)" : {{String}},
      "[DisplayName](#cfn-sagemaker-experiment-displayname)" : {{String}},
      "[ExperimentName](#cfn-sagemaker-experiment-experimentname)" : {{String}},
      "[Tags](#cfn-sagemaker-experiment-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-experiment-syntax.yaml"></a>

```
Type: AWS::SageMaker::Experiment
Properties:
  [Description](#cfn-sagemaker-experiment-description): {{String}}
  [DisplayName](#cfn-sagemaker-experiment-displayname): {{String}}
  [ExperimentName](#cfn-sagemaker-experiment-experimentname): {{String}}
  [Tags](#cfn-sagemaker-experiment-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-sagemaker-experiment-properties"></a>

`Description`  <a name="cfn-sagemaker-experiment-description"></a>
The description of the experiment.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `3072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-sagemaker-experiment-displayname"></a>
The name of the experiment as displayed. If `DisplayName` isn't specified, `ExperimentName` is displayed.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExperimentName`  <a name="cfn-sagemaker-experiment-experimentname"></a>
The name of the experiment.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-experiment-tags"></a>
The list of tags that are associated with the experiment. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-sagemaker-experiment-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-experiment-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-experiment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-experiment-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-experiment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the experiment was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the experiment was last modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
