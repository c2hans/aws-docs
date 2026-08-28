---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SrtListenerRouterInputConfiguration.html
---

# SrtListenerRouterInputConfiguration
<a name="API_SrtListenerRouterInputConfiguration"></a>

The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

## Contents
<a name="API_SrtListenerRouterInputConfiguration_Contents"></a>

 ** minimumLatencyMilliseconds **   <a name="mediaconnect-Type-SrtListenerRouterInputConfiguration-minimumLatencyMilliseconds"></a>
The minimum latency in milliseconds for the SRT protocol in listener mode.
Type: Long
Valid Range: Minimum value of 10. Maximum value of 10000.
Required: Yes

 ** port **   <a name="mediaconnect-Type-SrtListenerRouterInputConfiguration-port"></a>
The port number for the SRT protocol in listener mode.
Type: Integer
Valid Range: Minimum value of 3000. Maximum value of 30000.
Required: Yes

 ** decryptionConfiguration **   <a name="mediaconnect-Type-SrtListenerRouterInputConfiguration-decryptionConfiguration"></a>
Specifies the decryption settings for an SRT listener input, including the encryption key configuration and associated parameters.
Type: [SrtDecryptionConfiguration](API_SrtDecryptionConfiguration.md) object
Required: No

## See Also
<a name="API_SrtListenerRouterInputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SrtListenerRouterInputConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SrtListenerRouterInputConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SrtListenerRouterInputConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
