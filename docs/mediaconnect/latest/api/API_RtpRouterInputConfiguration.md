---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RtpRouterInputConfiguration.html
---

# RtpRouterInputConfiguration
<a name="API_RtpRouterInputConfiguration"></a>

The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

## Contents
<a name="API_RtpRouterInputConfiguration_Contents"></a>

 ** port **   <a name="mediaconnect-Type-RtpRouterInputConfiguration-port"></a>
The port number used for the RTP protocol in the router input configuration.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** forwardErrorCorrection **   <a name="mediaconnect-Type-RtpRouterInputConfiguration-forwardErrorCorrection"></a>
The state of forward error correction for the RTP protocol in the router input configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_RtpRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RtpRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RtpRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RtpRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
