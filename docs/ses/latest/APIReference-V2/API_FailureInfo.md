---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_FailureInfo.html
---

# FailureInfo
<a name="API_FailureInfo"></a>

An object that contains the failure details about a job.

## Contents
<a name="API_FailureInfo_Contents"></a>

 ** ErrorMessage **   <a name="SES-Type-FailureInfo-ErrorMessage"></a>
A message about why the job failed.
Type: String
Required: No

 ** FailedRecordsS3Url **   <a name="SES-Type-FailureInfo-FailedRecordsS3Url"></a>
An Amazon S3 pre-signed URL that contains all the failed records and related information.
Type: String
Required: No

## See Also
<a name="API_FailureInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/FailureInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/FailureInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/FailureInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
