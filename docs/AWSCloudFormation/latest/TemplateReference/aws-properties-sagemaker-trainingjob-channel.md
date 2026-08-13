---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob Channel
<a name="aws-properties-sagemaker-trainingjob-channel"></a>

A channel is a named input source that training algorithms can consume.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-channel-syntax.json"></a>

```
{
  "[ChannelName](#cfn-sagemaker-trainingjob-channel-channelname)" : {{String}},
  "[CompressionType](#cfn-sagemaker-trainingjob-channel-compressiontype)" : {{String}},
  "[ContentType](#cfn-sagemaker-trainingjob-channel-contenttype)" : {{String}},
  "[DataSource](#cfn-sagemaker-trainingjob-channel-datasource)" : {{DataSource}},
  "[InputMode](#cfn-sagemaker-trainingjob-channel-inputmode)" : {{String}},
  "[RecordWrapperType](#cfn-sagemaker-trainingjob-channel-recordwrappertype)" : {{String}},
  "[ShuffleConfig](#cfn-sagemaker-trainingjob-channel-shuffleconfig)" : {{ShuffleConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-channel-syntax.yaml"></a>

```
  [ChannelName](#cfn-sagemaker-trainingjob-channel-channelname): {{String}}
  [CompressionType](#cfn-sagemaker-trainingjob-channel-compressiontype): {{String}}
  [ContentType](#cfn-sagemaker-trainingjob-channel-contenttype): {{String}}
  [DataSource](#cfn-sagemaker-trainingjob-channel-datasource): {{
    DataSource}}
  [InputMode](#cfn-sagemaker-trainingjob-channel-inputmode): {{String}}
  [RecordWrapperType](#cfn-sagemaker-trainingjob-channel-recordwrappertype): {{String}}
  [ShuffleConfig](#cfn-sagemaker-trainingjob-channel-shuffleconfig): {{
    ShuffleConfig}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-channel-properties"></a>

`ChannelName`  <a name="cfn-sagemaker-trainingjob-channel-channelname"></a>
The name of the channel.
*Required*: Yes
*Type*: String
*Pattern*: `[A-Za-z0-9\.\-_]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompressionType`  <a name="cfn-sagemaker-trainingjob-channel-compressiontype"></a>
If training data is compressed, the compression type. The default value is `None`. `CompressionType` is used only in Pipe input mode. In File mode, leave this field unset or set it to None.
*Required*: No
*Type*: String
*Allowed values*: `None | Gzip`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContentType`  <a name="cfn-sagemaker-trainingjob-channel-contenttype"></a>
The MIME type of the data.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataSource`  <a name="cfn-sagemaker-trainingjob-channel-datasource"></a>
The location of the channel data.
*Required*: Yes
*Type*: [DataSource](aws-properties-sagemaker-trainingjob-datasource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputMode`  <a name="cfn-sagemaker-trainingjob-channel-inputmode"></a>
(Optional) The input mode to use for the data channel in a training job. If you don't set a value for `InputMode`, SageMaker uses the value set for `TrainingInputMode`. Use this parameter to override the `TrainingInputMode` setting in a [AlgorithmSpecification](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) request when you have a channel that needs a different input mode from the training job's general setting. To download the data from Amazon Simple Storage Service (Amazon S3) to the provisioned ML storage volume, and mount the directory to a Docker volume, use `File` input mode. To stream data directly from Amazon S3 to the container, choose `Pipe` input mode.
To use a model for incremental training, choose `File` input model.
*Required*: No
*Type*: String
*Allowed values*: `Pipe | File | FastFile`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordWrapperType`  <a name="cfn-sagemaker-trainingjob-channel-recordwrappertype"></a>

Specify RecordIO as the value when input data is in raw format but the training algorithm requires the RecordIO format. In this case, SageMaker wraps each individual S3 object in a RecordIO record. If the input data is already in RecordIO format, you don't need to set this attribute. For more information, see [Create a Dataset Using RecordIO](https://mxnet.apache.org/api/architecture/note_data_loading#data-format).
In File mode, leave this field unset or set it to None.
*Required*: No
*Type*: String
*Allowed values*: `None | RecordIO`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ShuffleConfig`  <a name="cfn-sagemaker-trainingjob-channel-shuffleconfig"></a>
A configuration for a shuffle option for input data in a channel. If you use `S3Prefix` for `S3DataType`, this shuffles the results of the S3 key prefix matches. If you use `ManifestFile`, the order of the S3 object references in the `ManifestFile` is shuffled. If you use `AugmentedManifestFile`, the order of the JSON lines in the `AugmentedManifestFile` is shuffled. The shuffling order is determined using the `Seed` value.
For Pipe input mode, shuffling is done at the start of every epoch. With large datasets this ensures that the order of the training data is different for each epoch, it helps reduce bias and possible overfitting. In a multi-node training job when ShuffleConfig is combined with `S3DataDistributionType` of `ShardedByS3Key`, the data is shuffled across nodes so that the content sent to a particular node on the first epoch might be sent to a different node on the second epoch.
*Required*: No
*Type*: [ShuffleConfig](aws-properties-sagemaker-trainingjob-shuffleconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
