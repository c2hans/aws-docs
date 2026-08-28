---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_PageClassification.html
---

# PageClassification
<a name="API_PageClassification"></a>

The class assigned to a Page object detected in an input document. Contains information regarding the predicted type/class of a document's page and the page number that the Page object was detected on.

## Contents
<a name="API_PageClassification_Contents"></a>

 ** PageNumber **   <a name="Textract-Type-PageClassification-PageNumber"></a>
 The page number the value was detected on, relative to Amazon Textract's starting position.
Type: Array of [Prediction](API_Prediction.md) objects
Required: Yes

 ** PageType **   <a name="Textract-Type-PageClassification-PageType"></a>
The class, or document type, assigned to a detected Page object. The class, or document type, assigned to a detected Page object.
Type: Array of [Prediction](API_Prediction.md) objects
Required: Yes

## See Also
<a name="API_PageClassification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/PageClassification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/PageClassification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/PageClassification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Textract. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query textract` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
