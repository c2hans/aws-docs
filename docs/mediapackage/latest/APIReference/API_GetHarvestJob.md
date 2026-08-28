---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_GetHarvestJob.html
---

# GetHarvestJob
<a name="API_GetHarvestJob"></a>

Retrieves the details of a specific harvest job.

## Request Syntax
<a name="API_GetHarvestJob_RequestSyntax"></a>

```
GET /channelGroup/{{ChannelGroupName}}/channel/{{ChannelName}}/originEndpoint/{{OriginEndpointName}}/harvestJob/{{HarvestJobName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetHarvestJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_GetHarvestJob_RequestSyntax) **   <a name="mediapackage-GetHarvestJob-request-uri-ChannelGroupName"></a>
The name of the channel group containing the channel associated with the harvest job.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_GetHarvestJob_RequestSyntax) **   <a name="mediapackage-GetHarvestJob-request-uri-ChannelName"></a>
The name of the channel associated with the harvest job.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [HarvestJobName](#API_GetHarvestJob_RequestSyntax) **   <a name="mediapackage-GetHarvestJob-request-uri-HarvestJobName"></a>
The name of the harvest job to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [OriginEndpointName](#API_GetHarvestJob_RequestSyntax) **   <a name="mediapackage-GetHarvestJob-request-uri-OriginEndpointName"></a>
The name of the origin endpoint associated with the harvest job.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_GetHarvestJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetHarvestJob_ResponseSyntax"></a>

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
<a name="API_GetHarvestJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-Arn"></a>
The Amazon Resource Name (ARN) of the harvest job.
Type: String

 ** [ChannelGroupName](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-ChannelGroupName"></a>
The name of the channel group containing the channel associated with the harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ChannelName](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-ChannelName"></a>
The name of the channel associated with the harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [CreatedAt](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-CreatedAt"></a>
The date and time when the harvest job was created.
Type: Timestamp

 ** [Description](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-Description"></a>
The description of the harvest job, if provided.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [Destination](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-Destination"></a>
The S3 destination where the harvested content is being placed.
Type: [Destination](API_Destination.md) object

 ** [ErrorMessage](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-ErrorMessage"></a>
An error message if the harvest job encountered any issues.
Type: String

 ** [ETag](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-ETag"></a>
The current version of the harvest job. Used for concurrency control.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\S]+`

 ** [HarvestedManifests](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-HarvestedManifests"></a>
A list of manifests that are being or have been harvested.
Type: [HarvestedManifests](API_HarvestedManifests.md) object

 ** [HarvestJobName](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-HarvestJobName"></a>
The name of the harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ModifiedAt](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-ModifiedAt"></a>
The date and time when the harvest job was last modified.
Type: Timestamp

 ** [OriginEndpointName](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-OriginEndpointName"></a>
The name of the origin endpoint associated with the harvest job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [ScheduleConfiguration](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-ScheduleConfiguration"></a>
The configuration for when the harvest job is scheduled to run, including start and end times.
Type: [HarvesterScheduleConfiguration](API_HarvesterScheduleConfiguration.md) object

 ** [Status](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-Status"></a>
The current status of the harvest job (e.g., QUEUED, IN\_PROGRESS, CANCELLED, COMPLETED, FAILED).
Type: String
Valid Values: `QUEUED | IN_PROGRESS | CANCELLED | COMPLETED | FAILED`

 ** [Tags](#API_GetHarvestJob_ResponseSyntax) **   <a name="mediapackage-GetHarvestJob-response-Tags"></a>
A collection of tags associated with the harvest job.
Type: String to string map

## Errors
<a name="API_GetHarvestJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied because either you don't have permissions to perform the requested operation or MediaPackage is getting throttling errors with CDN authorization. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see Access Management in the IAM User Guide. Or, if you're using CDN authorization, you will receive this exception if MediaPackage receives a throttling error from Secrets Manager.
HTTP Status Code: 403

 ** InternalServerException **
Indicates that an error from the service occurred while trying to process a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
 ** ResourceTypeNotFound **
The specified resource type wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The request throughput limit was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** ValidationExceptionType **
The type of ValidationException.
HTTP Status Code: 400

## See Also
<a name="API_GetHarvestJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/GetHarvestJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/GetHarvestJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
