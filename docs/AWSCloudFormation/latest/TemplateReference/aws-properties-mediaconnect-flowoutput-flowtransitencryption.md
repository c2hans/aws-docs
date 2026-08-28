---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flowoutput-flowtransitencryption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::FlowOutput FlowTransitEncryption
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryption"></a>

The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

## Syntax
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryption-syntax.json"></a>

```
{
  "[EncryptionKeyConfiguration](#cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeyconfiguration)" : {{FlowTransitEncryptionKeyConfiguration}},
  "[EncryptionKeyType](#cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryption-syntax.yaml"></a>

```
  [EncryptionKeyConfiguration](#cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeyconfiguration): {{
    FlowTransitEncryptionKeyConfiguration}}
  [EncryptionKeyType](#cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeytype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flowoutput-flowtransitencryption-properties"></a>

`EncryptionKeyConfiguration`  <a name="cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeyconfiguration"></a>
The configuration details for the encryption key.
*Required*: Yes
*Type*: [FlowTransitEncryptionKeyConfiguration](aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionKeyType`  <a name="cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeytype"></a>
The type of encryption key to use for flow transit encryption.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
