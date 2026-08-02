---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_PrometheusMonitoringConfiguration.html
---

# PrometheusMonitoringConfiguration
<a name="API_PrometheusMonitoringConfiguration"></a>

The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.

## Contents
<a name="API_PrometheusMonitoringConfiguration_Contents"></a>

 ** remoteWriteUrl **   <a name="emrserverless-Type-PrometheusMonitoringConfiguration-remoteWriteUrl"></a>
The remote write URL in the Amazon Managed Service for Prometheus workspace to send metrics to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10280.
Pattern: `https://aps-workspaces.([a-z]{2}-[a-z-]{1,20}-[1-9]).amazonaws(.[0-9A-Za-z]{2,4})+/workspaces/[-_.0-9A-Za-z]{1,100}/api/v1/remote_write`
Required: No

## See Also
<a name="API_PrometheusMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/PrometheusMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/PrometheusMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/PrometheusMonitoringConfiguration)
