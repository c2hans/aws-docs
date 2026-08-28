---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::PackagingConfiguration SpekeKeyProvider
<a name="aws-properties-mediapackage-packagingconfiguration-spekekeyprovider"></a>

A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that provides encryption keys.

## Syntax
<a name="aws-properties-mediapackage-packagingconfiguration-spekekeyprovider-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-packagingconfiguration-spekekeyprovider-syntax.json"></a>

```
{
  "[EncryptionContractConfiguration](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-encryptioncontractconfiguration)" : {{EncryptionContractConfiguration}},
  "[RoleArn](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn)" : {{String}},
  "[SystemIds](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids)" : {{[ String, ... ]}},
  "[Url](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackage-packagingconfiguration-spekekeyprovider-syntax.yaml"></a>

```
  [EncryptionContractConfiguration](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-encryptioncontractconfiguration): {{
    EncryptionContractConfiguration}}
  [RoleArn](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn): {{String}}
  [SystemIds](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids): {{
    - String}}
  [Url](#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url): {{String}}
```

## Properties
<a name="aws-properties-mediapackage-packagingconfiguration-spekekeyprovider-properties"></a>

`EncryptionContractConfiguration`  <a name="cfn-mediapackage-packagingconfiguration-spekekeyprovider-encryptioncontractconfiguration"></a>
Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.
*Required*: No
*Type*: [EncryptionContractConfiguration](aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn"></a>
The ARN for the IAM role that's granted by the key provider to provide access to the key provider API. Valid format: arn:aws:iam::{accountID}:role/{name}
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SystemIds`  <a name="cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids"></a>
List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-mediapackage-packagingconfiguration-spekekeyprovider-url"></a>
URL for the key provider's key retrieval API endpoint. Must start with https://.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
