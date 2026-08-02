---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-activity-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::Activity EncryptionConfiguration
<a name="aws-properties-stepfunctions-activity-encryptionconfiguration"></a>

Settings to configure server-side encryption for an activity. By default, Step Functions provides transparent server-side encryption. With this configuration, you can specify a customer managed AWS KMS key for encryption.

## Syntax
<a name="aws-properties-stepfunctions-activity-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-activity-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsDataKeyReusePeriodSeconds](#cfn-stepfunctions-activity-encryptionconfiguration-kmsdatakeyreuseperiodseconds)" : {{Integer}},
  "[KmsKeyId](#cfn-stepfunctions-activity-encryptionconfiguration-kmskeyid)" : {{String}},
  "[Type](#cfn-stepfunctions-activity-encryptionconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-stepfunctions-activity-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsDataKeyReusePeriodSeconds](#cfn-stepfunctions-activity-encryptionconfiguration-kmsdatakeyreuseperiodseconds): {{Integer}}
  [KmsKeyId](#cfn-stepfunctions-activity-encryptionconfiguration-kmskeyid): {{String}}
  [Type](#cfn-stepfunctions-activity-encryptionconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-stepfunctions-activity-encryptionconfiguration-properties"></a>

`KmsDataKeyReusePeriodSeconds`  <a name="cfn-stepfunctions-activity-encryptionconfiguration-kmsdatakeyreuseperiodseconds"></a>
Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call `GenerateDataKey`. Only applies to customer managed keys.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `900`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-stepfunctions-activity-encryptionconfiguration-kmskeyid"></a>
An alias, alias ARN, key ID, or key ARN of a symmetric encryption AWS KMS key to encrypt data. To specify a AWS KMS key in a different AWS account, you must use the key ARN or alias ARN.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-stepfunctions-activity-encryptionconfiguration-type"></a>
Encryption option for an activity.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KEY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
