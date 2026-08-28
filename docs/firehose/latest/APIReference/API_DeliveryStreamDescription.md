---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamDescription.html
---

# DeliveryStreamDescription
<a name="API_DeliveryStreamDescription"></a>

Contains information about a Firehose stream.

## Contents
<a name="API_DeliveryStreamDescription_Contents"></a>

 ** DeliveryStreamARN **   <a name="Firehose-Type-DeliveryStreamDescription-DeliveryStreamARN"></a>
The Amazon Resource Name (ARN) of the Firehose stream. For more information, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:firehose:[a-zA-Z0-9\-]+:\d{12}:deliverystream/[a-zA-Z0-9._-]+`
Required: Yes

 ** DeliveryStreamName **   <a name="Firehose-Type-DeliveryStreamDescription-DeliveryStreamName"></a>
The name of the Firehose stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** DeliveryStreamStatus **   <a name="Firehose-Type-DeliveryStreamDescription-DeliveryStreamStatus"></a>
The status of the Firehose stream. If the status of a Firehose stream is `CREATING_FAILED`, this status doesn't change, and you can't invoke `CreateDeliveryStream` again on it. However, you can invoke the [DeleteDeliveryStream](API_DeleteDeliveryStream.md) operation to delete it.
Type: String
Valid Values: `CREATING | CREATING_FAILED | DELETING | DELETING_FAILED | ACTIVE`
Required: Yes

 ** DeliveryStreamType **   <a name="Firehose-Type-DeliveryStreamDescription-DeliveryStreamType"></a>
The Firehose stream type. This can be one of the following values:
+  `DirectPut`: Provider applications access the Firehose stream directly.
+  `KinesisStreamAsSource`: The Firehose stream uses a Kinesis data stream as a source.
Type: String
Valid Values: `DirectPut | KinesisStreamAsSource | MSKAsSource | DatabaseAsSource`
Required: Yes

 ** Destinations **   <a name="Firehose-Type-DeliveryStreamDescription-Destinations"></a>
The destinations.
Type: Array of [DestinationDescription](API_DestinationDescription.md) objects
Required: Yes

 ** HasMoreDestinations **   <a name="Firehose-Type-DeliveryStreamDescription-HasMoreDestinations"></a>
Indicates whether there are more destinations available to list.
Type: Boolean
Required: Yes

 ** VersionId **   <a name="Firehose-Type-DeliveryStreamDescription-VersionId"></a>
Each time the destination is updated for a Firehose stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[0-9]+`
Required: Yes

 ** CreateTimestamp **   <a name="Firehose-Type-DeliveryStreamDescription-CreateTimestamp"></a>
The date and time that the Firehose stream was created.
Type: Timestamp
Required: No

 ** DeliveryStreamEncryptionConfiguration **   <a name="Firehose-Type-DeliveryStreamDescription-DeliveryStreamEncryptionConfiguration"></a>
Indicates the server-side encryption (SSE) status for the Firehose stream.
Type: [DeliveryStreamEncryptionConfiguration](API_DeliveryStreamEncryptionConfiguration.md) object
Required: No

 ** FailureDescription **   <a name="Firehose-Type-DeliveryStreamDescription-FailureDescription"></a>
Provides details in case one of the following operations fails due to an error related to KMS: [CreateDeliveryStream](API_CreateDeliveryStream.md), [DeleteDeliveryStream](API_DeleteDeliveryStream.md), [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md), [StopDeliveryStreamEncryption](API_StopDeliveryStreamEncryption.md).
Type: [FailureDescription](API_FailureDescription.md) object
Required: No

 ** LastUpdateTimestamp **   <a name="Firehose-Type-DeliveryStreamDescription-LastUpdateTimestamp"></a>
The date and time that the Firehose stream was last updated.
Type: Timestamp
Required: No

 ** Source **   <a name="Firehose-Type-DeliveryStreamDescription-Source"></a>
If the `DeliveryStreamType` parameter is `KinesisStreamAsSource`, a [SourceDescription](API_SourceDescription.md) object describing the source Kinesis data stream.
Type: [SourceDescription](API_SourceDescription.md) object
Required: No

## See Also
<a name="API_DeliveryStreamDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DeliveryStreamDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DeliveryStreamDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DeliveryStreamDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
