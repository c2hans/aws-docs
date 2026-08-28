---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_StageEndpoints.html
---

# StageEndpoints
<a name="API_StageEndpoints"></a>

Summary information about various endpoints for a stage. We recommend that you cache these values at stage creation; the values can be cached for up to 14 days.

## Contents
<a name="API_StageEndpoints_Contents"></a>

 ** events **   <a name="ivsrealtimeeapireference-Type-StageEndpoints-events"></a>
Events endpoint.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** rtmp **   <a name="ivsrealtimeeapireference-Type-StageEndpoints-rtmp"></a>
The endpoint to be used for IVS real-time streaming using the RTMP protocol.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** rtmps **   <a name="ivsrealtimeeapireference-Type-StageEndpoints-rtmps"></a>
The endpoint to be used for IVS real-time streaming using the RTMPS protocol.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** whip **   <a name="ivsrealtimeeapireference-Type-StageEndpoints-whip"></a>
The endpoint to be used for IVS real-time streaming using the WHIP protocol.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_StageEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/StageEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/StageEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/StageEndpoints)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon IVS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ivs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
