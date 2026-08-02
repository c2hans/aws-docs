---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ComplianceStringFilter.html
---

# ComplianceStringFilter
<a name="API_ComplianceStringFilter"></a>

One or more filters. Use a filter to return a more specific list of results.

## Contents
<a name="API_ComplianceStringFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-ComplianceStringFilter-Key"></a>
The name of the filter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** Type **   <a name="systemsmanager-Type-ComplianceStringFilter-Type"></a>
The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.
Type: String
Valid Values: `EQUAL | NOT_EQUAL | BEGIN_WITH | LESS_THAN | GREATER_THAN`
Required: No

 ** Values **   <a name="systemsmanager-Type-ComplianceStringFilter-Values"></a>
The value for which to search.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## See Also
<a name="API_ComplianceStringFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ComplianceStringFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ComplianceStringFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ComplianceStringFilter)
