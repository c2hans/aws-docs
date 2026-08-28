---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_S3ReportOutputConfiguration.html
---

# S3ReportOutputConfiguration
<a name="API_S3ReportOutputConfiguration"></a>

Configuration for delivering generated reports to an Amazon S3 bucket.

## Contents
<a name="API_S3ReportOutputConfiguration_Contents"></a>

 ** bucketOwner **   <a name="regionswitch-Type-S3ReportOutputConfiguration-bucketOwner"></a>
The AWS account ID that owns the S3 bucket. Required to ensure the bucket is still owned by the same expected owner at generation time.
Type: String
Pattern: `\d{12}`
Required: No

 ** bucketPath **   <a name="regionswitch-Type-S3ReportOutputConfiguration-bucketPath"></a>
The S3 bucket name and optional prefix where reports are stored. Format: bucket-name or bucket-name/prefix.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `(?:s3://)?[a-z0-9][a-z0-9-]{1,61}[a-z0-9](?:/[^/ ][^/]*)*/?`
Required: No

## See Also
<a name="API_S3ReportOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/S3ReportOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/S3ReportOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/S3ReportOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
