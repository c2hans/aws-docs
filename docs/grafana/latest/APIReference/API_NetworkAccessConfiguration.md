---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_NetworkAccessConfiguration.html
---

# NetworkAccessConfiguration
<a name="API_NetworkAccessConfiguration"></a>

The configuration settings for in-bound network access to your workspace.

When this is configured, only listed IP addresses and VPC endpoints will be able to access your workspace. Standard Grafana authentication and authorization are still required.

Access is granted to a caller that is in either the IP address list or the VPC endpoint list - they do not need to be in both.

If this is not configured, or is removed, then all IP addresses and VPC endpoints are allowed. Standard Grafana authentication and authorization are still required.

**Note**
While both `prefixListIds` and `vpceIds` are required, you can pass in an empty array of strings for either parameter if you do not want to allow any of that type.
If both are passed as empty arrays, no traffic is allowed to the workspace, because only *explicitly* allowed connections are accepted.

## Contents
<a name="API_NetworkAccessConfiguration_Contents"></a>

 ** prefixListIds **   <a name="ManagedGrafana-Type-NetworkAccessConfiguration-prefixListIds"></a>
An array of prefix list IDs. A prefix list is a list of CIDR ranges of IP addresses. The IP addresses specified are allowed to access your workspace. If the list is not included in the configuration (passed an empty array) then no IP addresses are allowed to access the workspace. You create a prefix list using the Amazon VPC console.
Prefix list IDs have the format `pl-1a2b3c4d `.
For more information about prefix lists, see [Group CIDR blocks using managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the *Amazon Virtual Private Cloud User Guide*.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** vpceIds **   <a name="ManagedGrafana-Type-NetworkAccessConfiguration-vpceIds"></a>
An array of Amazon VPC endpoint IDs for the workspace. You can create VPC endpoints to your Amazon Managed Grafana workspace for access from within a VPC. If a `NetworkAccessConfiguration` is specified then only VPC endpoints specified here are allowed to access the workspace. If you pass in an empty array of strings, then no VPCs are allowed to access the workspace.
VPC endpoint IDs have the format `vpce-1a2b3c4d `.
For more information about creating an interface VPC endpoint, see [Interface VPC endpoints](https://docs.aws.amazon.com/grafana/latest/userguide/VPC-endpoints) in the *Amazon Managed Grafana User Guide*.
The only VPC endpoints that can be specified here are interface VPC endpoints for Grafana workspaces (using the `com.amazonaws.[region].grafana-workspace` service endpoint). Other VPC endpoints are ignored.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_NetworkAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/NetworkAccessConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/NetworkAccessConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/NetworkAccessConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
