---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_DisableKeyRotation.html
---

# DisableKeyRotation
<a name="API_DisableKeyRotation"></a>

Disables [automatic rotation of the key material](https://docs.aws.amazon.com/kms/latest/developerguide/rotating-keys-enable-disable.html) of the specified symmetric encryption KMS key.

Automatic key rotation is supported only on symmetric encryption KMS keys. You cannot enable automatic rotation of [asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html), [HMAC KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html), KMS keys with [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html), or KMS keys in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html). To enable or disable automatic rotation of a set of related [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#multi-region-rotate), set the property on the primary key.

You can enable ([EnableKeyRotation](API_EnableKeyRotation.md)) and disable automatic rotation of the key material in [customer managed KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key). Key material rotation of [AWS managed KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-key) is not configurable. AWS KMS always rotates the key material for every year. Rotation of [AWS owned KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-key) varies.

**Note**
In May 2022, AWS KMS changed the rotation schedule for AWS managed keys from every three years to every year. For details, see [EnableKeyRotation](API_EnableKeyRotation.md).

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:DisableKeyRotation](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [EnableKeyRotation](API_EnableKeyRotation.md)
+  [GetKeyRotationStatus](API_GetKeyRotationStatus.md)
+  [ListKeyRotations](API_ListKeyRotations.md)
+  [RotateKeyOnDemand](API_RotateKeyOnDemand.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_DisableKeyRotation_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisableKeyRotation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_DisableKeyRotation_RequestSyntax) **   <a name="KMS-DisableKeyRotation-request-KeyId"></a>
Identifies a symmetric encryption KMS key. You cannot enable or disable automatic rotation of [asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html#asymmetric-cmks), [HMAC KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html), KMS keys with [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html), or KMS keys in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/key-store-overview.html).
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_DisableKeyRotation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableKeyRotation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## Examples
<a name="API_DisableKeyRotation_Examples"></a>

### Example Request
<a name="API_DisableKeyRotation_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 48
X-Amz-Target: TrentService.DisableKeyRotation
X-Amz-Date: 20161107T222236Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161107/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=2304622be05af2afa8c75bf784fb87b280c194746418b05d7af947c8c2bd8f04

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_DisableKeyRotation_Example_2"></a>

This example illustrates one usage of DisableKeyRotation.

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 07 Nov 2016 22:22:36 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: afd1c328-a538-11e6-861b-ad130425efbf
```

## See Also
<a name="API_DisableKeyRotation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/DisableKeyRotation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/DisableKeyRotation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
