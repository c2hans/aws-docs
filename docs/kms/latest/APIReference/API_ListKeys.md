---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ListKeys.html
---

# ListKeys

Gets a list of all KMS keys in the caller's AWS account and Region.

You can also use `ListKeys` to list KMS keys in the Region that other AWS accounts shared with the caller's AWS account through AWS Resource Access Manager (AWS RAM). To list them, use the `ResourceOwners` parameter. If you omit `ResourceOwners`, `ListKeys` lists only the KMS keys in the caller's AWS account.

When `ResourceOwners` includes `OTHER_ACCOUNTS_VIA_RAM`, `ListKeys` returns the KMS keys that other AWS accounts currently share with the caller's AWS account through AWS RAM. For information about how and when a resource that another account shares becomes available to your AWS account, see [Access AWS resources shared with you](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared.html) in the * AWS RAM User Guide*.

 **Cross-account use**: No. This operation doesn't take a KMS key parameter, so you can't use it to list the KMS keys of a specific AWS account. The only KMS keys in other AWS accounts that `ListKeys` returns are the ones that other accounts shared with the caller's AWS account through AWS RAM. To list them, set the `ResourceOwners` parameter to include `OTHER_ACCOUNTS_VIA_RAM`.

 **Required permissions**: [kms:ListKeys](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

The same `kms:ListKeys` permission lets you list the KMS keys that other accounts shared with you through AWS RAM. AWS KMS doesn't evaluate the key policies of shared KMS keys when it lists them. To use a shared KMS key, you need permission for each operation on that KMS key.

 **Related operations:**
+  [CreateKey](API_CreateKey.md)
+  [DescribeKey](API_DescribeKey.md)
+  [ListAliases](API_ListAliases.md)
+  [ListResourceTags](API_ListResourceTags.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

KMS keys that other AWS accounts share with you can take some time to appear in or disappear from `ListKeys` results after changes to resource shares, such as accepting an invitation or deleting a resource share.

## Request Syntax
<a name="API_ListKeys_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}",
   "ResourceOwners": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListKeys_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Limit](#API_ListKeys_RequestSyntax) **   <a name="KMS-ListKeys-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 1000, inclusive. If you do not include a value, it defaults to 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [Marker](#API_ListKeys_RequestSyntax) **   <a name="KMS-ListKeys-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

 ** [ResourceOwners](#API_ListKeys_RequestSyntax) **   <a name="KMS-ListKeys-request-ResourceOwners"></a>
Specifies whose KMS keys to list. Use this parameter to list KMS keys that other AWS accounts shared with your AWS account through AWS Resource Access Manager (AWS RAM).
Specify one or two values. Valid values are:
SELF
Lists the KMS keys in your AWS account and Region.
OTHER\_ACCOUNTS\_VIA\_RAM
Lists the KMS keys in the Region that other AWS accounts currently share with your AWS account through AWS RAM. This list doesn't include KMS keys that your AWS account owns. For each of these KMS keys, the key ARN in the response contains the account ID of the AWS account that owns the KMS key.
If you omit this parameter, `ListKeys` lists only the KMS keys in your AWS account. If you specify both values, in either order, `ListKeys` returns the KMS keys in your AWS account first, and then the KMS keys that other AWS accounts shared with you. A single response doesn't contain both kinds of KMS keys.
When `ResourceOwners` includes `OTHER_ACCOUNTS_VIA_RAM`, a response can contain fewer KMS keys than the `Limit` value, or none, even when `Truncated` is true. To get all of the KMS keys, continue calling `ListKeys` with the `NextMarker` value from each response until `Truncated` is false. Use a `NextMarker` value only in a request that has the same `ResourceOwners` value as the request that returned it. Otherwise, the request can fail with an `InvalidMarkerException`.
KMS keys that other AWS accounts share with you can take some time to appear in or disappear from the results after changes to resource shares.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `SELF | OTHER_ACCOUNTS_VIA_RAM`
Required: No

## Response Syntax
<a name="API_ListKeys_ResponseSyntax"></a>

```
{
   "Keys": [
      {
         "KeyArn": "string",
         "KeyId": "string"
      }
   ],
   "NextMarker": "string",
   "Truncated": boolean
}
```

## Response Elements
<a name="API_ListKeys_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Keys](#API_ListKeys_ResponseSyntax) **   <a name="KMS-ListKeys-response-Keys"></a>
A list of KMS keys. For a KMS key that another AWS account shared with you through AWS RAM, the key ARN contains the account ID of the AWS account that owns the KMS key.
Type: Array of [KeyListEntry](API_KeyListEntry.md) objects

 ** [NextMarker](#API_ListKeys_ResponseSyntax) **   <a name="KMS-ListKeys-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Truncated](#API_ListKeys_ResponseSyntax) **   <a name="KMS-ListKeys-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_ListKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyTimeoutException **
The system timed out while trying to fulfill the request. You can retry the request.
HTTP Status Code: 500

 ** InvalidMarkerException **
The request was rejected because the marker that specifies where pagination should next begin is not valid.
HTTP Status Code: 400

 ** KMSInternalException **
The request was rejected because an internal exception occurred. The request can be retried.
HTTP Status Code: 500

## Examples
<a name="API_ListKeys_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListKeys_Example_1"></a>

This example illustrates one usage of ListKeys.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 2
X-Amz-Target: TrentService.ListKeys
X-Amz-Date: 20161207T003550Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161207/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=2196a20c1a139ae8f6fe070881f41954616c775bb5a484814c35f8ee35cfa448

{}
```

### Example Response
<a name="API_ListKeys_Example_2"></a>

This example illustrates one usage of ListKeys.

```
HTTP/1.1 200 OK
Server: Server
Date: Wed, 07 Dec 2016 00:35:50 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 980
Connection: keep-alive
x-amzn-RequestId: 1a5f0a53-bc15-11e6-82b3-e9e4af764a06

{
  "Keys": [
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/0d990263-018e-4e65-a703-eff731de951e",
      "KeyId": "0d990263-018e-4e65-a703-eff731de951e"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/144be297-0ae1-44ac-9c8f-93cd8c82f841",
      "KeyId": "144be297-0ae1-44ac-9c8f-93cd8c82f841"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/21184251-b765-428e-b852-2c7353e72571",
      "KeyId": "21184251-b765-428e-b852-2c7353e72571"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/214fe92f-5b03-4ae1-b350-db2a45dbe10c",
      "KeyId": "214fe92f-5b03-4ae1-b350-db2a45dbe10c"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/339963f2-e523-49d3-af24-a0fe752aa458",
      "KeyId": "339963f2-e523-49d3-af24-a0fe752aa458"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/b776a44b-df37-4438-9be4-a27494e4271a",
      "KeyId": "b776a44b-df37-4438-9be4-a27494e4271a"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:111122223333:key/deaf6c9e-cf2c-46a6-bf6d-0b6d487cffbb",
      "KeyId": "deaf6c9e-cf2c-46a6-bf6d-0b6d487cffbb"
    }
  ],
  "Truncated": false
}
```

### Example – Request for KMS keys shared with you
<a name="API_ListKeys_Example_3"></a>

This example illustrates one usage of ListKeys.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 50
X-Amz-Target: TrentService.ListKeys
X-Amz-Date: 20261117T184227Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20261117/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=EXAMPLE

{
  "ResourceOwners": ["OTHER_ACCOUNTS_VIA_RAM"]
}
```

### Example – Response for KMS keys shared with you
<a name="API_ListKeys_Example_4"></a>

This example illustrates one usage of ListKeys.

```
HTTP/1.1 200 OK
Server: Server
Date: Tue, 17 Nov 2026 18:42:27 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 364
Connection: keep-alive
x-amzn-RequestId: 3e8c6f2a-7d41-4b9e-a5c0-9f1b2d3e4a5c

{
  "Keys": [
    {
      "KeyArn": "arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    {
      "KeyArn": "arn:aws:kms:us-east-2:444455556666:key/0987dcba-09fe-87dc-65ba-ab0987654321",
      "KeyId": "0987dcba-09fe-87dc-65ba-ab0987654321"
    }
  ],
  "Truncated": false
}
```

## See Also
<a name="API_ListKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ListKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ListKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ListKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ListKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ListKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ListKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ListKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ListKeys)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ListKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ListKeys)
