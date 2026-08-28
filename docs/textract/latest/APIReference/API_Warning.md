---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_Warning.html
---

# Warning
<a name="API_Warning"></a>

A warning about an issue that occurred during asynchronous text analysis ([StartDocumentAnalysis](API_StartDocumentAnalysis.md)) or asynchronous document text detection ([StartDocumentTextDetection](API_StartDocumentTextDetection.md)).

## Contents
<a name="API_Warning_Contents"></a>

 ** ErrorCode **   <a name="Textract-Type-Warning-ErrorCode"></a>
The error code for the warning.
Type: String
Required: No

 ** Pages **   <a name="Textract-Type-Warning-Pages"></a>
A list of the pages that the warning applies to.
Type: Array of integers
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_Warning_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/Warning)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/Warning)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/Warning)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
