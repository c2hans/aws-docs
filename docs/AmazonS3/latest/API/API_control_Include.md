---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_Include.html
---

# Include
<a name="API_control_Include"></a>

A container for what Amazon S3 Storage Lens configuration includes.

## Contents
<a name="API_control_Include_Contents"></a>

 ** Buckets **   <a name="AmazonS3-Type-control_Include-Buckets"></a>
A container for the S3 Storage Lens bucket includes.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:[^:]+:s3:.*`
Required: No

 ** Regions **   <a name="AmazonS3-Type-control_Include-Regions"></a>
A container for the S3 Storage Lens Region includes.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 30.
Pattern: `[a-z0-9\-]+`
Required: No

## See Also
<a name="API_control_Include_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/Include)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/Include)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/Include)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
