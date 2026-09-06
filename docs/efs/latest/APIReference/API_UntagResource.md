---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes tags from an EFS resource. You can remove tags from EFS file systems and access points using this API operation.

This operation requires permissions for the `elasticfilesystem:UntagResource` action.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /2015-02-01/resource-tags/{{ResourceId}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceId](#API_UntagResource_RequestSyntax) **   <a name="efs-UntagResource-request-uri-ResourceId"></a>
Specifies the EFS resource that you want to remove tags from.
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="efs-UntagResource-request-uri-TagKeys"></a>
The keys of the key-value tag pairs that you want to remove from the specified EFS resource.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessPointNotFound **
Returned if the specified `AccessPointId` value doesn't exist in the requester's AWS account.
 ** ErrorCode **
The error code is a string that uniquely identifies an error condition. It is meant to be read and understood by programs that detect and handle errors by type.
 ** Message **
The error message contains a generic description of the error condition in English. It is intended for a human audience. Simple programs display the message directly to the end user if they encounter an error condition they don't know how or don't care to handle. Sophisticated programs with more exhaustive error handling and proper internationalization are more likely to ignore the error message.
HTTP Status Code: 404

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
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UntagResource)
