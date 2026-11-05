---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwareStringFilter.html
---

# SoftwareStringFilter
<a name="API_SoftwareStringFilter"></a>

Enables filtering of software packages based on string field values.

## Contents
<a name="API_SoftwareStringFilter_Contents"></a>

 ** FieldName **   <a name="securityhub-Type-SoftwareStringFilter-FieldName"></a>
The name of the field.
Type: String
Valid Values: `AccountId | PackageName | PackageVersion | PackageType | Region | ResourceRegion | ResourceType | ResourceId | ResourceProvider | ResourceOwnerAccountId | ResourceOwnerOrgId | ResourceCloudPartition`
Required: No

 ** Filter **   <a name="securityhub-Type-SoftwareStringFilter-Filter"></a>
The string value and comparison operator to filter on. Supported comparisons are `EQUALS`, `NOT_EQUALS`, `PREFIX`, and `PREFIX_NOT_EQUALS`.
Type: [StringFilter](API_StringFilter.md) object
Required: No

## See Also
<a name="API_SoftwareStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwareStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwareStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwareStringFilter)
