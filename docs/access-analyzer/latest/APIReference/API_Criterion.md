---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Criterion.html
---

# Criterion
<a name="API_Criterion"></a>

The criteria to use in the filter that defines the archive rule. For more information on available filter keys, see [IAM Access Analyzer filter keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-filter-keys.html).

## Contents
<a name="API_Criterion_Contents"></a>

 ** contains **   <a name="accessanalyzer-Type-Criterion-contains"></a>
A "contains" operator to match for the filter used to create the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** eq **   <a name="accessanalyzer-Type-Criterion-eq"></a>
An "equals" operator to match for the filter used to create the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** exists **   <a name="accessanalyzer-Type-Criterion-exists"></a>
An "exists" operator to match for the filter used to create the rule.
Type: Boolean
Required: No

 ** neq **   <a name="accessanalyzer-Type-Criterion-neq"></a>
A "not equals" operator to match for the filter used to create the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

## See Also
<a name="API_Criterion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Criterion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Criterion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Criterion)
