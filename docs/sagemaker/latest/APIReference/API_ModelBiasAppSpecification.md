---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelBiasAppSpecification.html
---

# ModelBiasAppSpecification
<a name="API_ModelBiasAppSpecification"></a>

Docker container image configuration object for the model bias job.

## Contents
<a name="API_ModelBiasAppSpecification_Contents"></a>

 ** ConfigUri **   <a name="sagemaker-Type-ModelBiasAppSpecification-ConfigUri"></a>
JSON formatted S3 file that defines bias parameters. For more information on this JSON configuration file, see [Configure bias parameters](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-config-json-monitor-bias-parameters.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** ImageUri **   <a name="sagemaker-Type-ModelBiasAppSpecification-ImageUri"></a>
The container image to be run by the model bias job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** Environment **   <a name="sagemaker-Type-ModelBiasAppSpecification-Environment"></a>
Sets the environment variables in the Docker container.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `[a-zA-Z_][a-zA-Z0-9_]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ModelBiasAppSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelBiasAppSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelBiasAppSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelBiasAppSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
