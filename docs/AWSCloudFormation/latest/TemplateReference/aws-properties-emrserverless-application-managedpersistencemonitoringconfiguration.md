---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application ManagedPersistenceMonitoringConfiguration
<a name="aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration"></a>

The managed log persistence configuration for a job run.

## Syntax
<a name="aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-enabled)" : {{Boolean}},
  "[EncryptionKeyArn](#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-encryptionkeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-enabled): {{Boolean}}
  [EncryptionKeyArn](#cfn-emrserverless-application-managedpersistencemonitoringconfiguration-encryptionkeyarn): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-managedpersistencemonitoringconfiguration-properties"></a>

`Enabled`  <a name="cfn-emrserverless-application-managedpersistencemonitoringconfiguration-enabled"></a>
Enables managed logging and defaults to true. If set to false, managed logging will be turned off.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EncryptionKeyArn`  <a name="cfn-emrserverless-application-managedpersistencemonitoringconfiguration-encryptionkeyarn"></a>
The KMS key ARN to encrypt the logs stored in managed log persistence.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z0-9-]*):kms:[a-zA-Z0-9\-]*:(\d{12})?:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
