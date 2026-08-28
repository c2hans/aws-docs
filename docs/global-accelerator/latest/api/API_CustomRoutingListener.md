---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingListener.html
---

# CustomRoutingListener
<a name="API_CustomRoutingListener"></a>

A complex type for a listener for a custom routing accelerator.

## Contents
<a name="API_CustomRoutingListener_Contents"></a>

 ** ListenerArn **   <a name="globalaccelerator-Type-CustomRoutingListener-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** PortRanges **   <a name="globalaccelerator-Type-CustomRoutingListener-PortRanges"></a>
The port range to support for connections from clients to your accelerator.
Separately, you set port ranges for endpoints. For more information, see [About endpoints for custom routing accelerators](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html).
Type: Array of [PortRange](API_PortRange.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_CustomRoutingListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingListener)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
