---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_SplitDocument.html
---

# SplitDocument
<a name="API_SplitDocument"></a>

Contains information about the pages of a document, defined by logical boundary.

## Contents
<a name="API_SplitDocument_Contents"></a>

 ** Index **   <a name="Textract-Type-SplitDocument-Index"></a>
The index for a given document in a DocumentGroup of a specific Type.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** Pages **   <a name="Textract-Type-SplitDocument-Pages"></a>
An array of page numbers for a for a given document, ordered by logical boundary.
Type: Array of integers
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_SplitDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/SplitDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/SplitDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/SplitDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
