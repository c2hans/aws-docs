---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_MediaAnalysisJobDescription.html
---

# MediaAnalysisJobDescription
<a name="API_MediaAnalysisJobDescription"></a>

Description for a media analysis job.

## Contents
<a name="API_MediaAnalysisJobDescription_Contents"></a>

 ** CreationTimestamp **   <a name="rekognition-Type-MediaAnalysisJobDescription-CreationTimestamp"></a>
The Unix date and time when the job was started.
Type: Timestamp
Required: Yes

 ** Input **   <a name="rekognition-Type-MediaAnalysisJobDescription-Input"></a>
Reference to the input manifest that was provided in the job creation request.
Type: [MediaAnalysisInput](API_MediaAnalysisInput.md) object
Required: Yes

 ** JobId **   <a name="rekognition-Type-MediaAnalysisJobDescription-JobId"></a>
The identifier for a media analysis job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** OperationsConfig **   <a name="rekognition-Type-MediaAnalysisJobDescription-OperationsConfig"></a>
Operation configurations that were provided during job creation.
Type: [MediaAnalysisOperationsConfig](API_MediaAnalysisOperationsConfig.md) object
Required: Yes

 ** OutputConfig **   <a name="rekognition-Type-MediaAnalysisJobDescription-OutputConfig"></a>
Output configuration that was provided in the creation request.
Type: [MediaAnalysisOutputConfig](API_MediaAnalysisOutputConfig.md) object
Required: Yes

 ** Status **   <a name="rekognition-Type-MediaAnalysisJobDescription-Status"></a>
The status of the media analysis job being retrieved.
Type: String
Valid Values: `CREATED | QUEUED | IN_PROGRESS | SUCCEEDED | FAILED`
Required: Yes

 ** CompletionTimestamp **   <a name="rekognition-Type-MediaAnalysisJobDescription-CompletionTimestamp"></a>
The Unix date and time when the job finished.
Type: Timestamp
Required: No

 ** FailureDetails **   <a name="rekognition-Type-MediaAnalysisJobDescription-FailureDetails"></a>
Details about the error that resulted in failure of the job.
Type: [MediaAnalysisJobFailureDetails](API_MediaAnalysisJobFailureDetails.md) object
Required: No

 ** JobName **   <a name="rekognition-Type-MediaAnalysisJobDescription-JobName"></a>
The name of a media analysis job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: No

 ** KmsKeyId **   <a name="rekognition-Type-MediaAnalysisJobDescription-KmsKeyId"></a>
KMS Key that was provided in the creation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

 ** ManifestSummary **   <a name="rekognition-Type-MediaAnalysisJobDescription-ManifestSummary"></a>
Provides statistics on input manifest and errors identified in the input manifest.
Type: [MediaAnalysisManifestSummary](API_MediaAnalysisManifestSummary.md) object
Required: No

 ** Results **   <a name="rekognition-Type-MediaAnalysisJobDescription-Results"></a>
Output manifest that contains prediction results.
Type: [MediaAnalysisResults](API_MediaAnalysisResults.md) object
Required: No

## See Also
<a name="API_MediaAnalysisJobDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/MediaAnalysisJobDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/MediaAnalysisJobDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/MediaAnalysisJobDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
