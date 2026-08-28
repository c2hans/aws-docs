---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetMediaAnalysisJob.html
---

# GetMediaAnalysisJob
<a name="API_GetMediaAnalysisJob"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

Retrieves the results for a given media analysis job. Takes a `JobId` returned by StartMediaAnalysisJob.

## Request Syntax
<a name="API_GetMediaAnalysisJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMediaAnalysisJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_GetMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-GetMediaAnalysisJob-request-JobId"></a>
Unique identifier for the media analysis job for which you want to retrieve results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

## Response Syntax
<a name="API_GetMediaAnalysisJob_ResponseSyntax"></a>

```
{
   "CompletionTimestamp": number,
   "CreationTimestamp": number,
   "FailureDetails": {
      "Code": "string",
      "Message": "string"
   },
   "Input": {
      "S3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "JobId": "string",
   "JobName": "string",
   "KmsKeyId": "string",
   "ManifestSummary": {
      "S3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "OperationsConfig": {
      "DetectModerationLabels": {
         "MinConfidence": number,
         "ProjectVersion": "string"
      }
   },
   "OutputConfig": {
      "S3Bucket": "string",
      "S3KeyPrefix": "string"
   },
   "Results": {
      "ModelVersions": {
         "Moderation": "string"
      },
      "S3Object": {
         "Bucket": "string",
         "Name": "string",
         "Version": "string"
      }
   },
   "Status": "string"
}
```

## Response Elements
<a name="API_GetMediaAnalysisJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CompletionTimestamp](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-CompletionTimestamp"></a>
The Unix date and time when the job finished.
Type: Timestamp

 ** [CreationTimestamp](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-CreationTimestamp"></a>
The Unix date and time when the job was started.
Type: Timestamp

 ** [FailureDetails](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-FailureDetails"></a>
Details about the error that resulted in failure of the job.
Type: [MediaAnalysisJobFailureDetails](API_MediaAnalysisJobFailureDetails.md) object

 ** [Input](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-Input"></a>
Reference to the input manifest that was provided in the job creation request.
Type: [MediaAnalysisInput](API_MediaAnalysisInput.md) object

 ** [JobId](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-JobId"></a>
The identifier for the media analysis job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`

 ** [JobName](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-JobName"></a>
The name of the media analysis job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.\-]+`

 ** [KmsKeyId](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-KmsKeyId"></a>
KMS Key that was provided in the creation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

 ** [ManifestSummary](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-ManifestSummary"></a>
The summary manifest provides statistics on input manifest and errors identified in the input manifest.
Type: [MediaAnalysisManifestSummary](API_MediaAnalysisManifestSummary.md) object

 ** [OperationsConfig](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-OperationsConfig"></a>
Operation configurations that were provided during job creation.
Type: [MediaAnalysisOperationsConfig](API_MediaAnalysisOperationsConfig.md) object

 ** [OutputConfig](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-OutputConfig"></a>
Output configuration that was provided in the creation request.
Type: [MediaAnalysisOutputConfig](API_MediaAnalysisOutputConfig.md) object

 ** [Results](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-Results"></a>
Output manifest that contains prediction results.
Type: [MediaAnalysisResults](API_MediaAnalysisResults.md) object

 ** [Status](#API_GetMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-GetMediaAnalysisJob-response-Status"></a>
The current status of the media analysis job.
Type: String
Valid Values: `CREATED | QUEUED | IN_PROGRESS | SUCCEEDED | FAILED`

## Errors
<a name="API_GetMediaAnalysisJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_GetMediaAnalysisJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/GetMediaAnalysisJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/GetMediaAnalysisJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
