---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation TrainedModelExportsMaxSize
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize"></a>

The maximum size of the trained model metrics that can be exported. If the trained model metrics dataset is larger than this value, it will not be exported.

## Syntax
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-syntax.json"></a>

```
{
  "[Unit](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-unit)" : {{String}},
  "[Value](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-syntax.yaml"></a>

```
  [Unit](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-unit): {{String}}
  [Value](#cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-value): {{Number}}
```

## Properties
<a name="aws-properties-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-properties"></a>

`Unit`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-unit"></a>
The unit of measurement for the data size.
*Required*: Yes
*Type*: String
*Allowed values*: `GB`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-trainedmodelexportsmaxsize-value"></a>
The maximum size of the dataset to export.
*Required*: Yes
*Type*: Number
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
