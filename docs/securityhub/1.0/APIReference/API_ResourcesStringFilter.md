---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourcesStringFilter.html
---

# ResourcesStringFilter
<a name="API_ResourcesStringFilter"></a>

Enables filtering of AWS resources based on string field values.

## Contents
<a name="API_ResourcesStringFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-ResourcesStringFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `ResourceGuid | ResourceId | AccountId | AccountName | Region | ResourceProvider | ResourceOwnerAccountId | ResourceOwnerOrgId | ResourceCloudPartition | ResourceRegion | ResourceCategory | ResourceType | ResourceName | FindingsSummary.FindingType | FindingsSummary.ProductName | ResourceSubCategory | DiscoveryType | ResourceInfo.AIDetails.HostResourceGuid | ResourceInfo.AIDetails.HostResourceType | ResourceInfo.AIDetails.CanonicalId`
Required: No

 ** Filter **   <a name="securityhub-Type-ResourcesStringFilter-Filter"></a>
A string filter for filtering AWS Security Hub CSPM findings.
Type: [StringFilter](API_StringFilter.md) object
Required: No

## See Also
<a name="API_ResourcesStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourcesStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourcesStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourcesStringFilter)
