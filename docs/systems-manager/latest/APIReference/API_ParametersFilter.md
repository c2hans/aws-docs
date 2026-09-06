---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ParametersFilter.html
---

# ParametersFilter
<a name="API_ParametersFilter"></a>

This data type is deprecated. Instead, use [ParameterStringFilter](API_ParameterStringFilter.md).

## Contents
<a name="API_ParametersFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-ParametersFilter-Key"></a>
The name of the filter.
Type: String
Valid Values: `Name | Type | KeyId`
Required: Yes

 ** Values **   <a name="systemsmanager-Type-ParametersFilter-Values"></a>
The filter values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_ParametersFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ParametersFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ParametersFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ParametersFilter)
