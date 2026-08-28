---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_FailedDocument.html
---

# FailedDocument
<a name="API_FailedDocument"></a>

A list of documents that could not be removed from an Amazon Q Business index. Each entry contains an error message that indicates why the document couldn't be removed from the index.

## Contents
<a name="API_FailedDocument_Contents"></a>

 ** dataSourceId **   <a name="qbusiness-Type-FailedDocument-dataSourceId"></a>
The identifier of the Amazon Q Business data source connector that contains the failed document.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** error **   <a name="qbusiness-Type-FailedDocument-error"></a>
An explanation for why the document couldn't be removed from the index.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** id **   <a name="qbusiness-Type-FailedDocument-id"></a>
The identifier of the document that couldn't be removed from the Amazon Q Business index.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_FailedDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/FailedDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/FailedDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/FailedDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
