---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html
---

# UpdateJobPriority
<a name="API_control_UpdateJobPriority"></a>

Updates an existing S3 Batch Operations job's priority. For more information, see [S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/batch-ops.html) in the *Amazon S3 User Guide*.

Permissions
To use the `UpdateJobPriority` operation, you must have permission to perform the `s3:UpdateJobPriority` action.

Related actions include:
+  [CreateJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html)
+  [ListJobs](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html)
+  [DescribeJob](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html)
+  [UpdateJobStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html)

## Request Syntax
<a name="API_control_UpdateJobPriority_RequestSyntax"></a>

```
POST /v20180820/jobs/{{id}}/priority?priority={{Priority}} HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_UpdateJobPriority_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_control_UpdateJobPriority_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobPriority-request-uri-uri-JobId"></a>
The ID for the job whose priority you want to update.
Length Constraints: Minimum length of 5. Maximum length of 36.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [priority](#API_control_UpdateJobPriority_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobPriority-request-uri-querystring-Priority"></a>
The priority you want to assign to this job.
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: Yes

 ** [x-amz-account-id](#API_control_UpdateJobPriority_RequestSyntax) **   <a name="AmazonS3-control_UpdateJobPriority-request-header-AccountId"></a>
The AWS account ID associated with the S3 Batch Operations job.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_UpdateJobPriority_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_UpdateJobPriority_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<UpdateJobPriorityResult>
   <JobId>string</JobId>
   <Priority>integer</Priority>
</UpdateJobPriorityResult>
```

## Response Elements
<a name="API_control_UpdateJobPriority_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [UpdateJobPriorityResult](#API_control_UpdateJobPriority_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobPriority-response-UpdateJobPriorityResult"></a>
Root level tag for the UpdateJobPriorityResult parameters.
Required: Yes

 ** [JobId](#API_control_UpdateJobPriority_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobPriority-response-JobId"></a>
The ID for the job whose priority Amazon S3 updated.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 36.
Pattern: `[a-zA-Z0-9\-\_]+`

 ** [Priority](#API_control_UpdateJobPriority_ResponseSyntax) **   <a name="AmazonS3-control_UpdateJobPriority-response-Priority"></a>
The new priority assigned to the specified job.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

## Errors
<a name="API_control_UpdateJobPriority_Errors"></a>

 ** BadRequestException **

HTTP Status Code: 400

 ** InternalServiceException **

HTTP Status Code: 500

 ** NotFoundException **

HTTP Status Code: 400

 ** TooManyRequestsException **

HTTP Status Code: 400

## See Also
<a name="API_control_UpdateJobPriority_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/UpdateJobPriority)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/UpdateJobPriority)
