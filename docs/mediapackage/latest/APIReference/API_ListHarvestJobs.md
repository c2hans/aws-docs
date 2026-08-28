---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ListHarvestJobs.html
---

# ListHarvestJobs
<a name="API_ListHarvestJobs"></a>

Retrieves a list of harvest jobs that match the specified criteria.

## Request Syntax
<a name="API_ListHarvestJobs_RequestSyntax"></a>

```
GET /channelGroup/{{ChannelGroupName}}/harvestJob?channelName={{ChannelName}}&includeStatus={{Status}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&originEndpointName={{OriginEndpointName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListHarvestJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelGroupName](#API_ListHarvestJobs_RequestSyntax) **   <a name="mediapackage-ListHarvestJobs-request-uri-ChannelGroupName"></a>
The name of the channel group to filter the harvest jobs by. If specified, only harvest jobs associated with channels in this group will be returned.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** [ChannelName](#API_ListHarvestJobs_RequestSyntax) **   <a name="mediapackage-ListHarvestJobs-request-uri-ChannelName"></a>
The name of the channel to filter the harvest jobs by. If specified, only harvest jobs associated with this channel will be returned.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [MaxResults](#API_ListHarvestJobs_RequestSyntax) **   <a name="mediapackage-ListHarvestJobs-request-uri-MaxResults"></a>
The maximum number of harvest jobs to return in a single request. If not specified, a default value will be used.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListHarvestJobs_RequestSyntax) **   <a name="mediapackage-ListHarvestJobs-request-uri-NextToken"></a>
A token used for pagination. Provide this value in subsequent requests to retrieve the next set of results.

 ** [OriginEndpointName](#API_ListHarvestJobs_RequestSyntax) **   <a name="mediapackage-ListHarvestJobs-request-uri-OriginEndpointName"></a>
The name of the origin endpoint to filter the harvest jobs by. If specified, only harvest jobs associated with this origin endpoint will be returned.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`

 ** [Status](#API_ListHarvestJobs_RequestSyntax) **   <a name="mediapackage-ListHarvestJobs-request-uri-Status"></a>
The status to filter the harvest jobs by. If specified, only harvest jobs with this status will be returned.
Valid Values: `QUEUED | IN_PROGRESS | CANCELLED | COMPLETED | FAILED`

## Request Body
<a name="API_ListHarvestJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListHarvestJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
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
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListHarvestJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListHarvestJobs_ResponseSyntax) **   <a name="mediapackage-ListHarvestJobs-response-Items"></a>
An array of harvest job objects that match the specified criteria.
Type: Array of [HarvestJob](API_HarvestJob.md) objects

 ** [NextToken](#API_ListHarvestJobs_ResponseSyntax) **   <a name="mediapackage-ListHarvestJobs-response-NextToken"></a>
A token used for pagination. Include this value in subsequent requests to retrieve the next set of results. If null, there are no more results to retrieve.
Type: String

## Errors
<a name="API_ListHarvestJobs_Errors"></a>

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
<a name="API_ListHarvestJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediapackagev2-2022-12-25/ListHarvestJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ListHarvestJobs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
