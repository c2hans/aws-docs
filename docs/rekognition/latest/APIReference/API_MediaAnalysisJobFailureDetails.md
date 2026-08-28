---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_MediaAnalysisJobFailureDetails.html
---

# MediaAnalysisJobFailureDetails
<a name="API_MediaAnalysisJobFailureDetails"></a>

Details about the error that resulted in failure of the job.

## Contents
<a name="API_MediaAnalysisJobFailureDetails_Contents"></a>

 ** Code **   <a name="rekognition-Type-MediaAnalysisJobFailureDetails-Code"></a>
Error code for the failed job.
Type: String
Valid Values: `INTERNAL_ERROR | INVALID_S3_OBJECT | INVALID_MANIFEST | INVALID_OUTPUT_CONFIG | INVALID_KMS_KEY | ACCESS_DENIED | RESOURCE_NOT_FOUND | RESOURCE_NOT_READY | THROTTLED`
Required: No

 ** Message **   <a name="rekognition-Type-MediaAnalysisJobFailureDetails-Message"></a>
Human readable error message.
Type: String
Required: No

## See Also
<a name="API_MediaAnalysisJobFailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/MediaAnalysisJobFailureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/MediaAnalysisJobFailureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/MediaAnalysisJobFailureDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
