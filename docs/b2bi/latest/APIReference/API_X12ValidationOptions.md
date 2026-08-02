---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12ValidationOptions.html
---

# X12ValidationOptions
<a name="API_X12ValidationOptions"></a>

Contains configuration options for X12 EDI validation. This structure allows you to specify custom validation rules that will be applied during EDI document processing, including element length constraints, code list modifications, and element requirement changes. These validation options provide flexibility to accommodate trading partner-specific requirements while maintaining EDI compliance. The validation rules are applied in addition to standard X12 validation to ensure documents meet both standard and custom requirements.

## Contents
<a name="API_X12ValidationOptions_Contents"></a>

 ** validationRules **   <a name="b2bi-Type-X12ValidationOptions-validationRules"></a>
Specifies a list of validation rules to apply during EDI document processing. These rules can include code list modifications, element length constraints, and element requirement changes.
Type: Array of [X12ValidationRule](API_X12ValidationRule.md) objects
Required: No

## See Also
<a name="API_X12ValidationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12ValidationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12ValidationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12ValidationOptions)
