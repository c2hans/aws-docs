---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html
---

# UpdateJobStatus
<a name="API_control_UpdateJobStatus"></a>

Updates the status for the specified job. Use this operation to confirm that you want to run a job or to cancel an existing job. For more information, see [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html) in the *Amazon S3 User Guide*.

Permissions
To use the `UpdateJobStatus` operation, you must have permission to perform the `s3:UpdateJobStatus` action.

Related actions include:
+  [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)
+  [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html)
+  [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html)
+  [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)

## Request Syntax
<a name="API_control_UpdateJobStatus_RequestSyntax"></a>

```
POST /v20180820/jobs/{{id}}/status?requestedJobStatus={{RequestedJobStatus}}&statusUpdateReason={{StatusUpdateReason}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_UpdateJobStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_UpdateJobStatus_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-request-uri-uri-JobId"></a>
The ID of the job whose status you want to update.
Length Constraints: Minimum length of 5. Maximum length of 36.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [requestedJobStatus](#API_control_UpdateJobStatus_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-request-uri-querystring-RequestedJobStatus"></a>
The status that you want to move the specified job to.
Valid Values: `Cancelled | Ready`
Required: Yes

 ** [statusUpdateReason](#API_control_UpdateJobStatus_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-request-uri-querystring-StatusUpdateReason"></a>
A description of the reason why you want to change the specified job's status. This field can be any string up to the maximum length.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [x-amz-account-id](#API_control_UpdateJobStatus_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-request-header-AccountId"></a>
The AWS account ID associated with the S3 Batch Operations job.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_UpdateJobStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_UpdateJobStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateJobStatusResult>
   <JobId>string</JobId>
   <Status>string</Status>
   <StatusUpdateReason>string</StatusUpdateReason>
</UpdateJobStatusResult>
```

## Response Elements
<a name="API_control_UpdateJobStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [UpdateJobStatusResult](#API_control_UpdateJobStatus_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-response-UpdateJobStatusResult"></a>
Root level tag for the UpdateJobStatusResult parameters.
Required: Yes

 ** [JobId](#API_control_UpdateJobStatus_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-response-JobId"></a>
The ID for the job whose status was updated.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 36.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [Status](#API_control_UpdateJobStatus_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-response-Status"></a>
The current status for the specified job.
Type: String
Valid Values: `Active | Cancelled | Cancelling | Complete | Completing | Failed | Failing | New | Paused | Pausing | Preparing | Ready | Suspended`

 ** [StatusUpdateReason](#API_control_UpdateJobStatus_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobStatus-response-StatusUpdateReason"></a>
The reason that the specified job's status was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_control_UpdateJobStatus_Errors"></a>

 ** BadRequestException **

HTTP Status Code: 400

 ** InternalServiceException **

HTTP Status Code: 500

 ** JobStatusException **

HTTP Status Code: 400

 ** NotFoundException **

HTTP Status Code: 400

 ** TooManyRequestsException **

HTTP Status Code: 400

## See Also
<a name="API_control_UpdateJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateJobStatus)
