---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EmrServerlessComputeConfig.html
---

# EmrServerlessComputeConfig
<a name="API_EmrServerlessComputeConfig"></a>

**Note**
This data type is intended for use exclusively by SageMaker Canvas and cannot be used in other contexts at the moment.

Specifies the compute configuration for the EMR Serverless job.

## Contents
<a name="API_EmrServerlessComputeConfig_Contents"></a>

 ** ExecutionRoleARN **   <a name="sagemaker-Type-EmrServerlessComputeConfig-ExecutionRoleARN"></a>
The ARN of the IAM role granting the AutoML job V2 the necessary permissions access policies to list, connect to, or manage EMR Serverless jobs. For detailed information about the required permissions of this role, see "How to configure AutoML to initiate a remote job on EMR Serverless for large datasets" in [Create a regression or classification job for tabular data using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html) or [Create an AutoML job for time-series forecasting using the API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-timeseries-forecasting.html#timeseries-forecasting-api-optional-params).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

## See Also
<a name="API_EmrServerlessComputeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EmrServerlessComputeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EmrServerlessComputeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EmrServerlessComputeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
