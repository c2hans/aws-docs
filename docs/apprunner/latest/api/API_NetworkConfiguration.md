---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

Describes configuration settings related to network traffic of an AWS App Runner service. Consists of embedded objects for each configurable network feature.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** EgressConfiguration **   <a name="apprunner-Type-NetworkConfiguration-EgressConfiguration"></a>
Network configuration settings for outbound message traffic.
Type: [EgressConfiguration](API_EgressConfiguration.md) object
Required: No

 ** IngressConfiguration **   <a name="apprunner-Type-NetworkConfiguration-IngressConfiguration"></a>
Network configuration settings for inbound message traffic.
Type: [IngressConfiguration](API_IngressConfiguration.md) object
Required: No

 ** IpAddressType **   <a name="apprunner-Type-NetworkConfiguration-IpAddressType"></a>
App Runner provides you with the option to choose between *IPv4* and *dual stack* (IPv4 and IPv6). This is an optional parameter. If you do not specify an `IpAddressType`, it defaults to select IPv4.
Type: String
Valid Values: `IPV4 | DUAL_STACK`
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/NetworkConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Runner. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apprunner` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
