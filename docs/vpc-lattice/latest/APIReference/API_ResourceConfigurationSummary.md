---
source_url: https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_ResourceConfigurationSummary.html
---

# ResourceConfigurationSummary
<a name="API_ResourceConfigurationSummary"></a>

Summary information about a resource configuration.

## Contents
<a name="API_ResourceConfigurationSummary_Contents"></a>

 ** amazonManaged **   <a name="vpclattice-Type-ResourceConfigurationSummary-amazonManaged"></a>
Indicates whether the resource configuration was created and is managed by Amazon.
Type: Boolean
Required: No

 ** arn **   <a name="vpclattice-Type-ResourceConfigurationSummary-arn"></a>
The Amazon Resource Name (ARN) of the resource configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[a-z0-9f\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}`
Required: No

 ** createdAt **   <a name="vpclattice-Type-ResourceConfigurationSummary-createdAt"></a>
The date and time that the resource configuration was created, in ISO-8601 format.
Type: Timestamp
Required: No

 ** customDomainName **   <a name="vpclattice-Type-ResourceConfigurationSummary-customDomainName"></a>
 The custom domain name.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** domainVerificationId **   <a name="vpclattice-Type-ResourceConfigurationSummary-domainVerificationId"></a>
 The domain verification ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `dv-[a-fA-F0-9]{17}`
Required: No

 ** groupDomain **   <a name="vpclattice-Type-ResourceConfigurationSummary-groupDomain"></a>
 (GROUP) The group domain for a group resource configuration. Any domains that you create for the child resource are subdomains of the group domain. Child resources inherit the verification status of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Required: No

 ** id **   <a name="vpclattice-Type-ResourceConfigurationSummary-id"></a>
The ID of the resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`
Required: No

 ** lastUpdatedAt **   <a name="vpclattice-Type-ResourceConfigurationSummary-lastUpdatedAt"></a>
The most recent date and time that the resource configuration was updated, in ISO-8601 format.
Type: Timestamp
Required: No

 ** name **   <a name="vpclattice-Type-ResourceConfigurationSummary-name"></a>
The name of the resource configuration.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `(?!rcfg-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+`
Required: No

 ** resourceConfigurationGroupId **   <a name="vpclattice-Type-ResourceConfigurationSummary-resourceConfigurationGroupId"></a>
The ID of the group resource configuration.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `rcfg-[0-9a-z]{17}`
Required: No

 ** resourceGatewayId **   <a name="vpclattice-Type-ResourceConfigurationSummary-resourceGatewayId"></a>
The ID of the resource gateway.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rgw-[0-9a-z]{17}`
Required: No

 ** status **   <a name="vpclattice-Type-ResourceConfigurationSummary-status"></a>
The status of the resource configuration.
Type: String
Valid Values: `ACTIVE | CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED`
Required: No

 ** type **   <a name="vpclattice-Type-ResourceConfigurationSummary-type"></a>
The type of resource configuration.
+  `SINGLE` - A single resource.
+  `GROUP` - A group of resources. You must create a group resource configuration before you create a child resource configuration.
+  `CHILD` - A single resource that is part of a group resource configuration.
+  `ARN` - An AWS resource.
Type: String
Valid Values: `GROUP | CHILD | SINGLE | ARN`
Required: No

## See Also
<a name="API_ResourceConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/vpc-lattice-2022-11-30/ResourceConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/vpc-lattice-2022-11-30/ResourceConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/vpc-lattice-2022-11-30/ResourceConfigurationSummary)
