---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-voiceid-domain-serversideencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VoiceID::Domain ServerSideEncryptionConfiguration
<a name="aws-properties-voiceid-domain-serversideencryptionconfiguration"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

The configuration containing information about the customer managed key used for encrypting customer data.

## Syntax
<a name="aws-properties-voiceid-domain-serversideencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-voiceid-domain-serversideencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-voiceid-domain-serversideencryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-voiceid-domain-serversideencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-voiceid-domain-serversideencryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-voiceid-domain-serversideencryptionconfiguration-properties"></a>

`KmsKeyId`  <a name="cfn-voiceid-domain-serversideencryptionconfiguration-kmskeyid"></a>
The identifier of the KMS key to use to encrypt data stored by Voice ID. Voice ID doesn't support asymmetric customer managed keys.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
