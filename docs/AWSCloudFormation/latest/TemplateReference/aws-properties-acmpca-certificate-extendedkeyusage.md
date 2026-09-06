---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-acmpca-certificate-extendedkeyusage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ACMPCA::Certificate ExtendedKeyUsage
<a name="aws-properties-acmpca-certificate-extendedkeyusage"></a>

Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the `KeyUsage` extension.

## Syntax
<a name="aws-properties-acmpca-certificate-extendedkeyusage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-acmpca-certificate-extendedkeyusage-syntax.json"></a>

```
{
  "[ExtendedKeyUsageObjectIdentifier](#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusageobjectidentifier)" : {{String}},
  "[ExtendedKeyUsageType](#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusagetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-acmpca-certificate-extendedkeyusage-syntax.yaml"></a>

```
  [ExtendedKeyUsageObjectIdentifier](#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusageobjectidentifier): {{String}}
  [ExtendedKeyUsageType](#cfn-acmpca-certificate-extendedkeyusage-extendedkeyusagetype): {{String}}
```

## Properties
<a name="aws-properties-acmpca-certificate-extendedkeyusage-properties"></a>

`ExtendedKeyUsageObjectIdentifier`  <a name="cfn-acmpca-certificate-extendedkeyusage-extendedkeyusageobjectidentifier"></a>
Specifies a custom `ExtendedKeyUsage` with an object identifier (OID).
*Required*: No
*Type*: String
*Pattern*: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExtendedKeyUsageType`  <a name="cfn-acmpca-certificate-extendedkeyusage-extendedkeyusagetype"></a>
Specifies a standard `ExtendedKeyUsage` as defined as in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12).
*Required*: No
*Type*: String
*Allowed values*: `SERVER_AUTH | CLIENT_AUTH | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | SMART_CARD_LOGIN | DOCUMENT_SIGNING | CERTIFICATE_TRANSPARENCY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
