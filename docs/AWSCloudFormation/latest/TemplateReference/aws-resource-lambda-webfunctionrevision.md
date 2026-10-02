---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionrevision.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision
<a name="aws-resource-lambda-webfunctionrevision"></a>

<a name="aws-resource-lambda-webfunctionrevision-description"></a>The `AWS::Lambda::WebFunctionRevision` resource Property description not available. for Lambda.

## Syntax
<a name="aws-resource-lambda-webfunctionrevision-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-webfunctionrevision-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::WebFunctionRevision",
  "Properties" : {
      "[BuildConfig](#cfn-lambda-webfunctionrevision-buildconfig)" : {{BuildConfig}},
      "[Description](#cfn-lambda-webfunctionrevision-description)" : {{String}},
      "[FunctionName](#cfn-lambda-webfunctionrevision-functionname)" : {{String}},
      "[KmsKeyArn](#cfn-lambda-webfunctionrevision-kmskeyarn)" : {{String}},
      "[ServiceConfig](#cfn-lambda-webfunctionrevision-serviceconfig)" : {{ServiceConfig}}
    }
}
```

### YAML
<a name="aws-resource-lambda-webfunctionrevision-syntax.yaml"></a>

```
Type: AWS::Lambda::WebFunctionRevision
Properties:
  [BuildConfig](#cfn-lambda-webfunctionrevision-buildconfig): {{
    BuildConfig}}
  [Description](#cfn-lambda-webfunctionrevision-description): {{String}}
  [FunctionName](#cfn-lambda-webfunctionrevision-functionname): {{String}}
  [KmsKeyArn](#cfn-lambda-webfunctionrevision-kmskeyarn): {{String}}
  [ServiceConfig](#cfn-lambda-webfunctionrevision-serviceconfig): {{
    ServiceConfig}}
```

## Properties
<a name="aws-resource-lambda-webfunctionrevision-properties"></a>

`BuildConfig`  <a name="cfn-lambda-webfunctionrevision-buildconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [BuildConfig](aws-properties-lambda-webfunctionrevision-buildconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-lambda-webfunctionrevision-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionName`  <a name="cfn-lambda-webfunctionrevision-functionname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-lambda-webfunctionrevision-kmskeyarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-z-]*){1}:kms:[a-z0-9-]+:[0-9]{12}:key/.*$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceConfig`  <a name="cfn-lambda-webfunctionrevision-serviceconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [ServiceConfig](aws-properties-lambda-webfunctionrevision-serviceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-webfunctionrevision-return-values"></a>

### Ref
<a name="aws-resource-lambda-webfunctionrevision-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-webfunctionrevision-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-webfunctionrevision-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
Property description not available.

`RevisionArn`  <a name="RevisionArn-fn::getatt"></a>
Property description not available.

`RevisionId`  <a name="RevisionId-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.

`StateReason`  <a name="StateReason-fn::getatt"></a>
Property description not available.
