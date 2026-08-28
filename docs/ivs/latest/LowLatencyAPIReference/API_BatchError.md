---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchError.html
---

# BatchError
<a name="API_BatchError"></a>

Error related to a specific channel, specified by its ARN.

## Contents
<a name="API_BatchError_Contents"></a>

 ** arn **   <a name="ivs-Type-BatchError-arn"></a>
ARN of an IVS resource; e.g., channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+`
Required: No

 ** code **   <a name="ivs-Type-BatchError-code"></a>
Error code.
Type: String
Required: No

 ** message **   <a name="ivs-Type-BatchError-message"></a>
Error message, determined by the application.
Type: String
Required: No

## See Also
<a name="API_BatchError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/BatchError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/BatchError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/BatchError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
