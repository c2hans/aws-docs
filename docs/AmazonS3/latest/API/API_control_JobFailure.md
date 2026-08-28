---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobFailure.html
---

# JobFailure
<a name="API_control_JobFailure"></a>

If this job failed, this element indicates why the job failed.

## Contents
<a name="API_control_JobFailure_Contents"></a>

 ** FailureCode **   <a name="AmazonS3-Type-control_JobFailure-FailureCode"></a>
The failure code, if any, for the specified job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** FailureReason **   <a name="AmazonS3-Type-control_JobFailure-FailureReason"></a>
The failure reason, if any, for the specified job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_control_JobFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobFailure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
