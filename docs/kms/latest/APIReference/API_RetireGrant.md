---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html
---

# RetireGrant
<a name="API_RetireGrant"></a>

Deletes a grant. Typically, you retire a grant when you no longer need its permissions. To identify the grant to retire, use a [grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token), or both the grant ID and a key identifier (key ID or key ARN) of the KMS key. The [CreateGrant](API_CreateGrant.md) operation returns both values.

This operation can be called by the *retiring principal* for a grant, by the *grantee principal* if the grant allows the `RetireGrant` operation, and by the AWS account in which the grant is created. It can also be called by principals to whom permission for retiring a grant is delegated.

For detailed information about grants, including grant terminology, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the * * AWS Key Management Service Developer Guide* *. For examples of creating grants in several programming languages, see [Use CreateGrant with an AWS SDK or CLI](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateGrant_section.html).

 **Cross-account use**: Yes. You can retire a grant on a KMS key in a different AWS account.

 **Required permissions**: Permission to retire a grant is determined primarily by the grant. For details, see [Retiring and revoking grants](https://docs.aws.amazon.com/kms/latest/developerguide/grant-delete.html) in the * AWS Key Management Service Developer Guide*.

 **Related operations:**
+  [CreateGrant](API_CreateGrant.md)
+  [ListGrants](API_ListGrants.md)
+  [ListRetirableGrants](API_ListRetirableGrants.md)
+  [RevokeGrant](API_RevokeGrant.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_RetireGrant_RequestSyntax"></a>

```
{
   "DryRun": {{boolean}},
   "GrantId": "{{string}}",
   "GrantToken": "{{string}}",
   "KeyId": "{{string}}"
}
```

## Request Parameters
<a name="API_RetireGrant_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [DryRun](#API_RetireGrant_RequestSyntax) **   <a name="KMS-RetireGrant-request-DryRun"></a>
Checks if your request will succeed. `DryRun` is an optional parameter.
To learn more about how to use this parameter, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/testing-permissions.html) in the * AWS Key Management Service Developer Guide*.
Type: Boolean
Required: No

 ** [GrantId](#API_RetireGrant_RequestSyntax) **   <a name="KMS-RetireGrant-request-GrantId"></a>
Identifies the grant to retire. To get the grant ID, use [CreateGrant](API_CreateGrant.md), [ListGrants](API_ListGrants.md), or [ListRetirableGrants](API_ListRetirableGrants.md).
+ Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [GrantToken](#API_RetireGrant_RequestSyntax) **   <a name="KMS-RetireGrant-request-GrantToken"></a>
Identifies the grant to be retired. You can use a grant token to identify a new grant even before it has achieved eventual consistency.
Only the [CreateGrant](API_CreateGrant.md) operation returns a grant token. For details, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-eventual-consistency) in the * AWS Key Management Service Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [KeyId](#API_RetireGrant_RequestSyntax) **   <a name="KMS-RetireGrant-request-KeyId"></a>
The key ARN KMS key associated with the grant. To find the key ARN, use the [ListKeys](API_ListKeys.md) operation.
For example: `arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Elements
<a name="API_RetireGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RetireGrant_Errors"></a>

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

 ** InvalidGrantTokenException **
The request was rejected because the specified grant token is not valid.
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
<a name="API_RetireGrant_Examples"></a>

### Example Request
<a name="API_RetireGrant_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 167
X-Amz-Target: TrentService.RetireGrant
X-Amz-Date: 20161208T233237Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161208/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=e463f010eb7d997b4f89ae836288a67f362b0afd762fcf242a3f76ba282448dc

{
  "KeyId": "arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "GrantId": "1ea8e6c7d4d49ecf7e4461c792f6a27651d7ff0ee13a724c19e730337faa26b1"
}
```

### Example Response
<a name="API_RetireGrant_Example_2"></a>

This example illustrates one usage of RetireGrant.

```
HTTP/1.1 200 OK
Server: Server
Date: Thu, 08 Dec 2016 23:32:38 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: 9ad2b038-bd9e-11e6-ace2-6fb96f685e31
```

## See Also
<a name="API_RetireGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/RetireGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/RetireGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/RetireGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/RetireGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/RetireGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/RetireGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/RetireGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/RetireGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/RetireGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/RetireGrant)
