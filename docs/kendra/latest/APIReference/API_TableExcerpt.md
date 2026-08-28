---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_TableExcerpt.html
---

# TableExcerpt
<a name="API_TableExcerpt"></a>

An excerpt from a table within a document. The table excerpt displays up to five columns and three rows, depending on how many table cells are relevant to the query and how many columns are available in the original table. The top most relevant cell is displayed in the table excerpt, along with the next most relevant cells.

## Contents
<a name="API_TableExcerpt_Contents"></a>

 ** Rows **   <a name="kendra-Type-TableExcerpt-Rows"></a>
A list of rows in the table excerpt.
Type: Array of [TableRow](API_TableRow.md) objects
Required: No

 ** TotalNumberOfRows **   <a name="kendra-Type-TableExcerpt-TotalNumberOfRows"></a>
A count of the number of rows in the original table within the document.
Type: Integer
Required: No

## See Also
<a name="API_TableExcerpt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/TableExcerpt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/TableExcerpt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/TableExcerpt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
