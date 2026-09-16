---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_CreateHarvestJob.html
---

# CreateHarvestJob
<a name="API_CreateHarvestJob"></a>

Creates a new harvest job to export content from a MediaPackage v2 channel to an S3 bucket.

## Request Syntax
<a name="API_CreateHarvestJob_RequestSyntax"></a>

```
POST /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}}/harvestJob HTTP/1.1
x-amzn-client-token: {{ClientToken}}
Content-type: application/json

{
   "Description": "{{string}}",
   "Destination": {
      "S3Destination": {
         "BucketName": "{{string}}",
         "DestinationPath": "{{string}}"
      }
   },
   "HarvestedManifests": {
      "DashManifests": [
         {
            "ManifestName": "{{string}}"
         }
      ],
      "HlsManifests": [
         {
            "ManifestName": "{{string}}"
         }
      ],
      "LowLatencyHlsManifests": [
         {
            "ManifestName": "{{string}}"
         }
      ]
   },
   "HarvestJobName": "{{string}}",
   "ScheduleConfiguration": {
      "EndTime": {{number}},
      "StartTime": {{number}}
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateHarvestJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-uri-ChannelGroupName"></a>
The name of the channel group containing the channel from which to harvest content.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-uri-ChannelName"></a>
The name of the channel from which to harvest content.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ClientToken](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [OriginEndpointName](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-uri-OriginEndpointName"></a>
The name of the origin endpoint from which to harvest content.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_CreateHarvestJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-Description"></a>
An optional description for the harvest job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [Destination](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-Destination"></a>
The S3 destination where the harvested content will be placed.
Type: [Destination](API_Destination.md) object
Required: Yes

 ** [HarvestedManifests](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-HarvestedManifests"></a>
A list of manifests to be harvested.
Type: [HarvestedManifests](API_HarvestedManifests.md) object
Required: Yes

 ** [HarvestJobName](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-HarvestJobName"></a>
A name for the harvest job. This name must be unique within the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [ScheduleConfiguration](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-ScheduleConfiguration"></a>
The configuration for when the harvest job should run, including start and end times.
Type: [HarvesterScheduleConfiguration](API_HarvesterScheduleConfiguration.md) object
Required: Yes

 ** [Tags](#API_CreateHarvestJob_RequestSyntax) **   <a name="mediapackage-CreateHarvestJob-request-Tags"></a>
A collection of tags associated with the harvest job.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateHarvestJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "ChannelGroupName": "string",
   "ChannelName": "string",
   "CreatedAt": number,
   "Description": "string",
   "Destination": {
      "S3Destination": {
         "BucketName": "string",
         "DestinationPath": "string"
      }
   },
   "ErrorMessage": "string",
   "ETag": "string",
   "HarvestedManifests": {
      "DashManifests": [
         {
            "ManifestName": "string"
         }
      ],
      "HlsManifests": [
         {
            "ManifestName": "string"
         }
      ],
      "LowLatencyHlsManifests": [
         {
            "ManifestName": "string"
         }
      ]
   },
   "HarvestJobName": "string",
   "ModifiedAt": number,
   "OriginEndpointName": "string",
   "ScheduleConfiguration": {
      "EndTime": number,
      "StartTime": number
   },
   "Status": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_CreateHarvestJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the created harvest job.
Type: String

 ** [ChannelGroupName](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-ChannelGroupName"></a>
The name of the channel group containing the channel from which content is being harvested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ChannelName](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-ChannelName"></a>
The name of the channel from which content is being harvested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [CreatedAt](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-CreatedAt"></a>
The date and time the harvest job was created.
Type: Timestamp

 ** [Description](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-Description"></a>
The description of the harvest job, if provided.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Destination](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-Destination"></a>
The S3 destination where the harvested content will be placed.
Type: [Destination](API_Destination.md) object

 ** [ErrorMessage](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-ErrorMessage"></a>
An error message if the harvest job creation failed.
Type: String

 ** [ETag](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-ETag"></a>
The current version of the harvest job. Used for concurrency control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [HarvestedManifests](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-HarvestedManifests"></a>
A list of manifests that will be harvested.
Type: [HarvestedManifests](API_HarvestedManifests.md) object

 ** [HarvestJobName](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-HarvestJobName"></a>
The name of the created harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ModifiedAt](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-ModifiedAt"></a>
The date and time the harvest job was last modified.
Type: Timestamp

 ** [OriginEndpointName](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-OriginEndpointName"></a>
The name of the origin endpoint from which content is being harvested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ScheduleConfiguration](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-ScheduleConfiguration"></a>
The configuration for when the harvest job will run, including start and end times.
Type: [HarvesterScheduleConfiguration](API_HarvesterScheduleConfiguration.md) object

 ** [Status](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-Status"></a>
The current status of the harvest job (e.g., CREATED, IN\_PROGRESS, ABORTED, COMPLETED, FAILED).
Type: String
Valid Values: `QUEUED | IN_PROGRESS | CANCELLED | COMPLETED | FAILED`

 ** [Tags](#API_CreateHarvestJob_ResponseSyntax) **   <a name="mediapackage-CreateHarvestJob-response-Tags"></a>
A collection of tags associated with the harvest job.
Type: String to string map

## Errors
<a name="API_CreateHarvestJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting this resource can cause an inconsistent state.
 ** ConflictExceptionType **
The type of ConflictException.
HTTP Status Code: 409

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_CreateHarvestJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/CreateHarvestJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/CreateHarvestJob)
