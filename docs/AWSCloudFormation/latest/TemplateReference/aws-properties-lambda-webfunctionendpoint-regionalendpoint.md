---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionendpoint-regionalendpoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionEndpoint RegionalEndpoint
<a name="aws-properties-lambda-webfunctionendpoint-regionalendpoint"></a>

<a name="aws-properties-lambda-webfunctionendpoint-regionalendpoint-description"></a>The `RegionalEndpoint` property type specifies Property description not available. for an [AWS::Lambda::WebFunctionEndpoint](aws-resource-lambda-webfunctionendpoint.md).

## Syntax
<a name="aws-properties-lambda-webfunctionendpoint-regionalendpoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionendpoint-regionalendpoint-syntax.json"></a>

```
{
  "[AuthType](#cfn-lambda-webfunctionendpoint-regionalendpoint-authtype)" : {{String}},
  "[DomainName](#cfn-lambda-webfunctionendpoint-regionalendpoint-domainname)" : {{String}},
  "[RevisionWeights](#cfn-lambda-webfunctionendpoint-regionalendpoint-revisionweights)" : {{[ RevisionWeight, ... ]}},
  "[ScalingConfig](#cfn-lambda-webfunctionendpoint-regionalendpoint-scalingconfig)" : {{ScalingConfig}},
  "[State](#cfn-lambda-webfunctionendpoint-regionalendpoint-state)" : {{String}},
  "[StateReason](#cfn-lambda-webfunctionendpoint-regionalendpoint-statereason)" : {{String}},
  "[ThrottleConfig](#cfn-lambda-webfunctionendpoint-regionalendpoint-throttleconfig)" : {{ThrottleConfig}},
  "[UpdateStatus](#cfn-lambda-webfunctionendpoint-regionalendpoint-updatestatus)" : {{String}},
  "[UpdateStatusReason](#cfn-lambda-webfunctionendpoint-regionalendpoint-updatestatusreason)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionendpoint-regionalendpoint-syntax.yaml"></a>

```
  [AuthType](#cfn-lambda-webfunctionendpoint-regionalendpoint-authtype): {{String}}
  [DomainName](#cfn-lambda-webfunctionendpoint-regionalendpoint-domainname): {{String}}
  [RevisionWeights](#cfn-lambda-webfunctionendpoint-regionalendpoint-revisionweights): {{
    - RevisionWeight}}
  [ScalingConfig](#cfn-lambda-webfunctionendpoint-regionalendpoint-scalingconfig): {{
    ScalingConfig}}
  [State](#cfn-lambda-webfunctionendpoint-regionalendpoint-state): {{String}}
  [StateReason](#cfn-lambda-webfunctionendpoint-regionalendpoint-statereason): {{String}}
  [ThrottleConfig](#cfn-lambda-webfunctionendpoint-regionalendpoint-throttleconfig): {{
    ThrottleConfig}}
  [UpdateStatus](#cfn-lambda-webfunctionendpoint-regionalendpoint-updatestatus): {{String}}
  [UpdateStatusReason](#cfn-lambda-webfunctionendpoint-regionalendpoint-updatestatusreason): {{String}}
```

## Properties
<a name="aws-properties-lambda-webfunctionendpoint-regionalendpoint-properties"></a>

`AuthType`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-authtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ApplicationManaged | IamAuth`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-domainname"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RevisionWeights`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-revisionweights"></a>
Property description not available.
*Required*: No
*Type*: Array of [RevisionWeight](aws-properties-lambda-webfunctionendpoint-revisionweight.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScalingConfig`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-scalingconfig"></a>
Property description not available.
*Required*: No
*Type*: [ScalingConfig](aws-properties-lambda-webfunctionendpoint-scalingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-state"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Pending | Active | Failed | Deleting`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StateReason`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-statereason"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThrottleConfig`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-throttleconfig"></a>
Property description not available.
*Required*: No
*Type*: [ThrottleConfig](aws-properties-lambda-webfunctionendpoint-throttleconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateStatus`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-updatestatus"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `InProgress | Successful | Failed`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateStatusReason`  <a name="cfn-lambda-webfunctionendpoint-regionalendpoint-updatestatusreason"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
