---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-documentclassifierendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::DocumentClassifierEndpoint
<a name="aws-resource-comprehend-documentclassifierendpoint"></a>

<a name="aws-resource-comprehend-documentclassifierendpoint-description"></a>The `AWS::Comprehend::DocumentClassifierEndpoint` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-documentclassifierendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-documentclassifierendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::DocumentClassifierEndpoint",
  "Properties" : {
      "[DesiredInferenceUnits](#cfn-comprehend-documentclassifierendpoint-desiredinferenceunits)" : {{Integer}},
      "[EndpointName](#cfn-comprehend-documentclassifierendpoint-endpointname)" : {{String}},
      "[ModelArn](#cfn-comprehend-documentclassifierendpoint-modelarn)" : {{String}},
      "[Tags](#cfn-comprehend-documentclassifierendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-documentclassifierendpoint-syntax.yaml"></a>

```
Type: AWS::Comprehend::DocumentClassifierEndpoint
Properties:
  [DesiredInferenceUnits](#cfn-comprehend-documentclassifierendpoint-desiredinferenceunits): {{Integer}}
  [EndpointName](#cfn-comprehend-documentclassifierendpoint-endpointname): {{String}}
  [ModelArn](#cfn-comprehend-documentclassifierendpoint-modelarn): {{String}}
  [Tags](#cfn-comprehend-documentclassifierendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-comprehend-documentclassifierendpoint-properties"></a>

`DesiredInferenceUnits`  <a name="cfn-comprehend-documentclassifierendpoint-desiredinferenceunits"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-comprehend-documentclassifierendpoint-endpointname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelArn`  <a name="cfn-comprehend-documentclassifierendpoint-modelarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:document-classifier/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-comprehend-documentclassifierendpoint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-documentclassifierendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-comprehend-documentclassifierendpoint-return-values"></a>

### Ref
<a name="aws-resource-comprehend-documentclassifierendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-documentclassifierendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-documentclassifierendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`CurrentInferenceUnits`  <a name="CurrentInferenceUnits-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Property description not available.
