---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-index.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Index
<a name="aws-resource-iot-index"></a>

<a name="aws-resource-iot-index-description"></a>The `AWS::IoT::Index` resource Property description not available. for IoT.

## Syntax
<a name="aws-resource-iot-index-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iot-index-syntax.json"></a>

```
{
  "Type" : "AWS::IoT::Index",
  "Properties" : {
      "[IndexName](#cfn-iot-index-indexname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-iot-index-syntax.yaml"></a>

```
Type: AWS::IoT::Index
Properties:
  [IndexName](#cfn-iot-index-indexname): {{String}}
```

## Properties
<a name="aws-resource-iot-index-properties"></a>

`IndexName`  <a name="cfn-iot-index-indexname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iot-index-return-values"></a>

### Ref
<a name="aws-resource-iot-index-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iot-index-return-values-fn--getatt"></a>

####
<a name="aws-resource-iot-index-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`IndexStatus`  <a name="IndexStatus-fn::getatt"></a>
Property description not available.

`Schema`  <a name="Schema-fn::getatt"></a>
Property description not available.
