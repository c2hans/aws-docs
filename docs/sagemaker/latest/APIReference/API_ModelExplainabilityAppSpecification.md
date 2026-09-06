---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelExplainabilityAppSpecification.html
---

# ModelExplainabilityAppSpecification
<a name="API_ModelExplainabilityAppSpecification"></a>

Docker container image configuration object for the model explainability job.

## Contents
<a name="API_ModelExplainabilityAppSpecification_Contents"></a>

 ** ConfigUri **   <a name="sagemaker-Type-ModelExplainabilityAppSpecification-ConfigUri"></a>
JSON formatted Amazon S3 file that defines explainability parameters. For more information on this JSON configuration file, see [Configure model explainability parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-model-explainability-parameters.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** ImageUri **   <a name="sagemaker-Type-ModelExplainabilityAppSpecification-ImageUri"></a>
The container image to be run by the model explainability job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** Environment **   <a name="sagemaker-Type-ModelExplainabilityAppSpecification-Environment"></a>
Sets the environment variables in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ModelExplainabilityAppSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelExplainabilityAppSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelExplainabilityAppSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelExplainabilityAppSpecification)
