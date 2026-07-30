---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-engineconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup EngineConfiguration
<a name="aws-properties-athena-workgroup-engineconfiguration"></a>

The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).

To specify DPU values for PC queries the WG containing EngineConfiguration should have the following values: The name of the Classifications should be `athena-query-engine-properties`, with the only allowed properties as `max-dpu-count` and `min-dpu-count`.

## Syntax
<a name="aws-properties-athena-workgroup-engineconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-engineconfiguration-syntax.json"></a>

```
{
  "[AdditionalConfigs](#cfn-athena-workgroup-engineconfiguration-additionalconfigs)" : {{{{{Key}}: {{Value}}, ...}}},
  "[Classifications](#cfn-athena-workgroup-engineconfiguration-classifications)" : {{[ Classification, ... ]}},
  "[CoordinatorDpuSize](#cfn-athena-workgroup-engineconfiguration-coordinatordpusize)" : {{Integer}},
  "[DefaultExecutorDpuSize](#cfn-athena-workgroup-engineconfiguration-defaultexecutordpusize)" : {{Integer}},
  "[MaxConcurrentDpus](#cfn-athena-workgroup-engineconfiguration-maxconcurrentdpus)" : {{Integer}},
  "[SparkProperties](#cfn-athena-workgroup-engineconfiguration-sparkproperties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-engineconfiguration-syntax.yaml"></a>

```
  [AdditionalConfigs](#cfn-athena-workgroup-engineconfiguration-additionalconfigs): {{
    {{Key}}: {{Value}}}}
  [Classifications](#cfn-athena-workgroup-engineconfiguration-classifications): {{
    - Classification}}
  [CoordinatorDpuSize](#cfn-athena-workgroup-engineconfiguration-coordinatordpusize): {{Integer}}
  [DefaultExecutorDpuSize](#cfn-athena-workgroup-engineconfiguration-defaultexecutordpusize): {{Integer}}
  [MaxConcurrentDpus](#cfn-athena-workgroup-engineconfiguration-maxconcurrentdpus): {{Integer}}
  [SparkProperties](#cfn-athena-workgroup-engineconfiguration-sparkproperties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-athena-workgroup-engineconfiguration-properties"></a>

`AdditionalConfigs`  <a name="cfn-athena-workgroup-engineconfiguration-additionalconfigs"></a>
Contains additional notebook engine `MAP<string, string>` parameter mappings in the form of key-value pairs. To specify an Athena notebook that the Jupyter server will download and serve, specify a value for the StartSessionRequest$NotebookVersion field, and then add a key named `NotebookId` to `AdditionalConfigs` that has the value of the Athena notebook ID.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Classifications`  <a name="cfn-athena-workgroup-engineconfiguration-classifications"></a>
The configuration classifications that can be specified for the engine.
*Required*: No
*Type*: Array of [Classification](aws-properties-athena-workgroup-classification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoordinatorDpuSize`  <a name="cfn-athena-workgroup-engineconfiguration-coordinatordpusize"></a>
The number of DPUs to use for the coordinator. A coordinator is a special executor that orchestrates processing work and manages other executors in a notebook session. The default is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultExecutorDpuSize`  <a name="cfn-athena-workgroup-engineconfiguration-defaultexecutordpusize"></a>
The default number of DPUs to use for executors. An executor is the smallest unit of compute that a notebook session can request from Athena. The default is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxConcurrentDpus`  <a name="cfn-athena-workgroup-engineconfiguration-maxconcurrentdpus"></a>
The maximum number of DPUs that can run concurrently.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SparkProperties`  <a name="cfn-athena-workgroup-engineconfiguration-sparkproperties"></a>
Specifies custom jar files and Spark properties for use cases like cluster encryption, table formats, and general Spark tuning.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
