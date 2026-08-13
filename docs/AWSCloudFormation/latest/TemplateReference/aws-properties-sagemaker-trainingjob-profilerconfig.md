---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-profilerconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob ProfilerConfig
<a name="aws-properties-sagemaker-trainingjob-profilerconfig"></a>

Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-profilerconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-profilerconfig-syntax.json"></a>

```
{
  "[DisableProfiler](#cfn-sagemaker-trainingjob-profilerconfig-disableprofiler)" : {{Boolean}},
  "[ProfilingIntervalInMilliseconds](#cfn-sagemaker-trainingjob-profilerconfig-profilingintervalinmilliseconds)" : {{Integer}},
  "[ProfilingParameters](#cfn-sagemaker-trainingjob-profilerconfig-profilingparameters)" : {{{{{Key}}: {{Value}}, ...}}},
  "[S3OutputPath](#cfn-sagemaker-trainingjob-profilerconfig-s3outputpath)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-profilerconfig-syntax.yaml"></a>

```
  [DisableProfiler](#cfn-sagemaker-trainingjob-profilerconfig-disableprofiler): {{Boolean}}
  [ProfilingIntervalInMilliseconds](#cfn-sagemaker-trainingjob-profilerconfig-profilingintervalinmilliseconds): {{Integer}}
  [ProfilingParameters](#cfn-sagemaker-trainingjob-profilerconfig-profilingparameters): {{
    {{Key}}: {{Value}}}}
  [S3OutputPath](#cfn-sagemaker-trainingjob-profilerconfig-s3outputpath): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-profilerconfig-properties"></a>

`DisableProfiler`  <a name="cfn-sagemaker-trainingjob-profilerconfig-disableprofiler"></a>
Configuration to turn off Amazon SageMaker Debugger's system monitoring and profiling functionality. To turn it off, set to `True`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfilingIntervalInMilliseconds`  <a name="cfn-sagemaker-trainingjob-profilerconfig-profilingintervalinmilliseconds"></a>
A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfilingParameters`  <a name="cfn-sagemaker-trainingjob-profilerconfig-profilingparameters"></a>
Configuration information for capturing framework metrics. Available key strings for different profiling options are `DetailedProfilingConfig`, `PythonProfilingConfig`, and `DataLoaderProfilingConfig`. The following codes are configuration structures for the `ProfilingParameters` parameter. To learn more about how to configure the `ProfilingParameters` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
*Required*: No
*Type*: Object of String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3OutputPath`  <a name="cfn-sagemaker-trainingjob-profilerconfig-s3outputpath"></a>
Path to Amazon S3 storage location for system and framework metrics.
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
