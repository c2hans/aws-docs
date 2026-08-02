---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribePackagesFilter.html
---

# DescribePackagesFilter
<a name="API_DescribePackagesFilter"></a>

A filter to apply to the `DescribePackage` response.

## Contents
<a name="API_DescribePackagesFilter_Contents"></a>

 ** Name **   <a name="opensearchservice-Type-DescribePackagesFilter-Name"></a>
Any field from `PackageDetails`.
Type: String
Valid Values: `PackageID | PackageName | PackageStatus | PackageType | EngineVersion | PackageOwner`
Required: No

 ** Value **   <a name="opensearchservice-Type-DescribePackagesFilter-Value"></a>
A non-empty list of values for the specified filter field.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `^[0-9a-zA-Z\*\.\_\\\/\?-]+$`
Required: No

## See Also
<a name="API_DescribePackagesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribePackagesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribePackagesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribePackagesFilter)
