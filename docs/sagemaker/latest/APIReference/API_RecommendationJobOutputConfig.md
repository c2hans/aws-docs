---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RecommendationJobOutputConfig.html
---

# RecommendationJobOutputConfig
<a name="API_RecommendationJobOutputConfig"></a>

Provides information about the output configuration for the compiled model.

## Contents
<a name="API_RecommendationJobOutputConfig_Contents"></a>

 ** CompiledOutputConfig **   <a name="sagemaker-Type-RecommendationJobOutputConfig-CompiledOutputConfig"></a>
Provides information about the output configuration for the compiled model.
Type: [RecommendationJobCompiledOutputConfig](API_RecommendationJobCompiledOutputConfig.md) object
Required: No

 ** KmsKeyId **   <a name="sagemaker-Type-RecommendationJobOutputConfig-KmsKeyId"></a>
The Amazon Resource Name (ARN) of a AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt your output artifacts with Amazon S3 server-side encryption. The SageMaker execution role must have `kms:GenerateDataKey` permission.
The `KmsKeyId` can be any of the following formats:
+ // KMS Key ID

   `"1234abcd-12ab-34cd-56ef-1234567890ab"`
+ // Amazon Resource Name (ARN) of a KMS Key

   `"arn:aws:kms:<region>:<account>:key/<key-id-12ab-34cd-56ef-1234567890ab>"`
+ // KMS Key Alias

   `"alias/ExampleAlias"`
+ // Amazon Resource Name (ARN) of a KMS Key Alias

   `"arn:aws:kms:<region>:<account>:alias/<ExampleAlias>"`
For more information about key identifiers, see [Key identifiers (KeyID)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) in the AWS Key Management Service (AWS KMS) documentation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

## See Also
<a name="API_RecommendationJobOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/RecommendationJobOutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/RecommendationJobOutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/RecommendationJobOutputConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
