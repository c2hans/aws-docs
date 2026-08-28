---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamEncryptionConfiguration.html
---

# DeliveryStreamEncryptionConfiguration
<a name="API_DeliveryStreamEncryptionConfiguration"></a>

Contains information about the server-side encryption (SSE) status for the delivery stream, the type customer master key (CMK) in use, if any, and the ARN of the CMK. You can get `DeliveryStreamEncryptionConfiguration` by invoking the [DescribeDeliveryStream](API_DescribeDeliveryStream.md) operation.

## Contents
<a name="API_DeliveryStreamEncryptionConfiguration_Contents"></a>

 ** FailureDescription **   <a name="Firehose-Type-DeliveryStreamEncryptionConfiguration-FailureDescription"></a>
Provides details in case one of the following operations fails due to an error related to KMS: [CreateDeliveryStream](API_CreateDeliveryStream.md), [DeleteDeliveryStream](API_DeleteDeliveryStream.md), [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md), [StopDeliveryStreamEncryption](API_StopDeliveryStreamEncryption.md).
Type: [FailureDescription](API_FailureDescription.md) object
Required: No

 ** KeyARN **   <a name="Firehose-Type-DeliveryStreamEncryptionConfiguration-KeyARN"></a>
If `KeyType` is `CUSTOMER_MANAGED_CMK`, this field contains the ARN of the customer managed CMK. If `KeyType` is ` AWS_OWNED_CMK`, `DeliveryStreamEncryptionConfiguration` doesn't contain a value for `KeyARN`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:kms:[a-zA-Z0-9\-]+:\d{12}:key/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** KeyType **   <a name="Firehose-Type-DeliveryStreamEncryptionConfiguration-KeyType"></a>
Indicates the type of customer master key (CMK) that is used for encryption. The default setting is ` AWS_OWNED_CMK`. For more information about CMKs, see [Customer Master Keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys).
Type: String
Valid Values: `AWS_OWNED_CMK | CUSTOMER_MANAGED_CMK`
Required: No

 ** Status **   <a name="Firehose-Type-DeliveryStreamEncryptionConfiguration-Status"></a>
This is the server-side encryption (SSE) status for the Firehose stream. For a full description of the different values of this status, see [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md) and [StopDeliveryStreamEncryption](API_StopDeliveryStreamEncryption.md). If this status is `ENABLING_FAILED` or `DISABLING_FAILED`, it is the status of the most recent attempt to enable or disable SSE, respectively.
Type: String
Valid Values: `ENABLED | ENABLING | ENABLING_FAILED | DISABLED | DISABLING | DISABLING_FAILED`
Required: No

## See Also
<a name="API_DeliveryStreamEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DeliveryStreamEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DeliveryStreamEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DeliveryStreamEncryptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
