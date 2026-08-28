---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelArtifacts.html
---

# ModelArtifacts
<a name="API_ModelArtifacts"></a>

Provides information about the location that is configured for storing model artifacts.

Model artifacts are outputs that result from training a model. They typically consist of trained parameters, a model definition that describes how to compute inferences, and other metadata. A SageMaker container stores your trained model artifacts in the `/opt/ml/model` directory. After training has completed, by default, these artifacts are uploaded to your Amazon S3 bucket as compressed files.

## Contents
<a name="API_ModelArtifacts_Contents"></a>

 ** S3ModelArtifacts **   <a name="sagemaker-Type-ModelArtifacts-S3ModelArtifacts"></a>
The path of the S3 object that contains the model artifacts. For example, `s3://bucket-name/keynameprefix/model.tar.gz`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

## See Also
<a name="API_ModelArtifacts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ModelArtifacts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ModelArtifacts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ModelArtifacts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
