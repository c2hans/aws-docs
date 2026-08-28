---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html
---

# StartMediaAnalysisJob
<a name="API_StartMediaAnalysisJob"></a>

**Important**
Service availability notice: Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Rekognition feature availability changes](https://docs.aws.amazon.com/rekognition/latest/dg/rekognition-availability-changes.html).
 **This change does not impact the availability of other Amazon Rekognition features.**

Initiates a new media analysis job. Accepts a manifest file in an Amazon S3 bucket. The output is a manifest file and a summary of the manifest stored in the Amazon S3 bucket.

## Request Syntax
<a name="API_StartMediaAnalysisJob_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "Input": {
      "S3Object": {
         "Bucket": "{{string}}",
         "Name": "{{string}}",
         "Version": "{{string}}"
      }
   },
   "JobName": "{{string}}",
   "KmsKeyId": "{{string}}",
   "OperationsConfig": {
      "DetectModerationLabels": {
         "MinConfidence": {{number}},
         "ProjectVersion": "{{string}}"
      }
   },
   "OutputConfig": {
      "S3Bucket": "{{string}}",
      "S3KeyPrefix": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartMediaAnalysisJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-StartMediaAnalysisJob-request-ClientRequestToken"></a>
Idempotency token used to prevent the accidental creation of duplicate versions. If you use the same token with multiple `StartMediaAnalysisJobRequest` requests, the same response is returned. Use `ClientRequestToken` to prevent the same request from being processed more than once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [Input](#API_StartMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-StartMediaAnalysisJob-request-Input"></a>
Input data to be analyzed by the job.
Type: [MediaAnalysisInput](API_MediaAnalysisInput.md) object
Required: Yes

 ** [JobName](#API_StartMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-StartMediaAnalysisJob-request-JobName"></a>
The name of the job. Does not have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: No

 ** [KmsKeyId](#API_StartMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-StartMediaAnalysisJob-request-KmsKeyId"></a>
The identifier of customer managed AWS KMS key (name or ARN). The key is used to encrypt images copied into the service. The key is also used to encrypt results and manifest files written to the output Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

 ** [OperationsConfig](#API_StartMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-StartMediaAnalysisJob-request-OperationsConfig"></a>
Configuration options for the media analysis job to be created.
Type: [MediaAnalysisOperationsConfig](API_MediaAnalysisOperationsConfig.md) object
Required: Yes

 ** [OutputConfig](#API_StartMediaAnalysisJob_RequestSyntax) **   <a name="rekognition-StartMediaAnalysisJob-request-OutputConfig"></a>
The Amazon S3 bucket location to store the results.
Type: [MediaAnalysisOutputConfig](API_MediaAnalysisOutputConfig.md) object
Required: Yes

## Response Syntax
<a name="API_StartMediaAnalysisJob_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_StartMediaAnalysisJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StartMediaAnalysisJob_ResponseSyntax) **   <a name="rekognition-StartMediaAnalysisJob-response-JobId"></a>
Identifier for the created job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`

## Errors
<a name="API_StartMediaAnalysisJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
A `ClientRequestToken` input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidManifestException **
Indicates that a provided manifest file is empty or larger than the allowed limit.
HTTP Status Code: 400

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** InvalidS3ObjectException **
Amazon Rekognition is unable to access the S3 object specified in the request.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Rekognition service limit was exceeded. For example, if you start too many jobs concurrently, subsequent calls to start operations (ex: `StartLabelDetection`) will raise a `LimitExceededException` exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Rekognition service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ResourceNotReadyException **
The requested resource isn't ready. For example, this exception occurs when you call `DetectCustomLabels` with a model version that isn't deployed.
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_StartMediaAnalysisJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/StartMediaAnalysisJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/StartMediaAnalysisJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
