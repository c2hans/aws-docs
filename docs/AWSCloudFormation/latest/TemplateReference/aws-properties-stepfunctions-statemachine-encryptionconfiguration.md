---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-statemachine-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::StateMachine EncryptionConfiguration
<a name="aws-properties-stepfunctions-statemachine-encryptionconfiguration"></a>

Settings to configure server-side encryption for a state machine. By default, Step Functions provides transparent server-side encryption. With this configuration, you can specify a customer managed AWS KMS key for encryption.

## Syntax
<a name="aws-properties-stepfunctions-statemachine-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-statemachine-encryptionconfiguration-syntax.json"></a>

```
{
  "[KmsDataKeyReusePeriodSeconds](#cfn-stepfunctions-statemachine-encryptionconfiguration-kmsdatakeyreuseperiodseconds)" : {{Integer}},
  "[KmsKeyId](#cfn-stepfunctions-statemachine-encryptionconfiguration-kmskeyid)" : {{String}},
  "[Type](#cfn-stepfunctions-statemachine-encryptionconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-stepfunctions-statemachine-encryptionconfiguration-syntax.yaml"></a>

```
  [KmsDataKeyReusePeriodSeconds](#cfn-stepfunctions-statemachine-encryptionconfiguration-kmsdatakeyreuseperiodseconds): {{Integer}}
  [KmsKeyId](#cfn-stepfunctions-statemachine-encryptionconfiguration-kmskeyid): {{String}}
  [Type](#cfn-stepfunctions-statemachine-encryptionconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-stepfunctions-statemachine-encryptionconfiguration-properties"></a>

`KmsDataKeyReusePeriodSeconds`  <a name="cfn-stepfunctions-statemachine-encryptionconfiguration-kmsdatakeyreuseperiodseconds"></a>
Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call `GenerateDataKey`. Only applies to customer managed keys.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-stepfunctions-statemachine-encryptionconfiguration-kmskeyid"></a>
An alias, alias ARN, key ID, or key ARN of a symmetric encryption AWS KMS key to encrypt data. To specify a AWS KMS key in a different AWS account, you must use the key ARN or alias ARN.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-stepfunctions-statemachine-encryptionconfiguration-type"></a>
Encryption option for a state machine.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOMER_MANAGED_KMS_KEY | AWS_OWNED_KEY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
