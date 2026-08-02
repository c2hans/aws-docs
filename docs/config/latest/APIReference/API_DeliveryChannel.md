---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html
---

# DeliveryChannel
<a name="API_DeliveryChannel"></a>

The channel through which AWS Config delivers notifications and updated configuration states.

## Contents
<a name="API_DeliveryChannel_Contents"></a>

 ** configSnapshotDeliveryProperties **   <a name="config-Type-DeliveryChannel-configSnapshotDeliveryProperties"></a>
The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
Type: [ConfigSnapshotDeliveryProperties](API_ConfigSnapshotDeliveryProperties.md) object
Required: No

 ** name **   <a name="config-Type-DeliveryChannel-name"></a>
The name of the delivery channel. By default, AWS Config assigns the name "default" when creating the delivery channel. To change the delivery channel name, you must use the DeleteDeliveryChannel action to delete your current delivery channel, and then you must use the PutDeliveryChannel command to create a delivery channel that has the desired name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** s3BucketName **   <a name="config-Type-DeliveryChannel-s3BucketName"></a>
The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.
If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see [Permissions for the Amazon S3 Bucket](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html) in the * AWS Config Developer Guide*.
Type: String
Required: No

 ** s3KeyPrefix **   <a name="config-Type-DeliveryChannel-s3KeyPrefix"></a>
The prefix for the specified Amazon S3 bucket.
Type: String
Required: No

 ** s3KmsKeyArn **   <a name="config-Type-DeliveryChannel-s3KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config. Must belong to the same Region as the destination S3 bucket.
Type: String
Required: No

 ** snsTopicARN **   <a name="config-Type-DeliveryChannel-snsTopicARN"></a>
The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.
If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see [Permissions for the Amazon SNS Topic](https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html) in the * AWS Config Developer Guide*.
Type: String
Required: No

## See Also
<a name="API_DeliveryChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DeliveryChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DeliveryChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DeliveryChannel)
