---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingEndpointConfiguration.html
---

# CustomRoutingEndpointConfiguration
<a name="API_CustomRoutingEndpointConfiguration"></a>

The list of endpoint objects. For custom routing, this is a list of virtual private cloud (VPC) subnet IDs.

## Contents
<a name="API_CustomRoutingEndpointConfiguration_Contents"></a>

 ** AttachmentArn **   <a name="globalaccelerator-Type-CustomRoutingEndpointConfiguration-AttachmentArn"></a>
The Amazon Resource Name (ARN) of the cross-account attachment that specifies the endpoints (resources) that can be added to accelerators and principals that have permission to add the endpoints.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** EndpointId **   <a name="globalaccelerator-Type-CustomRoutingEndpointConfiguration-EndpointId"></a>
An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## See Also
<a name="API_CustomRoutingEndpointConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingEndpointConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingEndpointConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingEndpointConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
