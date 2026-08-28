---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PeeringConnectionOptions.html
---

# PeeringConnectionOptions
<a name="API_PeeringConnectionOptions"></a>

Describes the VPC peering connection options.

## Contents
<a name="API_PeeringConnectionOptions_Contents"></a>

 ** allowDnsResolutionFromRemoteVpc **
If true, the public DNS hostnames of instances in the specified VPC resolve to private IP addresses when queried from instances in the peer VPC.
Type: Boolean
Required: No

 ** allowEgressFromLocalClassicLinkToRemoteVpc **
Deprecated.
Type: Boolean
Required: No

 ** allowEgressFromLocalVpcToRemoteClassicLink **
Deprecated.
Type: Boolean
Required: No

## See Also
<a name="API_PeeringConnectionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PeeringConnectionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PeeringConnectionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PeeringConnectionOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
