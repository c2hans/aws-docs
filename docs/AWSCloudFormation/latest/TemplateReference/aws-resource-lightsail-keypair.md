---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lightsail-keypair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::KeyPair
<a name="aws-resource-lightsail-keypair"></a>

Describes an SSH key pair.

## Syntax
<a name="aws-resource-lightsail-keypair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lightsail-keypair-syntax.json"></a>

```
{
  "Type" : "AWS::Lightsail::KeyPair",
  "Properties" : {
      "[KeyPairName](#cfn-lightsail-keypair-keypairname)" : {{String}},
      "[Tags](#cfn-lightsail-keypair-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lightsail-keypair-syntax.yaml"></a>

```
Type: AWS::Lightsail::KeyPair
Properties:
  [KeyPairName](#cfn-lightsail-keypair-keypairname): {{String}}
  [Tags](#cfn-lightsail-keypair-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lightsail-keypair-properties"></a>

`KeyPairName`  <a name="cfn-lightsail-keypair-keypairname"></a>
The friendly name of the SSH key pair.
*Required*: Yes
*Type*: String
*Pattern*: `^\w[\w\-]*\w$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lightsail-keypair-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
*Required*: No
*Type*: Array of [Tag](aws-properties-lightsail-keypair-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lightsail-keypair-return-values"></a>

### Ref
<a name="aws-resource-lightsail-keypair-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lightsail-keypair-return-values-fn--getatt"></a>

####
<a name="aws-resource-lightsail-keypair-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the key pair was created (`1479816991.349`).

`Fingerprint`  <a name="Fingerprint-fn::getatt"></a>
The RSA fingerprint of the key pair.

`KeyPairArn`  <a name="KeyPairArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the key pair (`arn:aws:lightsail:us-east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`).

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
The resource type (usually `KeyPair`).

`SupportCode`  <a name="SupportCode-fn::getatt"></a>
The support code. Include this code in your email to support when you have questions about an instance or another resource in Lightsail. This code enables our support team to look up your Lightsail information more easily.
