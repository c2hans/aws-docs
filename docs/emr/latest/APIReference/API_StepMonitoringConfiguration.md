---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_StepMonitoringConfiguration.html
---

# StepMonitoringConfiguration
<a name="API_StepMonitoringConfiguration"></a>

Object that holds configuration properties for logging.

## Contents
<a name="API_StepMonitoringConfiguration_Contents"></a>

 ** S3MonitoringConfiguration **   <a name="EMR-Type-StepMonitoringConfiguration-S3MonitoringConfiguration"></a>
The Amazon S3 configuration for monitoring log publishing. You can configure your step to send log information to Amazon S3. When it's specified, it takes precedence over the cluster's logging configuration. If you don't specify this configuration entirely, or omit individual fields, EMR falls back to cluster-level logging behavior.
Type: [S3MonitoringConfiguration](API_S3MonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_StepMonitoringConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/StepMonitoringConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/StepMonitoringConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/StepMonitoringConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
