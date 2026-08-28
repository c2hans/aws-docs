---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_TlsInterceptPropertiesRequest.html
---

# TlsInterceptPropertiesRequest
<a name="API_TlsInterceptPropertiesRequest"></a>

This data type is used specifically for the [CreateProxy](API_CreateProxy.md) and [UpdateProxy](API_UpdateProxy.md) APIs.

TLS decryption on traffic to filter on attributes in the HTTP header.

## Contents
<a name="API_TlsInterceptPropertiesRequest_Contents"></a>

 ** PcaArn **   <a name="networkfirewall-Type-TlsInterceptPropertiesRequest-PcaArn"></a>
Private Certificate Authority (PCA) used to issue private TLS certificates so that the proxy can present PCA-signed certificates which applications trust through the same root, establishing a secure and consistent trust model for encrypted communication.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** TlsInterceptMode **   <a name="networkfirewall-Type-TlsInterceptPropertiesRequest-TlsInterceptMode"></a>
Specifies whether to enable or disable TLS Intercept Mode.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_TlsInterceptPropertiesRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/TlsInterceptPropertiesRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/TlsInterceptPropertiesRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/TlsInterceptPropertiesRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
