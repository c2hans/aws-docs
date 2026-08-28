---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_SignatureDetection.html
---

# SignatureDetection
<a name="API_SignatureDetection"></a>

Information regarding a detected signature on a page.

## Contents
<a name="API_SignatureDetection_Contents"></a>

 ** Confidence **   <a name="Textract-Type-SignatureDetection-Confidence"></a>
The confidence, from 0 to 100, in the predicted values for a detected signature.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Geometry **   <a name="Textract-Type-SignatureDetection-Geometry"></a>
Information about where the following items are located on a document page: detected page, text, key-value pairs, tables, table cells, and selection elements.
Type: [Geometry](API_Geometry.md) object
Required: No

## See Also
<a name="API_SignatureDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/SignatureDetection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/SignatureDetection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/SignatureDetection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
