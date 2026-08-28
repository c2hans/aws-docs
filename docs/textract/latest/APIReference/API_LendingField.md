---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_LendingField.html
---

# LendingField
<a name="API_LendingField"></a>

Holds the normalized key-value pairs returned by AnalyzeDocument, including the document type, detected text, and geometry.

## Contents
<a name="API_LendingField_Contents"></a>

 ** KeyDetection **   <a name="Textract-Type-LendingField-KeyDetection"></a>
The results extracted for a lending document.
Type: [LendingDetection](API_LendingDetection.md) object
Required: No

 ** Type **   <a name="Textract-Type-LendingField-Type"></a>
The type of the lending document.
Type: String
Required: No

 ** ValueDetections **   <a name="Textract-Type-LendingField-ValueDetections"></a>
An array of LendingDetection objects.
Type: Array of [LendingDetection](API_LendingDetection.md) objects
Required: No

## See Also
<a name="API_LendingField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/LendingField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/LendingField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/LendingField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
