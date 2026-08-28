---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_MergeRouterInputProtocolConfiguration.html
---

# MergeRouterInputProtocolConfiguration
<a name="API_MergeRouterInputProtocolConfiguration"></a>

Protocol configuration settings for merge router inputs.

## Contents
<a name="API_MergeRouterInputProtocolConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rist **   <a name="mediaconnect-Type-MergeRouterInputProtocolConfiguration-rist"></a>
The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
Type: [RistRouterInputConfiguration](API_RistRouterInputConfiguration.md) object
Required: No

 ** rtp **   <a name="mediaconnect-Type-MergeRouterInputProtocolConfiguration-rtp"></a>
The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
Type: [RtpRouterInputConfiguration](API_RtpRouterInputConfiguration.md) object
Required: No

## See Also
<a name="API_MergeRouterInputProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/MergeRouterInputProtocolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/MergeRouterInputProtocolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/MergeRouterInputProtocolConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
