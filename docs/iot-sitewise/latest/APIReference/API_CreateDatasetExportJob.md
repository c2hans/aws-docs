---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateDatasetExportJob.html
---

# CreateDatasetExportJob
<a name="API_CreateDatasetExportJob"></a>

Starts an asynchronous job that exports dataset and time-series data from a workspace to Amazon S3. The operation returns a jobId immediately; poll DescribeDatasetExportJob to track progress and ListDatasetExportJobs to enumerate a workspace's jobs.

## Request Syntax
<a name="API_CreateDatasetExportJob_RequestSyntax"></a>

```
POST /workspaces/{{workspaceName}}/dataset-export-jobs HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "destinationS3Uri": "{{string}}",
   "errorReportLocation": {
      "s3Uri": "{{string}}"
   },
   "input": { ... }
}
```

## URI Request Parameters
<a name="API_CreateDatasetExportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceName](#API_CreateDatasetExportJob_RequestSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-request-uri-workspaceName"></a>
The name of the workspace in which to create the dataset export job.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_CreateDatasetExportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateDatasetExportJob_RequestSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. The AWS SDKs and CLI populate this automatically.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 64.
Pattern: `\S{36,64}`
Required: No

 ** [destinationS3Uri](#API_CreateDatasetExportJob_RequestSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-request-destinationS3Uri"></a>
The S3 URI where output clips will be written.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
Required: Yes

 ** [errorReportLocation](#API_CreateDatasetExportJob_RequestSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-request-errorReportLocation"></a>
The location where the error report will be written on failure.
Type: [ExportErrorReportLocation](API_ExportErrorReportLocation.md) object
Required: Yes

 ** [input](#API_CreateDatasetExportJob_RequestSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-request-input"></a>
The processing input source.
Type: [ProcessingInput](API_ProcessingInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateDatasetExportJob_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "jobId": "string",
   "workspaceName": "string"
}
```

## Response Elements
<a name="API_CreateDatasetExportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_CreateDatasetExportJob_ResponseSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-response-jobId"></a>
The unique identifier for the dataset export job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [workspaceName](#API_CreateDatasetExportJob_ResponseSyntax) **   <a name="iotsitewise-CreateDatasetExportJob-response-workspaceName"></a>
The name of the workspace in which the dataset export job was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

## Errors
<a name="API_CreateDatasetExportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** ConflictingOperationException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
 ** resourceArn **
The ARN of the resource that conflicts with this operation.
 ** resourceId **
The ID of the resource that conflicts with this operation.
HTTP Status Code: 409

 ** InternalFailureException **
 AWS IoT SiteWise can't process your request right now. Try again later.
HTTP Status Code: 500

 ** InvalidRequestException **
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The requested resource can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
HTTP Status Code: 429

## See Also
<a name="API_CreateDatasetExportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotsitewise-2019-12-02/CreateDatasetExportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/CreateDatasetExportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
