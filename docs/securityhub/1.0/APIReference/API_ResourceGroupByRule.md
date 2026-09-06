---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourceGroupByRule.html
---

# ResourceGroupByRule
<a name="API_ResourceGroupByRule"></a>

Defines the configuration for organizing and categorizing AWS resources based on associated security findings.

## Contents
<a name="API_ResourceGroupByRule_Contents"></a>

 ** GroupByField **   <a name="securityhub-Type-ResourceGroupByRule-GroupByField"></a>
Specifies the attribute that resources should be grouped by.
Type: String
Valid Values: `AccountId | AccountName | Region | ResourceProvider | ResourceOwnerAccountId | ResourceOwnerOrgId | ResourceCloudPartition | ResourceRegion | ResourceCategory | ResourceType | ResourceName | FindingsSummary.FindingType | ResourceSubCategory | DiscoveryType | ResourceInfo.AIDetails.HostResourceType | ResourceInfo.AIDetails.CanonicalId`
Required: Yes

 ** Filters **   <a name="securityhub-Type-ResourceGroupByRule-Filters"></a>
The criteria used to select resources and associated security findings.
Type: [ResourcesFilters](API_ResourcesFilters.md) object
Required: No

## See Also
<a name="API_ResourceGroupByRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourceGroupByRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourceGroupByRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourceGroupByRule)
