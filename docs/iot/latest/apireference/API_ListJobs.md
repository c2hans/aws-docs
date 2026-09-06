---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListJobs.html
---

# ListJobs
<a name="API_ListJobs"></a>

Lists jobs.

Requires permission to access the [ListJobs](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_ListJobs_RequestSyntax"></a>

```
GET /jobs?maxResults={{maxResults}}&namespaceId={{namespaceId}}&nextToken={{nextToken}}&status={{status}}&targetSelection={{targetSelection}}&thingGroupId={{thingGroupId}}&thingGroupName={{thingGroupName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-maxResults"></a>
The maximum number of results to return per request.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [namespaceId](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-namespaceId"></a>
The namespace used to indicate that a job is a customer-managed job.
When you specify a value for this parameter, AWS IoT Core sends jobs notifications to MQTT topics that contain the value in the following format.
 `$aws/things/THING_NAME/jobs/JOB_ID/notify-namespace-NAMESPACE_ID/`
The `namespaceId` feature is only supported by AWS IoT Greengrass at this time. For more information, see [Setting up AWS IoT Greengrass core devices.](https://docs.aws.amazon.com/greengrass/v2/developerguide/setting-up.html)
Pattern: `[a-zA-Z0-9_-]+`

 ** [nextToken](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-nextToken"></a>
The token to retrieve the next set of results.

 ** [status](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-status"></a>
An optional filter that lets you search for jobs that have the specified status.
Valid Values: `IN_PROGRESS | CANCELED | COMPLETED | DELETION_IN_PROGRESS | SCHEDULED`

 ** [targetSelection](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-targetSelection"></a>
Specifies whether the job will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the job (SNAPSHOT). If continuous, the job may also be run on a thing when a change is detected in a target. For example, a job will run on a thing when the thing is added to a target group, even after the job was completed by all things originally in the group.
We recommend that you use continuous jobs instead of snapshot jobs for dynamic thing group targets. By using continuous jobs, devices that join the group receive the job execution even after the job has been created.
Valid Values: `CONTINUOUS | SNAPSHOT`

 ** [thingGroupId](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-thingGroupId"></a>
A filter that limits the returned jobs to those for the specified group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`

 ** [thingGroupName](#API_ListJobs_RequestSyntax) **   <a name="iot-ListJobs-request-uri-thingGroupName"></a>
A filter that limits the returned jobs to those for the specified group.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Request Body
<a name="API_ListJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [
      {
         "completedAt": number,
         "createdAt": number,
         "isConcurrent": boolean,
         "jobArn": "string",
         "jobId": "string",
         "lastUpdatedAt": number,
         "status": "string",
         "targetSelection": "string",
         "thingGroupId": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListJobs_ResponseSyntax) **   <a name="iot-ListJobs-response-jobs"></a>
A list of jobs.
Type: Array of [JobSummary](API_JobSummary.md) objects

 ** [nextToken](#API_ListJobs_ResponseSyntax) **   <a name="iot-ListJobs-response-nextToken"></a>
The token for the next set of results, or **null** if there are no additional results.
Type: String

## Errors
<a name="API_ListJobs_Errors"></a>

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListJobs)
