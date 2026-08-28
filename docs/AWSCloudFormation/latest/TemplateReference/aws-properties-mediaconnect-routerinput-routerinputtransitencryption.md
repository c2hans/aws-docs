---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-routerinputtransitencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RouterInputTransitEncryption
<a name="aws-properties-mediaconnect-routerinput-routerinputtransitencryption"></a>

The transit encryption settings for a router input.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-routerinputtransitencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-routerinputtransitencryption-syntax.json"></a>

```
{
  "[EncryptionKeyConfiguration](#cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeyconfiguration)" : {{RouterInputTransitEncryptionKeyConfiguration}},
  "[EncryptionKeyType](#cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-routerinputtransitencryption-syntax.yaml"></a>

```
  [EncryptionKeyConfiguration](#cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeyconfiguration): {{
    RouterInputTransitEncryptionKeyConfiguration}}
  [EncryptionKeyType](#cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeytype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-routerinputtransitencryption-properties"></a>

`EncryptionKeyConfiguration`  <a name="cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeyconfiguration"></a>
Contains the configuration details for the encryption key used in transit encryption, including the key source and associated parameters.
*Required*: Yes
*Type*: [RouterInputTransitEncryptionKeyConfiguration](aws-properties-mediaconnect-routerinput-routerinputtransitencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyType`  <a name="cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeytype"></a>
Specifies the type of encryption key to use for transit encryption.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
