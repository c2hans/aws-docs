---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DLM::LifecyclePolicy EncryptionConfiguration
<a name="aws-properties-dlm-lifecyclepolicy-encryptionconfiguration"></a>

**[Event-based policies only]** Specifies the encryption settings for cross-Region snapshot copies created by event-based policies.

## Syntax
<a name="aws-properties-dlm-lifecyclepolicy-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dlm-lifecyclepolicy-encryptionconfiguration-syntax.json"></a>

```
{
  "[CmkArn](#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn)" : {{String}},
  "[Encrypted](#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-dlm-lifecyclepolicy-encryptionconfiguration-syntax.yaml"></a>

```
  [CmkArn](#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn): {{String}}
  [Encrypted](#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted): {{Boolean}}
```

## Properties
<a name="aws-properties-dlm-lifecyclepolicy-encryptionconfiguration-properties"></a>

`CmkArn`  <a name="cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.
*Required*: No
*Type*: String
*Pattern*: `arn:aws(-[a-z]{1,4}){0,2}:kms:([a-z]+-){2,3}\d:\d+:key/.*`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encrypted`  <a name="cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted"></a>
To encrypt a copy of an unencrypted snapshot when encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or when encryption by default is not enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
