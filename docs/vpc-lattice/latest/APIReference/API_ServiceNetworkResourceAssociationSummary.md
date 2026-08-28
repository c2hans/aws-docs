---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ServiceNetworkResourceAssociationSummary.html
---

# ServiceNetworkResourceAssociationSummary
<a name="API_ServiceNetworkResourceAssociationSummary"></a>

Summary information about an association between a service network and a resource configuration.

## Contents
<a name="API_ServiceNetworkResourceAssociationSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-arn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 22. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetworkresourceassociation/snra-[0-9a-f]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-createdAt"></a>
The date and time that the association was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** createdBy **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** dnsEntry **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-dnsEntry"></a>
The DNS entry for the service.
Type: [DnsEntry](API_DnsEntry.md) object
Required: No

 ** failureCode **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-failureCode"></a>
The failure code.
Type: String
Required: No

 ** id **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-id"></a>
The ID of the association between the service network and resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `snra-[0-9a-f]{17}`
Required: No

 ** isManagedAssociation **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-isManagedAssociation"></a>
Specifies whether the association is managed by Amazon.
Type: Boolean
Required: No

 ** privateDnsEnabled **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-privateDnsEnabled"></a>
 Indicates if private DNS is enabled for the service network resource association.
Type: Boolean
Required: No

 ** privateDnsEntry **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-privateDnsEntry"></a>
The private DNS entry for the service.
Type: [DnsEntry](API_DnsEntry.md) object
Required: No

 ** resourceConfigurationArn **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-resourceConfigurationArn"></a>
The Amazon Resource Name (ARN) of the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`
Required: No

 ** resourceConfigurationId **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-resourceConfigurationId"></a>
The ID of the resource configuration associated with the service network.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`
Required: No

 ** resourceConfigurationName **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-resourceConfigurationName"></a>
The name of the resource configuration associated with the service network.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** serviceNetworkArn **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-serviceNetworkArn"></a>
The Amazon Resource Name (ARN) of the service network associated with the resource configuration.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 2048.
Required: No

 ** serviceNetworkId **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-serviceNetworkId"></a>
The ID of the service network associated with the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Required: No

 ** serviceNetworkName **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-serviceNetworkName"></a>
The name of the service network associated with the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: No

 ** status **   <a name="vpclattice-Type-ServiceNetworkResourceAssociationSummary-status"></a>
The status of the service network’s association with the resource configuration. If the deletion fails, try to delete again.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | PARTIAL | DELETE_IN_PROGRESS | CREATE_FAILED | DELETE_FAILED`
Required: No

## See Also
<a name="API_ServiceNetworkResourceAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ServiceNetworkResourceAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ServiceNetworkResourceAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ServiceNetworkResourceAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
