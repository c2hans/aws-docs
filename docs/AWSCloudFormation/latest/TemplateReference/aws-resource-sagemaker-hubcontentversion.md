---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-hubcontentversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::HubContentVersion
<a name="aws-resource-sagemaker-hubcontentversion"></a>

<a name="aws-resource-sagemaker-hubcontentversion-description"></a>The `AWS::SageMaker::HubContentVersion` resource Property description not available. for SageMaker.

## Syntax
<a name="aws-resource-sagemaker-hubcontentversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-hubcontentversion-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::HubContentVersion",
  "Properties" : {
      "[HubContentName](#cfn-sagemaker-hubcontentversion-hubcontentname)" : {{String}},
      "[HubContentType](#cfn-sagemaker-hubcontentversion-hubcontenttype)" : {{String}},
      "[HubName](#cfn-sagemaker-hubcontentversion-hubname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-hubcontentversion-syntax.yaml"></a>

```
Type: AWS::SageMaker::HubContentVersion
Properties:
  [HubContentName](#cfn-sagemaker-hubcontentversion-hubcontentname): {{String}}
  [HubContentType](#cfn-sagemaker-hubcontentversion-hubcontenttype): {{String}}
  [HubName](#cfn-sagemaker-hubcontentversion-hubname): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-hubcontentversion-properties"></a>

`HubContentName`  <a name="cfn-sagemaker-hubcontentversion-hubcontentname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HubContentType`  <a name="cfn-sagemaker-hubcontentversion-hubcontenttype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `Model | Notebook | ModelReference | DataSet | JsonDoc`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HubName`  <a name="cfn-sagemaker-hubcontentversion-hubname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-hubcontentversion-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-hubcontentversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-hubcontentversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-hubcontentversion-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`DocumentSchemaVersion`  <a name="DocumentSchemaVersion-fn::getatt"></a>
Property description not available.

`HubArn`  <a name="HubArn-fn::getatt"></a>
Property description not available.

`HubContentArn`  <a name="HubContentArn-fn::getatt"></a>
Property description not available.

`HubContentDescription`  <a name="HubContentDescription-fn::getatt"></a>
Property description not available.

`HubContentDisplayName`  <a name="HubContentDisplayName-fn::getatt"></a>
Property description not available.

`HubContentStatus`  <a name="HubContentStatus-fn::getatt"></a>
Property description not available.

`HubContentVersion`  <a name="HubContentVersion-fn::getatt"></a>
Property description not available.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
Property description not available.

`ReferenceMinVersion`  <a name="ReferenceMinVersion-fn::getatt"></a>
Property description not available.

`ResourceArn`  <a name="ResourceArn-fn::getatt"></a>
Property description not available.

`SageMakerPublicHubContentArn`  <a name="SageMakerPublicHubContentArn-fn::getatt"></a>
Property description not available.

`SupportStatus`  <a name="SupportStatus-fn::getatt"></a>
Property description not available.
