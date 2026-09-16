---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotsitewise-task-containertaskconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Task ContainerTaskConfiguration
<a name="aws-properties-iotsitewise-task-containertaskconfiguration"></a>

<a name="aws-properties-iotsitewise-task-containertaskconfiguration-description"></a>The `ContainerTaskConfiguration` property type specifies Property description not available. for an [AWS::IoTSiteWise::Task](aws-resource-iotsitewise-task.md).

## Syntax
<a name="aws-properties-iotsitewise-task-containertaskconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotsitewise-task-containertaskconfiguration-syntax.json"></a>

```
{
  "[Command](#cfn-iotsitewise-task-containertaskconfiguration-command)" : {{[ String, ... ]}},
  "[EcrUri](#cfn-iotsitewise-task-containertaskconfiguration-ecruri)" : {{String}},
  "[EnvironmentVariables](#cfn-iotsitewise-task-containertaskconfiguration-environmentvariables)" : {{{{{Key}}: {{Value}}, ...}}},
  "[EphemeralStorageConfiguration](#cfn-iotsitewise-task-containertaskconfiguration-ephemeralstorageconfiguration)" : {{EphemeralStorageConfiguration}},
  "[Mounts](#cfn-iotsitewise-task-containertaskconfiguration-mounts)" : {{[ Mount, ... ]}},
  "[ProcessingType](#cfn-iotsitewise-task-containertaskconfiguration-processingtype)" : {{String}},
  "[ProcessingUnit](#cfn-iotsitewise-task-containertaskconfiguration-processingunit)" : {{String}},
  "[TaskExecutionRole](#cfn-iotsitewise-task-containertaskconfiguration-taskexecutionrole)" : {{String}},
  "[TimeoutSeconds](#cfn-iotsitewise-task-containertaskconfiguration-timeoutseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iotsitewise-task-containertaskconfiguration-syntax.yaml"></a>

```
  [Command](#cfn-iotsitewise-task-containertaskconfiguration-command): {{
    - String}}
  [EcrUri](#cfn-iotsitewise-task-containertaskconfiguration-ecruri): {{String}}
  [EnvironmentVariables](#cfn-iotsitewise-task-containertaskconfiguration-environmentvariables): {{
    {{Key}}: {{Value}}}}
  [EphemeralStorageConfiguration](#cfn-iotsitewise-task-containertaskconfiguration-ephemeralstorageconfiguration): {{
    EphemeralStorageConfiguration}}
  [Mounts](#cfn-iotsitewise-task-containertaskconfiguration-mounts): {{
    - Mount}}
  [ProcessingType](#cfn-iotsitewise-task-containertaskconfiguration-processingtype): {{String}}
  [ProcessingUnit](#cfn-iotsitewise-task-containertaskconfiguration-processingunit): {{String}}
  [TaskExecutionRole](#cfn-iotsitewise-task-containertaskconfiguration-taskexecutionrole): {{String}}
  [TimeoutSeconds](#cfn-iotsitewise-task-containertaskconfiguration-timeoutseconds): {{Integer}}
```

## Properties
<a name="aws-properties-iotsitewise-task-containertaskconfiguration-properties"></a>

`Command`  <a name="cfn-iotsitewise-task-containertaskconfiguration-command"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EcrUri`  <a name="cfn-iotsitewise-task-containertaskconfiguration-ecruri"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^((\d{12}\.dkr\.ecr\.[a-z0-9-]+\.[a-z.]+)|public\.ecr\.aws/[a-z][a-z0-9]+([._-][a-z0-9]+)*)/[a-z0-9]+((\.||__|__|-+)[a-z0-9]+)*(/[a-z0-9]+((\.||__|__|-+)[a-z0-9]+)*)*(:[a-zA-Z0-9._-]+|@sha256:[a-f0-9]{64})?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-iotsitewise-task-containertaskconfiguration-environmentvariables"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z_][a-zA-Z0-9_]*$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EphemeralStorageConfiguration`  <a name="cfn-iotsitewise-task-containertaskconfiguration-ephemeralstorageconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [EphemeralStorageConfiguration](aws-properties-iotsitewise-task-ephemeralstorageconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mounts`  <a name="cfn-iotsitewise-task-containertaskconfiguration-mounts"></a>
Property description not available.
*Required*: No
*Type*: Array of [Mount](aws-properties-iotsitewise-task-mount.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessingType`  <a name="cfn-iotsitewise-task-containertaskconfiguration-processingtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `GENERIC_COMPUTE_PROCESSING | HARDWARE_ACCELERATED_PROCESSING`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProcessingUnit`  <a name="cfn-iotsitewise-task-containertaskconfiguration-processingunit"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `UNITS_2 | UNITS_4 | UNITS_8 | UNITS_12 | UNITS_16 | UNITS_24 | UNITS_32 | UNITS_36 | UNITS_48 | UNITS_60 | UNITS_64 | UNITS_72 | UNITS_84 | UNITS_96`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TaskExecutionRole`  <a name="cfn-iotsitewise-task-containertaskconfiguration-taskexecutionrole"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:iam::[0-9]+:role/[\w+=,.@/-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutSeconds`  <a name="cfn-iotsitewise-task-containertaskconfiguration-timeoutseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
