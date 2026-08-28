---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-certificate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Certificate
<a name="aws-resource-transfer-certificate"></a>

Imports the signing and encryption certificates that you need to create local (AS2) profiles and partner profiles.

You can import both the certificate and its chain in the `Certificate` parameter.

After importing a certificate, AWS Transfer Family automatically creates a Amazon CloudWatch metric called `DaysUntilExpiry` that tracks the number of days until the certificate expires. The metric is based on the `InactiveDate` parameter and is published daily in the `AWS/Transfer` namespace.

**Important**
It can take up to a full day after importing a certificate for Transfer Family to emit the `DaysUntilExpiry` metric to your account.

**Note**
If you use the `Certificate` parameter to upload both the certificate and its chain, don't use the `CertificateChain` parameter.

 **CloudWatch monitoring**

The `DaysUntilExpiry` metric includes the following specifications:
+ **Units:** Count (days)
+ **Dimensions:**`CertificateId` (always present), `Description` (if provided during certificate import)
+ **Statistics:** Minimum, Maximum, Average
+ **Frequency:** Published daily

## Syntax
<a name="aws-resource-transfer-certificate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-certificate-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::Certificate",
  "Properties" : {
      "[ActiveDate](#cfn-transfer-certificate-activedate)" : {{String}},
      "[Certificate](#cfn-transfer-certificate-certificate)" : {{String}},
      "[CertificateChain](#cfn-transfer-certificate-certificatechain)" : {{String}},
      "[Description](#cfn-transfer-certificate-description)" : {{String}},
      "[InactiveDate](#cfn-transfer-certificate-inactivedate)" : {{String}},
      "[PrivateKey](#cfn-transfer-certificate-privatekey)" : {{String}},
      "[Tags](#cfn-transfer-certificate-tags)" : {{[ Tag, ... ]}},
      "[Usage](#cfn-transfer-certificate-usage)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-transfer-certificate-syntax.yaml"></a>

```
Type: AWS::Transfer::Certificate
Properties:
  [ActiveDate](#cfn-transfer-certificate-activedate): {{String}}
  [Certificate](#cfn-transfer-certificate-certificate): {{String}}
  [CertificateChain](#cfn-transfer-certificate-certificatechain): {{String}}
  [Description](#cfn-transfer-certificate-description): {{String}}
  [InactiveDate](#cfn-transfer-certificate-inactivedate): {{String}}
  [PrivateKey](#cfn-transfer-certificate-privatekey): {{String}}
  [Tags](#cfn-transfer-certificate-tags): {{
    - Tag}}
  [Usage](#cfn-transfer-certificate-usage): {{String}}
```

## Properties
<a name="aws-resource-transfer-certificate-properties"></a>

`ActiveDate`  <a name="cfn-transfer-certificate-activedate"></a>
An optional date that specifies when the certificate becomes active. If you do not specify a value, `ActiveDate` takes the same value as `NotBeforeDate`, which is specified by the CA.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Certificate`  <a name="cfn-transfer-certificate-certificate"></a>
The file name for the certificate.
*Required*: Yes
*Type*: String
*Pattern*: `^[\t\n\r\u0020-\u00FF]+$`
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificateChain`  <a name="cfn-transfer-certificate-certificatechain"></a>
The list of certificates that make up the chain for the certificate.
*Required*: No
*Type*: String
*Pattern*: `^[\t\n\r\u0020-\u00FF]+$`
*Minimum*: `1`
*Maximum*: `2097152`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-transfer-certificate-description"></a>
The name or description that's used to identity the certificate.
*Required*: No
*Type*: String
*Pattern*: `^[\u0021-\u007E]+$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InactiveDate`  <a name="cfn-transfer-certificate-inactivedate"></a>
An optional date that specifies when the certificate becomes inactive. If you do not specify a value, `InactiveDate` takes the same value as `NotAfterDate`, which is specified by the CA.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateKey`  <a name="cfn-transfer-certificate-privatekey"></a>
The file that contains the private key for the certificate that's being imported.
*Required*: No
*Type*: String
*Pattern*: `^[\t\n\r\u0020-\u00FF]+$`
*Minimum*: `1`
*Maximum*: `16384`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-transfer-certificate-tags"></a>
Key-value pairs that can be used to group and search for certificates.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-certificate-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Usage`  <a name="cfn-transfer-certificate-usage"></a>
Specifies how this certificate is used. It can be used in the following ways:
+ `SIGNING`: For signing AS2 messages
+ `ENCRYPTION`: For encrypting AS2 messages
+ `TLS`: For securing AS2 communications sent over HTTPS
*Required*: Yes
*Type*: String
*Allowed values*: `SIGNING | ENCRYPTION | TLS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-certificate-return-values"></a>

### Ref
<a name="aws-resource-transfer-certificate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `certificateId` , such as `cert-1c698edce1654f869` .

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-transfer-certificate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-transfer-certificate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The unique Amazon Resource Name (ARN) for the certificate.

`CertificateId`  <a name="CertificateId-fn::getatt"></a>
An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.

`NotAfterDate`  <a name="NotAfterDate-fn::getatt"></a>
The final date that the certificate is valid.

`NotBeforeDate`  <a name="NotBeforeDate-fn::getatt"></a>
The earliest date that the certificate is valid.

`Serial`  <a name="Serial-fn::getatt"></a>
The serial number for the certificate.

`Status`  <a name="Status-fn::getatt"></a>
 The certificate can be either `ACTIVE` , `PENDING_ROTATION` , or `INACTIVE` . `PENDING_ROTATION` means that this certificate will replace the current certificate when it expires.

`Type`  <a name="Type-fn::getatt"></a>
 If a private key has been specified for the certificate, its type is `CERTIFICATE_WITH_PRIVATE_KEY` . If there is no private key, the type is `CERTIFICATE` .

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
