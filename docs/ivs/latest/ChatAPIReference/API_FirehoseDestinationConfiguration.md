---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_FirehoseDestinationConfiguration.html
---

# FirehoseDestinationConfiguration
<a name="API_FirehoseDestinationConfiguration"></a>

Specifies a Kinesis Firehose location where chat logs will be stored.

## Contents
<a name="API_FirehoseDestinationConfiguration_Contents"></a>

 ** deliveryStreamName **   <a name="ivs-Type-FirehoseDestinationConfiguration-deliveryStreamName"></a>
Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## See Also
<a name="API_FirehoseDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/FirehoseDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/FirehoseDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/FirehoseDestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
