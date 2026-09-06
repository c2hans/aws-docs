---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ModelTrainingDataChannel.html
---

# ModelTrainingDataChannel
<a name="API_ModelTrainingDataChannel"></a>

Information about the model training data channel. A training data channel is a named data source that the training algorithms can consume.

## Contents
<a name="API_ModelTrainingDataChannel_Contents"></a>

 ** channelName **   <a name="API-Type-ModelTrainingDataChannel-channelName"></a>
The name of the training data channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9\.\-_]+`
Required: Yes

 ** mlInputChannelArn **   <a name="API-Type-ModelTrainingDataChannel-mlInputChannelArn"></a>
The Amazon Resource Name (ARN) of the ML input channel for this model training data channel.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/ml-input-channel/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** s3DataDistributionType **   <a name="API-Type-ModelTrainingDataChannel-s3DataDistributionType"></a>
Specifies how the training data stored in Amazon S3 should be distributed to training instances. This parameter controls the data distribution strategy for the training job:
+  `FullyReplicated` - The entire dataset is replicated on each training instance. This is suitable for smaller datasets and algorithms that require access to the complete dataset.
+  `ShardedByS3Key` - The dataset is distributed across training instances based on Amazon S3 key names. This is suitable for larger datasets and distributed training scenarios where each instance processes a subset of the data.
Type: String
Valid Values: `FullyReplicated | ShardedByS3Key`
Required: No

## See Also
<a name="API_ModelTrainingDataChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ModelTrainingDataChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ModelTrainingDataChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ModelTrainingDataChannel)
