---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_EthernetPayload.html
---

# EthernetPayload
<a name="API_EthernetPayload"></a>

A device's network configuration.

## Contents
<a name="API_EthernetPayload_Contents"></a>

 ** ConnectionType **   <a name="panorama-Type-EthernetPayload-ConnectionType"></a>
How the device gets an IP address.
Type: String
Valid Values: `STATIC_IP | DHCP`
Required: Yes

 ** StaticIpConnectionInfo **   <a name="panorama-Type-EthernetPayload-StaticIpConnectionInfo"></a>
Network configuration for a static IP connection.
Type: [StaticIpConnectionInfo](API_StaticIpConnectionInfo.md) object
Required: No

## See Also
<a name="API_EthernetPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/EthernetPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/EthernetPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/EthernetPayload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
