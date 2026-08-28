---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ServiceNetworkVpcAssociationSummary.html
---

# ServiceNetworkVpcAssociationSummary
<a name="API_ServiceNetworkVpcAssociationSummary"></a>

Summary information about an association between a service network and a VPC.

## Contents
<a name="API_ServiceNetworkVpcAssociationSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkvpcassociation/snva-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** createdBy **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** dnsOptions **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-dnsOptions"></a>
 The DNS options for the service network VPC association.
Type: [DnsOptions](API_DnsOptions.md) object
Required: No

 ** id **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-id"></a>
The ID of the association.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `snva-[0-9a-z]{17}`
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-lastUpdatedAt"></a>
The date and time that the association was last updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** privateDnsEnabled **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-privateDnsEnabled"></a>
 Indicates if private DNS is enabled for the service network VPC association.
Type: Boolean
Required: No

 ** serviceNetworkArn **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`
Required: No

 ** serviceNetworkId **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-serviceNetworkId"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`
Required: No

 ** serviceNetworkName **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-serviceNetworkName"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** status **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-status"></a>
The status.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED | UPDATE_FAILED`
Required: No

 ** vpcId **   <a name="vpclattice-Type-ServiceNetworkVpcAssociationSummary-vpcId"></a>
The ID of the VPC.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_ServiceNetworkVpcAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ServiceNetworkVpcAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ServiceNetworkVpcAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ServiceNetworkVpcAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
