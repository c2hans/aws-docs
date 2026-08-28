---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ColumnSelector.html
---

# ColumnSelector
<a name="API_ColumnSelector"></a>

Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression.

## Contents
<a name="API_ColumnSelector_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-ColumnSelector-Name"></a>
The name of a column from a dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Regex **   <a name="databrew-Type-ColumnSelector-Regex"></a>
A regular expression for selecting a column from a dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ColumnSelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ColumnSelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ColumnSelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ColumnSelector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
