---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_FilterRule.html
---

# FilterRule
<a name="API_FilterRule"></a>

Specifies which files, folders, and objects to include or exclude when transferring files from source to destination.

## Contents
<a name="API_FilterRule_Contents"></a>

 ** FilterType **   <a name="DataSync-Type-FilterRule-FilterType"></a>
The type of filter rule to apply. AWS DataSync only supports the SIMPLE\_PATTERN rule type.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^[A-Z0-9_]+$`
Valid Values: `SIMPLE_PATTERN`
Required: No

 ** Value **   <a name="DataSync-Type-FilterRule-Value"></a>
A single filter string that consists of the patterns to include or exclude. The patterns are delimited by "\|" (that is, a pipe), for example: `/folder1|/folder2`

Type: String
Length Constraints: Maximum length of 102400.
Pattern: `^[^\x00]+$`
Required: No

## See Also
<a name="API_FilterRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/FilterRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/FilterRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/FilterRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
