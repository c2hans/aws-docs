---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html
---

# PatchFilter
<a name="API_PatchFilter"></a>

 Defines which patches should be included in a patch baseline.

A patch filter consists of a key and a set of values. The filter key is a patch property. For example, the available filter keys for `WINDOWS` are `PATCH_SET`, `PRODUCT`, `PRODUCT_FAMILY`, `CLASSIFICATION`, and `MSRC_SEVERITY`.

The filter values define a matching criterion for the patch property indicated by the key. For example, if the filter key is `PRODUCT` and the filter values are `["Office 2013", "Office 2016"]`, then the filter accepts all patches where product name is either "Office 2013" or "Office 2016". The filter values can be exact values for the patch property given as a key, or a wildcard (\*), which matches all values.

You can view lists of valid values for the patch properties by running the `DescribePatchProperties` command. For information about which patch properties can be used with each major operating system, see [DescribePatchProperties](API_DescribePatchProperties.md).

## Contents
<a name="API_PatchFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-PatchFilter-Key"></a>
The key for the filter.
Run the [DescribePatchProperties](API_DescribePatchProperties.md) command to view lists of valid keys for each operating system type.
Type: String
Valid Values: `ARCH | ADVISORY_ID | BUGZILLA_ID | PATCH_SET | PRODUCT | PRODUCT_FAMILY | CLASSIFICATION | CVE_ID | EPOCH | MSRC_SEVERITY | NAME | PATCH_ID | SECTION | PRIORITY | REPOSITORY | RELEASE | SEVERITY | SECURITY | VERSION`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-PatchFilter-Values"></a>
The value for the filter key.
Run the [DescribePatchProperties](API_DescribePatchProperties.md) command to view lists of valid values for each key based on operating system type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_PatchFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/PatchFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/PatchFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/PatchFilter)
