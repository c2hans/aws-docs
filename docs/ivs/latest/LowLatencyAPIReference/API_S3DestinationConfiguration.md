---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_S3DestinationConfiguration.html
---

# S3DestinationConfiguration
<a name="API_S3DestinationConfiguration"></a>

A complex type that describes an S3 location where recorded videos will be stored.

## Contents
<a name="API_S3DestinationConfiguration_Contents"></a>

 ** bucketName **   <a name="ivs-Type-S3DestinationConfiguration-bucketName"></a>
Location (S3 bucket name) where recorded videos will be stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[a-z0-9-.]+`
Required: Yes

## See Also
<a name="API_S3DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/S3DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/S3DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/S3DestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
