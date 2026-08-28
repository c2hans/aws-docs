---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_CreateTags.html
---

# CreateTags
<a name="API_CreateTags"></a>

**Note**
DEPRECATED - `CreateTags` is deprecated and not maintained. To create tags for EFS resources, use the [TagResource](API_TagResource.md) API action.

Creates or overwrites tags associated with a file system. Each tag is a key-value pair. If a tag key specified in the request already exists on the file system, this operation overwrites its value with the value provided in the request. If you add the `Name` tag to your file system, Amazon EFS returns it in the response to the [DescribeFileSystems](API_DescribeFileSystems.md) operation.

This operation requires permission for the `elasticfilesystem:CreateTags` action.

## Request Syntax
<a name="API_CreateTags_RequestSyntax"></a>

```
POST /2015-02-01/create-tags/{{FileSystemId}} HTTP/1.1
Content-type: application/json

{
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateTags_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FileSystemId](#API_CreateTags_RequestSyntax) **   <a name="efs-CreateTags-request-uri-FileSystemId"></a>
The ID of the file system whose tags you want to modify (String). This operation modifies the tags only, not the file system.
Length Constraints: Maximum length of 128.
Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`
Required: Yes

## Request Body
<a name="API_CreateTags_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Tags](#API_CreateTags_RequestSyntax) **   <a name="efs-CreateTags-request-Tags"></a>
An array of `Tag` objects to add. Each `Tag` object is a key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Syntax
<a name="API_CreateTags_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_CreateTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_CreateTags_Errors"></a>

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
<a name="API_CreateTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticfilesystem-2015-02-01/CreateTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateTags)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
