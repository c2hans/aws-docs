---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MonitoringS3Output.html
---

# MonitoringS3Output
<a name="API_MonitoringS3Output"></a>

Information about where and how you want to store the results of a monitoring job.

## Contents
<a name="API_MonitoringS3Output_Contents"></a>

 ** LocalPath **   <a name="sagemaker-Type-MonitoringS3Output-LocalPath"></a>
The local path to the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job. LocalPath is an absolute path for the output data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: Yes

 ** S3Uri **   <a name="sagemaker-Type-MonitoringS3Output-S3Uri"></a>
A URI that identifies the Amazon S3 storage location where Amazon SageMaker AI saves the results of a monitoring job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** S3UploadMode **   <a name="sagemaker-Type-MonitoringS3Output-S3UploadMode"></a>
Whether to upload the results of the monitoring job continuously or after the job completes.
Type: String
Valid Values: `Continuous | EndOfJob`
Required: No

## See Also
<a name="API_MonitoringS3Output_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MonitoringS3Output)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MonitoringS3Output)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MonitoringS3Output)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
