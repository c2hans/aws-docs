---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html
---

# PutKeyPolicy
<a name="API_PutKeyPolicy"></a>

Attaches a key policy to the specified KMS key.

For more information about key policies, see [Key Policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the * AWS Key Management Service Developer Guide*. For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the * * AWS Identity and Access Management User Guide* *. For examples of adding a key policy in multiple programming languages, see [Use PutKeyPolicy with an AWS SDK or CLI](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_PutKeyPolicy_section.html) in the * AWS Key Management Service Developer Guide*.

 **Cross-account use**: No. You cannot perform this operation on a KMS key in a different AWS account.

 **Required permissions**: [kms:PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations**: [GetKeyPolicy](API_GetKeyPolicy.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_PutKeyPolicy_RequestSyntax"></a>

```
{
   "BypassPolicyLockoutSafetyCheck": {{boolean}},
   "KeyId": "{{string}}",
   "Policy": "{{string}}",
   "PolicyName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutKeyPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_PutKeyPolicy_RequestSyntax) **   <a name="KMS-PutKeyPolicy-request-KeyId"></a>
Sets the key policy on the specified KMS key.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [Policy](#API_PutKeyPolicy_RequestSyntax) **   <a name="KMS-PutKeyPolicy-request-Policy"></a>
The key policy to attach to the KMS key.
The key policy must meet the following criteria:
+ The key policy must allow the calling principal to make a subsequent `PutKeyPolicy` request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the * AWS Key Management Service Developer Guide*. (To omit this condition, set `BypassPolicyLockoutSafetyCheck` to true.)
+ Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to AWS KMS. When you create a new AWS principal, you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to AWS KMS. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the * AWS Identity and Access Management User Guide*.
If either of the required `Resource` or `Action` elements are missing from a key policy statement, the policy statement has no effect. When a key policy statement is missing one of these elements, the AWS KMS console correctly reports an error, but the `PutKeyPolicy` API request succeeds, even though the policy statement is ineffective.
For more information on required key policy elements, see [Elements in a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html#key-policy-elements) in the * AWS Key Management Service Developer Guide*.
A key policy document can include only the following characters:
+ Printable ASCII characters from the space character (`\u0020`) through the end of the ASCII character range.
+ Printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF`).
+ The tab (`\u0009`), line feed (`\u000A`), and carriage return (`\u000D`) special characters
If the key policy exceeds the length constraint, AWS KMS returns a `LimitExceededException`.
For information about key policies, see [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the * AWS Key Management Service Developer Guide*.For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the * * AWS Identity and Access Management User Guide* *.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32768.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** [BypassPolicyLockoutSafetyCheck](#API_PutKeyPolicy_RequestSyntax) **   <a name="KMS-PutKeyPolicy-request-BypassPolicyLockoutSafetyCheck"></a>
Skips ("bypasses") the key policy lockout safety check. The default value is false.
Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.
For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the * AWS Key Management Service Developer Guide*.
Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key.
Type: Boolean
Required: No

 ** [PolicyName](#API_PutKeyPolicy_RequestSyntax) **   <a name="KMS-PutKeyPolicy-request-PolicyName"></a>
The name of the key policy. If no policy name is specified, the default value is `default`. The only valid value is `default`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w]+`
Required: No

## Response Elements
<a name="API_PutKeyPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutKeyPolicy_Errors"></a>

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

 ** MalformedPolicyDocumentException **
The request was rejected because the specified policy is not syntactically or semantically correct.
HTTP Status Code: 400

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The request was rejected because a specified parameter is not supported or a specified resource is not valid for this operation.
HTTP Status Code: 400

## Examples
<a name="API_PutKeyPolicy_Examples"></a>

### Example Request
<a name="API_PutKeyPolicy_Example_1"></a>

The following example is formatted for legibility.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 2396
X-Amz-Target: TrentService.PutKeyPolicy
X-Amz-Date: 20161207T203023Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161207/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=e58ea91db06afc1bc7a1f204769cf6bc4d003ee090095a13caef361c69739ede

{
    "Policy": "{
        \"Version\": \"2012-10-17\",
        \"Id\": \"custom-policy-2016-12-07\",
        \"Statement\": [
            {
                \"Sid\": \"Enable IAM User Permissions\",
                \"Effect\": \"Allow\",
                \"Principal\": {
                    \"AWS\": \"arn:aws:iam::111122223333:root\"
                },
                \"Action\": \"kms:*\",
                \"Resource\": \"*\"
            },
            {
                \"Sid\": \"Allow access for Key Administrators\",
                \"Effect\": \"Allow\",
                \"Principal\": {
                    \"AWS\": [
                        \"arn:aws:iam::111122223333:user/ExampleAdminUser\",
                        \"arn:aws:iam::111122223333:role/ExampleAdminRole\"
                    ]
                },
                \"Action\": [
                    \"kms:Create*\",
                    \"kms:Describe*\",
                    \"kms:Enable*\",
                    \"kms:List*\",
                    \"kms:Put*\",
                    \"kms:Update*\",
                    \"kms:Revoke*\",
                    \"kms:Disable*\",
                    \"kms:Get*\",
                    \"kms:Delete*\",
                    \"kms:ScheduleKeyDeletion\",
                    \"kms:CancelKeyDeletion\"
                ],
                \"Resource\": \"*\"
            },
            {
                \"Sid\": \"Allow use of the key\",
                \"Effect\": \"Allow\",
                \"Principal\": {
                    \"AWS\": \"arn:aws:iam::111122223333:role/ExamplePowerUserRole\"
                },
                \"Action\": [
                    \"kms:Encrypt\",
                    \"kms:Decrypt\",
                    \"kms:ReEncrypt*\",
                    \"kms:GenerateDataKey*\",
                    \"kms:DescribeKey\"
                ],
                \"Resource\": \"*\"
            },
            {
                \"Sid\": \"Allow attachment of persistent resources\",
                \"Effect\": \"Allow\",
                \"Principal\": {
                    \"AWS\": \"arn:aws:iam::111122223333:role/ExamplePowerUserRole\"
                },
                \"Action\": [
                    \"kms:CreateGrant\",
                    \"kms:ListGrants\",
                    \"kms:RevokeGrant\"
                ],
                \"Resource\": \"*\",
                \"Condition\": {
                    \"Bool\": {
                        \"kms:GrantIsForAWSResource\": \"true\"
                    }
                }
            }
        ]
    }",
    "PolicyName": "default",
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

### Example Response
<a name="API_PutKeyPolicy_Example_2"></a>

This example illustrates one usage of PutKeyPolicy.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 07 Dec 2016 20:30:23 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 0
Connection: keep-alive
x-amzn-RequestId: fb114d4c-bcbb-11e6-82b3-e9e4af764a06
```

## See Also
<a name="API_PutKeyPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/PutKeyPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/PutKeyPolicy)
