---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_VPCDerivedInfo.html
---

# VPCDerivedInfo
<a name="API_VPCDerivedInfo"></a>

Information about the subnets and security groups for an Amazon OpenSearch Service domain provisioned within a virtual private cloud (VPC). For more information, see [Launching your Amazon OpenSearch Service domains using a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html). This information only exists if the domain was created with `VPCOptions`.

## Contents
<a name="API_VPCDerivedInfo_Contents"></a>

 ** AvailabilityZones **   <a name="opensearchservice-Type-VPCDerivedInfo-AvailabilityZones"></a>
The list of Availability Zones associated with the VPC subnets.
Type: Array of strings
Required: No

 ** EgressEnabled **   <a name="opensearchservice-Type-VPCDerivedInfo-EgressEnabled"></a>
Indicates whether egress traffic from the domain is routed through the customer VPC. When `true`, outbound traffic flows through the VPC. When `false`, outbound traffic goes through the public internet.
Type: Boolean
Required: No

 ** SecurityGroupIds **   <a name="opensearchservice-Type-VPCDerivedInfo-SecurityGroupIds"></a>
The list of security group IDs associated with the VPC endpoints for the domain.
Type: Array of strings
Required: No

 ** SubnetIds **   <a name="opensearchservice-Type-VPCDerivedInfo-SubnetIds"></a>
A list of subnet IDs associated with the VPC endpoints for the domain.
Type: Array of strings
Required: No

 ** VPCId **   <a name="opensearchservice-Type-VPCDerivedInfo-VPCId"></a>
The ID for your VPC. Amazon VPC generates this value when you create a VPC.
Type: String
Required: No

## See Also
<a name="API_VPCDerivedInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/VPCDerivedInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/VPCDerivedInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/VPCDerivedInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
