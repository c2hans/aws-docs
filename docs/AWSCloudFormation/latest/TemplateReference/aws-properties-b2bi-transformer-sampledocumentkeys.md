---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-b2bi-transformer-sampledocumentkeys.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer SampleDocumentKeys
<a name="aws-properties-b2bi-transformer-sampledocumentkeys"></a>

An array of the Amazon S3 keys used to identify the location for your sample documents.

## Syntax
<a name="aws-properties-b2bi-transformer-sampledocumentkeys-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-b2bi-transformer-sampledocumentkeys-syntax.json"></a>

```
{
  "[Input](#cfn-b2bi-transformer-sampledocumentkeys-input)" : {{String}},
  "[Output](#cfn-b2bi-transformer-sampledocumentkeys-output)" : {{String}}
}
```

### YAML
<a name="aws-properties-b2bi-transformer-sampledocumentkeys-syntax.yaml"></a>

```
  [Input](#cfn-b2bi-transformer-sampledocumentkeys-input): {{String}}
  [Output](#cfn-b2bi-transformer-sampledocumentkeys-output): {{String}}
```

## Properties
<a name="aws-properties-b2bi-transformer-sampledocumentkeys-properties"></a>

`Input`  <a name="cfn-b2bi-transformer-sampledocumentkeys-input"></a>
An array of keys for your input sample documents.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Output`  <a name="cfn-b2bi-transformer-sampledocumentkeys-output"></a>
An array of keys for your output sample documents.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
