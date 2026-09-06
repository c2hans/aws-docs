---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClarifyShapBaselineConfig.html
---

# ClarifyShapBaselineConfig
<a name="API_ClarifyShapBaselineConfig"></a>

The configuration for the [SHAP baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.html) (also called the background or reference dataset) of the Kernal SHAP algorithm.

**Note**
The number of records in the baseline data determines the size of the synthetic dataset, which has an impact on latency of explainability requests. For more information, see the **Synthetic data** of [Configure and create an endpoint](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-online-explainability-create-endpoint.html).
 `ShapBaseline` and `ShapBaselineUri` are mutually exclusive parameters. One or the either is required to configure a SHAP baseline.

## Contents
<a name="API_ClarifyShapBaselineConfig_Contents"></a>

 ** MimeType **   <a name="sagemaker-Type-ClarifyShapBaselineConfig-MimeType"></a>
The MIME type of the baseline data. Choose from `'text/csv'` or `'application/jsonlines'`. Defaults to `'text/csv'`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*\/[a-zA-Z0-9](-*[a-zA-Z0-9+.])*`
Required: No

 ** ShapBaseline **   <a name="sagemaker-Type-ClarifyShapBaselineConfig-ShapBaseline"></a>
The inline SHAP baseline data in string format. `ShapBaseline` can have one or multiple records to be used as the baseline dataset. The format of the SHAP baseline file should be the same format as the training dataset. For example, if the training dataset is in CSV format and each record contains four features, and all features are numerical, then the format of the baseline data should also share these characteristics. For natural language processing (NLP) of text columns, the baseline value should be the value used to replace the unit of text specified by the `Granularity` of the `TextConfig` parameter. The size limit for `ShapBasline` is 4 KB. Use the `ShapBaselineUri` parameter if you want to provide more than 4 KB of baseline data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\s\S]+`
Required: No

 ** ShapBaselineUri **   <a name="sagemaker-Type-ClarifyShapBaselineConfig-ShapBaselineUri"></a>
The uniform resource identifier (URI) of the S3 bucket where the SHAP baseline file is stored. The format of the SHAP baseline file should be the same format as the format of the training dataset. For example, if the training dataset is in CSV format, and each record in the training dataset has four features, and all features are numerical, then the baseline file should also have this same format. Each record should contain only the features. If you are using a virtual private cloud (VPC), the `ShapBaselineUri` should be accessible to the VPC. For more information about setting up endpoints with Amazon Virtual Private Cloud, see [Give SageMaker access to Resources in your Amazon Virtual Private Cloud](https://docs.aws.amazon.com/sagemaker/latest/dg/infrastructure-give-access.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_ClarifyShapBaselineConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClarifyShapBaselineConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClarifyShapBaselineConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClarifyShapBaselineConfig)
