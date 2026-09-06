---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ResourceEndpointAssociationSummary.html
---

# ResourceEndpointAssociationSummary
<a name="API_ResourceEndpointAssociationSummary"></a>

Summary information about a VPC endpoint association.

## Contents
<a name="API_ResourceEndpointAssociationSummary_Contents"></a>

 ** arn **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-arn"></a>
The Amazon Resource Name (ARN) of the VPC endpoint association.
Type: String
Length Constraints: Minimum length of 21. Maximum length of 2048.
Pattern: `arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceendpointassociation/rea-[0-9a-f]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-createdAt"></a>
The date and time that the VPC endpoint association was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** createdBy **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-createdBy"></a>
The account that created the association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** id **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-id"></a>
The ID of the VPC endpoint association.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rea-[0-9a-f]{17}`
Required: No

 ** resourceConfigurationArn **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-resourceConfigurationArn"></a>
The Amazon Resource Name (ARN) of the resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`
Required: No

 ** resourceConfigurationId **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-resourceConfigurationId"></a>
The ID of the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`
Required: No

 ** resourceConfigurationName **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-resourceConfigurationName"></a>
The name of the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** vpcEndpointId **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-vpcEndpointId"></a>
The ID of the VPC endpoint.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `vpce-[0-9a-f]{17}`
Required: No

 ** vpcEndpointOwner **   <a name="vpclattice-Type-ResourceEndpointAssociationSummary-vpcEndpointOwner"></a>
The owner of the VPC endpoint.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_ResourceEndpointAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ResourceEndpointAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ResourceEndpointAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ResourceEndpointAssociationSummary)
