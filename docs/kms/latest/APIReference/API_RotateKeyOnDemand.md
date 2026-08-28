---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_RotateKeyOnDemand.html
---

# RotateKeyOnDemand
<a name="API_RotateKeyOnDemand"></a>

Immediately initiates rotation of the key material of the specified symmetric encryption KMS key.

You can perform [on-demand rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-on-demand.html) of the key material in customer managed KMS keys, regardless of whether or not [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable-disable.html) is enabled. On-demand rotations do not change existing automatic rotation schedules. For example, consider a KMS key that has automatic key rotation enabled with a rotation period of 730 days. If the key is scheduled to automatically rotate on April 14, 2024, and you perform an on-demand rotation on April 10, 2024, the key will automatically rotate, as scheduled, on April 14, 2024 and every 730 days thereafter.

**Note**
You can perform on-demand key rotation a **maximum of 25 times** per KMS key. You can use the AWS KMS console to view the number of remaining on-demand rotations available for a KMS key.

You can use [GetKeyRotationStatus](API_GetKeyRotationStatus.md) to identify any in progress on-demand rotations. You can use [ListKeyRotations](API_ListKeyRotations.md) to identify the date that completed on-demand rotations were performed. You can monitor rotation of the key material for your KMS keys in AWS CloudTrail and Amazon CloudWatch.

On-demand key rotation is supported only on symmetric encryption KMS keys. You cannot perform on-demand rotation of [asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html), [HMAC KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html), or KMS keys in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). When you initiate on-demand key rotation on a symmetric encryption KMS key with imported key material, you must have already imported [new key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-import-key-material.html) and that key material's state should be `PENDING_ROTATION`. Use the `ListKeyRotations` operation to check the state of all key materials associated with a KMS key. To perform on-demand rotation of a set of related [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#multi-region-rotate), import new key material in the primary Region key, import the same key material in each replica Region key, and invoke the on-demand rotation on the primary Region key.

You cannot initiate on-demand rotation of [AWS managed KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key). AWS KMS always rotates the key material of AWS managed keys every year. Rotation of [AWS owned KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-key) is managed by the AWS service that owns the key.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:RotateKeyOnDemand](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [EnableKeyRotation](API_EnableKeyRotation.md)
+  [DisableKeyRotation](API_DisableKeyRotation.md)
+  [GetKeyRotationStatus](API_GetKeyRotationStatus.md)
+  [ImportKeyMaterial](API_ImportKeyMaterial.md)
+  [ListKeyRotations](API_ListKeyRotations.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_RotateKeyOnDemand_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_RotateKeyOnDemand_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_RotateKeyOnDemand_RequestSyntax) **   <a name="KMS-RotateKeyOnDemand-request-KeyId"></a>
Identifies a symmetric encryption KMS key. You cannot perform on-demand rotation of [asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html), [HMAC KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html), multi-Region KMS keys with [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html), or KMS keys in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). To perform on-demand rotation of a set of related [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#multi-region-rotate), invoke the on-demand rotation on the primary key.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_RotateKeyOnDemand_ResponseSyntax"></a>

```
{
   "KeyId": "string"
}
```

## Response Elements
<a name="API_RotateKeyOnDemand_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_RotateKeyOnDemand_ResponseSyntax) **   <a name="KMS-RotateKeyOnDemand-response-KeyId"></a>
Identifies the symmetric encryption KMS key that you initiated on-demand rotation on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_RotateKeyOnDemand_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request was rejected because an automatic rotation of this key is currently in progress or scheduled to begin within the next 20 minutes.
HTTP Status Code: 400

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

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

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## Examples
<a name="API_RotateKeyOnDemand_Examples"></a>

### Example Request
<a name="API_RotateKeyOnDemand_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 48
X-Amz-Target: TrentService.RotateKeyOnDemand
X-Amz-Date: 20240405T151426Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161107/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=4783e177036ca78627fe0cda9dcfdaf4ad7c8312d0e7c3d71d814b0c4cff1c0b

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_RotateKeyOnDemand_Example_2"></a>

This example illustrates one usage of RotateKeyOnDemand.

```
HTTP/1.1 200 OK
Server: Server
Date: Fri, 05 Apr 2024 15:14:26 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: 2077c3bf-a538-11e6-b6fb-794e83344f84

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

## See Also
<a name="API_RotateKeyOnDemand_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/RotateKeyOnDemand)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/RotateKeyOnDemand)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
