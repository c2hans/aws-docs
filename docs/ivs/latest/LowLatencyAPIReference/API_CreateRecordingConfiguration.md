---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_CreateRecordingConfiguration.html
---

# CreateRecordingConfiguration
<a name="API_CreateRecordingConfiguration"></a>

Creates a new recording configuration, used to enable recording to Amazon S3.

 **Known issue:** In the us-east-1 region, if you use the AWS CLI to create a recording configuration, it returns success even if the S3 bucket is in a different region. In this case, the `state` of the recording configuration is `CREATE_FAILED` (instead of `ACTIVE`). (In other regions, the CLI correctly returns failure if the bucket is in a different region.)

 **Workaround:** Ensure that your S3 bucket is in the same region as the recording configuration. If you create a recording configuration in a different region as your S3 bucket, delete that recording configuration and create a new one with an S3 bucket from the correct region.

## Request Syntax
<a name="API_CreateRecordingConfiguration_RequestSyntax"></a>

```
POST /CreateRecordingConfiguration HTTP/1.1
Content-type: application/json

{
   "destinationConfiguration": {
      "s3": {
         "bucketName": "{{string}}"
      }
   },
   "name": "{{string}}",
   "recordingReconnectWindowSeconds": {{number}},
   "renditionConfiguration": {
      "renditions": [ "{{string}}" ],
      "renditionSelection": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "thumbnailConfiguration": {
      "recordingMode": "{{string}}",
      "resolution": "{{string}}",
      "storage": [ "{{string}}" ],
      "targetIntervalSeconds": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateRecordingConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRecordingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationConfiguration](#API_CreateRecordingConfiguration_RequestSyntax) **   <a name="ivs-CreateRecordingConfiguration-request-destinationConfiguration"></a>
A complex type that contains a destination configuration for where recorded video will be stored.
Type: [DestinationConfiguration](API_DestinationConfiguration.md) object
Required: Yes

 ** [name](#API_CreateRecordingConfiguration_RequestSyntax) **   <a name="ivs-CreateRecordingConfiguration-request-name"></a>
Recording-configuration name. The value does not need to be unique.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [recordingReconnectWindowSeconds](#API_CreateRecordingConfiguration_RequestSyntax) **   <a name="ivs-CreateRecordingConfiguration-request-recordingReconnectWindowSeconds"></a>
If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 300.
Required: No

 ** [renditionConfiguration](#API_CreateRecordingConfiguration_RequestSyntax) **   <a name="ivs-CreateRecordingConfiguration-request-renditionConfiguration"></a>
Object that describes which renditions should be recorded for a stream.
Type: [RenditionConfiguration](API_RenditionConfiguration.md) object
Required: No

 ** [tags](#API_CreateRecordingConfiguration_RequestSyntax) **   <a name="ivs-CreateRecordingConfiguration-request-tags"></a>
Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** [thumbnailConfiguration](#API_CreateRecordingConfiguration_RequestSyntax) **   <a name="ivs-CreateRecordingConfiguration-request-thumbnailConfiguration"></a>
A complex type that allows you to enable/disable the recording of thumbnails for a live session and modify the interval at which thumbnails are generated for the live session.
Type: [ThumbnailConfiguration](API_ThumbnailConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateRecordingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recordingConfiguration": {
      "arn": "string",
      "destinationConfiguration": {
         "s3": {
            "bucketName": "string"
         }
      },
      "name": "string",
      "recordingReconnectWindowSeconds": number,
      "renditionConfiguration": {
         "renditions": [ "string" ],
         "renditionSelection": "string"
      },
      "state": "string",
      "tags": {
         "string" : "string"
      },
      "thumbnailConfiguration": {
         "recordingMode": "string",
         "resolution": "string",
         "storage": [ "string" ],
         "targetIntervalSeconds": number
      }
   }
}
```

## Response Elements
<a name="API_CreateRecordingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recordingConfiguration](#API_CreateRecordingConfiguration_ResponseSyntax) **   <a name="ivs-CreateRecordingConfiguration-response-recordingConfiguration"></a>
An object representing a configuration to record a channel stream.
Type: [RecordingConfiguration](API_RecordingConfiguration.md) object

## Errors
<a name="API_CreateRecordingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateRecordingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/CreateRecordingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/CreateRecordingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
