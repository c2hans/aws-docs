---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayMulticastDomainOptions.html
---

# TransitGatewayMulticastDomainOptions
<a name="API_TransitGatewayMulticastDomainOptions"></a>

Describes the options for a transit gateway multicast domain.

## Contents
<a name="API_TransitGatewayMulticastDomainOptions_Contents"></a>

 ** autoAcceptSharedAssociations **
Indicates whether to automatically cross-account subnet associations that are associated with the transit gateway multicast domain.
Type: String
Valid Values: `enable | disable`
Required: No

 ** igmpv2Support **
Indicates whether Internet Group Management Protocol (IGMP) version 2 is turned on for the transit gateway multicast domain.
Type: String
Valid Values: `enable | disable`
Required: No

 ** staticSourcesSupport **
Indicates whether support for statically configuring transit gateway multicast group sources is turned on.
Type: String
Valid Values: `enable | disable`
Required: No

## See Also
<a name="API_TransitGatewayMulticastDomainOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayMulticastDomainOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayMulticastDomainOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayMulticastDomainOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
