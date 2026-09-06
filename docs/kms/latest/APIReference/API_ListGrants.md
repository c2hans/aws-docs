---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ListGrants.html
---

# ListGrants
<a name="API_ListGrants"></a>

Gets a list of all grants for the specified KMS key.

You must specify the KMS key in all requests. You can filter the grant list by grant ID, grantee principal, or grantee service principal.

For detailed information about grants, including grant terminology, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the * * AWS Key Management Service Developer Guide* *. For examples of creating grants in several programming languages, see [Use CreateGrant with an AWS SDK or CLI](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateGrant_section.html).

**Note**
When a grant is created with the `GranteePrincipal` field, the `ListGrants` response usually contains the user or role designated as the grantee principal in the grant. However, if the grantee principal is an AWS service, the `GranteePrincipal` field contains an AWS [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services), which might correspond to several different grantee principals, such as an IAM user, IAM role, or AWS account.
When a grant is created with the `GranteeServicePrincipal` field, the `ListGrants` response always includes a `GranteeServicePrincipal` that indicates the grantee is actually an AWS [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services).

 **Cross-account use**: Yes. To perform this operation on a KMS key in a different AWS account, specify the key ARN in the value of the `KeyId` parameter.

 **Required permissions**: [kms:ListGrants](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

 **Related operations:**
+  [CreateGrant](API_CreateGrant.md)
+  [ListRetirableGrants](API_ListRetirableGrants.md)
+  [RetireGrant](API_RetireGrant.md)
+  [RevokeGrant](API_RevokeGrant.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ListGrants_RequestSyntax"></a>

```
{
   "GranteePrincipal": "{{string}}",
   "GranteeServicePrincipal": "{{string}}",
   "GrantId": "{{string}}",
   "KeyId": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGrants_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_ListGrants_RequestSyntax) **   <a name="KMS-ListGrants-request-KeyId"></a>
Returns only grants for the specified KMS key. This parameter is required.
Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different AWS account, you must use the key ARN.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** [GranteePrincipal](#API_ListGrants_RequestSyntax) **   <a name="KMS-ListGrants-request-GranteePrincipal"></a>
Returns only grants where the specified principal is the grantee principal for the grant.
You can specify either `GranteePrincipal` or `GranteeServicePrincipal`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@:/-]+$`
Required: No

 ** [GranteeServicePrincipal](#API_ListGrants_RequestSyntax) **   <a name="KMS-ListGrants-request-GranteeServicePrincipal"></a>
Returns only grants where the specified AWS service principal is the grantee service principal for the grant. This filter is only usable by callers in a service principal.
You can specify either `GranteePrincipal` or `GranteeServicePrincipal`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([A-Za-z0-9\-]+)\.([A-Za-z0-9\-]+)(\.[A-Za-z0-9\-]+)+$`
Required: No

 ** [GrantId](#API_ListGrants_RequestSyntax) **   <a name="KMS-ListGrants-request-GrantId"></a>
Returns only the grant with the specified grant ID. The grant ID uniquely identifies the grant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [Limit](#API_ListGrants_RequestSyntax) **   <a name="KMS-ListGrants-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [Marker](#API_ListGrants_RequestSyntax) **   <a name="KMS-ListGrants-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

## Response Syntax
<a name="API_ListGrants_ResponseSyntax"></a>

```
{
   "Grants": [
      {
         "Constraints": {
            "EncryptionContextEquals": {
               "string" : "string"
            },
            "EncryptionContextSubset": {
               "string" : "string"
            },
            "SourceArn": "string"
         },
         "CreationDate": number,
         "GranteePrincipal": "string",
         "GranteeServicePrincipal": "string",
         "GrantId": "string",
         "IssuingAccount": "string",
         "KeyId": "string",
         "Name": "string",
         "Operations": [ "string" ],
         "RetiringPrincipal": "string",
         "RetiringServicePrincipal": "string"
      }
   ],
   "NextMarker": "string",
   "Truncated": boolean
}
```

## Response Elements
<a name="API_ListGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Grants](#API_ListGrants_ResponseSyntax) **   <a name="KMS-ListGrants-response-Grants"></a>
A list of grants.
Type: Array of [GrantListEntry](API_GrantListEntry.md) objects

 ** [NextMarker](#API_ListGrants_ResponseSyntax) **   <a name="KMS-ListGrants-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Truncated](#API_ListGrants_ResponseSyntax) **   <a name="KMS-ListGrants-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_ListGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** InvalidGrantIdException **
The request was rejected because the specified `GrantId` is not valid.
HTTP Status Code: 400

 ** InvalidMarkerException **
The request was rejected because the marker that specifies where pagination should next begin is not valid.
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
<a name="API_ListGrants_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListGrants_Example_1"></a>

This example illustrates one usage of ListGrants.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 49
X-Amz-Target: TrentService.ListGrants
X-Amz-Date: 20161206T231134Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161206/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=157e1dd2ef1992e70e403e96c9f7122c5eb18bf82e4e5a71a83d63dcbc1c681b

{"KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"}
```

### Example Response
<a name="API_ListGrants_Example_2"></a>

This example illustrates one usage of ListGrants.

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 06 Dec 2016 23:11:34 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 1652
Connection: keep-alive
x-amzn-RequestId: 54ee4e2f-bc09-11e6-8073-89d6c33fcd1f

{
  "Grants": [
    {
      "CreationDate": 1.477431461E9,
      "GrantId": "91ad875e49b04a9d1f3bdeb84d821f9db6ea95e1098813f6d47f0c65fbe2a172",
      "GranteePrincipal": "acm.us-east-2.amazonaws.com",
      "IssuingAccount": "arn:aws:iam::111122223333:root",
      "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Name": "",
      "Operations": [
        "Encrypt",
        "ReEncryptFrom",
        "ReEncryptTo"
      ],
      "RetiringPrincipal": "acm.us-east-2.amazonaws.com"
    },
    {
      "CreationDate": 1.477431461E9,
      "GrantId": "a5d67d3e207a8fc1f4928749ee3e52eb0440493a8b9cf05bbfad91655b056200",
      "GranteePrincipal": "acm.us-east-2.amazonaws.com",
      "IssuingAccount": "arn:aws:iam::111122223333:root",
      "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Name": "",
      "Operations": [
        "ReEncryptFrom",
        "ReEncryptTo"
      ],
      "RetiringPrincipal": "acm.us-east-2.amazonaws.com"
    },
    {
      "CreationDate": 1.477431461E9,
      "GrantId": "c541aaf05d90cb78846a73b346fc43e65be28b7163129488c738e0c9e0628f4f",
      "GranteePrincipal": "acm.us-east-2.amazonaws.com",
      "IssuingAccount": "arn:aws:iam::111122223333:root",
      "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Name": "",
      "Operations": [
        "Encrypt",
        "ReEncryptFrom",
        "ReEncryptTo"
      ],
      "RetiringPrincipal": "acm.us-east-2.amazonaws.com"
    },
    {
      "CreationDate": 1.477431461E9,
      "GrantId": "dd2052c67b4c76ee45caf1dc6a1e2d24e8dc744a51b36ae2f067dc540ce0105c",
      "GranteePrincipal": "acm.us-east-2.amazonaws.com",
      "IssuingAccount": "arn:aws:iam::111122223333:root",
      "KeyId": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Name": "",
      "Operations": [
        "Encrypt",
        "ReEncryptFrom",
        "ReEncryptTo"
      ],
      "RetiringPrincipal": "acm.us-east-2.amazonaws.com"
    }
  ],
  "Truncated": false
}
```

## See Also
<a name="API_ListGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ListGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ListGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ListGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ListGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ListGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ListGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ListGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ListGrants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ListGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ListGrants)
