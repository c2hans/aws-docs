---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_X12AdvancedOptions.html
---

# X12AdvancedOptions
<a name="API_X12AdvancedOptions"></a>

Contains advanced options specific to X12 EDI processing, such as splitting large X12 files into smaller units.

## Contents
<a name="API_X12AdvancedOptions_Contents"></a>

 ** splitOptions **   <a name="b2bi-Type-X12AdvancedOptions-splitOptions"></a>
Specifies options for splitting X12 EDI files. These options control how large X12 files are divided into smaller, more manageable units.
Type: [X12SplitOptions](API_X12SplitOptions.md) object
Required: No

 ** validationOptions **   <a name="b2bi-Type-X12AdvancedOptions-validationOptions"></a>
Specifies validation options for X12 EDI processing. These options control how validation rules are applied during EDI document processing, including custom validation rules for element length constraints, code list validations, and element requirement checks.
Type: [X12ValidationOptions](API_X12ValidationOptions.md) object
Required: No

## See Also
<a name="API_X12AdvancedOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/X12AdvancedOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/X12AdvancedOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/X12AdvancedOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
