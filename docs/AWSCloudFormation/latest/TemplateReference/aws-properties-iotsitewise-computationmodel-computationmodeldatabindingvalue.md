---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::ComputationModel ComputationModelDataBindingValue
<a name="aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue"></a>

Contains computation model data binding value information, which can be one of `assetModelProperty`, `list`.

## Syntax
<a name="aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue-syntax.json"></a>

```
{
  "[AssetModelProperty](#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetmodelproperty)" : {{AssetModelPropertyBindingValue}},
  "[AssetProperty](#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetproperty)" : {{AssetPropertyBindingValue}},
  "[List](#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-list)" : {{[ ComputationModelDataBindingValue, ... ]}}
}
```

### YAML
<a name="aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue-syntax.yaml"></a>

```
  [AssetModelProperty](#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetmodelproperty): {{
    AssetModelPropertyBindingValue}}
  [AssetProperty](#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetproperty): {{
    AssetPropertyBindingValue}}
  [List](#cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-list): {{
    - ComputationModelDataBindingValue}}
```

## Properties
<a name="aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue-properties"></a>

`AssetModelProperty`  <a name="cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetmodelproperty"></a>
Specifies an asset model property data binding value.
*Required*: No
*Type*: [AssetModelPropertyBindingValue](aws-properties-iotsitewise-computationmodel-assetmodelpropertybindingvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AssetProperty`  <a name="cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-assetproperty"></a>
The asset property value used for computation model data binding.
*Required*: No
*Type*: [AssetPropertyBindingValue](aws-properties-iotsitewise-computationmodel-assetpropertybindingvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`List`  <a name="cfn-iotsitewise-computationmodel-computationmodeldatabindingvalue-list"></a>
Specifies a list of data binding value.
*Required*: No
*Type*: Array of [ComputationModelDataBindingValue](#aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
