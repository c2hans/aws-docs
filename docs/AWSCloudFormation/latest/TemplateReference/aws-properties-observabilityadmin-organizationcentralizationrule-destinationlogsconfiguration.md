---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule DestinationLogsConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration"></a>

Configuration for centralization destination log groups, including encryption and backup settings.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-syntax.json"></a>

```
{
  "[BackupConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-backupconfiguration)" : {{LogsBackupConfiguration}},
  "[LogGroupNameConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-loggroupnameconfiguration)" : {{LogGroupNameConfiguration}},
  "[LogsEncryptionConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-logsencryptionconfiguration)" : {{LogsEncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-syntax.yaml"></a>

```
  [BackupConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-backupconfiguration): {{
    LogsBackupConfiguration}}
  [LogGroupNameConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-loggroupnameconfiguration): {{
    LogGroupNameConfiguration}}
  [LogsEncryptionConfiguration](#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-logsencryptionconfiguration): {{
    LogsEncryptionConfiguration}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-properties"></a>

`BackupConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-backupconfiguration"></a>
Configuration defining the backup region and an optional KMS key for the backup destination.
*Required*: No
*Type*: [LogsBackupConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroupNameConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-loggroupnameconfiguration"></a>
Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.
*Required*: No
*Type*: [LogGroupNameConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogsEncryptionConfiguration`  <a name="cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-logsencryptionconfiguration"></a>
The encryption configuration for centralization destination log groups.
*Required*: No
*Type*: [LogsEncryptionConfiguration](aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
