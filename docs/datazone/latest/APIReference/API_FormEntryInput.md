---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_FormEntryInput.html
---

# FormEntryInput
<a name="API_FormEntryInput"></a>

The details of the form entry.

## Contents
<a name="API_FormEntryInput_Contents"></a>

 ** typeIdentifier **   <a name="datazone-Type-FormEntryInput-typeIdentifier"></a>
The type ID of the form entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 385.
Pattern: `(?!\.)[\w\.]*\w`
Required: Yes

 ** typeRevision **   <a name="datazone-Type-FormEntryInput-typeRevision"></a>
The type revision of the form entry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** required **   <a name="datazone-Type-FormEntryInput-required"></a>
Specifies whether a form entry is required.
Type: Boolean
Required: No

## See Also
<a name="API_FormEntryInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/FormEntryInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/FormEntryInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/FormEntryInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
