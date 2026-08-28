---
source_url: https://docs.aws.amazon.com/global-accelerator/latest/api/API_CustomRoutingDestinationDescription.html
---

# CustomRoutingDestinationDescription
<a name="API_CustomRoutingDestinationDescription"></a>

For a custom routing accelerator, describes the port range and protocol for all endpoints (virtual private cloud subnets) in an endpoint group to accept client traffic on.

## Contents
<a name="API_CustomRoutingDestinationDescription_Contents"></a>

 ** FromPort **   <a name="globalaccelerator-Type-CustomRoutingDestinationDescription-FromPort"></a>
The first port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocols **   <a name="globalaccelerator-Type-CustomRoutingDestinationDescription-Protocols"></a>
The protocol for the endpoint group that is associated with a custom routing accelerator. The protocol can be either TCP or UDP.
Type: Array of strings
Valid Values: `TCP | UDP`
Required: No

 ** ToPort **   <a name="globalaccelerator-Type-CustomRoutingDestinationDescription-ToPort"></a>
The last port, inclusive, in the range of ports for the endpoint group that is associated with a custom routing accelerator.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_CustomRoutingDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CustomRoutingDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CustomRoutingDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CustomRoutingDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Accelerator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query global-accelerator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
