---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-foundationmodel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FoundationModel
<a name="aws-resource-bedrock-foundationmodel"></a>

Request a model access agreement for the specified model.

## Syntax
<a name="aws-resource-bedrock-foundationmodel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-foundationmodel-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::FoundationModel"
}
```

### YAML
<a name="aws-resource-bedrock-foundationmodel-syntax.yaml"></a>

```
Type: AWS::Bedrock::FoundationModel
```

## Return values
<a name="aws-resource-bedrock-foundationmodel-return-values"></a>

### Ref
<a name="aws-resource-bedrock-foundationmodel-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrock-foundationmodel-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-foundationmodel-return-values-fn--getatt-fn--getatt"></a>

`CustomizationsSupported`  <a name="CustomizationsSupported-fn::getatt"></a>
The customization that the model supports.

`InferenceTypesSupported`  <a name="InferenceTypesSupported-fn::getatt"></a>
The inference types that the model supports.

`InputModalities`  <a name="InputModalities-fn::getatt"></a>
The input modalities that the model supports.

`ModelArn`  <a name="ModelArn-fn::getatt"></a>
The model Amazon Resource Name (ARN).

`ModelId`  <a name="ModelId-fn::getatt"></a>
The model identifier.

`ModelName`  <a name="ModelName-fn::getatt"></a>
The model name.

`OutputModalities`  <a name="OutputModalities-fn::getatt"></a>
The output modalities that the model supports.

`ProviderName`  <a name="ProviderName-fn::getatt"></a>
The model's provider name.

`ResponseStreamingSupported`  <a name="ResponseStreamingSupported-fn::getatt"></a>
Indicates whether the model supports streaming.
