---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-hostkey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::HostKey
<a name="aws-resource-transfer-hostkey"></a>

<a name="aws-resource-transfer-hostkey-description"></a>The `AWS::Transfer::HostKey` resource Property description not available. for Transfer.

## Syntax
<a name="aws-resource-transfer-hostkey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-hostkey-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::HostKey",
  "Properties" : {
      "[Description](#cfn-transfer-hostkey-description)" : {{String}},
      "[HostKeyBody](#cfn-transfer-hostkey-hostkeybody)" : {{String}},
      "[ServerId](#cfn-transfer-hostkey-serverid)" : {{String}},
      "[Tags](#cfn-transfer-hostkey-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-transfer-hostkey-syntax.yaml"></a>

```
Type: AWS::Transfer::HostKey
Properties:
  [Description](#cfn-transfer-hostkey-description): {{String}}
  [HostKeyBody](#cfn-transfer-hostkey-hostkeybody): {{String}}
  [ServerId](#cfn-transfer-hostkey-serverid): {{String}}
  [Tags](#cfn-transfer-hostkey-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-transfer-hostkey-properties"></a>

`Description`  <a name="cfn-transfer-hostkey-description"></a>
The text description for this host key.
*Required*: No
*Type*: String
*Pattern*: `^[\p{Print}]*$`
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HostKeyBody`  <a name="cfn-transfer-hostkey-hostkeybody"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServerId`  <a name="cfn-transfer-hostkey-serverid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^s-([0-9a-f]{17})$`
*Minimum*: `19`
*Maximum*: `19`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-transfer-hostkey-tags"></a>
Key-value pairs that can be used to group and search for host keys.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-hostkey-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-hostkey-return-values"></a>

### Ref
<a name="aws-resource-transfer-hostkey-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-transfer-hostkey-return-values-fn--getatt"></a>

####
<a name="aws-resource-transfer-hostkey-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique Amazon Resource Name (ARN) for the host key.

`DateImported`  <a name="DateImported-fn::getatt"></a>
The date on which the host key was added to the server.

`HostKeyFingerprint`  <a name="HostKeyFingerprint-fn::getatt"></a>
The public key fingerprint, which is a short sequence of bytes used to identify the longer public key.

`HostKeyId`  <a name="HostKeyId-fn::getatt"></a>
A unique identifier for the host key.

`Type`  <a name="Type-fn::getatt"></a>
The encryption algorithm that is used for the host key. The `Type` parameter is specified by using one of the following values:
+  `ssh-rsa`
+  `ssh-ed25519`
+  `ecdsa-sha2-nistp256`
+  `ecdsa-sha2-nistp384`
+  `ecdsa-sha2-nistp521`
