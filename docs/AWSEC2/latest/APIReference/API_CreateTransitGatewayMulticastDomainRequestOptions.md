---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayMulticastDomainRequestOptions.html
---

# CreateTransitGatewayMulticastDomainRequestOptions
<a name="API_CreateTransitGatewayMulticastDomainRequestOptions"></a>

The options for the transit gateway multicast domain.

## Contents
<a name="API_CreateTransitGatewayMulticastDomainRequestOptions_Contents"></a>

 ** AutoAcceptSharedAssociations **
Indicates whether to automatically accept cross-account subnet associations that are associated with the transit gateway multicast domain.
Type: String
Valid Values: `enable | disable`
Required: No

 ** Igmpv2Support **
Specify whether to enable Internet Group Management Protocol (IGMP) version 2 for the transit gateway multicast domain.
Type: String
Valid Values: `enable | disable`
Required: No

 ** StaticSourcesSupport **
Specify whether to enable support for statically configuring multicast group sources for a domain.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_CreateTransitGatewayMulticastDomainRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayMulticastDomainRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayMulticastDomainRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayMulticastDomainRequestOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
