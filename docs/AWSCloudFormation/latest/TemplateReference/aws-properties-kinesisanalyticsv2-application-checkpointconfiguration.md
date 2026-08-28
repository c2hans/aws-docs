---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application CheckpointConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-checkpointconfiguration"></a>

Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see [ Checkpoints for Fault Tolerance](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/datastream/fault-tolerance/checkpointing/) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-master).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-checkpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-checkpointconfiguration-syntax.json"></a>

```
{
  "[CheckpointingEnabled](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled)" : {{Boolean}},
  "[CheckpointInterval](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval)" : {{Integer}},
  "[ConfigurationType](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype)" : {{String}},
  "[MinPauseBetweenCheckpoints](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-checkpointconfiguration-syntax.yaml"></a>

```
  [CheckpointingEnabled](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled): {{Boolean}}
  [CheckpointInterval](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval): {{Integer}}
  [ConfigurationType](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype): {{String}}
  [MinPauseBetweenCheckpoints](#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-checkpointconfiguration-properties"></a>

`CheckpointingEnabled`  <a name="cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled"></a>
Describes whether checkpointing is enabled for a Managed Service for Apache Flink application.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointingEnabled` value of `true`, even if this value is set to another value using this API or in application code.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CheckpointInterval`  <a name="cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval"></a>
Describes the interval in milliseconds between checkpoint operations.
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `CheckpointInterval` value of 60000, even if this value is set to another value using this API or in application code.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `9223372036854775807`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConfigurationType`  <a name="cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype"></a>
Describes whether the application uses Managed Service for Apache Flink' default checkpointing behavior. You must set this property to `CUSTOM` in order to set the `CheckpointingEnabled`, `CheckpointInterval`, or `MinPauseBetweenCheckpoints` parameters.
If this value is set to `DEFAULT`, the application will use the following values, even if they are set to other values using APIs or application code:
+ **CheckpointingEnabled:** true
+ **CheckpointInterval:** 60000
+ **MinPauseBetweenCheckpoints:** 5000
*Required*: Yes
*Type*: String
*Allowed values*: `DEFAULT | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinPauseBetweenCheckpoints`  <a name="cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints"></a>
Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start. If a checkpoint operation takes longer than the `CheckpointInterval`, the application otherwise performs continual checkpoint operations. For more information, see [ Tuning Checkpointing](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/large_state_tuning/#tuning-checkpointing) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-master).
If `CheckpointConfiguration.ConfigurationType` is `DEFAULT`, the application will use a `MinPauseBetweenCheckpoints` value of 5000, even if this value is set using this API or in application code.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `9223372036854775807`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-checkpointconfiguration--seealso"></a>
+ [CheckpointConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CheckpointConfiguration.html) in the *Amazon Kinesis Data Analytics API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
