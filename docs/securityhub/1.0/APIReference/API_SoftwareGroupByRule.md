---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwareGroupByRule.html
---

# SoftwareGroupByRule
<a name="API_SoftwareGroupByRule"></a>

Defines the configuration for organizing and categorizing software packages installed on your resources.

## Contents
<a name="API_SoftwareGroupByRule_Contents"></a>

 ** GroupByField **   <a name="securityhub-Type-SoftwareGroupByRule-GroupByField"></a>
Specifies the attribute that software statistics should be grouped by.
Type: String
Valid Values: `AccountId | PackageName | PackageVersion | PackageType | Region | ResourceRegion | ResourceType | ResourceId | ResourceProvider | ResourceOwnerAccountId | ResourceOwnerOrgId | ResourceCloudPartition`
Required: Yes

 ** Filters **   <a name="securityhub-Type-SoftwareGroupByRule-Filters"></a>
The criteria used to select the software packages included in the statistics. You can nest composite filters up to three levels deep.
Type: [SoftwareFilters](API_SoftwareFilters.md) object
Required: No

## See Also
<a name="API_SoftwareGroupByRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwareGroupByRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwareGroupByRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwareGroupByRule)
