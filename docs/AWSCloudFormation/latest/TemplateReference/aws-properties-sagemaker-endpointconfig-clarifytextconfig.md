---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-clarifytextconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ClarifyTextConfig
<a name="aws-properties-sagemaker-endpointconfig-clarifytextconfig"></a>

A parameter used to configure the SageMaker Clarify explainer to treat text features as text so that explanations are provided for individual units of text. Required only for natural language processing (NLP) explainability.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-clarifytextconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-clarifytextconfig-syntax.json"></a>

```
{
  "[Granularity](#cfn-sagemaker-endpointconfig-clarifytextconfig-granularity)" : {{String}},
  "[Language](#cfn-sagemaker-endpointconfig-clarifytextconfig-language)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-clarifytextconfig-syntax.yaml"></a>

```
  [Granularity](#cfn-sagemaker-endpointconfig-clarifytextconfig-granularity): {{String}}
  [Language](#cfn-sagemaker-endpointconfig-clarifytextconfig-language): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-clarifytextconfig-properties"></a>

`Granularity`  <a name="cfn-sagemaker-endpointconfig-clarifytextconfig-granularity"></a>
The unit of granularity for the analysis of text features. For example, if the unit is `'token'`, then each token (like a word in English) of the text is treated as a feature. SHAP values are computed for each unit/feature.
*Required*: Yes
*Type*: String
*Allowed values*: `token | sentence | paragraph`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Language`  <a name="cfn-sagemaker-endpointconfig-clarifytextconfig-language"></a>
Specifies the language of the text features in [ISO 639-1]( https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) or [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) code of a supported language.
For a mix of multiple languages, use code `'xx'`.
*Required*: Yes
*Type*: String
*Allowed values*: `af | sq | ar | hy | eu | bn | bg | ca | zh | hr | cs | da | nl | en | et | fi | fr | de | el | gu | he | hi | hu | is | id | ga | it | kn | ky | lv | lt | lb | mk | ml | mr | ne | nb | fa | pl | pt | ro | ru | sa | sr | tn | si | sk | sl | es | sv | tl | ta | tt | te | tr | uk | ur | yo | lij | xx`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
