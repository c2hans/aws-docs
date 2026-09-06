---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_ChoiceUpdate.html
---

# ChoiceUpdate
<a name="API_ChoiceUpdate"></a>

A list of choices to be updated.

## Contents
<a name="API_ChoiceUpdate_Contents"></a>

 ** Status **   <a name="wellarchitected-Type-ChoiceUpdate-Status"></a>
The status of a choice.
Type: String
Valid Values: `SELECTED | NOT_APPLICABLE | UNSELECTED`
Required: Yes

 ** Notes **   <a name="wellarchitected-Type-ChoiceUpdate-Notes"></a>
The notes associated with a choice.
Type: String
Length Constraints: Maximum length of 250.
Required: No

 ** Reason **   <a name="wellarchitected-Type-ChoiceUpdate-Reason"></a>
The reason why a choice is non-applicable to a question in your workload.
Type: String
Valid Values: `OUT_OF_SCOPE | BUSINESS_PRIORITIES | ARCHITECTURE_CONSTRAINTS | OTHER | NONE`
Required: No

## See Also
<a name="API_ChoiceUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/ChoiceUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/ChoiceUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/ChoiceUpdate)
