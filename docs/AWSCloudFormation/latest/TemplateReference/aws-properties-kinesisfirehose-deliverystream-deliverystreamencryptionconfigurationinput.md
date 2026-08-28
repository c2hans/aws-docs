---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DeliveryStreamEncryptionConfigurationInput
<a name="aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput"></a>

Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-syntax.json"></a>

```
{
  "[KeyARN](#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn)" : {{String}},
  "[KeyType](#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-syntax.yaml"></a>

```
  [KeyARN](#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn): {{String}}
  [KeyType](#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-properties"></a>

`KeyARN`  <a name="cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn"></a>
If you set `KeyType` to `CUSTOMER_MANAGED_CMK`, you must specify the Amazon Resource Name (ARN) of the CMK. If you set `KeyType` to `AWS_OWNED_CMK`, Firehose uses a service-account CMK.
*Required*: No
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyType`  <a name="cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype"></a>
Indicates the type of customer master key (CMK) to use for encryption. The default setting is `AWS_OWNED_CMK`. For more information about CMKs, see [Customer Master Keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys).
You can use a CMK of type CUSTOMER\_MANAGED\_CMK to encrypt up to 500 delivery streams.
To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see [About Symmetric and Asymmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html) in the AWS Key Management Service developer guide.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_OWNED_CMK | CUSTOMER_MANAGED_CMK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
