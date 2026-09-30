---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-comprehend-entityrecognizerendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizerEndpoint
<a name="aws-resource-comprehend-entityrecognizerendpoint"></a>

<a name="aws-resource-comprehend-entityrecognizerendpoint-description"></a>The `AWS::Comprehend::EntityRecognizerEndpoint` resource Property description not available. for Comprehend.

## Syntax
<a name="aws-resource-comprehend-entityrecognizerendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-comprehend-entityrecognizerendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::Comprehend::EntityRecognizerEndpoint",
  "Properties" : {
      "[DataAccessRoleArn](#cfn-comprehend-entityrecognizerendpoint-dataaccessrolearn)" : {{String}},
      "[DesiredInferenceUnits](#cfn-comprehend-entityrecognizerendpoint-desiredinferenceunits)" : {{Integer}},
      "[EndpointName](#cfn-comprehend-entityrecognizerendpoint-endpointname)" : {{String}},
      "[FlywheelArn](#cfn-comprehend-entityrecognizerendpoint-flywheelarn)" : {{String}},
      "[ModelArn](#cfn-comprehend-entityrecognizerendpoint-modelarn)" : {{String}},
      "[Tags](#cfn-comprehend-entityrecognizerendpoint-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-comprehend-entityrecognizerendpoint-syntax.yaml"></a>

```
Type: AWS::Comprehend::EntityRecognizerEndpoint
Properties:
  [DataAccessRoleArn](#cfn-comprehend-entityrecognizerendpoint-dataaccessrolearn): {{String}}
  [DesiredInferenceUnits](#cfn-comprehend-entityrecognizerendpoint-desiredinferenceunits): {{Integer}}
  [EndpointName](#cfn-comprehend-entityrecognizerendpoint-endpointname): {{String}}
  [FlywheelArn](#cfn-comprehend-entityrecognizerendpoint-flywheelarn): {{String}}
  [ModelArn](#cfn-comprehend-entityrecognizerendpoint-modelarn): {{String}}
  [Tags](#cfn-comprehend-entityrecognizerendpoint-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-comprehend-entityrecognizerendpoint-properties"></a>

`DataAccessRoleArn`  <a name="cfn-comprehend-entityrecognizerendpoint-dataaccessrolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesiredInferenceUnits`  <a name="cfn-comprehend-entityrecognizerendpoint-desiredinferenceunits"></a>
Property description not available.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-comprehend-entityrecognizerendpoint-endpointname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FlywheelArn`  <a name="cfn-comprehend-entityrecognizerendpoint-flywheelarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelArn`  <a name="cfn-comprehend-entityrecognizerendpoint-modelarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:entity-recognizer/[a-zA-Z0-9](-*[a-zA-Z0-9])*(/version/[a-zA-Z0-9](-*[a-zA-Z0-9])*)?$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-comprehend-entityrecognizerendpoint-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-comprehend-entityrecognizerendpoint-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-comprehend-entityrecognizerendpoint-return-values"></a>

### Ref
<a name="aws-resource-comprehend-entityrecognizerendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-comprehend-entityrecognizerendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-comprehend-entityrecognizerendpoint-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`CurrentInferenceUnits`  <a name="CurrentInferenceUnits-fn::getatt"></a>
Property description not available.

`EndpointStatus`  <a name="EndpointStatus-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Property description not available.
