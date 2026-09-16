---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyRotationStatus.html
---

# GetKeyRotationStatus
<a name="API_GetKeyRotationStatus"></a>

Provides detailed information about the rotation status for a KMS key, including whether [automatic rotation of the key material](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable-disable.html) is enabled for the specified KMS key, the [rotation period](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotation-period), and the next scheduled rotation date.

Automatic key rotation is supported only on symmetric encryption KMS keys. You cannot enable automatic rotation of [asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html), [HMAC KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html), KMS keys with [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html), or KMS keys in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). To enable or disable automatic rotation of a set of related [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#multi-region-rotate), set the property on the primary key.

You can enable ([EnableKeyRotation](API_EnableKeyRotation.md)) and disable automatic rotation ([DisableKeyRotation](API_DisableKeyRotation.md)) of the key material in customer managed KMS keys. Key material rotation of [AWS managed KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key) is not configurable. AWS KMS always rotates the key material in AWS managed KMS keys every year. The key rotation status for AWS managed KMS keys is always `true`.

You can perform on-demand ([RotateKeyOnDemand](API_RotateKeyOnDemand.md)) rotation of the key material in customer managed KMS keys, regardless of whether or not automatic key rotation is enabled. You can use GetKeyRotationStatus to identify the date and time that an in progress on-demand rotation was initiated. You can use [ListKeyRotations](API_ListKeyRotations.md) to view the details of completed rotations.

**Note**
In May 2022, AWS KMS changed the rotation schedule for AWS managed keys from every three years to every year. For details, see [EnableKeyRotation](API_EnableKeyRotation.md).

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.
+ Disabled: The key rotation status does not change when you disable a KMS key. However, while the KMS key is disabled, AWS KMS does not rotate the key material. When you re-enable the KMS key, rotation resumes. If the key material in the re-enabled KMS key hasn't been rotated in one year, AWS KMS rotates it immediately, and every year thereafter. If it's been less than a year since the key material in the re-enabled KMS key was rotated, the KMS key resumes its prior rotation schedule.
+ Pending deletion: While a KMS key is pending deletion, its key rotation status is `false` and AWS KMS does not rotate the key material. If you cancel the deletion, the original key rotation status returns to `true`.

 **Cross-account use**: Yes. To perform this operation on a KMS key in a different AWS account, specify the key ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [DisableKeyRotation](API_DisableKeyRotation.md)
+  [EnableKeyRotation](API_EnableKeyRotation.md)
+  [ListKeyRotations](API_ListKeyRotations.md)
+  [RotateKeyOnDemand](API_RotateKeyOnDemand.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GetKeyRotationStatus_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetKeyRotationStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GetKeyRotationStatus_RequestSyntax) **   <a name="KMS-GetKeyRotationStatus-request-KeyId"></a>
Gets the rotation status for the specified KMS key.
Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different AWS account, you must use the key ARN.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_GetKeyRotationStatus_ResponseSyntax"></a>

```
{
   "KeyId": "string",
   "KeyRotationEnabled": boolean,
   "NextRotationDate": number,
   "OnDemandRotationStartDate": number,
   "RotationPeriodInDays": number
}
```

## Response Elements
<a name="API_GetKeyRotationStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [KeyId](#API_GetKeyRotationStatus_ResponseSyntax) **   <a name="KMS-GetKeyRotationStatus-response-KeyId"></a>
Identifies the specified symmetric encryption KMS key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [KeyRotationEnabled](#API_GetKeyRotationStatus_ResponseSyntax) **   <a name="KMS-GetKeyRotationStatus-response-KeyRotationEnabled"></a>
A Boolean value that specifies whether key rotation is enabled.
Type: Boolean

 ** [NextRotationDate](#API_GetKeyRotationStatus_ResponseSyntax) **   <a name="KMS-GetKeyRotationStatus-response-NextRotationDate"></a>
The next date that AWS KMS will automatically rotate the key material.
Type: Timestamp

 ** [OnDemandRotationStartDate](#API_GetKeyRotationStatus_ResponseSyntax) **   <a name="KMS-GetKeyRotationStatus-response-OnDemandRotationStartDate"></a>
Identifies the date and time that an in progress on-demand rotation was initiated.
 AWS KMS uses a background process to perform rotations. As a result, there might be a slight delay between initiating on-demand key rotation and the rotation's completion. Once the on-demand rotation is complete, AWS KMS removes this field from the response. You can use [ListKeyRotations](API_ListKeyRotations.md) to view the details of the completed on-demand rotation.
Type: Timestamp

 ** [RotationPeriodInDays](#API_GetKeyRotationStatus_ResponseSyntax) **   <a name="KMS-GetKeyRotationStatus-response-RotationPeriodInDays"></a>
The number of days between each automatic rotation. The default value is 365 days.
Type: Integer
Valid Range: Minimum value of 90. Maximum value of 2560.

## Errors
<a name="API_GetKeyRotationStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

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

## Examples
<a name="API_GetKeyRotationStatus_Examples"></a>

### Example Request
<a name="API_GetKeyRotationStatus_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 49
X-Amz-Target: TrentService.GetKeyRotationStatus
X-Amz-Date: 20161115T005817Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161115/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=282cb3a4a5d10684ff6c363300c34569a0707c4d503b88778e78cc51ea52f9be

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_GetKeyRotationStatus_Example_2"></a>

This example illustrates one usage of GetKeyRotationStatus.

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 15 Nov 2016 00:58:18 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 28
Connection: keep-alive
x-amzn-RequestId: 98b59330-aace-11e6-aff0-8333261e2fbd

{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "KeyRotationEnabled": true,
    "NextRotationDate": "2024-02-14T18:14:33.587000+00:00",
    "RotationPeriodInDays": 365
}
```

## See Also
<a name="API_GetKeyRotationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GetKeyRotationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GetKeyRotationStatus)
