---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-trialcomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrialComponent
<a name="aws-resource-sagemaker-trialcomponent"></a>

The properties of a trial component as returned by the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API.

## Syntax
<a name="aws-resource-sagemaker-trialcomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-trialcomponent-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::TrialComponent",
  "Properties" : {
      "[DisplayName](#cfn-sagemaker-trialcomponent-displayname)" : {{String}},
      "[InputArtifacts](#cfn-sagemaker-trialcomponent-inputartifacts)" : {{{{{Key}}: {{Value}}, ...}}},
      "[MetadataProperties](#cfn-sagemaker-trialcomponent-metadataproperties)" : {{MetadataProperties}},
      "[OutputArtifacts](#cfn-sagemaker-trialcomponent-outputartifacts)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Parameters](#cfn-sagemaker-trialcomponent-parameters)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Status](#cfn-sagemaker-trialcomponent-status)" : {{TrialComponentStatus}},
      "[Tags](#cfn-sagemaker-trialcomponent-tags)" : {{[ TagsItems, ... ]}},
      "[TrialComponentName](#cfn-sagemaker-trialcomponent-trialcomponentname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-trialcomponent-syntax.yaml"></a>

```
Type: AWS::SageMaker::TrialComponent
Properties:
  [DisplayName](#cfn-sagemaker-trialcomponent-displayname): {{String}}
  [InputArtifacts](#cfn-sagemaker-trialcomponent-inputartifacts): {{
    {{Key}}: {{Value}}}}
  [MetadataProperties](#cfn-sagemaker-trialcomponent-metadataproperties): {{
    MetadataProperties}}
  [OutputArtifacts](#cfn-sagemaker-trialcomponent-outputartifacts): {{
    {{Key}}: {{Value}}}}
  [Parameters](#cfn-sagemaker-trialcomponent-parameters): {{
    {{Key}}: {{Value}}}}
  [Status](#cfn-sagemaker-trialcomponent-status): {{
    TrialComponentStatus}}
  [Tags](#cfn-sagemaker-trialcomponent-tags): {{
    - TagsItems}}
  [TrialComponentName](#cfn-sagemaker-trialcomponent-trialcomponentname): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-trialcomponent-properties"></a>

`DisplayName`  <a name="cfn-sagemaker-trialcomponent-displayname"></a>
The name of the component as displayed. If `DisplayName` isn't specified, `TrialComponentName` is displayed.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputArtifacts`  <a name="cfn-sagemaker-trialcomponent-inputartifacts"></a>
The input artifacts of the component.
*Required*: No
*Type*: Object of [TrialComponentArtifact](aws-properties-sagemaker-trialcomponent-trialcomponentartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataProperties`  <a name="cfn-sagemaker-trialcomponent-metadataproperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
*Required*: No
*Type*: [MetadataProperties](aws-properties-sagemaker-trialcomponent-metadataproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputArtifacts`  <a name="cfn-sagemaker-trialcomponent-outputartifacts"></a>
The output artifacts of the component.
*Required*: No
*Type*: Object of [TrialComponentArtifact](aws-properties-sagemaker-trialcomponent-trialcomponentartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-sagemaker-trialcomponent-parameters"></a>
The hyperparameters of the component.
*Required*: No
*Type*: Object of [TrialComponentParameterValue](aws-properties-sagemaker-trialcomponent-trialcomponentparametervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-sagemaker-trialcomponent-status"></a>
The status of the component. States include:
+ InProgress
+ Completed
+ Failed
*Required*: No
*Type*: [TrialComponentStatus](aws-properties-sagemaker-trialcomponent-trialcomponentstatus.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-trialcomponent-tags"></a>
The list of tags that are associated with the component. You can use [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API to search on the tags.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-sagemaker-trialcomponent-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrialComponentName`  <a name="cfn-sagemaker-trialcomponent-trialcomponentname"></a>
The name of the trial component.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-trialcomponent-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-trialcomponent-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-trialcomponent-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-trialcomponent-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
When the component was created.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
When the component was last modified.

`LineageGroupArn`  <a name="LineageGroupArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the lineage group resource.

`TrialComponentArn`  <a name="TrialComponentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the trial component.
