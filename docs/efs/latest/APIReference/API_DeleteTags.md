---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_DeleteTags.html
---

# DeleteTags
<a name="API_DeleteTags"></a>

**Note**
DEPRECATED - `DeleteTags` is deprecated and not maintained. To remove tags from EFS resources, use the [UntagResource](API_UntagResource.md) API action.

Deletes the specified tags from a file system. If the `DeleteTags` request includes a tag key that doesn't exist, Amazon EFS ignores it and doesn't cause an error. For more information about tags and related restrictions, see [Tag restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the * AWS Billing and Cost Management User Guide*.

This operation requires permissions for the `elasticfilesystem:DeleteTags` action.

## Request Syntax
<a name="API_DeleteTags_RequestSyntax"></a>

```
POST /2015-02-01/delete-tags/{{FileSystemId}} HTTP/1.1
Content-type: application/json

{
   "TagKeys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeleteTags_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FileSystemId](#API_DeleteTags_RequestSyntax) **   <a name="efs-DeleteTags-request-uri-FileSystemId"></a>
The ID of the file system whose tags you want to delete (String).
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
Required: Yes

## Request Body
<a name="API_DeleteTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [TagKeys](#API_DeleteTags_RequestSyntax) **   <a name="efs-DeleteTags-request-TagKeys"></a>
A list of tag keys to delete.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Required: Yes

## Response Syntax
<a name="API_DeleteTags_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **
Returned if the request is malformed or contains an error such as an invalid parameter value or a missing required parameter.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 400

 ** FileSystemNotFound **
Returned if the specified `FileSystemId` value doesn't exist in the requester's AWS account.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 404

 ** InternalServerError **
Returned if an error occurred on the server side.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 500

## See Also
<a name="API_DeleteTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/DeleteTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteTags)
