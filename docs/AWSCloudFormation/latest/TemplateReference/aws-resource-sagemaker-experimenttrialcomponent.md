---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-experimenttrialcomponent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ExperimentTrialComponent
<a name="aws-resource-sagemaker-experimenttrialcomponent"></a>

<a name="aws-resource-sagemaker-experimenttrialcomponent-description"></a>The `AWS::SageMaker::ExperimentTrialComponent` resource Property description not available. for SageMaker.

## Syntax
<a name="aws-resource-sagemaker-experimenttrialcomponent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-experimenttrialcomponent-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::ExperimentTrialComponent",
  "Properties" : {
      "[DisplayName](#cfn-sagemaker-experimenttrialcomponent-displayname)" : {{String}},
      "[EndTime](#cfn-sagemaker-experimenttrialcomponent-endtime)" : {{String}},
      "[MetadataProperties](#cfn-sagemaker-experimenttrialcomponent-metadataproperties)" : {{MetadataProperties}},
      "[StartTime](#cfn-sagemaker-experimenttrialcomponent-starttime)" : {{String}},
      "[Status](#cfn-sagemaker-experimenttrialcomponent-status)" : {{Status}},
      "[Tags](#cfn-sagemaker-experimenttrialcomponent-tags)" : {{[ TagsItems, ... ]}},
      "[TrialComponentName](#cfn-sagemaker-experimenttrialcomponent-trialcomponentname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-experimenttrialcomponent-syntax.yaml"></a>

```
Type: AWS::SageMaker::ExperimentTrialComponent
Properties:
  [DisplayName](#cfn-sagemaker-experimenttrialcomponent-displayname): {{String}}
  [EndTime](#cfn-sagemaker-experimenttrialcomponent-endtime): {{String}}
  [MetadataProperties](#cfn-sagemaker-experimenttrialcomponent-metadataproperties): {{
    MetadataProperties}}
  [StartTime](#cfn-sagemaker-experimenttrialcomponent-starttime): {{String}}
  [Status](#cfn-sagemaker-experimenttrialcomponent-status): {{
    Status}}
  [Tags](#cfn-sagemaker-experimenttrialcomponent-tags): {{
    - TagsItems}}
  [TrialComponentName](#cfn-sagemaker-experimenttrialcomponent-trialcomponentname): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-experimenttrialcomponent-properties"></a>

`DisplayName`  <a name="cfn-sagemaker-experimenttrialcomponent-displayname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndTime`  <a name="cfn-sagemaker-experimenttrialcomponent-endtime"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataProperties`  <a name="cfn-sagemaker-experimenttrialcomponent-metadataproperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
*Required*: No
*Type*: [MetadataProperties](aws-properties-sagemaker-experimenttrialcomponent-metadataproperties.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartTime`  <a name="cfn-sagemaker-experimenttrialcomponent-starttime"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-sagemaker-experimenttrialcomponent-status"></a>
Property description not available.
*Required*: No
*Type*: [Status](aws-properties-sagemaker-experimenttrialcomponent-status.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-experimenttrialcomponent-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-sagemaker-experimenttrialcomponent-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrialComponentName`  <a name="cfn-sagemaker-experimenttrialcomponent-trialcomponentname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}$`
*Minimum*: `1`
*Maximum*: `120`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-experimenttrialcomponent-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-experimenttrialcomponent-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-experimenttrialcomponent-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-experimenttrialcomponent-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Property description not available.

`LineageGroupArn`  <a name="LineageGroupArn-fn::getatt"></a>
Property description not available.
