---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_ParentChildFieldOptionsMapping.html
---

# ParentChildFieldOptionsMapping
<a name="API_connect-cases_ParentChildFieldOptionsMapping"></a>

A mapping between a parent field option value and child field option values.

## Contents
<a name="API_connect-cases_ParentChildFieldOptionsMapping_Contents"></a>

 ** childFieldOptionValues **   <a name="connect-Type-connect-cases_ParentChildFieldOptionsMapping-childFieldOptionValues"></a>
A list of allowed values in the child field.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1500 items.
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `$|^.*[\S]`
Required: Yes

 ** parentFieldOptionValue **   <a name="connect-Type-connect-cases_ParentChildFieldOptionsMapping-parentFieldOptionValue"></a>
The value in the parent field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `$|^.*[\S]`
Required: Yes

## See Also
<a name="API_connect-cases_ParentChildFieldOptionsMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/ParentChildFieldOptionsMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/ParentChildFieldOptionsMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/ParentChildFieldOptionsMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
