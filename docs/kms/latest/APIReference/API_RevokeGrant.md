---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_RevokeGrant.html
---

# RevokeGrant
<a name="API_RevokeGrant"></a>

Deletes the specified grant. You revoke a grant to terminate the permissions that the grant allows. For more information, see [Retiring and revoking grants](https://docs.aws.amazon.com/kms/latest/developerguide/grant-delete.html) in the * * AWS Key Management Service Developer Guide* *.

When you create, retire, or revoke a grant, there might be a brief delay, usually less than five minutes, until the grant is available throughout AWS KMS. This state is known as *eventual consistency*. For details, see [Eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-eventual-consistency) in the * * AWS Key Management Service Developer Guide* *.

For detailed information about grants, including grant terminology, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the * * AWS Key Management Service Developer Guide* *. For examples of creating grants in several programming languages, see [Use CreateGrant with an AWS SDK or CLI](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateGrant_section.html).

 **Cross-account use**: Yes. To perform this operation on a KMS key in a different AWS account, specify the key ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:RevokeGrant](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy).

 **Related operations:**
+  [CreateGrant](API_CreateGrant.md)
+  [ListGrants](API_ListGrants.md)
+  [ListRetirableGrants](API_ListRetirableGrants.md)
+  [RetireGrant](API_RetireGrant.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_RevokeGrant_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "GrantId": "{{string}}",
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_RevokeGrant_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [GrantId](#API_RevokeGrant_RequestSyntax) **   <a name="KMS-RevokeGrant-request-GrantId"></a>
Identifies the grant to revoke. To get the grant ID, use [CreateGrant](API_CreateGrant.md), [ListGrants](API_ListGrants.md), or [ListRetirableGrants](API_ListRetirableGrants.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [KeyId](#API_RevokeGrant_RequestSyntax) **   <a name="KMS-RevokeGrant-request-KeyId"></a>
A unique identifier for the KMS key associated with the grant. To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different AWS account, you must use the key ARN.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [DryRun](#API_RevokeGrant_RequestSyntax) **   <a name="KMS-RevokeGrant-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

## Response Elements
<a name="API_RevokeGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RevokeGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** DryRunOperationException **
 The request was rejected because the DryRun parameter was specified.
HTTP Status Code: 400

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** InvalidGrantIdException **
The request was rejected because the specified `GrantId` is not valid.
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

## Examples
<a name="API_RevokeGrant_Examples"></a>

### Example Request
<a name="API_RevokeGrant_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-west-2.amazonaws.com
Content-Length: 128
X-Amz-Target: TrentService.RevokeGrant
X-Amz-Date: 20161210T000739Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161210/us-west-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=3f4073c96c38c8bc006b3a74a67fb2108cfe2d6ff23f96f09047924919806a7d

{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "GrantId": "f271e8328717f8bde5d03f4981f06a6b3fc18bcae2da12ac38bd9186e7925d11"
}
```

### Example Response
<a name="API_RevokeGrant_Example_2"></a>

This example illustrates one usage of RevokeGrant.

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 10 Dec 2016 00:07:40 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: aa49887b-be6c-11e6-b749-7394871b1b43
```

## See Also
<a name="API_RevokeGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/RevokeGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/RevokeGrant)
