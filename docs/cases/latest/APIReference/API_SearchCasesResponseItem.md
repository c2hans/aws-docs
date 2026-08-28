---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_SearchCasesResponseItem.html
---

# SearchCasesResponseItem
<a name="API_connect-cases_SearchCasesResponseItem"></a>

A list of items that represent cases.

## Contents
<a name="API_connect-cases_SearchCasesResponseItem_Contents"></a>

 ** caseId **   <a name="connect-Type-connect-cases_SearchCasesResponseItem-caseId"></a>
A unique identifier of the case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** fields **   <a name="connect-Type-connect-cases_SearchCasesResponseItem-fields"></a>
List of case field values.
Type: Array of [FieldValue](API_connect-cases_FieldValue.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Required: Yes

 ** templateId **   <a name="connect-Type-connect-cases_SearchCasesResponseItem-templateId"></a>
A unique identifier of a template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** tags **   <a name="connect-Type-connect-cases_SearchCasesResponseItem-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map
Required: No

## See Also
<a name="API_connect-cases_SearchCasesResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/SearchCasesResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/SearchCasesResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/SearchCasesResponseItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
