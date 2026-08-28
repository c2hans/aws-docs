---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesForecastingSettings.html
---

# TimeSeriesForecastingSettings
<a name="API_TimeSeriesForecastingSettings"></a>

Time series forecast settings for the SageMaker Canvas application.

## Contents
<a name="API_TimeSeriesForecastingSettings_Contents"></a>

 ** AmazonForecastRoleArn **   <a name="sagemaker-Type-TimeSeriesForecastingSettings-AmazonForecastRoleArn"></a>
The IAM role that Canvas passes to Amazon Forecast for time series forecasting. By default, Canvas uses the execution role specified in the `UserProfile` that launches the Canvas application. If an execution role is not specified in the `UserProfile`, Canvas uses the execution role specified in the Domain that owns the `UserProfile`. To allow time series forecasting, this IAM role should have the [ AmazonSageMakerCanvasForecastAccess](https://docs.aws.amazon.com/sagemaker/latest/dg/security-iam-awsmanpol-canvas.html#security-iam-awsmanpol-AmazonSageMakerCanvasForecastAccess) policy attached and `forecast.amazonaws.com` added in the trust relationship as a service principal.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Status **   <a name="sagemaker-Type-TimeSeriesForecastingSettings-Status"></a>
Describes whether time series forecasting is enabled or disabled in the Canvas application.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_TimeSeriesForecastingSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TimeSeriesForecastingSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TimeSeriesForecastingSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TimeSeriesForecastingSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
