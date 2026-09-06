---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application FlinkRunConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration"></a>

Describes the starting parameters for a Managed Service for Apache Flink application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration-syntax.json"></a>

```
{
  "[AllowNonRestoredState](#cfn-kinesisanalyticsv2-application-flinkrunconfiguration-allownonrestoredstate)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration-syntax.yaml"></a>

```
  [AllowNonRestoredState](#cfn-kinesisanalyticsv2-application-flinkrunconfiguration-allownonrestoredstate): {{Boolean}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-flinkrunconfiguration-properties"></a>

`AllowNonRestoredState`  <a name="cfn-kinesisanalyticsv2-application-flinkrunconfiguration-allownonrestoredstate"></a>
When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see [ Allowing Non-Restored State](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#allowing-non-restored-state) in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-master).
This value defaults to `false`. If you update your application without specifying this parameter, `AllowNonRestoredState` will be set to `false`, even if it was previously set to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
