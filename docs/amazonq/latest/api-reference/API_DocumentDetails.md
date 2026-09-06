---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentDetails.html
---

# DocumentDetails
<a name="API_DocumentDetails"></a>

The details of a document within an Amazon Q Business index.

## Contents
<a name="API_DocumentDetails_Contents"></a>

 ** createdAt **   <a name="qbusiness-Type-DocumentDetails-createdAt"></a>
The timestamp for when the document was created.
Type: Timestamp
Required: No

 ** documentId **   <a name="qbusiness-Type-DocumentDetails-documentId"></a>
The identifier of the document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1825.
Pattern: `\P{C}*`
Required: No

 ** error **   <a name="qbusiness-Type-DocumentDetails-error"></a>
An error message associated with the document.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** status **   <a name="qbusiness-Type-DocumentDetails-status"></a>
The current status of the document.
Type: String
Valid Values: `RECEIVED | PROCESSING | INDEXED | UPDATED | FAILED | DELETING | DELETED | DOCUMENT_FAILED_TO_INDEX`
Required: No

 ** updatedAt **   <a name="qbusiness-Type-DocumentDetails-updatedAt"></a>
The timestamp for when the document was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_DocumentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentDetails)
