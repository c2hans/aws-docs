---
source_url: https://docs.aws.amazon.com/kendra/latest/APIReference/API_BatchGetDocumentStatusResponseError.html
---

# BatchGetDocumentStatusResponseError
<a name="API_BatchGetDocumentStatusResponseError"></a>

Provides a response when the status of a document could not be retrieved.

## Contents
<a name="API_BatchGetDocumentStatusResponseError_Contents"></a>

 ** DataSourceId **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-DataSourceId"></a>
 The identifier of the data source connector that the failed document belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** DocumentId **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-DocumentId"></a>
The identifier of the document whose status could not be retrieved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ErrorCode **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-ErrorCode"></a>
Indicates the source of the error.
Type: String
Valid Values: `InternalError | InvalidRequest`
Required: No

 ** ErrorMessage **   <a name="kendra-Type-BatchGetDocumentStatusResponseError-ErrorMessage"></a>
States that the API could not get the status of a document. This could be because the request is not valid or there is a system error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^\P{C}*$`
Required: No

## See Also
<a name="API_BatchGetDocumentStatusResponseError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/BatchGetDocumentStatusResponseError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/BatchGetDocumentStatusResponseError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/BatchGetDocumentStatusResponseError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kendra. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kendra` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
