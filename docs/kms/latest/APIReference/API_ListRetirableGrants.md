---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ListRetirableGrants.html
---

# ListRetirableGrants
<a name="API_ListRetirableGrants"></a>

Returns information about all grants in the AWS account and Region that have the specified retiring principal or retiring service principal.

You can specify any principal in your AWS account. The grants that are returned include grants for KMS keys in your AWS account and other AWS accounts. You might use this operation to determine which grants you may retire. To retire a grant, use the [RetireGrant](API_RetireGrant.md) operation.

For detailed information about grants, including grant terminology, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the * * AWS Key Management Service Developer Guide* *. For examples of creating grants in several programming languages, see [Use CreateGrant with an AWS SDK or CLI](https://docs.aws.amazon.com/kms/latest/developerguide/example_kms_CreateGrant_section.html).

 **Cross-account use**: You must specify a principal in your AWS account. This operation returns a list of grants where the retiring principal specified in the `ListRetirableGrants` request is the same retiring principal on the grant. This can include grants on KMS keys owned by other AWS accounts, but you do not need `kms:ListRetirableGrants` permission (or any other additional permission) in any AWS account other than your own.

 **Required permissions**: [kms:ListRetirableGrants](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy) in your AWS account.

**Note**
When listing retirable grants by `RetiringPrincipal`, AWS KMS authorizes `ListRetirableGrants` requests by evaluating the caller account's kms:ListRetirableGrants permissions. The authorized resource in `ListRetirableGrants` calls is the retiring principal specified in the request. AWS KMS does not evaluate the caller's permissions to verify their access to any KMS keys or grants that might be returned by the `ListRetirableGrants` call.
The `RetiringServicePrincipal` filter is only usable by callers in a service principal.

 **Related operations:**
+  [CreateGrant](API_CreateGrant.md)
+  [ListGrants](API_ListGrants.md)
+  [RetireGrant](API_RetireGrant.md)
+  [RevokeGrant](API_RevokeGrant.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ListRetirableGrants_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}",
   "RetiringPrincipal": "{{string}}",
   "RetiringServicePrincipal": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRetirableGrants_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_ListRetirableGrants_RequestSyntax) **   <a name="KMS-ListRetirableGrants-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [Marker](#API_ListRetirableGrants_RequestSyntax) **   <a name="KMS-ListRetirableGrants-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

 ** [RetiringPrincipal](#API_ListRetirableGrants_RequestSyntax) **   <a name="KMS-ListRetirableGrants-request-RetiringPrincipal"></a>
The retiring principal for which to list grants. Enter a principal in your AWS account.
To specify the retiring principal, use the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an AWS principal. Valid principals include AWS accounts, IAM users, IAM roles, federated users, and assumed role users. For help with the ARN syntax for a principal, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) in the * * AWS Identity and Access Management User Guide* *.
You must specify either `RetiringPrincipal` or `RetiringServicePrincipal`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[\w+=,.@:/-]+$`
Required: No

 ** [RetiringServicePrincipal](#API_ListRetirableGrants_RequestSyntax) **   <a name="KMS-ListRetirableGrants-request-RetiringServicePrincipal"></a>
The retiring service principal for which to list grants. This filter is only usable by callers in a service principal.
You must specify either `RetiringPrincipal` or `RetiringServicePrincipal`, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([A-Za-z0-9\-]+)\.([A-Za-z0-9\-]+)(\.[A-Za-z0-9\-]+)+$`
Required: No

## Response Syntax
<a name="API_ListRetirableGrants_ResponseSyntax"></a>

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
<a name="API_ListRetirableGrants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Grants](#API_ListRetirableGrants_ResponseSyntax) **   <a name="KMS-ListRetirableGrants-response-Grants"></a>
A list of grants.
Type: Array of [GrantListEntry](API_GrantListEntry.md) objects

 ** [NextMarker](#API_ListRetirableGrants_ResponseSyntax) **   <a name="KMS-ListRetirableGrants-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Truncated](#API_ListRetirableGrants_ResponseSyntax) **   <a name="KMS-ListRetirableGrants-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_ListRetirableGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidArnException **
The request was rejected because a specified ARN, or an ARN in a key policy, is not valid.
HTTP Status Code: 400

 ** InvalidMarkerException **
The request was rejected because the marker that specifies where pagination should next begin is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

 ** NotFoundException **
The request was rejected because the specified entity or resource could not be found.
HTTP Status Code: 400

## Examples
<a name="API_ListRetirableGrants_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListRetirableGrants_Example_1"></a>

This example illustrates one usage of ListRetirableGrants.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 61
X-Amz-Target: TrentService.ListRetirableGrants
X-Amz-Date: 20161207T191040Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161207/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=d5e43f0cfd75a3251f40bc27e76f83b3110b33e3d972142ae118b2b3c0f67b39

{"RetiringPrincipal": "arn:aws:iam::111122223333:role/ExampleRole"}
```

### Example Response
<a name="API_ListRetirableGrants_Example_2"></a>

This example illustrates one usage of ListRetirableGrants.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 07 Dec 2016 19:10:41 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 436
Connection: keep-alive
x-amzn-RequestId: d86125dc-bcb0-11e6-82b3-e9e4af764a06

{
  "Grants": [
    {
      "CreationDate": 1.481137775E9,
      "GrantId": "0c237476b39f8bc44e45212e08498fbe3151305030726c0590dd8d3e9f3d6a60",
      "GranteePrincipal": "arn:aws:iam::111122223333:role/ExampleRole",
      "IssuingAccount": "arn:aws:iam::444455556666:root",
      "KeyId": "arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Name": "",
      "Operations": [
        "Decrypt",
        "Encrypt"
      ],
      "RetiringPrincipal": "arn:aws:iam::111122223333:role/ExampleRole"
    }
  ],
  "Truncated": false
}
```

## See Also
<a name="API_ListRetirableGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ListRetirableGrants)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ListRetirableGrants)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
