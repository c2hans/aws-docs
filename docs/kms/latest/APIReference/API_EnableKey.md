---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_EnableKey.html
---

# EnableKey
<a name="API_EnableKey"></a>

Sets the key state of a KMS key to enabled. This allows you to use the KMS key for [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html#cryptographic-operations).

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:EnableKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations**: [DisableKey](API_DisableKey.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_EnableKey_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_EnableKey_RequestSyntax) **   <a name="KMS-EnableKey-request-KeyId"></a>
Identifies the KMS key to enable.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Elements
<a name="API_EnableKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableKey_Errors"></a>

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

 ** LimitExceededException **
The request was rejected because a length constraint or quota was exceeded. For more information, see [Quotas](https://docs.aws.amazon.com/kms/latest/developerguide/limits.html) in the * AWS Key Management Service Developer Guide*.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## Examples
<a name="API_EnableKey_Examples"></a>

### Example Request
<a name="API_EnableKey_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 48
X-Amz-Target: TrentService.EnableKey
X-Amz-Date: 20161107T221800Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161107/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=74d02e36580c1759255dfef66f1e51f3542e469de8c7c8fa5fb21c042e518295

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_EnableKey_Example_2"></a>

This example illustrates one usage of EnableKey.

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 07 Nov 2016 22:18:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: 0b588162-a538-11e6-b4ed-059c103e7a90
```

## See Also
<a name="API_EnableKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/EnableKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/EnableKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/EnableKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/EnableKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/EnableKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/EnableKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/EnableKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/EnableKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/EnableKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/EnableKey)
