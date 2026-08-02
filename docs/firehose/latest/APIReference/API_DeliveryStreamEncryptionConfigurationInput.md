---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DeliveryStreamEncryptionConfigurationInput.html
---

# DeliveryStreamEncryptionConfigurationInput
<a name="API_DeliveryStreamEncryptionConfigurationInput"></a>

Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).

## Contents
<a name="API_DeliveryStreamEncryptionConfigurationInput_Contents"></a>

 ** KeyType **   <a name="Firehose-Type-DeliveryStreamEncryptionConfigurationInput-KeyType"></a>
Indicates the type of customer master key (CMK) to use for encryption. The default setting is ` AWS_OWNED_CMK`. For more information about CMKs, see [Customer Master Keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). When you invoke [CreateDeliveryStream](API_CreateDeliveryStream.md) or [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md) with `KeyType` set to CUSTOMER\_MANAGED\_CMK, Firehose invokes the Amazon KMS operation [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) to create a grant that allows the Firehose service to use the customer managed CMK to perform encryption and decryption. Firehose manages that grant.
When you invoke [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md) to change the CMK for a Firehose stream that is encrypted with a customer managed CMK, Firehose schedules the grant it had on the old CMK for retirement.
You can use a CMK of type CUSTOMER\_MANAGED\_CMK to encrypt up to 500 Firehose streams. If a [CreateDeliveryStream](API_CreateDeliveryStream.md) or [StartDeliveryStreamEncryption](API_StartDeliveryStreamEncryption.md) operation exceeds this limit, Firehose throws a `LimitExceededException`.
To encrypt your Firehose stream, use symmetric CMKs. Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see [About Symmetric and Asymmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html) in the AWS Key Management Service developer guide.
Type: String
Valid Values: `AWS_OWNED_CMK | CUSTOMER_MANAGED_CMK`
Required: Yes

 ** KeyARN **   <a name="Firehose-Type-DeliveryStreamEncryptionConfigurationInput-KeyARN"></a>
If you set `KeyType` to `CUSTOMER_MANAGED_CMK`, you must specify the Amazon Resource Name (ARN) of the CMK. If you set `KeyType` to ` AWS_OWNED_CMK`, Firehose uses a service-account CMK.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:.*:kms:[a-zA-Z0-9\-]+:\d{12}:key/[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## See Also
<a name="API_DeliveryStreamEncryptionConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DeliveryStreamEncryptionConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DeliveryStreamEncryptionConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DeliveryStreamEncryptionConfigurationInput)
