---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-routersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input RouterSettings
<a name="aws-properties-medialive-input-routersettings"></a>

Settings that apply only if the input is a MEDIACONNECT\_ROUTER type of input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-routersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-routersettings-syntax.json"></a>

```
{
  "[Destinations](#cfn-medialive-input-routersettings-destinations)" : {{[ RouterDestinationSettings, ... ]}},
  "[EncryptionType](#cfn-medialive-input-routersettings-encryptiontype)" : {{String}},
  "[SecretArn](#cfn-medialive-input-routersettings-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-input-routersettings-syntax.yaml"></a>

```
  [Destinations](#cfn-medialive-input-routersettings-destinations): {{
    - RouterDestinationSettings}}
  [EncryptionType](#cfn-medialive-input-routersettings-encryptiontype): {{String}}
  [SecretArn](#cfn-medialive-input-routersettings-secretarn): {{String}}
```

## Properties
<a name="aws-properties-medialive-input-routersettings-properties"></a>

`Destinations`  <a name="cfn-medialive-input-routersettings-destinations"></a>
The destinations for the input from MediaConnect Router. Specify one destination for a single-pipeline input, or two destinations for a standard (redundant) input. This property is required.
*Required*: No
*Type*: Array of [RouterDestinationSettings](aws-properties-medialive-input-routerdestinationsettings.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionType`  <a name="cfn-medialive-input-routersettings-encryptiontype"></a>
The type of encryption for the MediaConnect router input. Specify `AUTOMATIC` to use a service-managed encryption key, or `SECRETS_MANAGER` to supply your own AES-256 encryption key via AWS Secrets Manager. This property is required.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretArn`  <a name="cfn-medialive-input-routersettings-secretarn"></a>
The ARN of the secret in AWS Secrets Manager that is used to encrypt the MediaConnect router input. This property is required when `EncryptionType` is `SECRETS_MANAGER`, and must not be specified when `EncryptionType` is `AUTOMATIC`.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
