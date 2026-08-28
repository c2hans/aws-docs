---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ServiceNetworkEndpointAssociation.html
---

# ServiceNetworkEndpointAssociation
<a name="API_ServiceNetworkEndpointAssociation"></a>

Describes the association between a service network and a VPC endpoint.

## Contents
<a name="API_ServiceNetworkEndpointAssociation_Contents"></a>

 ** createdAt **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** id **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-id"></a>
The ID of the association.
Type: String
Required: No

 ** serviceNetworkArn **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`
Required: No

 ** state **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-state"></a>
The state of the association.
Type: String
Required: No

 ** vpcEndpointId **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-vpcEndpointId"></a>
The ID of the VPC endpoint associated with the service network.
Type: String
Required: No

 ** vpcEndpointOwnerId **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-vpcEndpointOwnerId"></a>
The owner of the VPC endpoint associated with the service network.
Type: String
Required: No

 ** vpcId **   <a name="vpclattice-Type-ServiceNetworkEndpointAssociation-vpcId"></a>
The ID of the VPC for the association.
Type: String
Required: No

## See Also
<a name="API_ServiceNetworkEndpointAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ServiceNetworkEndpointAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ServiceNetworkEndpointAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ServiceNetworkEndpointAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
