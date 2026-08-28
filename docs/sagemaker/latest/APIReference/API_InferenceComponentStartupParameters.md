---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InferenceComponentStartupParameters.html
---

# InferenceComponentStartupParameters
<a name="API_InferenceComponentStartupParameters"></a>

Settings that take effect while the model container starts up.

## Contents
<a name="API_InferenceComponentStartupParameters_Contents"></a>

 ** ContainerStartupHealthCheckTimeoutInSeconds **   <a name="sagemaker-Type-InferenceComponentStartupParameters-ContainerStartupHealthCheckTimeoutInSeconds"></a>
The timeout value, in seconds, for your inference container to pass health check by Amazon S3 Hosting. For more information about health check, see [How Your Container Should Respond to Health Check (Ping) Requests](https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-algo-ping-requests).
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 3600.
Required: No

 ** ModelDataDownloadTimeoutInSeconds **   <a name="sagemaker-Type-InferenceComponentStartupParameters-ModelDataDownloadTimeoutInSeconds"></a>
The timeout value, in seconds, to download and extract the model that you want to host from Amazon S3 to the individual inference instance associated with this inference component.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 3600.
Required: No

## See Also
<a name="API_InferenceComponentStartupParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InferenceComponentStartupParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InferenceComponentStartupParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InferenceComponentStartupParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
