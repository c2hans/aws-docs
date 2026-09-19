---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-supportauthz-supportpermit-signingkeyinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit SigningKeyInfo
<a name="aws-properties-supportauthz-supportpermit-signingkeyinfo"></a>

The customer managed AWS KMS key used to cryptographically sign a support permit.

## Syntax
<a name="aws-properties-supportauthz-supportpermit-signingkeyinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-supportauthz-supportpermit-signingkeyinfo-syntax.json"></a>

```
{
  "[KmsKey](#cfn-supportauthz-supportpermit-signingkeyinfo-kmskey)" : {{String}}
}
```

### YAML
<a name="aws-properties-supportauthz-supportpermit-signingkeyinfo-syntax.yaml"></a>

```
  [KmsKey](#cfn-supportauthz-supportpermit-signingkeyinfo-kmskey): {{String}}
```

## Properties
<a name="aws-properties-supportauthz-supportpermit-signingkeyinfo-properties"></a>

`KmsKey`  <a name="cfn-supportauthz-supportpermit-signingkeyinfo-kmskey"></a>
The Amazon Resource Name (ARN) of the customer managed AWS KMS key used to sign permit grants. The key must be an asymmetric AWS KMS key configured for signing and verification (key spec `ECC_NIST_P384`, key usage `SIGN_VERIFY`).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9/:_-]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
