---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClarifyTextConfig.html
---

# ClarifyTextConfig
<a name="API_ClarifyTextConfig"></a>

A parameter used to configure the SageMaker Clarify explainer to treat text features as text so that explanations are provided for individual units of text. Required only for natural language processing (NLP) explainability.

## Contents
<a name="API_ClarifyTextConfig_Contents"></a>

 ** Granularity **   <a name="sagemaker-Type-ClarifyTextConfig-Granularity"></a>
The unit of granularity for the analysis of text features. For example, if the unit is `'token'`, then each token (like a word in English) of the text is treated as a feature. SHAP values are computed for each unit/feature.
Type: String
Valid Values: `token | sentence | paragraph`
Required: Yes

 ** Language **   <a name="sagemaker-Type-ClarifyTextConfig-Language"></a>
Specifies the language of the text features in [ISO 639-1]( https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) or [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) code of a supported language.
For a mix of multiple languages, use code `'xx'`.
Type: String
Valid Values: `af | sq | ar | hy | eu | bn | bg | ca | zh | hr | cs | da | nl | en | et | fi | fr | de | el | gu | he | hi | hu | is | id | ga | it | kn | ky | lv | lt | lb | mk | ml | mr | ne | nb | fa | pl | pt | ro | ru | sa | sr | tn | si | sk | sl | es | sv | tl | ta | tt | te | tr | uk | ur | yo | lij | xx`
Required: Yes

## See Also
<a name="API_ClarifyTextConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClarifyTextConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClarifyTextConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClarifyTextConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
