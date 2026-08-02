---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-transformjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TransformJob
<a name="aws-resource-sagemaker-transformjob"></a>

A batch transform job. For information about SageMaker batch transform, see [Use Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html).

## Syntax
<a name="aws-resource-sagemaker-transformjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-transformjob-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::TransformJob",
  "Properties" : {
      "[BatchStrategy](#cfn-sagemaker-transformjob-batchstrategy)" : {{String}},
      "[DataCaptureConfig](#cfn-sagemaker-transformjob-datacaptureconfig)" : {{DataCaptureConfig}},
      "[DataProcessing](#cfn-sagemaker-transformjob-dataprocessing)" : {{DataProcessing}},
      "[Environment](#cfn-sagemaker-transformjob-environment)" : {{{{{Key}}: {{Value}}, ...}}},
      "[ExperimentConfig](#cfn-sagemaker-transformjob-experimentconfig)" : {{ExperimentConfig}},
      "[MaxConcurrentTransforms](#cfn-sagemaker-transformjob-maxconcurrenttransforms)" : {{Integer}},
      "[MaxPayloadInMB](#cfn-sagemaker-transformjob-maxpayloadinmb)" : {{Integer}},
      "[ModelClientConfig](#cfn-sagemaker-transformjob-modelclientconfig)" : {{ModelClientConfig}},
      "[ModelName](#cfn-sagemaker-transformjob-modelname)" : {{String}},
      "[Tags](#cfn-sagemaker-transformjob-tags)" : {{[ TagsItems, ... ]}},
      "[TransformInput](#cfn-sagemaker-transformjob-transforminput)" : {{TransformInput}},
      "[TransformOutput](#cfn-sagemaker-transformjob-transformoutput)" : {{TransformOutput}},
      "[TransformResources](#cfn-sagemaker-transformjob-transformresources)" : {{TransformResources}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-transformjob-syntax.yaml"></a>

```
Type: AWS::SageMaker::TransformJob
Properties:
  [BatchStrategy](#cfn-sagemaker-transformjob-batchstrategy): {{String}}
  [DataCaptureConfig](#cfn-sagemaker-transformjob-datacaptureconfig): {{
    DataCaptureConfig}}
  [DataProcessing](#cfn-sagemaker-transformjob-dataprocessing): {{
    DataProcessing}}
  [Environment](#cfn-sagemaker-transformjob-environment): {{
    {{Key}}: {{Value}}}}
  [ExperimentConfig](#cfn-sagemaker-transformjob-experimentconfig): {{
    ExperimentConfig}}
  [MaxConcurrentTransforms](#cfn-sagemaker-transformjob-maxconcurrenttransforms): {{Integer}}
  [MaxPayloadInMB](#cfn-sagemaker-transformjob-maxpayloadinmb): {{Integer}}
  [ModelClientConfig](#cfn-sagemaker-transformjob-modelclientconfig): {{
    ModelClientConfig}}
  [ModelName](#cfn-sagemaker-transformjob-modelname): {{String}}
  [Tags](#cfn-sagemaker-transformjob-tags): {{
    - TagsItems}}
  [TransformInput](#cfn-sagemaker-transformjob-transforminput): {{
    TransformInput}}
  [TransformOutput](#cfn-sagemaker-transformjob-transformoutput): {{
    TransformOutput}}
  [TransformResources](#cfn-sagemaker-transformjob-transformresources): {{
    TransformResources}}
```

## Properties
<a name="aws-resource-sagemaker-transformjob-properties"></a>

`BatchStrategy`  <a name="cfn-sagemaker-transformjob-batchstrategy"></a>
Specifies the number of records to include in a mini-batch for an HTTP inference request. A record is a single unit of input data that inference can be made on. For example, a single line in a CSV file is a record.
*Required*: No
*Type*: String
*Allowed values*: `MultiRecord | SingleRecord`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataCaptureConfig`  <a name="cfn-sagemaker-transformjob-datacaptureconfig"></a>
Configuration to control how SageMaker AI captures inference data.
*Required*: No
*Type*: [DataCaptureConfig](aws-properties-sagemaker-transformjob-datacaptureconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataProcessing`  <a name="cfn-sagemaker-transformjob-dataprocessing"></a>
The data structure used to specify the data to be used for inference in a batch transform job and to associate the data that is relevant to the prediction results in the output. The input filter provided allows you to exclude input data that is not needed for inference in a batch transform job. The output filter provided allows you to include input data relevant to interpreting the predictions in the output from the job. For more information, see [Associate Prediction Results with their Corresponding Input Records](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html).
*Required*: No
*Type*: [DataProcessing](aws-properties-sagemaker-transformjob-dataprocessing.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Environment`  <a name="cfn-sagemaker-transformjob-environment"></a>
The environment variables to set in the Docker container. We support up to 16 key and values entries in the map.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z_][a-zA-Z0-9_]*`
*Maximum*: `10240`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExperimentConfig`  <a name="cfn-sagemaker-transformjob-experimentconfig"></a>
Associates a SageMaker job as a trial component with an experiment and trial. Specified when you call the following APIs:
+  [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
+  [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
+  [CreateTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
*Required*: No
*Type*: [ExperimentConfig](aws-properties-sagemaker-transformjob-experimentconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxConcurrentTransforms`  <a name="cfn-sagemaker-transformjob-maxconcurrenttransforms"></a>
The maximum number of parallel requests that can be sent to each instance in a transform job. If `MaxConcurrentTransforms` is set to 0 or left unset, SageMaker checks the optional execution-parameters to determine the settings for your chosen algorithm. If the execution-parameters endpoint is not enabled, the default value is 1. For built-in algorithms, you don't need to set a value for `MaxConcurrentTransforms`.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxPayloadInMB`  <a name="cfn-sagemaker-transformjob-maxpayloadinmb"></a>
The maximum allowed size of the payload, in MB. A payload is the data portion of a record (without metadata). The value in `MaxPayloadInMB` must be greater than, or equal to, the size of a single record. To estimate the size of a record in MB, divide the size of your dataset by the number of records. To ensure that the records fit within the maximum payload size, we recommend using a slightly larger value. The default value is 6 MB. For cases where the payload might be arbitrarily large and is transmitted using HTTP chunked encoding, set the value to 0. This feature works only in supported algorithms. Currently, SageMaker built-in algorithms do not support HTTP chunked encoding.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelClientConfig`  <a name="cfn-sagemaker-transformjob-modelclientconfig"></a>
Configures the timeout and maximum number of retries for processing a transform job invocation.
*Required*: No
*Type*: [ModelClientConfig](aws-properties-sagemaker-transformjob-modelclientconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModelName`  <a name="cfn-sagemaker-transformjob-modelname"></a>
The name of the model associated with the transform job.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-transformjob-tags"></a>
A list of tags associated with the transform job.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-sagemaker-transformjob-tagsitems.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransformInput`  <a name="cfn-sagemaker-transformjob-transforminput"></a>
A description of the input source and the way the transform job consumes it.
*Required*: Yes
*Type*: [TransformInput](aws-properties-sagemaker-transformjob-transforminput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransformOutput`  <a name="cfn-sagemaker-transformjob-transformoutput"></a>
Identifies the Amazon S3 location where you want Amazon SageMaker to save the results from the transform job.
*Required*: Yes
*Type*: [TransformOutput](aws-properties-sagemaker-transformjob-transformoutput.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransformResources`  <a name="cfn-sagemaker-transformjob-transformresources"></a>
Identifies the ML compute instances for the transform job.
*Required*: Yes
*Type*: [TransformResources](aws-properties-sagemaker-transformjob-transformresources.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-transformjob-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-transformjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-transformjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-transformjob-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
A timestamp that shows when the transform Job was created.

`TransformEndTime`  <a name="TransformEndTime-fn::getatt"></a>
Indicates when the transform job has been completed, or has stopped or failed. You are billed for the time interval between this time and the value of `TransformStartTime`.

`TransformJobArn`  <a name="TransformJobArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the transform job.

`TransformJobName`  <a name="TransformJobName-fn::getatt"></a>
The name of the transform job.

`TransformJobStatus`  <a name="TransformJobStatus-fn::getatt"></a>
The status of the transform job.
Transform job statuses are:
+ `InProgress` - The job is in progress.
+ `Completed` - The job has completed.
+ `Failed` - The transform job has failed. To see the reason for the failure, see the `FailureReason` field in the response to a `DescribeTransformJob` call.
+ `Stopping` - The transform job is stopping.
+ `Stopped` - The transform job has stopped.

`TransformStartTime`  <a name="TransformStartTime-fn::getatt"></a>
Indicates when the transform job starts on ML instances. You are billed for the time interval between this time and the value of `TransformEndTime`.
