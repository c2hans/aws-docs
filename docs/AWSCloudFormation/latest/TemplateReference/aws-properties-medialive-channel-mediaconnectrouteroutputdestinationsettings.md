---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaConnectRouterOutputDestinationSettings
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings"></a>

MediaConnect Router output destination settings.

The parent of this entity is OutputDestination.

## Syntax
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings-syntax.json"></a>

```
{
  "[EncryptionType](#cfn-medialive-channel-mediaconnectrouteroutputdestinationsettings-encryptiontype)" : {{String}},
  "[SecretArn](#cfn-medialive-channel-mediaconnectrouteroutputdestinationsettings-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings-syntax.yaml"></a>

```
  [EncryptionType](#cfn-medialive-channel-mediaconnectrouteroutputdestinationsettings-encryptiontype): {{String}}
  [SecretArn](#cfn-medialive-channel-mediaconnectrouteroutputdestinationsettings-secretarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings-properties"></a>

`EncryptionType`  <a name="cfn-medialive-channel-mediaconnectrouteroutputdestinationsettings-encryptiontype"></a>
Encryption configuration for MediaConnect Router. When using SECRETS\_MANAGER encryption, you must provide the ARN of the secret used to encrypt data in transit. When using AUTOMATIC encryption, a service-managed secret will be used instead.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretArn`  <a name="cfn-medialive-channel-mediaconnectrouteroutputdestinationsettings-secretarn"></a>
ARN of the secret used to encrypt this input. Used only with the SECRETS\_MANAGER encryption type.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
