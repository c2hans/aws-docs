---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricsEndpoint.html
---

# MetricsEndpoint
<a name="API_MetricsEndpoint"></a>

Specifies a metrics endpoint for a container, including the path where the container exposes Prometheus-formatted metrics and the frequency at which to publish them to Amazon CloudWatch.

## Contents
<a name="API_MetricsEndpoint_Contents"></a>

 ** MetricsEndpointPath **   <a name="sagemaker-Type-MetricsEndpoint-MetricsEndpointPath"></a>
The path to the metrics endpoint exposed by the container. For example, `/metrics` or `/server/metrics`. The path must start with `/` and can contain alphanumeric characters, forward slashes, underscores, hyphens, and periods. Maximum length is 256 characters. If not specified, defaults to `/metrics`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `/(?!.*\.\.)[a-zA-Z0-9/_.\-]+`
Required: Yes

 ** MetricPublishFrequencyInSeconds **   <a name="sagemaker-Type-MetricsEndpoint-MetricPublishFrequencyInSeconds"></a>
The interval, in seconds, at which container metrics scraped from the endpoint are published to Amazon CloudWatch. Valid values: `10`, `30`, `60`, `120`, `180`, `240`, `300`. Defaults to `60`.
Type: Integer
Required: No

## See Also
<a name="API_MetricsEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/MetricsEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/MetricsEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/MetricsEndpoint)
