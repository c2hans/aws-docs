---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-paymentcryptography-key-keymodesofuse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PaymentCryptography::Key KeyModesOfUse
<a name="aws-properties-paymentcryptography-key-keymodesofuse"></a>

The list of cryptographic operations that you can perform using the key. The modes of use are deﬁned in section A.5.3 of the TR-31 spec.

## Syntax
<a name="aws-properties-paymentcryptography-key-keymodesofuse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-paymentcryptography-key-keymodesofuse-syntax.json"></a>

```
{
  "[Decrypt](#cfn-paymentcryptography-key-keymodesofuse-decrypt)" : {{Boolean}},
  "[DeriveKey](#cfn-paymentcryptography-key-keymodesofuse-derivekey)" : {{Boolean}},
  "[Encrypt](#cfn-paymentcryptography-key-keymodesofuse-encrypt)" : {{Boolean}},
  "[Generate](#cfn-paymentcryptography-key-keymodesofuse-generate)" : {{Boolean}},
  "[NoRestrictions](#cfn-paymentcryptography-key-keymodesofuse-norestrictions)" : {{Boolean}},
  "[Sign](#cfn-paymentcryptography-key-keymodesofuse-sign)" : {{Boolean}},
  "[Unwrap](#cfn-paymentcryptography-key-keymodesofuse-unwrap)" : {{Boolean}},
  "[Verify](#cfn-paymentcryptography-key-keymodesofuse-verify)" : {{Boolean}},
  "[Wrap](#cfn-paymentcryptography-key-keymodesofuse-wrap)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-paymentcryptography-key-keymodesofuse-syntax.yaml"></a>

```
  [Decrypt](#cfn-paymentcryptography-key-keymodesofuse-decrypt): {{Boolean}}
  [DeriveKey](#cfn-paymentcryptography-key-keymodesofuse-derivekey): {{Boolean}}
  [Encrypt](#cfn-paymentcryptography-key-keymodesofuse-encrypt): {{Boolean}}
  [Generate](#cfn-paymentcryptography-key-keymodesofuse-generate): {{Boolean}}
  [NoRestrictions](#cfn-paymentcryptography-key-keymodesofuse-norestrictions): {{Boolean}}
  [Sign](#cfn-paymentcryptography-key-keymodesofuse-sign): {{Boolean}}
  [Unwrap](#cfn-paymentcryptography-key-keymodesofuse-unwrap): {{Boolean}}
  [Verify](#cfn-paymentcryptography-key-keymodesofuse-verify): {{Boolean}}
  [Wrap](#cfn-paymentcryptography-key-keymodesofuse-wrap): {{Boolean}}
```

## Properties
<a name="aws-properties-paymentcryptography-key-keymodesofuse-properties"></a>

`Decrypt`  <a name="cfn-paymentcryptography-key-keymodesofuse-decrypt"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to decrypt data.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeriveKey`  <a name="cfn-paymentcryptography-key-keymodesofuse-derivekey"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to derive new keys.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encrypt`  <a name="cfn-paymentcryptography-key-keymodesofuse-encrypt"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to encrypt data.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Generate`  <a name="cfn-paymentcryptography-key-keymodesofuse-generate"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NoRestrictions`  <a name="cfn-paymentcryptography-key-keymodesofuse-norestrictions"></a>
Speciﬁes whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by `KeyUsage`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sign`  <a name="cfn-paymentcryptography-key-keymodesofuse-sign"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used for signing.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unwrap`  <a name="cfn-paymentcryptography-key-keymodesofuse-unwrap"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Verify`  <a name="cfn-paymentcryptography-key-keymodesofuse-verify"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to verify signatures.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Wrap`  <a name="cfn-paymentcryptography-key-keymodesofuse-wrap"></a>
Speciﬁes whether an AWS Payment Cryptography key can be used to wrap other keys.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
