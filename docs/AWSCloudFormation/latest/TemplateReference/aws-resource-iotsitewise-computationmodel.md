---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-computationmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::ComputationModel
<a name="aws-resource-iotsitewise-computationmodel"></a>

Create a computation model with a configuration and data binding.

## Syntax
<a name="aws-resource-iotsitewise-computationmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-computationmodel-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::ComputationModel",
  "Properties" : {
      "[ComputationModelConfiguration](#cfn-iotsitewise-computationmodel-computationmodelconfiguration)" : {{ComputationModelConfiguration}},
      "[ComputationModelDataBinding](#cfn-iotsitewise-computationmodel-computationmodeldatabinding)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ComputationModelDescription](#cfn-iotsitewise-computationmodel-computationmodeldescription)" : {{String}},
      "[ComputationModelName](#cfn-iotsitewise-computationmodel-computationmodelname)" : {{String}},
      "[Tags](#cfn-iotsitewise-computationmodel-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-computationmodel-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::ComputationModel
Properties:
  [ComputationModelConfiguration](#cfn-iotsitewise-computationmodel-computationmodelconfiguration): {{
    ComputationModelConfiguration}}
  [ComputationModelDataBinding](#cfn-iotsitewise-computationmodel-computationmodeldatabinding): {{
    {{Key}}: {{Value}}}}
  [ComputationModelDescription](#cfn-iotsitewise-computationmodel-computationmodeldescription): {{String}}
  [ComputationModelName](#cfn-iotsitewise-computationmodel-computationmodelname): {{String}}
  [Tags](#cfn-iotsitewise-computationmodel-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotsitewise-computationmodel-properties"></a>

`ComputationModelConfiguration`  <a name="cfn-iotsitewise-computationmodel-computationmodelconfiguration"></a>
The configuration for the computation model.
*Required*: Yes
*Type*: [ComputationModelConfiguration](aws-properties-iotsitewise-computationmodel-computationmodelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationModelDataBinding`  <a name="cfn-iotsitewise-computationmodel-computationmodeldatabinding"></a>
The data binding for the computation model. Key is a variable name defined in configuration. Value is a `ComputationModelDataBindingValue` referenced by the variable.
*Required*: Yes
*Type*: Object of [ComputationModelDataBindingValue](aws-properties-iotsitewise-computationmodel-computationmodeldatabindingvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationModelDescription`  <a name="cfn-iotsitewise-computationmodel-computationmodeldescription"></a>
The description of the computation model.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _\-#$*!@]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComputationModelName`  <a name="cfn-iotsitewise-computationmodel-computationmodelname"></a>
The name of the computation model.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9 _\-#$*!@]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotsitewise-computationmodel-tags"></a>
A list of key-value pairs that contain metadata for the asset. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-computationmodel-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotsitewise-computationmodel-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-computationmodel-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ComputationModelId`.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-computationmodel-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-computationmodel-return-values-fn--getatt-fn--getatt"></a>

`ComputationModelArn`  <a name="ComputationModelArn-fn::getatt"></a>
The ARN of the computation model, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:computation-model/${ComputationModelId}`
For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`ComputationModelId`  <a name="ComputationModelId-fn::getatt"></a>
The ID of the computation model.
For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
