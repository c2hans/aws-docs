---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_ListAliases.html
---

# ListAliases
<a name="API_ListAliases"></a>

Gets a list of aliases in the caller's AWS account and region. For more information about aliases, see [CreateAlias](API_CreateAlias.md).

By default, the `ListAliases` operation returns all aliases in the account and region. To get only the aliases associated with a particular KMS key, use the `KeyId` parameter.

The `ListAliases` response can include aliases that you created and associated with your customer managed keys, and aliases that AWS created and associated with AWS managed keys in your account. You can recognize AWS aliases because their names have the format `aws/<service-name>`, such as `aws/dynamodb`.

The response might also include aliases that have no `TargetKeyId` field. These are predefined aliases that AWS has created but has not yet associated with a KMS key. Aliases that AWS creates in your account, including predefined aliases, do not count against your [AWS KMS aliases quota](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html#aliases-per-key).

 **Cross-account use**: No. `ListAliases` does not return aliases in other AWS accounts.

 **Required permissions**: [kms:ListAliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy)

For details, see [Controlling access to aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-access.html) in the * AWS Key Management Service Developer Guide*.

 **Related operations:**
+  [CreateAlias](API_CreateAlias.md)
+  [DeleteAlias](API_DeleteAlias.md)
+  [UpdateAlias](API_UpdateAlias.md)

 **Eventual consistency**: The AWS KMS API follows an eventual consistency model. For more information, see [AWS KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/accessing-kms.html#programming-eventual-consistency).

## Request Syntax
<a name="API_ListAliases_RequestSyntax"></a>

```
{
   "KeyId": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [KeyId](#API_ListAliases_RequestSyntax) **   <a name="KMS-ListAliases-request-KeyId"></a>
Lists only aliases that are associated with the specified KMS key. Enter a KMS key in your AWS account.
This parameter is optional. If you omit it, `ListAliases` returns all aliases in the account and Region.
Specify the key ID or key ARN of the KMS key.
For example:
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
To get the key ID and key ARN for a KMS key, use [ListKeys](API_ListKeys.md) or [DescribeKey](API_DescribeKey.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Limit](#API_ListAliases_RequestSyntax) **   <a name="KMS-ListAliases-request-Limit"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS KMS does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [Marker](#API_ListAliases_RequestSyntax) **   <a name="KMS-ListAliases-request-Marker"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextMarker` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`
Required: No

## Response Syntax
<a name="API_ListAliases_ResponseSyntax"></a>

```
{
   "Aliases": [
      {
         "AliasArn": "string",
         "AliasName": "string",
         "CreationDate": number,
         "LastUpdatedDate": number,
         "TargetKeyId": "string"
      }
   ],
   "NextMarker": "string",
   "Truncated": boolean
}
```

## Response Elements
<a name="API_ListAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_ListAliases_ResponseSyntax) **   <a name="KMS-ListAliases-response-Aliases"></a>
A list of aliases.
Type: Array of [AliasListEntry](API_AliasListEntry.md) objects

 ** [NextMarker](#API_ListAliases_ResponseSyntax) **   <a name="KMS-ListAliases-response-NextMarker"></a>
When `Truncated` is true, this element is present and contains the value to use for the `Marker` parameter in a subsequent request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\u00FF]*`

 ** [Truncated](#API_ListAliases_ResponseSyntax) **   <a name="KMS-ListAliases-response-Truncated"></a>
A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the `NextMarker` element in this response to the `Marker` parameter in a subsequent request.
Type: Boolean

## Errors
<a name="API_ListAliases_Errors"></a>

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
<a name="API_ListAliases_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListAliases_Example_1"></a>

This example illustrates one usage of ListAliases.

```
POST / HTTP/1.1
Host: kms.us-east-2.amazonaws.com
Content-Length: 2
X-Amz-Target: TrentService.ListAliases
X-Amz-Date: 20161203T011453Z
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256\
 Credential=AKIAI44QH8DHBEXAMPLE/20161203/us-east-2/kms/aws4_request,\
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,\
 Signature=c2867e5f45167bf713e8f2c9998772ad72a20958db2cc0ef46bfba1632ca4d62

{}
```

### Example Response
<a name="API_ListAliases_Example_2"></a>

This example illustrates one usage of ListAliases.

```
HTTP/1.1 200 OK
Server: Server
Date: Sat, 03 Dec 2016 01:14:55 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2874
Connection: keep-alive
x-amzn-RequestId: e6196175-b8f5-11e6-b404-15dcd0a7add5

{
  "Aliases": [
    {
      "AliasArn": "arn:aws:kms:us-east-2:111122223333:alias/aws/acm",
      "AliasName": "alias/aws/acm",
      "TargetKeyId": "da03f6f7-d279-427a-9cae-de48d07e5b66",
      "CreationDate": 1566518783.394,
      "LastUpdatedDate": 1566518783.394
    },
    {
      "AliasArn": "arn:aws:kms:us-east-2:111122223333:alias/aws/ebs",
      "AliasName": "alias/aws/ebs",
      "TargetKeyId": "25a217e7-7170-4b8c-8bf6-045ea5f70e5b",
      "CreationDate": 1493622000.704,
      "LastUpdatedDate": 1493622000.704
    },
    {
      "AliasArn": "arn:aws:kms:us-east-2:111122223333:alias/aws/elasticfilesystem",
      "AliasName": "alias/aws/elasticfilesystem",
      "TargetKeyId": "",
      "CreationDate": 1493622000.704,
      "LastUpdatedDate":
    }
    {
      "AliasArn": "arn:aws:kms:us-east-2:111122223333:alias/example1",
      "AliasName": "alias/example1",
      "TargetKeyId": "4da1e216-62d0-46c5-a7c0-5f3a3d2f8046",
      "CreationDate": 1593622000.191,
      "LastUpdatedDate": 1604158407.202
    },
    {
      "AliasArn": "arn:aws:kms:us-east-2:111122223333:alias/example2",
      "AliasName": "alias/example2",
      "TargetKeyId": "f32fef59-2cc2-445b-8573-2d73328acbee",
      "CreationDate": 1516435200.399,
      "LastUpdatedDate": 1516435200.399
    },
    {
      "AliasArn": "arn:aws:kms:us-east-2:111122223333:alias/example3",
      "AliasName": "alias/example3",
      "TargetKeyId": "1374ef38-d34e-4d5f-b2c9-4e0daee38855",
      "CreationDate": 1589526000.454,
      "LastUpdatedDate": 1589612400.106
    }
  ],
  "Truncated": false
}
```

## See Also
<a name="API_ListAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kms-2014-11-01/ListAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kms-2014-11-01/ListAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/ListAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kms-2014-11-01/ListAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/ListAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kms-2014-11-01/ListAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kms-2014-11-01/ListAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kms-2014-11-01/ListAliases)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kms-2014-11-01/ListAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/ListAliases)
