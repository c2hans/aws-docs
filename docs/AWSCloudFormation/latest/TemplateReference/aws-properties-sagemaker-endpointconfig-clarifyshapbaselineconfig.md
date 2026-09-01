---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig ClarifyShapBaselineConfig
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig"></a>

The configuration for the [SHAP baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.html) (also called the background or reference dataset) of the Kernal SHAP algorithm.

**Note**
The number of records in the baseline data determines the size of the synthetic dataset, which has an impact on latency of explainability requests. For more information, see the **Synthetic data** of [Configure and create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html).
`ShapBaseline` and `ShapBaselineUri` are mutually exclusive parameters. One or the either is required to configure a SHAP baseline.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig-syntax.json"></a>

```
{
  "[MimeType](#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-mimetype)" : {{String}},
  "[ShapBaseline](#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaseline)" : {{String}},
  "[ShapBaselineUri](#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaselineuri)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig-syntax.yaml"></a>

```
  [MimeType](#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-mimetype): {{String}}
  [ShapBaseline](#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaseline): {{String}}
  [ShapBaselineUri](#cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaselineuri): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-clarifyshapbaselineconfig-properties"></a>

`MimeType`  <a name="cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-mimetype"></a>
The MIME type of the baseline data. Choose from `'text/csv'` or `'application/jsonlines'`. Defaults to `'text/csv'`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*\/[a-zA-Z0-9](-*[a-zA-Z0-9+.])*`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ShapBaseline`  <a name="cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaseline"></a>
The inline SHAP baseline data in string format. `ShapBaseline` can have one or multiple records to be used as the baseline dataset. The format of the SHAP baseline file should be the same format as the training dataset. For example, if the training dataset is in CSV format and each record contains four features, and all features are numerical, then the format of the baseline data should also share these characteristics. For natural language processing (NLP) of text columns, the baseline value should be the value used to replace the unit of text specified by the `Granularity` of the `TextConfig` parameter. The size limit for `ShapBasline` is 4 KB. Use the `ShapBaselineUri` parameter if you want to provide more than 4 KB of baseline data.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]+`
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ShapBaselineUri`  <a name="cfn-sagemaker-endpointconfig-clarifyshapbaselineconfig-shapbaselineuri"></a>
The uniform resource identifier (URI) of the S3 bucket where the SHAP baseline file is stored. The format of the SHAP baseline file should be the same format as the format of the training dataset. For example, if the training dataset is in CSV format, and each record in the training dataset has four features, and all features are numerical, then the baseline file should also have this same format. Each record should contain only the features. If you are using a virtual private cloud (VPC), the `ShapBaselineUri` should be accessible to the VPC. For more information about setting up endpoints with Amazon Virtual Private Cloud, see [Give SageMaker access to Resources in your Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
*Required*: No
*Type*: String
*Pattern*: `^(https|s3)://([^/]+)/?(.*)$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
