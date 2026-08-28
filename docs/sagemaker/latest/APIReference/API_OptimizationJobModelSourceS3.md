---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OptimizationJobModelSourceS3.html
---

# OptimizationJobModelSourceS3
<a name="API_OptimizationJobModelSourceS3"></a>

The Amazon S3 location of a source model to optimize with an optimization job.

## Contents
<a name="API_OptimizationJobModelSourceS3_Contents"></a>

 ** ModelAccessConfig **   <a name="sagemaker-Type-OptimizationJobModelSourceS3-ModelAccessConfig"></a>
The access configuration settings for the source ML model for an optimization job, where you can accept the model end-user license agreement (EULA).
Type: [OptimizationModelAccessConfig](API_OptimizationModelAccessConfig.md) object
Required: No

 ** S3Uri **   <a name="sagemaker-Type-OptimizationJobModelSourceS3-S3Uri"></a>
An Amazon S3 URI that locates a source model to optimize with an optimization job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_OptimizationJobModelSourceS3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/OptimizationJobModelSourceS3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/OptimizationJobModelSourceS3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/OptimizationJobModelSourceS3)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
