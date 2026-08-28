---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ReadOptions.html
---

# ReadOptions
<a name="API_ReadOptions"></a>

Read options for an annotation import job.

## Contents
<a name="API_ReadOptions_Contents"></a>

 ** comment **   <a name="omics-Type-ReadOptions-comment"></a>
The file's comment character.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** encoding **   <a name="omics-Type-ReadOptions-encoding"></a>
The file's encoding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** escape **   <a name="omics-Type-ReadOptions-escape"></a>
A character for escaping quotes in the file.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** escapeQuotes **   <a name="omics-Type-ReadOptions-escapeQuotes"></a>
Whether quotes need to be escaped in the file.
Type: Boolean
Required: No

 ** header **   <a name="omics-Type-ReadOptions-header"></a>
Whether the file has a header row.
Type: Boolean
Required: No

 ** lineSep **   <a name="omics-Type-ReadOptions-lineSep"></a>
A line separator for the file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** quote **   <a name="omics-Type-ReadOptions-quote"></a>
The file's quote character.
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** quoteAll **   <a name="omics-Type-ReadOptions-quoteAll"></a>
Whether all values need to be quoted, or just those that contain quotes.
Type: Boolean
Required: No

 ** sep **   <a name="omics-Type-ReadOptions-sep"></a>
The file's field separator.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

## See Also
<a name="API_ReadOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ReadOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ReadOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ReadOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
