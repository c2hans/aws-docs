---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-amazonmq-broker-encryptionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmazonMQ::Broker EncryptionOptions
<a name="aws-properties-amazonmq-broker-encryptionoptions"></a>

Encryption options for the broker.

## Syntax
<a name="aws-properties-amazonmq-broker-encryptionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-amazonmq-broker-encryptionoptions-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-amazonmq-broker-encryptionoptions-kmskeyid)" : {{String}},
  "[UseAwsOwnedKey](#cfn-amazonmq-broker-encryptionoptions-useawsownedkey)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-amazonmq-broker-encryptionoptions-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-amazonmq-broker-encryptionoptions-kmskeyid): {{String}}
  [UseAwsOwnedKey](#cfn-amazonmq-broker-encryptionoptions-useawsownedkey): {{Boolean}}
```

## Properties
<a name="aws-properties-amazonmq-broker-encryptionoptions-properties"></a>

`KmsKeyId`  <a name="cfn-amazonmq-broker-encryptionoptions-kmskeyid"></a>
The customer master key (CMK) to use for the A AWS KMS (KMS). This key is used to encrypt your data at rest. If not provided, Amazon MQ will use a default CMK to encrypt your data.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UseAwsOwnedKey`  <a name="cfn-amazonmq-broker-encryptionoptions-useawsownedkey"></a>
Enables the use of an AWS owned CMK using AWS KMS (KMS). Set to `true` by default, if no value is provided, for example, for RabbitMQ brokers.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
