---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html
---

# GetKeyPolicy
<a name="API_GetKeyPolicy"></a>

Gets a key policy attached to the specified KMS key.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations**: [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_GetKeyPolicy_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}",
   "PolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetKeyPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_GetKeyPolicy_RequestSyntax) **   <a name="KMS-GetKeyPolicy-request-KeyId"></a>
Gets the key policy for the specified KMS key.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [PolicyName](#API_GetKeyPolicy_RequestSyntax) **   <a name="KMS-GetKeyPolicy-request-PolicyName"></a>
Specifies the name of the key policy. If no policy name is specified, the default value is `default`. The only valid name is `default`. To get the names of key policies, use [ListKeyPolicies](API_ListKeyPolicies.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w]+`
Required: No

## Response Syntax
<a name="API_GetKeyPolicy_ResponseSyntax"></a>

```
{
   "Policy": "string",
   "PolicyName": "string"
}
```

## Response Elements
<a name="API_GetKeyPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetKeyPolicy_ResponseSyntax) **   <a name="KMS-GetKeyPolicy-response-Policy"></a>
A key policy document in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 131072.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

 ** [PolicyName](#API_GetKeyPolicy_ResponseSyntax) **   <a name="KMS-GetKeyPolicy-response-PolicyName"></a>
The name of the key policy. The only valid value is `default`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w]+`

## Errors
<a name="API_GetKeyPolicy_Errors"></a>

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

## Examples
<a name="API_GetKeyPolicy_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GetKeyPolicy_Example_1"></a>

This example illustrates one usage of GetKeyPolicy.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 74
X-Amz-Target: TrentService.GetKeyPolicy
X-Amz-Date: 20161114T225546Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161114/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=a88e20eebfbea3bf62d1512d0d2987e2d233becc7631a442237d3661df623a40

{
  "PolicyName": "default",
  "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

### Example Response
<a name="API_GetKeyPolicy_Example_2"></a>

This example illustrates one usage of GetKeyPolicy.

```
HTTP/1.1 200 OK
Server: Server
Date: Mon, 14 Nov 2016 22:55:47 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 326
Connection: keep-alive
x-amzn-RequestId: 7b105e7b-aabd-11e6-8039-3123b558b719

{
    "Policy":"{\n
        \"Version\" : \"2012-10-17\",\n
        \"Id\" : \"key-default-1\",\n
        \"Statement\" : [ {\n
            \"Sid\" : \"Enable IAM User Permissions\",\n
            \"Effect\" : \"Allow\",\n
            \"Principal\" : {\n
                \"AWS\" : \"arn:aws:iam::111122223333:root\"\n
            },\n
            \"Action\" : \"kms:*\",\n
            \"Resource\" : \"*\"\n
        } ]\n
    }",
    "PolicyName": "default"
}
```

## See Also
<a name="API_GetKeyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/GetKeyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/GetKeyPolicy)
