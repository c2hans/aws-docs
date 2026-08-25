---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule LogsEncryptionConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration"></a>

Configuration for encrypting centralized destination log groups. By default, this configuration applies only to destination log groups whose corresponding source log groups are encrypted using customer managed KMS keys. To encrypt all destination log groups created by the rule, set `EncryptionScope` to `NEW_DESTINATION_LOG_GROUPS`.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionConflictResolutionStrategy](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionconflictresolutionstrategy)" : {{String}},
  "[EncryptionScope](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionscope)" : {{String}},
  "[EncryptionStrategy](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionstrategy)" : {{String}},
  "[KmsKeyArn](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionConflictResolutionStrategy](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionconflictresolutionstrategy): {{String}}
  [EncryptionScope](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionscope): {{String}}
  [EncryptionStrategy](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionstrategy): {{String}}
  [KmsKeyArn](#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-properties"></a>

`EncryptionConflictResolutionStrategy`  <a name="cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionconflictresolutionstrategy"></a>
Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER\_MANAGED and the destination log group is encrypted with an AWS\_OWNED KMS Key. ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW | SKIP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionScope`  <a name="cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionscope"></a>
Determines which newly created destination log groups are encrypted with the configured `KmsKeyArn` when `EncryptionStrategy` is `CUSTOMER_MANAGED`.
If you set this to `ENCRYPTED_SOURCE_ONLY` (the default), only destination log groups whose source log group is encrypted with a customer managed KMS key use the configured `KmsKeyArn`. Destination log groups derived from AWS owned encrypted source log groups remain AWS owned encrypted.
If you set this to `NEW_DESTINATION_LOG_GROUPS`, every new destination log group created by this rule uses the configured `KmsKeyArn`, regardless of the source log group's encryption posture.
This field is not valid when `EncryptionStrategy` is `AWS_OWNED`.
*Required*: No
*Type*: String
*Allowed values*: `ENCRYPTED_SOURCE_ONLY | NEW_DESTINATION_LOG_GROUPS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionStrategy`  <a name="cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionstrategy"></a>
Configuration that determines the encryption strategy of the destination log groups. CUSTOMER\_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOMER_MANAGED | AWS_OWNED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-kmskeyarn"></a>
KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
