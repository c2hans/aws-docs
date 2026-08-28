---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_UpdatePrimaryRegion.html
---

# UpdatePrimaryRegion
<a name="API_UpdatePrimaryRegion"></a>

Changes the primary key of a multi-Region key.

This operation changes the replica key in the specified Region to a primary key and changes the former primary key to a replica key. For example, suppose you have a primary key in `us-east-1` and a replica key in `eu-west-2`. If you run `UpdatePrimaryRegion` with a `PrimaryRegion` value of `eu-west-2`, the primary key is now the key in `eu-west-2`, and the key in `us-east-1` becomes a replica key. For details, see [Change the primary key in a set of multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-update.html) in the * AWS Key Management Service Developer Guide*.

This operation supports *multi-Region keys*, an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one AWS Region and decrypt it in a different AWS Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.

The *primary key* of a multi-Region key is the source for properties that are always shared by primary and replica keys, including the key material, [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id), [key spec](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-spec), [key usage](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-usage), [key material origin](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-origin), and [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html). It's the only key that can be replicated. You cannot [delete the primary key](https://docs.aws.amazon.com/kms/latest/APIReference/API_ScheduleKeyDeletion.html) until all replica keys are deleted.

The key ID and primary Region that you specify uniquely identify the replica key that will become the primary key. The primary Region must already have a replica key. This operation does not create a KMS key in the specified Region. To find the replica keys, use the [DescribeKey](API_DescribeKey.md) operation on the primary key or any replica key. To create a replica key, use the [ReplicateKey](API_ReplicateKey.md) operation.

You can run this operation while using the affected multi-Region keys in cryptographic operations. This operation should not delay, interrupt, or cause failures in cryptographic operations.

Even after this operation completes, the process of updating the primary Region might still be in progress for a few more seconds. Operations such as `DescribeKey` might display both the old and new primary keys as replicas. The old and new primary keys have a transient key state of `Updating`. The original key state is restored when the update is complete. While the key state is `Updating`, you can use the keys in cryptographic operations, but you cannot replicate the new primary key or perform certain management operations, such as enabling or disabling these keys. For details about the `Updating` key state, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

This operation does not return any output. To verify that primary key is changed, use the [DescribeKey](API_DescribeKey.md) operation.

 **Cross-account use**: No. You cannot use this operation in a different AWS account.

 **Required permissions**:
+  `kms:UpdatePrimaryRegion` on the current primary key (in the primary key's Region). Include this permission primary key's key policy.
+  `kms:UpdatePrimaryRegion` on the current replica key (in the replica key's Region). Include this permission in the replica key's key policy.

 **Related operations**
+  [CreateKey](API_CreateKey.md)
+  [ReplicateKey](API_ReplicateKey.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_UpdatePrimaryRegion_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}",
   "PrimaryRegion": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePrimaryRegion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_UpdatePrimaryRegion_RequestSyntax) **   <a name="KMS-UpdatePrimaryRegion-request-KeyId"></a>
Identifies the current primary key. When the operation completes, this KMS key will be a replica key.
Specify the key ID or key ARN of a multi-Region primary key.
For example:
+ Key ID: `mrk-1234abcd12ab34cd56ef1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [PrimaryRegion](#API_UpdatePrimaryRegion_RequestSyntax) **   <a name="KMS-UpdatePrimaryRegion-request-PrimaryRegion"></a>
The AWS Region of the new primary key. Enter the Region ID, such as `us-east-1` or `ap-southeast-2`. There must be an existing replica key in this Region.
When the operation completes, the multi-Region key in this Region will be the primary key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-z]+-){2,3}\d+$`
Required: Yes

## Response Elements
<a name="API_UpdatePrimaryRegion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdatePrimaryRegion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledException **
The request was rejected because the specified KMS key is not enabled.
HTTP Status Code: 400

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** KMSInvalidStateException **
The request was rejected because the state of the specified resource is not valid for this request.
This exceptions means one of the following:
+ The key state of the KMS key is not compatible with the operation.

  To find the key state, use the [DescribeKey](API_DescribeKey.md) operation. For more information about which key states are compatible with each AWS KMS operation, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * * AWS Key Management Service Developer Guide* *.
+ For cryptographic operations on KMS keys in custom key stores, this exception represents a general failure with many possible causes. To identify the cause, see the error message that accompanies the exception.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePrimaryRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/UpdatePrimaryRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/UpdatePrimaryRegion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
