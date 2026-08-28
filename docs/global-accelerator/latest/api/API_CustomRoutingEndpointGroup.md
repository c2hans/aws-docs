---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingEndpointGroup.html
---

# CustomRoutingEndpointGroup
<a name="API_CustomRoutingEndpointGroup"></a>

A complex type for the endpoint group for a custom routing accelerator. An AWS Region can have only one endpoint group for a specific listener.

## Contents
<a name="API_CustomRoutingEndpointGroup_Contents"></a>

 ** DestinationDescriptions **   <a name="globalaccelerator-Type-CustomRoutingEndpointGroup-DestinationDescriptions"></a>
For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.
Type: Array of [CustomRoutingDestinationDescription](API_CustomRoutingDestinationDescription.md) objects
Required: No

 ** EndpointDescriptions **   <a name="globalaccelerator-Type-CustomRoutingEndpointGroup-EndpointDescriptions"></a>
For a custom routing accelerator, describes the endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.
Type: Array of [CustomRoutingEndpointDescription](API_CustomRoutingEndpointDescription.md) objects
Required: No

 ** EndpointGroupArn **   <a name="globalaccelerator-Type-CustomRoutingEndpointGroup-EndpointGroupArn"></a>
The Amazon Resource Name (ARN) of the endpoint group.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** EndpointGroupRegion **   <a name="globalaccelerator-Type-CustomRoutingEndpointGroup-EndpointGroupRegion"></a>
The AWS Region where the endpoint group is located.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_CustomRoutingEndpointGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingEndpointGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingEndpointGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingEndpointGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
