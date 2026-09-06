---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ExportStreamSessionFiles.html
---

# ExportStreamSessionFiles
<a name="API_ExportStreamSessionFiles"></a>

 Export the files that your application modifies or generates in a stream session, which can help you debug or verify your application. When your application runs, it generates output files such as logs, diagnostic information, crash dumps, save files, user data, screenshots, and so on. The files can be defined by the engine or frameworks that your application uses, or information that you've programmed your application to output.

 You can only call this action on a stream session that is in progress, specifically in one of the following statuses `ACTIVE`, `CONNECTED`, `PENDING_CLIENT_RECONNECTION`, and `RECONNECTING`. You must provide an Amazon Simple Storage Service (Amazon S3) bucket to store the files in. When the session ends, Amazon GameLift Streams produces a compressed folder that contains all of the files and directories that were modified or created by the application during the stream session. AWS uses your security credentials to authenticate and authorize access to your Amazon S3 bucket.

Amazon GameLift Streams collects the following generated and modified files. Find them in the corresponding folders in the `.zip` archive.
+  `application/`: The folder where your application or game is stored.
+  `profile/`: The user profile folder.
+  `temp/`: The system temp folder.

To verify the status of the exported files, use GetStreamSession.

To delete the files, delete the object in the S3 bucket.

## Request Syntax
<a name="API_ExportStreamSessionFiles_RequestSyntax"></a>

```
PUT /streamgroups/{{Identifier}}/streamsessions/{{StreamSessionIdentifier}}/exportfiles HTTP/1.1
Content-type: application/json

{
   "OutputUri": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ExportStreamSessionFiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_ExportStreamSessionFiles_RequestSyntax) **   <a name="gameliftstreams-ExportStreamSessionFiles-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [StreamSessionIdentifier](#API_ExportStreamSessionFiles_RequestSyntax) **   <a name="gameliftstreams-ExportStreamSessionFiles-request-uri-StreamSessionIdentifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream session resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567`. Example ID: `ABC123def4567`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_ExportStreamSessionFiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [OutputUri](#API_ExportStreamSessionFiles_RequestSyntax) **   <a name="gameliftstreams-ExportStreamSessionFiles-request-OutputUri"></a>
 The S3 bucket URI where Amazon GameLift Streams uploads the set of compressed exported files for this stream session. Amazon GameLift Streams generates a ZIP file name based on the stream session metadata. Alternatively, you can provide a custom file name with a `.zip` file extension.
 Example 1: If you provide an S3 URI called `s3://amzn-s3-demo-destination-bucket/MyGame_Session1.zip`, then Amazon GameLift Streams will save the files at that location.
 Example 2: If you provide an S3 URI called `s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/`, then Amazon GameLift Streams will save the files at `s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/YYYYMMDD-HHMMSS-appId-sg-Id-sessionId.zip` or another similar name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://.*(/|\.zip|\.ZIP)`
Required: Yes

## Response Syntax
<a name="API_ExportStreamSessionFiles_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_ExportStreamSessionFiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ExportStreamSessionFiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource specified in the request was not found. Correct the request before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## Examples
<a name="API_ExportStreamSessionFiles_Examples"></a>

### CLI Example
<a name="API_ExportStreamSessionFiles_Example_1"></a>

 This example shows how to use the CLI to tell Amazon GameLift Streams to export the generated files when the stream session ends.

#### Sample Request
<a name="API_ExportStreamSessionFiles_Example_1_Request"></a>

```
aws gameliftstreams export-stream-session-files \
    --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
    --stream-session-identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567 \
    --output-uri s3://amzn-s3-demo-destination-bucket/prefix/
```

## See Also
<a name="API_ExportStreamSessionFiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ExportStreamSessionFiles)
