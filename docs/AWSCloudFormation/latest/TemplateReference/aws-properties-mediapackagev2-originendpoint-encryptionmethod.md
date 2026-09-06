---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-encryptionmethod.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint EncryptionMethod
<a name="aws-properties-mediapackagev2-originendpoint-encryptionmethod"></a>

The encryption method associated with the origin endpoint.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-encryptionmethod-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-encryptionmethod-syntax.json"></a>

```
{
  "[CmafEncryptionMethod](#cfn-mediapackagev2-originendpoint-encryptionmethod-cmafencryptionmethod)" : {{String}},
  "[IsmEncryptionMethod](#cfn-mediapackagev2-originendpoint-encryptionmethod-ismencryptionmethod)" : {{String}},
  "[TsEncryptionMethod](#cfn-mediapackagev2-originendpoint-encryptionmethod-tsencryptionmethod)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-encryptionmethod-syntax.yaml"></a>

```
  [CmafEncryptionMethod](#cfn-mediapackagev2-originendpoint-encryptionmethod-cmafencryptionmethod): {{String}}
  [IsmEncryptionMethod](#cfn-mediapackagev2-originendpoint-encryptionmethod-ismencryptionmethod): {{String}}
  [TsEncryptionMethod](#cfn-mediapackagev2-originendpoint-encryptionmethod-tsencryptionmethod): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-encryptionmethod-properties"></a>

`CmafEncryptionMethod`  <a name="cfn-mediapackagev2-originendpoint-encryptionmethod-cmafencryptionmethod"></a>
The encryption method to use.
*Required*: No
*Type*: String
*Allowed values*: `CENC | CBCS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsmEncryptionMethod`  <a name="cfn-mediapackagev2-originendpoint-encryptionmethod-ismencryptionmethod"></a>
The encryption method used for Microsoft Smooth Streaming (MSS) content. This specifies how the MSS segments are encrypted to protect the content during delivery to client players.
*Required*: No
*Type*: String
*Allowed values*: `CENC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TsEncryptionMethod`  <a name="cfn-mediapackagev2-originendpoint-encryptionmethod-tsencryptionmethod"></a>
The encryption method to use.
*Required*: No
*Type*: String
*Allowed values*: `AES_128 | SAMPLE_AES`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
