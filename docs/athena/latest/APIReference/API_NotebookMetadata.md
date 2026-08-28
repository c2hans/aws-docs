---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_NotebookMetadata.html
---

# NotebookMetadata
<a name="API_NotebookMetadata"></a>

Contains metadata for notebook, including the notebook name, ID, workgroup, and time created.

## Contents
<a name="API_NotebookMetadata_Contents"></a>

 ** CreationTime **   <a name="athena-Type-NotebookMetadata-CreationTime"></a>
The time when the notebook was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="athena-Type-NotebookMetadata-LastModifiedTime"></a>
The time when the notebook was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="athena-Type-NotebookMetadata-Name"></a>
The name of the notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?!.*[/:\\])[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]+`
Required: No

 ** NotebookId **   <a name="athena-Type-NotebookMetadata-NotebookId"></a>
The notebook ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** Type **   <a name="athena-Type-NotebookMetadata-Type"></a>
The type of notebook. Currently, the only valid type is `IPYNB`.
Type: String
Valid Values: `IPYNB`
Required: No

 ** WorkGroup **   <a name="athena-Type-NotebookMetadata-WorkGroup"></a>
The name of the Spark enabled workgroup to which the notebook belongs.
Type: String
Pattern: `[a-zA-Z0-9._-]{1,128}`
Required: No

## See Also
<a name="API_NotebookMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/NotebookMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/NotebookMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/NotebookMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
