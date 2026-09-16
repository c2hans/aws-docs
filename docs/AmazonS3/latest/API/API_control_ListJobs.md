---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html
---

# ListJobs
<a name="API_control_ListJobs"></a>

Lists current S3 Batch Operations jobs as well as the jobs that have ended within the last 90 days for the AWS account making the request. For more information, see [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html) in the *Amazon S3 User Guide*.

Permissions
To use the `ListJobs` operation, you must have permission to perform the `s3:ListJobs` action.

Related actions include:

+  [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)
+  [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html)
+  [UpdateJobPriority](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html)
+  [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)

## Request Syntax
<a name="API_control_ListJobs_RequestSyntax"></a>

```
GET /v20180820/jobs?jobStatuses={{JobStatuses}}&maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_ListJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobStatuses](#API_control_ListJobs_RequestSyntax) **   <a name="AmazonS3-control_ListJobs-request-uri-querystring-JobStatuses"></a>
The `List Jobs` request returns jobs that match the statuses listed in this element.
Valid Values: `Active | Cancelled | Cancelling | Complete | Completing | Failed | Failing | New | Paused | Pausing | Preparing | Ready | Suspended`

 ** [maxResults](#API_control_ListJobs_RequestSyntax) **   <a name="AmazonS3-control_ListJobs-request-uri-querystring-MaxResults"></a>
The maximum number of jobs that Amazon S3 will include in the `List Jobs` response. If there are more jobs than this number, the response will include a pagination token in the `NextToken` field to enable you to retrieve the next page of results.
Valid Range: Minimum value of 0. Maximum value of 1000.

 ** [nextToken](#API_control_ListJobs_RequestSyntax) **   <a name="AmazonS3-control_ListJobs-request-uri-querystring-NextToken"></a>
A pagination token to request the next page of results. Use the token that Amazon S3 returned in the `NextToken` element of the `ListJobsResult` from the previous `List Jobs` request.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`

 ** [x-amz-account-id](#API_control_ListJobs_RequestSyntax) **   <a name="AmazonS3-control_ListJobs-request-header-AccountId"></a>
The AWS account ID associated with the S3 Batch Operations job.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_ListJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_ListJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListJobsResult>
   <NextToken>string</NextToken>
   <Jobs>
      <JobListDescriptor>
         <CreationTime>timestamp</CreationTime>
         <Description>string</Description>
         <JobId>string</JobId>
         <Operation>string</Operation>
         <Priority>integer</Priority>
         <ProgressSummary>
            <NumberOfTasksFailed>long</NumberOfTasksFailed>
            <NumberOfTasksSucceeded>long</NumberOfTasksSucceeded>
            <Timers>
               <ElapsedTimeInActiveSeconds>long</ElapsedTimeInActiveSeconds>
            </Timers>
            <TotalNumberOfTasks>long</TotalNumberOfTasks>
         </ProgressSummary>
         <Status>string</Status>
         <TerminationDate>timestamp</TerminationDate>
      </JobListDescriptor>
   </Jobs>
</ListJobsResult>
```

## Response Elements
<a name="API_control_ListJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListJobsResult](#API_control_ListJobs_ResponseSyntax) **   <a name="AmazonS3-control_ListJobs-response-ListJobsResult"></a>
Root level tag for the ListJobsResult parameters.
Required: Yes

 ** [Jobs](#API_control_ListJobs_ResponseSyntax) **   <a name="AmazonS3-control_ListJobs-response-Jobs"></a>
The list of current jobs and jobs that have ended within the last 30 days.
Type: Array of [JobListDescriptor](API_control_JobListDescriptor.md) data types

 ** [NextToken](#API_control_ListJobs_ResponseSyntax) **   <a name="AmazonS3-control_ListJobs-response-NextToken"></a>
If the `List Jobs` request produced more than the maximum number of results, you can pass this value into a subsequent `List Jobs` request in order to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`

## Errors
<a name="API_control_ListJobs_Errors"></a>

 ** InternalServiceException **

HTTP Status Code: 500

 ** InvalidNextTokenException **

HTTP Status Code: 400

 ** InvalidRequestException **

HTTP Status Code: 400

## See Also
<a name="API_control_ListJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/ListJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListJobs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListJobs)
