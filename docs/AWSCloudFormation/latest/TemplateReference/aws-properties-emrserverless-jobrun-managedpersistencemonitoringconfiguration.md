---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::JobRun ManagedPersistenceMonitoringConfiguration
<a name="aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration"></a>

The managed log persistence configuration for a job run.

## Syntax
<a name="aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-emrserverless-jobrun-managedpersistencemonitoringconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-emrserverless-jobrun-managedpersistencemonitoringconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-emrserverless-jobrun-managedpersistencemonitoringconfiguration-properties"></a>

`Enabled`  <a name="cfn-emrserverless-jobrun-managedpersistencemonitoringconfiguration-enabled"></a>
Enables managed logging and defaults to true. If set to false, managed logging will be turned off.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
