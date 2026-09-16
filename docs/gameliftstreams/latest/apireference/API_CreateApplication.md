---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

Creates an application resource in Amazon GameLift Streams, which specifies the application content you want to stream, such as a game build or other software, and configures the settings to run it.

 Before you create an application, upload your application content files to an Amazon Simple Storage Service (Amazon S3) bucket. For more information, see **Getting Started** in the Amazon GameLift Streams Developer Guide.

**Important**
 Make sure that your files in the Amazon S3 bucket are the correct version you want to use. If you change the files at a later time, you will need to create a new Amazon GameLift Streams application.

**Note**
 Creating an application is the only time Amazon GameLift Streams accesses your Amazon S3 bucket. After the application reaches `READY` status, you can delete the original files from your Amazon S3 bucket without affecting the application.

 If the request is successful, Amazon GameLift Streams begins to create an application and sets the status to `INITIALIZED`. When an application reaches `READY` status, you can use the application to set up stream groups and start streams. To track application status, call [GetApplication](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetApplication.html).

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
POST /applications HTTP/1.1
Content-type: application/json

{
   "ApplicationLogOutputUri": "{{string}}",
   "ApplicationLogPaths": [ "{{string}}" ],
   "ApplicationSourceUri": "{{string}}",
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "ExecutablePath": "{{string}}",
   "RuntimeEnvironment": {
      "Type": "{{string}}",
      "Version": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationSourceUri](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-ApplicationSourceUri"></a>
The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.
This value is immutable. To designate a different content location, create a new application.
The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [Description](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-Description"></a>
A human-readable label for the application. You can update this value later.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`
Required: Yes

 ** [ExecutablePath](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-ExecutablePath"></a>
The relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the location set in `ApplicationSourceUri`. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('`#!`').
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [RuntimeEnvironment](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-RuntimeEnvironment"></a>
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
Required: Yes

 ** [ApplicationLogOutputUri](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-ApplicationLogOutputUri"></a>
An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths`.
The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see [Application log bucket permission policy](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template) in the *Amazon GameLift Streams Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?`
Required: No

 ** [ApplicationLogPaths](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-ApplicationLogPaths"></a>
Locations of log files that your content generates during a stream session. Enter path values that are relative to the `ApplicationSourceUri` location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.
Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: `.txt`, `.log`, and `.utrace`. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.
The following path variables are recognized when they appear as the first component of a path: `%USERPROFILE%` (Windows and Proton), `$HOME` or `~` (Linux). Use a path variable when your application writes logs outside of the application directory.
Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [ClientToken](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-ClientToken"></a>
 A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [Tags](#API_CreateApplication_RequestSyntax) **   <a name="gameliftstreams-CreateApplication-request-Tags"></a>
A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management and cost allocation. See [ Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference*. You can use [TagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html) to add tags, [UntagResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html) to remove tags, and [ListTagsForResource](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html) to view tags on existing resources.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-Arn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that's assigned to an application resource and uniquely identifies it across all AWS Regions. Format is `arn:aws:gameliftstreams:[AWS Region]:[AWS account]:application/[resource ID]`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`

 ** [ApplicationLogOutputUri](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-ApplicationLogOutputUri"></a>
An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more `ApplicationLogPaths`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `$|^s3://([a-zA-Z0-9][a-zA-Z0-9._-]{1,61}[a-zA-Z0-9])(/[a-zA-Z0-9._-]+)*/?`

 ** [ApplicationLogPaths](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-ApplicationLogPaths"></a>
Locations of log files that your content generates during a stream session. Amazon GameLift Streams uploads log files to the Amazon S3 bucket that you specify in `ApplicationLogOutputUri` at the end of a stream session. To retrieve stored log files, call [GetStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html) and get the `LogFileLocationUri`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ApplicationSourceUri](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-ApplicationSourceUri"></a>
The original Amazon S3 location of uploaded stream content for the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [AssociatedStreamGroups](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-AssociatedStreamGroups"></a>
A newly created application is not associated to any stream groups. This value is empty.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [CreatedAt](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-CreatedAt"></a>
A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [Description](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-Description"></a>
A human-readable label for the application. You can edit this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Pattern: `[a-zA-Z0-9-_.!+@/][a-zA-Z0-9-_.!+@/ ]*`

 ** [ExecutablePath](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-ExecutablePath"></a>
The relative path and file name of the executable file that launches the content for streaming.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [Id](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-Id"></a>
A unique ID value that is assigned to the resource when it's created. Format example: `a-9ZY8X7Wv6`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-zA-Z0-9-]+`

 ** [LastUpdatedAt](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-LastUpdatedAt"></a>
A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: `2022-12-27T22:29:40+00:00` (UTC).
Type: Timestamp

 ** [ReplicationStatuses](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-ReplicationStatuses"></a>
A set of replication statuses for each location.
Type: Array of [ReplicationStatus](API_ReplicationStatus.md) objects

 ** [RuntimeEnvironment](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-RuntimeEnvironment"></a>
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

 ** [Status](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-Status"></a>
The current status of the application resource. Possible statuses include the following:
+  `INITIALIZED`: Amazon GameLift Streams has received the request and is initiating the work flow to create an application.
+  `PROCESSING`: The create application work flow is in process. Amazon GameLift Streams is copying the content and caching for future deployment in a stream group.
+  `READY`: The application is ready to deploy in a stream group.
+  `ERROR`: An error occurred when setting up the application. See `StatusReason` for more information.
+  `DELETING`: Amazon GameLift Streams is in the process of deleting the application.
Type: String
Valid Values: `INITIALIZED | PROCESSING | READY | DELETING | ERROR`

 ** [StatusReason](#API_CreateApplication_ResponseSyntax) **   <a name="gameliftstreams-CreateApplication-response-StatusReason"></a>
A short description of the status reason when the application is in `ERROR` status.
Type: String
Valid Values: `internalError | accessDenied | sourceModified`

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** Message **
Description of the error.
HTTP Status Code: 409

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The request would cause the resource to exceed an allowed service quota. Resolve the issue before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 402

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
<a name="API_CreateApplication_Examples"></a>

### CLI Example
<a name="API_CreateApplication_Example_1"></a>

The following example shows how to use the AWS CLI to create a Amazon GameLift Streams application.

#### Sample Request
<a name="API_CreateApplication_Example_1_Request"></a>

```
aws gameliftstreams create-application \
  --description "MyGame v1" \
  --runtime-environment '{"Type":"PROTON", "Version":"20241007"}' \
  --executable-path "launcher.exe" \
  --application-source-uri "s3://amzn-s3-demo-bucket/example-game" \
  --application-log-paths '[".\\logs"]' \
  --application-log-output-uri "s3://amzn-s3-demo-logging-bucket/example-game/logs"
```

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/CreateApplication)
