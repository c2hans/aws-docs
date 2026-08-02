---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ParameterStringFilter.html
---

# ParameterStringFilter
<a name="API_ParameterStringFilter"></a>

One or more filters. Use a filter to return a more specific list of results.

## Contents
<a name="API_ParameterStringFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-ParameterStringFilter-Key"></a>
The name of the filter.
The `ParameterStringFilter` object is used by the [DescribeParameters](API_DescribeParameters.md) and [GetParametersByPath](API_GetParametersByPath.md) API operations. However, not all of the pattern values listed for `Key` can be used with both operations.
For `DescribeParameters`, all of the listed patterns are valid except `Label`.
For `GetParametersByPath`, the following patterns listed for `Key` aren't valid: `tag`, `DataType`, `Name`, `Path`, and `Tier`.
For examples of AWS CLI commands demonstrating valid parameter filter constructions, see [Searching for Systems Manager parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html) in the * AWS Systems Manager User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 132.
Pattern: `tag:.+|Name|Type|KeyId|Path|Label|Tier|DataType`
Required: Yes

 ** Option **   <a name="systemsmanager-Type-ParameterStringFilter-Option"></a>
For all filters used with [DescribeParameters](API_DescribeParameters.md), valid options include `Equals` and `BeginsWith`. The `Name` filter additionally supports the `Contains` option. (Exception: For filters using the key `Path`, valid options include `Recursive` and `OneLevel`.)
For filters used with [GetParametersByPath](API_GetParametersByPath.md), valid options include `Equals` and `BeginsWith`. (Exception: For filters using `Label` as the Key name, the only valid option is `Equals`.)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** Values **   <a name="systemsmanager-Type-ParameterStringFilter-Values"></a>
The value you want to search for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_ParameterStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ParameterStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ParameterStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ParameterStringFilter)
