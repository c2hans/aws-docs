---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

 Updates the mutable configuration settings for a Amazon GameLift Streams application resource. You can change the `Description`, `ApplicationLogOutputUri`, and `ApplicationLogPaths`.

To update application settings, specify the application ID and provide the new values. If the operation is successful, it returns the complete updated set of settings for the application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
PATCH /applications/{{Identifier}} HTTP/1.1
Content-type: application/json

{
   "ApplicationLogOutputUri": "{{string}}",
   "ApplicationLogPaths": [ "{{string}}" ],
   "Description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_UpdateApplication_RequestSyntax) **   <a name="gameliftstreams-UpdateApplication-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_UpdateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationLogOutputUri](#API_UpdateApplication_RequestSyntax) **   <a name="gameliftstreams-UpdateApplication-request-ApplicationLogOutputUri"></a>
An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths`.
The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see [Application log bucket permission policy](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?`
Required: No

 ** [ApplicationLogPaths](#API_UpdateApplication_RequestSyntax) **   <a name="gameliftstreams-UpdateApplication-request-ApplicationLogPaths"></a>
Locations of log files that your content generates during a stream session. Enter path values that are relative to the `ApplicationSourceUri` location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.
Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: `.txt`, `.log`, and `.utrace`. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.
The following path variables are recognized when they appear as the first component of a path: `%USERPROFILE%` (Windows and Proton), `$HOME` or `~` (Linux). Use a path variable when your application writes logs outside of the application directory.
Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Description](#API_UpdateApplication_RequestSyntax) **   <a name="gameliftstreams-UpdateApplication-request-Description"></a>
A human-readable label for the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: No

## Response Syntax
<a name="API_UpdateApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationLogOutputUri": "string",
   "ApplicationLogPaths": [ "string" ],
   "ApplicationSourceUri": "string",
   "Arn": "string",
   "AssociatedStreamGroups": [ "string" ],
   "CreatedAt": number,
   "Description": "string",
   "ExecutablePath": "string",
   "Id": "string",
   "LastUpdatedAt": number,
   "ReplicationStatuses": [
      {
         "Location": "string",
         "Status": "string"
      }
   ],
   "RuntimeEnvironment": {
      "Type": "string",
      "Version": "string"
   },
   "Status": "string",
   "StatusReason": "string"
}
```

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that's assigned to an application resource and uniquely identifies it across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:application/[resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`

 ** [ApplicationLogOutputUri](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-ApplicationLogOutputUri"></a>
An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?`

 ** [ApplicationLogPaths](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-ApplicationLogPaths"></a>
Locations of log files that your content generates during a stream session. Amazon GameLift Streams uploads log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ApplicationSourceUri](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-ApplicationSourceUri"></a>
The original Amazon S3 location of uploaded stream content for the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [AssociatedStreamGroups](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-AssociatedStreamGroups"></a>
 A set of stream groups that this application is associated with. You can use any of these stream groups to stream your application.
This value is a set of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identify stream group resources. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [CreatedAt](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Description](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-Description"></a>
A human-readable label for the application. You can edit this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [ExecutablePath](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-ExecutablePath"></a>
The relative path and file name of the executable file that launches the content for streaming.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [Id](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-Id"></a>
A unique ID value that is assigned to the resource when it's created. Format example: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [LastUpdatedAt](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [ReplicationStatuses](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-ReplicationStatuses"></a>
A set of replication statuses for each location.
Type: Array of [ReplicationStatus](API_ReplicationStatus.md) objects

 ** [RuntimeEnvironment](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-RuntimeEnvironment"></a>
 Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.
A runtime environment can be one of the following:
+  For Linux applications
  +  Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS`)
+  For Windows applications
  + Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022`)
  + Proton 10.0-4 (`Type=PROTON, Version=20260204`)
  + Proton 9.0-2 (`Type=PROTON, Version=20250516`)
  + Proton 8.0-5 (`Type=PROTON, Version=20241007`)
  + Proton 8.0-2c (`Type=PROTON, Version=20230704`)
Type: [RuntimeEnvironment](API_RuntimeEnvironment.md) object

 ** [Status](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-Status"></a>
The current status of the application resource. Possible statuses include the following:
+  `INITIALIZED`: Amazon GameLift Streams has received the request and is initiating the work flow to create an application.
+  `PROCESSING`: The create application work flow is in process. Amazon GameLift Streams is copying the content and caching for future deployment in a stream group.
+  `READY`: The application is ready to deploy in a stream group.
+  `ERROR`: An error occurred when setting up the application. See `StatusReason` for more information.
+  `DELETING`: Amazon GameLift Streams is in the process of deleting the application.
Type: String
Valid Values: `INITIALIZED | PROCESSING | READY | DELETING | ERROR`

 ** [StatusReason](#API_UpdateApplication_ResponseSyntax) **   <a name="gameliftstreams-UpdateApplication-response-StatusReason"></a>
A short description of the status reason when the application is in `ERROR` status.
Type: String
Valid Values: `internalError | accessDenied | sourceModified`

## Errors
<a name="API_UpdateApplication_Errors"></a>

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
<a name="API_UpdateApplication_Examples"></a>

### CLI Example
<a name="API_UpdateApplication_Example_1"></a>

The following example shows how to use the AWS CLI to update the mutable metadata for a Amazon GameLift Streams application. This example uses the application ID value.

#### Sample Request
<a name="API_UpdateApplication_Example_1_Request"></a>

```
aws gameliftstreams update-application \
  --identifier arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6 \
  --description "MyGame_jp v1"
```

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
