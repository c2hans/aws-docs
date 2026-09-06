---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeJob.html
---

# DescribeJob
<a name="API_DescribeJob"></a>

Returns detailed information about a job, including its current status, secondary status, configuration, and timestamps. Use `SecondaryStatus` for granular progress tracking and `SecondaryStatusTransitions` to see the full history of status changes with timestamps.

The following operations are related to `DescribeJob`:
+  `CreateJob`
+  `ListJobs`
+  `StopJob`
+  `DeleteJob`

## Request Syntax
<a name="API_DescribeJob_RequestSyntax"></a>

```
{
   "JobCategory": "{{string}}",
   "JobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobCategory](#API_DescribeJob_RequestSyntax) **   <a name="sagemaker-DescribeJob-request-JobCategory"></a>
The category of the job.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: Yes

 ** [JobName](#API_DescribeJob_RequestSyntax) **   <a name="sagemaker-DescribeJob-request-JobName"></a>
The name of the job to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeJob_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "EndTime": number,
   "FailureReason": "string",
   "JobArn": "string",
   "JobCategory": "string",
   "JobConfigDocument": "string",
   "JobConfigSchemaVersion": "string",
   "JobName": "string",
   "JobStatus": "string",
   "LastModifiedTime": number,
   "RoleArn": "string",
   "SecondaryStatus": "string",
   "SecondaryStatusTransitions": [
      {
         "EndTime": number,
         "StartTime": number,
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-CreationTime"></a>
The date and time that the job was created.
Type: Timestamp

 ** [EndTime](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-EndTime"></a>
The date and time that the job ended.
Type: Timestamp

 ** [FailureReason](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-FailureReason"></a>
If the job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [JobArn](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-JobArn"></a>
The Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:job/[a-zA-Z0-9]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [JobCategory](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-JobCategory"></a>
The category of the job.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`

 ** [JobConfigDocument](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-JobConfigDocument"></a>
The JSON configuration document for the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.

 ** [JobConfigSchemaVersion](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-JobConfigSchemaVersion"></a>
The schema version used for the job configuration document.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 16.
Pattern: `\d+\.\d+\.\d+`

 ** [JobName](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-JobName"></a>
The name of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [JobStatus](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-JobStatus"></a>
The current status of the job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped | Deleting | DeleteFailed`

 ** [LastModifiedTime](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-LastModifiedTime"></a>
The date and time that the job was last modified.
Type: Timestamp

 ** [RoleArn](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-RoleArn"></a>
The ARN of the IAM role associated with the job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [SecondaryStatus](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-SecondaryStatus"></a>
The detailed secondary status of the job, providing more granular information about the job's progress. Secondary statuses may change between releases.
Type: String
Valid Values: `Starting | Downloading | Training | Uploading | Stopping | Stopped | MaxRuntimeExceeded | Interrupted | Failed | Completed | Restarting | Pending | Evaluating | Deleting | DeleteFailed`

 ** [SecondaryStatusTransitions](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-SecondaryStatusTransitions"></a>
A list of secondary status transitions for the job, with timestamps and optional status messages.
Type: Array of [JobSecondaryStatusTransition](API_JobSecondaryStatusTransition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [Tags](#API_DescribeJob_ResponseSyntax) **   <a name="sagemaker-DescribeJob-response-Tags"></a>
The tags associated with the job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_DescribeJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeJob)
