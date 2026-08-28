---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ContainerMetricsConfig.html
---

# ContainerMetricsConfig
<a name="API_ContainerMetricsConfig"></a>

The configuration for container-level metrics scraping. Use this configuration to specify a custom metrics endpoint path and publishing frequency for container metrics. When `EnableDetailedObservability` is set to `True` in `MetricsConfig`, metrics are scraped from the container's Prometheus endpoint. If this configuration is not provided, the default path `/metrics` on port `8080` is used with a default publishing frequency of `60` seconds. For first-party and Deep Learning Containers (DLC), the endpoint path is determined automatically and this configuration is optional.

## Contents
<a name="API_ContainerMetricsConfig_Contents"></a>

 ** MetricsEndpoints **   <a name="sagemaker-Type-ContainerMetricsConfig-MetricsEndpoints"></a>
A list of metrics endpoints to scrape from the container. Each endpoint specifies the path where the container exposes Prometheus-formatted metrics and the frequency at which to publish them. You can specify a maximum of 1 endpoint.
Type: Array of [MetricsEndpoint](API_MetricsEndpoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

## See Also
<a name="API_ContainerMetricsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ContainerMetricsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ContainerMetricsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ContainerMetricsConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
