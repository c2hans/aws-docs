---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule LogsBackupConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration"></a>

Configuration for backing up centralized log data to a secondary region.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-kmskeyarn)" : {{String}},
  "[Region](#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-region)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-kmskeyarn): {{String}}
  [Region](#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-region): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-kmskeyarn"></a>
KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Region`  <a name="cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-region"></a>
Logs specific backup destination region within the primary destination account to which log data should be centralized.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
