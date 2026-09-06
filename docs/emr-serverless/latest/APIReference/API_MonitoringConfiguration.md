---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_MonitoringConfiguration.html
---

# MonitoringConfiguration
<a name="API_MonitoringConfiguration"></a>

The configuration setting for monitoring.

## Contents
<a name="API_MonitoringConfiguration_Contents"></a>

 ** cloudWatchLoggingConfiguration **   <a name="emrserverless-Type-MonitoringConfiguration-cloudWatchLoggingConfiguration"></a>
The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.
Type: [CloudWatchLoggingConfiguration](API_CloudWatchLoggingConfiguration.md) object
Required: No

 ** managedPersistenceMonitoringConfiguration **   <a name="emrserverless-Type-MonitoringConfiguration-managedPersistenceMonitoringConfiguration"></a>
The managed log persistence configuration for a job run.
Type: [ManagedPersistenceMonitoringConfiguration](API_ManagedPersistenceMonitoringConfiguration.md) object
Required: No

 ** prometheusMonitoringConfiguration **   <a name="emrserverless-Type-MonitoringConfiguration-prometheusMonitoringConfiguration"></a>
The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.
Type: [PrometheusMonitoringConfiguration](API_PrometheusMonitoringConfiguration.md) object
Required: No

 ** s3MonitoringConfiguration **   <a name="emrserverless-Type-MonitoringConfiguration-s3MonitoringConfiguration"></a>
The Amazon S3 configuration for monitoring log publishing.
Type: [S3MonitoringConfiguration](API_S3MonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_MonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/MonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/MonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/MonitoringConfiguration)
