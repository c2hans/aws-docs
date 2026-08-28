---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtpRouterOutputConfiguration.html
---

# RtpRouterOutputConfiguration
<a name="API_RtpRouterOutputConfiguration"></a>

The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.

## Contents
<a name="API_RtpRouterOutputConfiguration_Contents"></a>

 ** destinationAddress **   <a name="mediaconnect-Type-RtpRouterOutputConfiguration-destinationAddress"></a>
The destination IP address for the RTP protocol in the router output configuration.
Type: String
Required: Yes

 ** destinationPort **   <a name="mediaconnect-Type-RtpRouterOutputConfiguration-destinationPort"></a>
The destination port number for the RTP protocol in the router output configuration.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65531.
Required: Yes

 ** forwardErrorCorrection **   <a name="mediaconnect-Type-RtpRouterOutputConfiguration-forwardErrorCorrection"></a>
The state of forward error correction for the RTP protocol in the router output configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_RtpRouterOutputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtpRouterOutputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtpRouterOutputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtpRouterOutputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
