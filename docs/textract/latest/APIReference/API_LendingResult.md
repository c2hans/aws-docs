---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_LendingResult.html
---

# LendingResult
<a name="API_LendingResult"></a>

Contains the detections for each page analyzed through the Analyze Lending API.

## Contents
<a name="API_LendingResult_Contents"></a>

 ** Extractions **   <a name="Textract-Type-LendingResult-Extractions"></a>
An array of Extraction to hold structured data. e.g. normalized key value pairs instead of raw OCR detections .
Type: Array of [Extraction](API_Extraction.md) objects
Required: No

 ** Page **   <a name="Textract-Type-LendingResult-Page"></a>
The page number for a page, with regard to whole submission.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PageClassification **   <a name="Textract-Type-LendingResult-PageClassification"></a>
The classifier result for a given page.
Type: [PageClassification](API_PageClassification.md) object
Required: No

## See Also
<a name="API_LendingResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/LendingResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/LendingResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/LendingResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
