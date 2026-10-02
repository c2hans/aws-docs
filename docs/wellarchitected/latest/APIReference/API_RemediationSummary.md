---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_RemediationSummary.html
---

# RemediationSummary
<a name="API_RemediationSummary"></a>

A high-level remediation summary returned in the detail response.

## Contents
<a name="API_RemediationSummary_Contents"></a>

 ** recommendation **   <a name="wellarchitected-Type-RemediationSummary-recommendation"></a>
A short imperative statement of the recommended action.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 240.
Required: Yes

 ** steps **   <a name="wellarchitected-Type-RemediationSummary-steps"></a>
High-level steps to implement the fix.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 20. Maximum length of 200.
Required: Yes

## See Also
<a name="API_RemediationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/RemediationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/RemediationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/RemediationSummary)
