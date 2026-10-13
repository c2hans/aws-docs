---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-spekekeyprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint SpekeKeyProvider
<a name="aws-properties-mediapackagev2-originendpoint-spekekeyprovider"></a>

The parameters for the SPEKE key provider.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-spekekeyprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-spekekeyprovider-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-mediapackagev2-originendpoint-spekekeyprovider-certificatearn)" : {{String}},
  "[ContentKeyPeriodConfiguration](#cfn-mediapackagev2-originendpoint-spekekeyprovider-contentkeyperiodconfiguration)" : {{ContentKeyPeriodConfiguration}},
  "[DrmSystems](#cfn-mediapackagev2-originendpoint-spekekeyprovider-drmsystems)" : {{[ String, ... ]}},
  "[EncryptionContractConfiguration](#cfn-mediapackagev2-originendpoint-spekekeyprovider-encryptioncontractconfiguration)" : {{EncryptionContractConfiguration}},
  "[ResourceId](#cfn-mediapackagev2-originendpoint-spekekeyprovider-resourceid)" : {{String}},
  "[RoleArn](#cfn-mediapackagev2-originendpoint-spekekeyprovider-rolearn)" : {{String}},
  "[SpekeVersion](#cfn-mediapackagev2-originendpoint-spekekeyprovider-spekeversion)" : {{String}},
  "[Url](#cfn-mediapackagev2-originendpoint-spekekeyprovider-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-spekekeyprovider-syntax.yaml"></a>

```
  [CertificateArn](#cfn-mediapackagev2-originendpoint-spekekeyprovider-certificatearn): {{String}}
  [ContentKeyPeriodConfiguration](#cfn-mediapackagev2-originendpoint-spekekeyprovider-contentkeyperiodconfiguration): {{
    ContentKeyPeriodConfiguration}}
  [DrmSystems](#cfn-mediapackagev2-originendpoint-spekekeyprovider-drmsystems): {{
    - String}}
  [EncryptionContractConfiguration](#cfn-mediapackagev2-originendpoint-spekekeyprovider-encryptioncontractconfiguration): {{
    EncryptionContractConfiguration}}
  [ResourceId](#cfn-mediapackagev2-originendpoint-spekekeyprovider-resourceid): {{String}}
  [RoleArn](#cfn-mediapackagev2-originendpoint-spekekeyprovider-rolearn): {{String}}
  [SpekeVersion](#cfn-mediapackagev2-originendpoint-spekekeyprovider-spekeversion): {{String}}
  [Url](#cfn-mediapackagev2-originendpoint-spekekeyprovider-url): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-spekekeyprovider-properties"></a>

`CertificateArn`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-certificatearn"></a>
The ARN for the certificate that you imported to AWS Certificate Manager to add content key encryption to this endpoint. For this feature to work, your DRM key provider must support content key encryption.
*Required*: No
*Type*: String
*Pattern*: `^arn:([^:\n]+):acm:([^:\n]+):([0-9]+):certificate/[a-zA-Z0-9-_]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentKeyPeriodConfiguration`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-contentkeyperiodconfiguration"></a>
The configuration that controls whether MediaPackage signals the start and end times a content key is used for, in the `ContentKeyPeriod` sent to your DRM key provider. Signaling this timing is supported only when key rotation is enabled (`KeyRotationIntervalSeconds` is set to a non-zero value) and `SpekeVersion` is `V2_1`. You can update these settings on an existing origin endpoint.
*Required*: No
*Type*: [ContentKeyPeriodConfiguration](aws-properties-mediapackagev2-originendpoint-contentkeyperiodconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrmSystems`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-drmsystems"></a>
The DRM solution provider you're using to protect your content during distribution.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionContractConfiguration`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-encryptioncontractconfiguration"></a>
The encryption contract configuration associated with the SPEKE key provider.
*Required*: Yes
*Type*: [EncryptionContractConfiguration](aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceId`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-resourceid"></a>
The unique identifier for the content. The service sends this identifier to the key server to identify the current endpoint. How unique you make this identifier depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.
The following example shows a resource ID: `MovieNight20171126093045`
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-rolearn"></a>
The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.
Valid format: `arn:aws:iam::{accountID}:role/{name}`. The following example shows a role ARN: `arn:aws:iam::444455556666:role/SpekeAccess`
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpekeVersion`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-spekeversion"></a>
Specifies the SPEKE version used with your DRM key provider. If you don't specify a value, the default is `V2_0`.
The allowed values are:
+ `V2_0` - Follows the SPEKE Version 2.0 contract and signals only the content key index in key requests. This is the default.
+ `V2_1` - Follows the SPEKE Version 2.1 contract and additionally supports signaling the start and end times a content key is used for, using `ContentKeyPeriodConfiguration`.
For more information, see [SPEKE Version 2.0 payload](https://docs.aws.amazon.com/speke/latest/documentation/standard-payload-components-v2.html).
*Required*: No
*Type*: String
*Allowed values*: `V2_0 | V2_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediapackagev2-originendpoint-spekekeyprovider-url"></a>
The URL of the SPEKE key provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
