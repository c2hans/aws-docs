---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-clientcertificate-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApiGateway::ClientCertificate Tag
<a name="aws-properties-apigateway-clientcertificate-tag"></a>

An array of key-value pairs to apply to this resource.

For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).

## Syntax
<a name="aws-properties-apigateway-clientcertificate-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apigateway-clientcertificate-tag-syntax.json"></a>

```
{
  "[Key](#cfn-apigateway-clientcertificate-tag-key)" : {{String}},
  "[Value](#cfn-apigateway-clientcertificate-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-apigateway-clientcertificate-tag-syntax.yaml"></a>

```
  [Key](#cfn-apigateway-clientcertificate-tag-key): {{String}}
  [Value](#cfn-apigateway-clientcertificate-tag-value): {{String}}
```

## Properties
<a name="aws-properties-apigateway-clientcertificate-tag-properties"></a>

`Key`  <a name="cfn-apigateway-clientcertificate-tag-key"></a>
A string you can use to assign a value. The combination of tag keys and values can help you organize and categorize your resources.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-apigateway-clientcertificate-tag-value"></a>
The value for the specified tag key.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
