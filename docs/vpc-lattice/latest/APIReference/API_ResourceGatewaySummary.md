---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ResourceGatewaySummary.html
---

# ResourceGatewaySummary
<a name="API_ResourceGatewaySummary"></a>

Summary information about a resource gateway.

## Contents
<a name="API_ResourceGatewaySummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ResourceGatewaySummary-arn"></a>
The Amazon Resource Name (ARN) of the resource gateway.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourcegateway/rgw-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ResourceGatewaySummary-createdAt"></a>
The date and time that the VPC endpoint association was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** id **   <a name="vpclattice-Type-ResourceGatewaySummary-id"></a>
The ID of the resource gateway.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`
Required: No

 ** ipAddressType **   <a name="vpclattice-Type-ResourceGatewaySummary-ipAddressType"></a>
The type of IP address used by the resource gateway.
Type: String
Valid Values: `IPV4 | IPV6 | DUALSTACK`
Required: No

 ** ipv4AddressesPerEni **   <a name="vpclattice-Type-ResourceGatewaySummary-ipv4AddressesPerEni"></a>
The number of IPv4 addresses in each ENI for the resource gateway.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 62.
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-ResourceGatewaySummary-lastUpdatedAt"></a>
The most recent date and time that the resource gateway was updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** name **   <a name="vpclattice-Type-ResourceGatewaySummary-name"></a>
The name of the resource gateway.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rgw-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** resourceConfigDnsResolution **   <a name="vpclattice-Type-ResourceGatewaySummary-resourceConfigDnsResolution"></a>
The DNS resolution type for resource configurations that are associated with this resource gateway.
Type: String
Valid Values: `IN_VPC | PUBLIC`
Required: No

 ** securityGroupIds **   <a name="vpclattice-Type-ResourceGatewaySummary-securityGroupIds"></a>
The IDs of the security groups applied to the resource gateway.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

 ** status **   <a name="vpclattice-Type-ResourceGatewaySummary-status"></a>
The name of the resource gateway.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`
Required: No

 ** subnetIds **   <a name="vpclattice-Type-ResourceGatewaySummary-subnetIds"></a>
The IDs of the VPC subnets for the resource gateway.
Type: Array of strings
Length Constraints: Minimum length of 5. Maximum length of 200.
Required: No

 ** vpcIdentifier **   <a name="vpclattice-Type-ResourceGatewaySummary-vpcIdentifier"></a>
The ID of the VPC for the resource gateway.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 50.
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
Required: No

## See Also
<a name="API_ResourceGatewaySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ResourceGatewaySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ResourceGatewaySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ResourceGatewaySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC Lattice. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc-lattice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
