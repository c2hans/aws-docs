---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SrtCallerRouterInputConfiguration.html
---

# SrtCallerRouterInputConfiguration
<a name="API_SrtCallerRouterInputConfiguration"></a>

The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.

## Contents
<a name="API_SrtCallerRouterInputConfiguration_Contents"></a>

 ** minimumLatencyMilliseconds **   <a name="mediaconnect-Type-SrtCallerRouterInputConfiguration-minimumLatencyMilliseconds"></a>
The minimum latency in milliseconds for the SRT protocol in caller mode.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

 ** sourceAddress **   <a name="mediaconnect-Type-SrtCallerRouterInputConfiguration-sourceAddress"></a>
The source IP address for the SRT protocol in caller mode.
Type: String
Required: Yes

 ** sourcePort **   <a name="mediaconnect-Type-SrtCallerRouterInputConfiguration-sourcePort"></a>
The source port number for the SRT protocol in caller mode.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: Yes

 ** decryptionConfiguration **   <a name="mediaconnect-Type-SrtCallerRouterInputConfiguration-decryptionConfiguration"></a>
Specifies the decryption settings for an SRT caller input, including the encryption key configuration and associated parameters.
Type: [SrtDecryptionConfiguration](API_SrtDecryptionConfiguration.md) object
Required: No

 ** streamId **   <a name="mediaconnect-Type-SrtCallerRouterInputConfiguration-streamId"></a>
The stream ID for the SRT protocol in caller mode.
Type: String
Required: No

## See Also
<a name="API_SrtCallerRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SrtCallerRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SrtCallerRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SrtCallerRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
