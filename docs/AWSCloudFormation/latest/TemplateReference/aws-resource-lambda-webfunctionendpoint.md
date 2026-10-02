---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint
<a name="aws-resource-lambda-webfunctionendpoint"></a>

<a name="aws-resource-lambda-webfunctionendpoint-description"></a>The `AWS::Lambda::WebFunctionEndpoint` resource Property description not available. for Lambda.

## Syntax
<a name="aws-resource-lambda-webfunctionendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-webfunctionendpoint-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::WebFunctionEndpoint",
  "Properties" : {
      "[AuthType](#cfn-lambda-webfunctionendpoint-authtype)" : {{String}},
      "[Description](#cfn-lambda-webfunctionendpoint-description)" : {{String}},
      "[EndpointName](#cfn-lambda-webfunctionendpoint-endpointname)" : {{String}},
      "[EndpointType](#cfn-lambda-webfunctionendpoint-endpointtype)" : {{String}},
      "[FunctionName](#cfn-lambda-webfunctionendpoint-functionname)" : {{String}},
      "[Regions](#cfn-lambda-webfunctionendpoint-regions)" : {{[ String, ... ]}},
      "[RevisionWeights](#cfn-lambda-webfunctionendpoint-revisionweights)" : {{[ RevisionWeight, ... ]}},
      "[ScalingConfig](#cfn-lambda-webfunctionendpoint-scalingconfig)" : {{ScalingConfig}},
      "[ThrottleConfig](#cfn-lambda-webfunctionendpoint-throttleconfig)" : {{ThrottleConfig}}
    }
}
```

### YAML
<a name="aws-resource-lambda-webfunctionendpoint-syntax.yaml"></a>

```
Type: AWS::Lambda::WebFunctionEndpoint
Properties:
  [AuthType](#cfn-lambda-webfunctionendpoint-authtype): {{String}}
  [Description](#cfn-lambda-webfunctionendpoint-description): {{String}}
  [EndpointName](#cfn-lambda-webfunctionendpoint-endpointname): {{String}}
  [EndpointType](#cfn-lambda-webfunctionendpoint-endpointtype): {{String}}
  [FunctionName](#cfn-lambda-webfunctionendpoint-functionname): {{String}}
  [Regions](#cfn-lambda-webfunctionendpoint-regions): {{
    - String}}
  [RevisionWeights](#cfn-lambda-webfunctionendpoint-revisionweights): {{
    - RevisionWeight}}
  [ScalingConfig](#cfn-lambda-webfunctionendpoint-scalingconfig): {{
    ScalingConfig}}
  [ThrottleConfig](#cfn-lambda-webfunctionendpoint-throttleconfig): {{
    ThrottleConfig}}
```

## Properties
<a name="aws-resource-lambda-webfunctionendpoint-properties"></a>

`AuthType`  <a name="cfn-lambda-webfunctionendpoint-authtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ApplicationManaged | IamAuth`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lambda-webfunctionendpoint-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointName`  <a name="cfn-lambda-webfunctionendpoint-endpointname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointType`  <a name="cfn-lambda-webfunctionendpoint-endpointtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `HomeRegion | MultiRegion | PerRegion`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionName`  <a name="cfn-lambda-webfunctionendpoint-functionname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Regions`  <a name="cfn-lambda-webfunctionendpoint-regions"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RevisionWeights`  <a name="cfn-lambda-webfunctionendpoint-revisionweights"></a>
Property description not available.
*Required*: No
*Type*: Array of [RevisionWeight](aws-properties-lambda-webfunctionendpoint-revisionweight.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingConfig`  <a name="cfn-lambda-webfunctionendpoint-scalingconfig"></a>
(Amazon SQS only) The scaling configuration for the event source. To remove the configuration, pass an empty value.
*Required*: No
*Type*: [ScalingConfig](aws-properties-lambda-webfunctionendpoint-scalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottleConfig`  <a name="cfn-lambda-webfunctionendpoint-throttleconfig"></a>
Property description not available.
*Required*: No
*Type*: [ThrottleConfig](aws-properties-lambda-webfunctionendpoint-throttleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-webfunctionendpoint-return-values"></a>

### Ref
<a name="aws-resource-lambda-webfunctionendpoint-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-webfunctionendpoint-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-webfunctionendpoint-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`DomainName`  <a name="DomainName-fn::getatt"></a>
Property description not available.

`EndpointArn`  <a name="EndpointArn-fn::getatt"></a>
Property description not available.

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.

`StateReason`  <a name="StateReason-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.

`UpdateStatus`  <a name="UpdateStatus-fn::getatt"></a>
Property description not available.

`UpdateStatusReason`  <a name="UpdateStatusReason-fn::getatt"></a>
Property description not available.
