---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_BatchGetAttachedFileMetadata.html
---

# BatchGetAttachedFileMetadata
<a name="API_BatchGetAttachedFileMetadata"></a>

Allows you to retrieve metadata about multiple attached files on an associated resource. Each attached file provided in the input list must be associated with the input AssociatedResourceArn.

## Request Syntax
<a name="API_BatchGetAttachedFileMetadata_RequestSyntax"></a>

```
POST /attached-files/{{InstanceId}}?associatedResourceArn={{AssociatedResourceArn}} HTTP/1.1
Content-type: application/json

{
   "FileIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetAttachedFileMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AssociatedResourceArn](#API_BatchGetAttachedFileMetadata_RequestSyntax) **   <a name="connect-BatchGetAttachedFileMetadata-request-uri-AssociatedResourceArn"></a>
The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html), [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html), and [Task](https://docs.aws.amazon.com/connect/latest/adminguide/concepts-getting-started-tasks.html).
This value must be a valid ARN.
Required: Yes

 ** [InstanceId](#API_BatchGetAttachedFileMetadata_RequestSyntax) **   <a name="connect-BatchGetAttachedFileMetadata-request-uri-InstanceId"></a>
The unique identifier of the Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_BatchGetAttachedFileMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [FileIds](#API_BatchGetAttachedFileMetadata_RequestSyntax) **   <a name="connect-BatchGetAttachedFileMetadata-request-FileIds"></a>
The unique identifiers of the attached file resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_BatchGetAttachedFileMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "FileId": "string"
      }
   ],
   "Files": [
      {
         "AssociatedResourceArn": "string",
         "CreatedBy": { ... },
         "CreationTime": "string",
         "FileArn": "string",
         "FileId": "string",
         "FileName": "string",
         "FileSizeInBytes": number,
         "FileStatus": "string",
         "FileUseCaseType": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetAttachedFileMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchGetAttachedFileMetadata_ResponseSyntax) **   <a name="connect-BatchGetAttachedFileMetadata-response-Errors"></a>
List of errors of attached files that could not be retrieved.
Type: Array of [AttachedFileError](API_AttachedFileError.md) objects

 ** [Files](#API_BatchGetAttachedFileMetadata_ResponseSyntax) **   <a name="connect-BatchGetAttachedFileMetadata-response-Files"></a>
List of attached files that were successfully retrieved.
Type: Array of [AttachedFile](API_AttachedFile.md) objects

## Errors
<a name="API_BatchGetAttachedFileMetadata_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_BatchGetAttachedFileMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/BatchGetAttachedFileMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/BatchGetAttachedFileMetadata)
