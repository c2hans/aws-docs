---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-session-engineconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::Session EngineConfiguration
<a name="aws-properties-athena-session-engineconfiguration"></a>

The engine configuration for the workgroup, which includes the minimum/maximum number of Data Processing Units (DPU) that queries should use when running in provisioned capacity. If not specified, Athena uses default values (Default value for min is 4 and for max is Minimum of 124 and allocated DPUs).

To specify DPU values for PC queries the WG containing EngineConfiguration should have the following values: The name of the Classifications should be `athena-query-engine-properties`, with the only allowed properties as `max-dpu-count` and `min-dpu-count`.

## Syntax
<a name="aws-properties-athena-session-engineconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-session-engineconfiguration-syntax.json"></a>

```
{
  "[AdditionalConfigs](#cfn-athena-session-engineconfiguration-additionalconfigs)" : {{{{{Key}}: {{Value}}, ...}}},
  "[CoordinatorDpuSize](#cfn-athena-session-engineconfiguration-coordinatordpusize)" : {{Integer}},
  "[DefaultExecutorDpuSize](#cfn-athena-session-engineconfiguration-defaultexecutordpusize)" : {{Integer}},
  "[MaxConcurrentDpus](#cfn-athena-session-engineconfiguration-maxconcurrentdpus)" : {{Integer}},
  "[SparkProperties](#cfn-athena-session-engineconfiguration-sparkproperties)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-athena-session-engineconfiguration-syntax.yaml"></a>

```
  [AdditionalConfigs](#cfn-athena-session-engineconfiguration-additionalconfigs): {{
    {{Key}}: {{Value}}}}
  [CoordinatorDpuSize](#cfn-athena-session-engineconfiguration-coordinatordpusize): {{Integer}}
  [DefaultExecutorDpuSize](#cfn-athena-session-engineconfiguration-defaultexecutordpusize): {{Integer}}
  [MaxConcurrentDpus](#cfn-athena-session-engineconfiguration-maxconcurrentdpus): {{Integer}}
  [SparkProperties](#cfn-athena-session-engineconfiguration-sparkproperties): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-athena-session-engineconfiguration-properties"></a>

`AdditionalConfigs`  <a name="cfn-athena-session-engineconfiguration-additionalconfigs"></a>
Contains additional notebook engine `MAP<string, string>` parameter mappings in the form of key-value pairs. To specify an Athena notebook that the Jupyter server will download and serve, specify a value for the StartSessionRequest$NotebookVersion field, and then add a key named `NotebookId` to `AdditionalConfigs` that has the value of the Athena notebook ID.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CoordinatorDpuSize`  <a name="cfn-athena-session-engineconfiguration-coordinatordpusize"></a>
The number of DPUs to use for the coordinator. A coordinator is a special executor that orchestrates processing work and manages other executors in a notebook session. The default is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultExecutorDpuSize`  <a name="cfn-athena-session-engineconfiguration-defaultexecutordpusize"></a>
The default number of DPUs to use for executors. An executor is the smallest unit of compute that a notebook session can request from Athena. The default is 1.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxConcurrentDpus`  <a name="cfn-athena-session-engineconfiguration-maxconcurrentdpus"></a>
The maximum number of DPUs that can run concurrently.
*Required*: Yes
*Type*: Integer
*Minimum*: `2`
*Maximum*: `5000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SparkProperties`  <a name="cfn-athena-session-engineconfiguration-sparkproperties"></a>
Specifies custom jar files and Spark properties for use cases like cluster encryption, table formats, and general Spark tuning.
*Required*: No
*Type*: Object of String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
