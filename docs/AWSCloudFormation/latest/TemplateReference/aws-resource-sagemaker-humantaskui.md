---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-humantaskui.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HumanTaskUi
<a name="aws-resource-sagemaker-humantaskui"></a>

Defines the settings you will use for the human review workflow user interface. Reviewers will see a three-panel interface with an instruction area, the item to review, and an input area.

## Syntax
<a name="aws-resource-sagemaker-humantaskui-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-humantaskui-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::HumanTaskUi",
  "Properties" : {
      "[HumanTaskUiName](#cfn-sagemaker-humantaskui-humantaskuiname)" : {{String}},
      "[Tags](#cfn-sagemaker-humantaskui-tags)" : {{[ Tag, ... ]}},
      "[UiTemplate](#cfn-sagemaker-humantaskui-uitemplate)" : {{UiTemplate}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-humantaskui-syntax.yaml"></a>

```
Type: AWS::SageMaker::HumanTaskUi
Properties:
  [HumanTaskUiName](#cfn-sagemaker-humantaskui-humantaskuiname): {{String}}
  [Tags](#cfn-sagemaker-humantaskui-tags): {{
    - Tag}}
  [UiTemplate](#cfn-sagemaker-humantaskui-uitemplate): {{
    UiTemplate}}
```

## Properties
<a name="aws-resource-sagemaker-humantaskui-properties"></a>

`HumanTaskUiName`  <a name="cfn-sagemaker-humantaskui-humantaskuiname"></a>
The name of the human task user interface.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9](-*[a-z0-9])*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-humantaskui-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-humantaskui-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UiTemplate`  <a name="cfn-sagemaker-humantaskui-uitemplate"></a>
The Liquid template for the worker user interface.
*Required*: No
*Type*: [UiTemplate](aws-properties-sagemaker-humantaskui-uitemplate.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-humantaskui-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-humantaskui-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-humantaskui-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-humantaskui-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A timestamp when SageMaker created the human task user interface.

`HumanTaskUiArn`  <a name="HumanTaskUiArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the human task user interface.
