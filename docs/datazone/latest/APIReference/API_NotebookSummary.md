---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_NotebookSummary.html
---

# NotebookSummary
<a name="API_NotebookSummary"></a>

The summary of a notebook in Amazon SageMaker Unified Studio.

## Contents
<a name="API_NotebookSummary_Contents"></a>

 ** domainId **   <a name="datazone-Type-NotebookSummary-domainId"></a>
The identifier of the Amazon SageMaker Unified Studio domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-NotebookSummary-id"></a>
The identifier of the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-NotebookSummary-name"></a>
The name of the notebook.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-NotebookSummary-owningProjectId"></a>
The identifier of the project that owns the notebook.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** status **   <a name="datazone-Type-NotebookSummary-status"></a>
The status of the notebook.
Type: String
Valid Values: `ACTIVE | ARCHIVED | SYNC_IN_PROGRESS | SYNC_FAILED`
Required: Yes

 ** createdAt **   <a name="datazone-Type-NotebookSummary-createdAt"></a>
The timestamp of when the notebook was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-NotebookSummary-createdBy"></a>
The identifier of the user who created the notebook.
Type: String
Required: No

 ** description **   <a name="datazone-Type-NotebookSummary-description"></a>
The description of the notebook.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** updatedAt **   <a name="datazone-Type-NotebookSummary-updatedAt"></a>
The timestamp of when the notebook was last updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="datazone-Type-NotebookSummary-updatedBy"></a>
The identifier of the user who last updated the notebook.
Type: String
Required: No

## See Also
<a name="API_NotebookSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/NotebookSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/NotebookSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/NotebookSummary)
