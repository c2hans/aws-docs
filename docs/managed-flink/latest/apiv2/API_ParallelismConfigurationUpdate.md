---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ParallelismConfigurationUpdate.html
---

# ParallelismConfigurationUpdate
<a name="API_ParallelismConfigurationUpdate"></a>

Describes updates to parameters for how an application executes multiple tasks simultaneously.

## Contents
<a name="API_ParallelismConfigurationUpdate_Contents"></a>

 ** AutoScalingEnabledUpdate **   <a name="APIReference-Type-ParallelismConfigurationUpdate-AutoScalingEnabledUpdate"></a>
Describes updates to whether the Managed Service for Apache Flink service can increase the parallelism of a Managed Service for Apache Flink application in response to increased throughput.
Type: Boolean
Required: No

 ** ConfigurationTypeUpdate **   <a name="APIReference-Type-ParallelismConfigurationUpdate-ConfigurationTypeUpdate"></a>
Describes updates to whether the application uses the default parallelism for the Managed Service for Apache Flink service, or if a custom parallelism is used. You must set this property to `CUSTOM` in order to change your application's `AutoScalingEnabled`, `Parallelism`, or `ParallelismPerKPU` properties.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** ParallelismPerKPUUpdate **   <a name="APIReference-Type-ParallelismConfigurationUpdate-ParallelismPerKPUUpdate"></a>
Describes updates to the number of parallel tasks an application can perform per Kinesis Processing Unit (KPU) used by the application.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ParallelismUpdate **   <a name="APIReference-Type-ParallelismConfigurationUpdate-ParallelismUpdate"></a>
Describes updates to the initial number of parallel tasks an application can perform. If `AutoScalingEnabled` is set to True, then Managed Service for Apache Flink can increase the `CurrentParallelism` value in response to application load. The service can increase `CurrentParallelism` up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service will reduce `CurrentParallelism` down to the `Parallelism` setting.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ParallelismConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ParallelismConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ParallelismConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ParallelismConfigurationUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
