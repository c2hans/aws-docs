---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ReplicateKey.html
---

# ReplicateKey
<a name="API_ReplicateKey"></a>

Replicates a multi-Region key into the specified Region. This operation creates a multi-Region replica key based on a multi-Region primary key in a different Region of the same AWS partition. You can create multiple replicas of a primary key, but each must be in a different Region. To create a multi-Region primary key, use the [CreateKey](API_CreateKey.md) operation.

This operation supports *multi-Region keys*, an AWS KMS feature that lets you create multiple interoperable KMS keys in different AWS Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one AWS Region and decrypt it in a different AWS Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the * AWS Key Management Service Developer Guide*.

A *replica key* is a fully-functional KMS key that can be used independently of its primary and peer replica keys. A primary key and its replica keys share properties that make them interoperable. They have the same [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) and key material. They also have the same key spec, key usage, key material origin, and automatic key rotation status. AWS KMS automatically synchronizes these shared properties among related multi-Region keys. All other properties of a replica key can differ, including its [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html), [tags](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html), [aliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html), and [key state](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html). AWS KMS pricing and quotas for KMS keys apply to each primary key and replica key.

When this operation completes, the new replica key has a transient key state of `Creating`. This key state changes to `Enabled` (or `PendingImport`) after a few seconds when the process of creating the new replica key is complete. While the key state is `Creating`, you can manage key, but you cannot yet use it in cryptographic operations. If you are creating and using the replica key programmatically, retry on `KMSInvalidStateException` or call `DescribeKey` to check its `KeyState` value before using it. For details about the `Creating` key state, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

You cannot create more than one replica of a primary key in any Region. If the Region already includes a replica of the key you're trying to replicate, `ReplicateKey` returns an `AlreadyExistsException` error. If the key state of the existing replica is `PendingDeletion`, you can cancel the scheduled key deletion ([CancelKeyDeletion](API_CancelKeyDeletion.md)) or wait for the key to be deleted. The new replica key you create will have the same [shared properties](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-sync-properties) as the original replica key.

The AWS CloudTrail log of a `ReplicateKey` operation records a `ReplicateKey` operation in the primary key's Region and a [CreateKey](API_CreateKey.md) operation in the replica key's Region.

If you replicate a multi-Region primary key with imported key material, the replica key is created with no key material. You must import the same key material that you imported into the primary key.

To convert a replica key to a primary key, use the [UpdatePrimaryRegion](API_UpdatePrimaryRegion.md) operation.

**Note**
 `ReplicateKey` uses different default values for the `KeyPolicy` and `Tags` parameters than those used in the AWS KMS console. For details, see the parameter descriptions.

 **Cross-account use**: No. You cannot use this operation to create a replica key in a different AWS account.

 **Required permissions**:
+  `kms:ReplicateKey` on the primary key (in the primary key's Region). Include this permission in the primary key's key policy.
+  `kms:CreateKey` in an IAM policy in the replica Region.
+ To use the `Tags` parameter, `kms:TagResource` in an IAM policy in the replica Region.

 **Related operations**
+  [CreateKey](API_CreateKey.md)
+  [UpdatePrimaryRegion](API_UpdatePrimaryRegion.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ReplicateKey_RequestSyntax"></a>

```
{
   "BypassPolicyLockoutSafetyCheck": {{boolean}},
   "Description": "{{string}}",
   "KeyId": "{{string}}",
   "Policy": "{{string}}",
   "ReplicaRegion": "{{string}}",
   "Tags": [
      {
         "TagKey": "{{string}}",
         "TagValue": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_ReplicateKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_ReplicateKey_RequestSyntax) **   <a name="KMS-ReplicateKey-request-KeyId"></a>
Identifies the multi-Region primary key that is being replicated. To determine whether a KMS key is a multi-Region primary key, use the [DescribeKey](API_DescribeKey.md) operation to check the value of the `MultiRegionKeyType` property.
Specify the key ID or key ARN of a multi-Region primary key.
For example:
+ Key ID: `mrk-1234abcd12ab34cd56ef1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [ReplicaRegion](#API_ReplicateKey_RequestSyntax) **   <a name="KMS-ReplicateKey-request-ReplicaRegion"></a>
The Region ID of the AWS Region for this replica key.
Enter the Region ID, such as `us-east-1` or `ap-southeast-2`. For a list of AWS Regions in which AWS KMS is supported, see [AWS KMS service endpoints](https://docs.aws.amazon.com/general/latest/gr/kms.html#kms_region) in the *Amazon Web Services General Reference*.
The replica must be in a different AWS Region than its primary key and other replicas of that primary key, but in the same AWS partition. AWS KMS must be available in the replica Region. If the Region is not enabled by default, the AWS account must be enabled in the Region. For information about AWS partitions, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference*. For information about enabling and disabling Regions, see [Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) and [Disabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-disable) in the *Amazon Web Services General Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([a-z]+-){2,3}\d+$`
Required: Yes

 ** [BypassPolicyLockoutSafetyCheck](#API_ReplicateKey_RequestSyntax) **   <a name="KMS-ReplicateKey-request-BypassPolicyLockoutSafetyCheck"></a>
Skips ("bypasses") the key policy lockout safety check. The default value is false.
Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.
For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the * AWS Key Management Service Developer Guide*.
Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key.
Type: Boolean
Required: No

 ** [Description](#API_ReplicateKey_RequestSyntax) **   <a name="KMS-ReplicateKey-request-Description"></a>
A description of the KMS key. The default value is an empty string (no description).
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
The description is not a shared property of multi-Region keys. You can specify the same description or a different description for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Required: No

 ** [Policy](#API_ReplicateKey_RequestSyntax) **   <a name="KMS-ReplicateKey-request-Policy"></a>
The key policy to attach to the KMS key. This parameter is optional. If you do not provide a key policy, AWS KMS attaches the [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html) to the KMS key.
The key policy is not a shared property of multi-Region keys. You can specify the same key policy or a different key policy for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property.
If you provide a key policy, it must meet the following criteria:
+ The key policy must allow the calling principal to make a subsequent `PutKeyPolicy` request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the * AWS Key Management Service Developer Guide*. (To omit this condition, set `BypassPolicyLockoutSafetyCheck` to true.)
+ Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal, you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the * AWS Identity and Access Management User Guide*.
A key policy document can include only the following characters:
+ Printable ASCII characters from the space character (`\u0020`) through the end of the ASCII character range.
+ Printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`).
+ The tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`) special characters
For information about key policies, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the * AWS Key Management Service Developer Guide*. For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the * * AWS Identity and Access Management User Guide* *.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: No

 ** [Tags](#API_ReplicateKey_RequestSyntax) **   <a name="KMS-ReplicateKey-request-Tags"></a>
Assigns one or more tags to the replica key. Use this parameter to tag the KMS key when it is created. To tag an existing KMS key, use the [TagResource](API_TagResource.md) operation.
Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.
Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see [ABAC for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the * AWS Key Management Service Developer Guide*.
To use this parameter, you must have [kms:TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission in an IAM policy.
Tags are not a shared property of multi-Region keys. You can specify the same tags or different tags for each key in a set of related multi-Region keys. AWS KMS does not synchronize this property.
Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You cannot have more than one tag on a KMS key with the same tag key. If you specify an existing tag key with a different tag value, AWS KMS replaces the current tag value with the specified one.
When you add tags to an AWS resource, AWS generates a cost allocation report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For details, see [Tags in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_ReplicateKey_ResponseSyntax"></a>

```
{
   "ReplicaKeyMetadata": {
      "Arn": "string",
      "AWSAccountId": "string",
      "CloudHsmClusterId": "string",
      "CreationDate": number,
      "CurrentKeyMaterialId": "string",
      "CustomerMasterKeySpec": "string",
      "CustomKeyStoreId": "string",
      "DeletionDate": number,
      "Description": "string",
      "Enabled": boolean,
      "EncryptionAlgorithms": [ "string" ],
      "ExpirationModel": "string",
      "KeyAgreementAlgorithms": [ "string" ],
      "KeyId": "string",
      "KeyManager": "string",
      "KeySpec": "string",
      "KeyState": "string",
      "KeyUsage": "string",
      "MacAlgorithms": [ "string" ],
      "MultiRegion": boolean,
      "MultiRegionConfiguration": {
         "MultiRegionKeyType": "string",
         "PrimaryKey": {
            "Arn": "string",
            "Region": "string"
         },
         "ReplicaKeys": [
            {
               "Arn": "string",
               "Region": "string"
            }
         ]
      },
      "Origin": "string",
      "PendingDeletionWindowInDays": number,
      "SigningAlgorithms": [ "string" ],
      "ValidTo": number,
      "XksKeyConfiguration": {
         "Id": "string"
      }
   },
   "ReplicaPolicy": "string",
   "ReplicaTags": [
      {
         "TagKey": "string",
         "TagValue": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ReplicateKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReplicaKeyMetadata](#API_ReplicateKey_ResponseSyntax) **   <a name="KMS-ReplicateKey-response-ReplicaKeyMetadata"></a>
Displays details about the new replica key, including its Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN)) and [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html). It also includes the ARN and AWS Region of its primary key and other replica keys.
Type: [KeyMetadata](API_KeyMetadata.md) object

 ** [ReplicaPolicy](#API_ReplicateKey_ResponseSyntax) **   <a name="KMS-ReplicateKey-response-ReplicaPolicy"></a>
The key policy of the new replica key. The value is a key policy document in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

 ** [ReplicaTags](#API_ReplicateKey_ResponseSyntax) **   <a name="KMS-ReplicateKey-response-ReplicaTags"></a>
The tags on the new replica key. The value is a list of tag key and tag value pairs.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ReplicateKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AlreadyExistsException **
The request was rejected because it attempted to create a resource that already exists.
HTTP Status Code: 400

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

 ** LimitExceededException **
The request was rejected because a length constraint or quota was exceeded. For more information, see [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the * AWS Key Management Service Developer Guide*.
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **
The request was rejected because the specified policy is not syntactically or semantically correct.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** TagException **
The request was rejected because one or more tags are not valid.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## See Also
<a name="API_ReplicateKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ReplicateKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ReplicateKey)
