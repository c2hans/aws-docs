---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trialcomponent-trialcomponentartifact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrialComponent TrialComponentArtifact
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentartifact"></a>

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

## Syntax
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentartifact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentartifact-syntax.json"></a>

```
{
  "[MediaType](#cfn-sagemaker-trialcomponent-trialcomponentartifact-mediatype)" : {{String}},
  "[Value](#cfn-sagemaker-trialcomponent-trialcomponentartifact-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentartifact-syntax.yaml"></a>

```
  [MediaType](#cfn-sagemaker-trialcomponent-trialcomponentartifact-mediatype): {{String}}
  [Value](#cfn-sagemaker-trialcomponent-trialcomponentartifact-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trialcomponent-trialcomponentartifact-properties"></a>

`MediaType`  <a name="cfn-sagemaker-trialcomponent-trialcomponentartifact-mediatype"></a>
The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.
*Required*: No
*Type*: String
*Pattern*: `^[-\w]+\/[-\w+]+$`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-sagemaker-trialcomponent-trialcomponentartifact-value"></a>
The location of the artifact.
*Required*: Yes
*Type*: String
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
