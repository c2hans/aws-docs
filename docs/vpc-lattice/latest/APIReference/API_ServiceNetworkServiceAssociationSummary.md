---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ServiceNetworkServiceAssociationSummary.html
---

# ServiceNetworkServiceAssociationSummary
<a name="API_ServiceNetworkServiceAssociationSummary"></a>

Summary information about an association between a service network and a service.

## Contents
<a name="API_ServiceNetworkServiceAssociationSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** createdBy **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** customDomainName **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-customDomainName"></a>
The custom domain name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** dnsEntry **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-dnsEntry"></a>
The DNS information.
Type: [DnsEntry](API_DnsEntry.md) object
Required: No

 ** id **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-id"></a>
The ID of the association.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 2048.
Pattern: `((snsa-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkserviceassociation/snsa-[0-9a-z]{17}))`
Required: No

 ** serviceArn **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-serviceArn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:service/svc-[0-9a-z]{17}`
Required: No

 ** serviceId **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-serviceId"></a>
The ID of the service.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `svc-[0-9a-z]{17}`
Required: No

 ** serviceName **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-serviceName"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!svc-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** serviceNetworkArn **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}`
Required: No

 ** serviceNetworkId **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-serviceNetworkId"></a>
The ID of the service network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-z]{17}`
Required: No

 ** serviceNetworkName **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-serviceNetworkName"></a>
The name of the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** status **   <a name="vpclattice-Type-ServiceNetworkServiceAssociationSummary-status"></a>
The status of the service network’s association with the service. If the deletion fails, try to delete again.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`
Required: No

## See Also
<a name="API_ServiceNetworkServiceAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ServiceNetworkServiceAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ServiceNetworkServiceAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ServiceNetworkServiceAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
