---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ManagedResourceDetails.html
---

# ManagedResourceDetails
<a name="API_ManagedResourceDetails"></a>

Details of a resource created and managed by the gateway for private endpoint connectivity.

## Contents
<a name="API_ManagedResourceDetails_Contents"></a>

 ** domain **   <a name="bedrockagentcorecontrol-Type-ManagedResourceDetails-domain"></a>
The domain associated with this managed resource.
Type: String
Required: No

 ** resourceAssociationArn **   <a name="bedrockagentcorecontrol-Type-ManagedResourceDetails-resourceAssociationArn"></a>
The ARN of the service network resource association.
Type: String
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}`
Required: No

 ** resourceGatewayArn **   <a name="bedrockagentcorecontrol-Type-ManagedResourceDetails-resourceGatewayArn"></a>
The ARN of the VPC Lattice resource gateway created in your account.
Type: String
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`
Required: No

## See Also
<a name="API_ManagedResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ManagedResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ManagedResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ManagedResourceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
