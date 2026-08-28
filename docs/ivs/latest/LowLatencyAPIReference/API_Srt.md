---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_Srt.html
---

# Srt
<a name="API_Srt"></a>

Specifies information needed to stream using the SRT protocol.

## Contents
<a name="API_Srt_Contents"></a>

 ** endpoint **   <a name="ivs-Type-Srt-endpoint"></a>
The endpoint to be used when streaming with IVS using the SRT protocol.
Type: String
Required: No

 ** passphrase **   <a name="ivs-Type-Srt-passphrase"></a>
Auto-generated passphrase to enable encryption. This field is applicable only if the end user has *not* enabled the `insecureIngest` option for the channel.
Type: String
Required: No

## See Also
<a name="API_Srt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/Srt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/Srt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/Srt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
