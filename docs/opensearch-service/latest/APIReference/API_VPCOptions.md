---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VPCOptions.html
---

# VPCOptions
<a name="API_VPCOptions"></a>

Options to specify the subnets and security groups for an Amazon OpenSearch Service VPC endpoint. For more information, see [Launching your Amazon OpenSearch Service domains using a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html).

## Contents
<a name="API_VPCOptions_Contents"></a>

 ** EgressEnabled **   <a name="opensearchservice-Type-VPCOptions-EgressEnabled"></a>
Controls whether egress traffic from the domain is routed through the customer VPC. When `true`, outbound traffic flows through the VPC. When `false`, outbound traffic goes through the public internet.
Type: Boolean
Required: No

 ** SecurityGroupIds **   <a name="opensearchservice-Type-VPCOptions-SecurityGroupIds"></a>
The list of security group IDs associated with the VPC endpoints for the domain. If you do not provide a security group ID, OpenSearch Service uses the default security group for the VPC.
Type: Array of strings
Required: No

 ** SubnetIds **   <a name="opensearchservice-Type-VPCOptions-SubnetIds"></a>
A list of subnet IDs associated with the VPC endpoints for the domain. If your domain uses multiple Availability Zones, you need to provide two subnet IDs, one per zone. Otherwise, provide only one.
Type: Array of strings
Required: No

## See Also
<a name="API_VPCOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/VPCOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/VPCOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/VPCOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
