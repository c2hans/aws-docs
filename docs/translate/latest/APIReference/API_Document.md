---
source_url: https://docs.aws.amazon.com/translate/latest/APIReference/API_Document.html
---

# Document
<a name="API_Document"></a>

The content and content type of a document.

## Contents
<a name="API_Document_Contents"></a>

 ** Content **   <a name="translate-Type-Document-Content"></a>
The `Content`field type is Binary large object (blob). This object contains the document content converted into base64-encoded binary data. If you use one of the AWS SDKs, the SDK performs the Base64-encoding on this field before sending the request.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 102400.
Required: Yes

 ** ContentType **   <a name="translate-Type-Document-ContentType"></a>
Describes the format of the document. You can specify one of the following:
+  `text/html` - The input data consists of HTML content. Amazon Translate translates only the text in the HTML element.
+  `text/plain` - The input data consists of unformatted text. Amazon Translate translates every character in the content.
+  `application/vnd.openxmlformats-officedocument.wordprocessingml.document` - The input data consists of a Word document (.docx).
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[-\w.]+\/[-\w.+]+$`
Required: Yes

## See Also
<a name="API_Document_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/translate-2017-07-01/Document)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/translate-2017-07-01/Document)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/translate-2017-07-01/Document)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Translate. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query translate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
