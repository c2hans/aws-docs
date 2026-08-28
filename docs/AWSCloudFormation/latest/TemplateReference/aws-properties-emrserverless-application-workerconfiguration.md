---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrserverless-application-workerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRServerless::Application WorkerConfiguration
<a name="aws-properties-emrserverless-application-workerconfiguration"></a>

The configuration of a worker. For more information, see [ Supported worker configurations](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/app-behavior.html#worker-configs).

## Syntax
<a name="aws-properties-emrserverless-application-workerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrserverless-application-workerconfiguration-syntax.json"></a>

```
{
  "[Cpu](#cfn-emrserverless-application-workerconfiguration-cpu)" : {{String}},
  "[Disk](#cfn-emrserverless-application-workerconfiguration-disk)" : {{String}},
  "[DiskType](#cfn-emrserverless-application-workerconfiguration-disktype)" : {{String}},
  "[Memory](#cfn-emrserverless-application-workerconfiguration-memory)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrserverless-application-workerconfiguration-syntax.yaml"></a>

```
  [Cpu](#cfn-emrserverless-application-workerconfiguration-cpu): {{String}}
  [Disk](#cfn-emrserverless-application-workerconfiguration-disk): {{String}}
  [DiskType](#cfn-emrserverless-application-workerconfiguration-disktype): {{String}}
  [Memory](#cfn-emrserverless-application-workerconfiguration-memory): {{String}}
```

## Properties
<a name="aws-properties-emrserverless-application-workerconfiguration-properties"></a>

`Cpu`  <a name="cfn-emrserverless-application-workerconfiguration-cpu"></a>
The CPU requirements of the worker configuration. Each worker can have 1, 2, 4, 8, or 16 vCPUs.
*Required*: Yes
*Type*: String
*Pattern*: `^[1-9][0-9]*(\s)?(vCPU|vcpu|VCPU)?$`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Disk`  <a name="cfn-emrserverless-application-workerconfiguration-disk"></a>
The disk requirements of the worker configuration.
*Required*: No
*Type*: String
*Pattern*: `^[1-9][0-9]*(\s)?(GB|gb|gB|Gb)$`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`DiskType`  <a name="cfn-emrserverless-application-workerconfiguration-disktype"></a>
The disk type for every worker instance of the work type. Shuffle optimized disks have higher performance characteristics and are better for shuffle heavy workloads. Default is `STANDARD`.
*Required*: No
*Type*: String
*Pattern*: `^(SHUFFLE_OPTIMIZED|[Ss]huffle_[Oo]ptimized|STANDARD|[Ss]tandard)$`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Memory`  <a name="cfn-emrserverless-application-workerconfiguration-memory"></a>
The memory requirements of the worker configuration.
*Required*: Yes
*Type*: String
*Pattern*: `^[1-9][0-9]*(\s)?(GB|gb|gB|Gb)?$`
*Minimum*: `1`
*Maximum*: `15`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
