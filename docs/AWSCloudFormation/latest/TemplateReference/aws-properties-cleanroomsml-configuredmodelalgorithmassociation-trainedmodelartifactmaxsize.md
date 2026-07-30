---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation TrainedModelArtifactMaxSize
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize"></a>

Specifies the maximum size limit for trained model artifacts. This configuration helps control storage costs and ensures that trained models don't exceed specified size constraints. The size limit applies to the total size of all artifacts produced by the training job.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-syntax.json"></a>

```
{
  "[Unit](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-unit)" : {{String}},
  "[Value](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-syntax.yaml"></a>

```
  [Unit](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-unit): {{String}}
  [Value](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-value): {{Number}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-properties"></a>

`Unit`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-unit"></a>
The unit of measurement for the maximum artifact size. Valid values include common storage units such as bytes, kilobytes, megabytes, gigabytes, and terabytes.
*Required*: Yes
*Type*: String
*Allowed values*: `GB`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelartifactmaxsize-value"></a>
The numerical value for the maximum artifact size limit. This value is interpreted according to the specified unit.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
