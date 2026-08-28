---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ParallelismConfiguration.html
---

# ParallelismConfiguration
<a name="API_ParallelismConfiguration"></a>

Describes parameters for how a Managed Service for Apache Flink application executes multiple tasks simultaneously. For more information about parallelism, see [Parallel Execution](https://nightlies.apache.org/flink/flink-docs-release-1.20/dev/parallel.html) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-release-1.20/).

## Contents
<a name="API_ParallelismConfiguration_Contents"></a>

 ** ConfigurationType **   <a name="APIReference-Type-ParallelismConfiguration-ConfigurationType"></a>
Describes whether the application uses the default parallelism for the Managed Service for Apache Flink service. You must set this property to `CUSTOM` in order to change your application's `AutoScalingEnabled`, `Parallelism`, or `ParallelismPerKPU` properties.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: Yes

 ** AutoScalingEnabled **   <a name="APIReference-Type-ParallelismConfiguration-AutoScalingEnabled"></a>
Describes whether the Managed Service for Apache Flink service can increase the parallelism of the application in response to increased throughput.
Type: Boolean
Required: No

 ** Parallelism **   <a name="APIReference-Type-ParallelismConfiguration-Parallelism"></a>
Describes the initial number of parallel tasks that a Managed Service for Apache Flink application can perform. If `AutoScalingEnabled` is set to True, Managed Service for Apache Flink increases the `CurrentParallelism` value in response to application load. The service can increase the `CurrentParallelism` value up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 64 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the `CurrentParallelism` value down to the `Parallelism` setting.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ParallelismPerKPU **   <a name="APIReference-Type-ParallelismConfiguration-ParallelismPerKPU"></a>
Describes the number of parallel tasks that a Managed Service for Apache Flink application can perform per Kinesis Processing Unit (KPU) used by the application. For more information about KPUs, see [Amazon Managed Service for Apache Flink Pricing](http://aws.amazon.com/kinesis/data-analytics/pricing/).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ParallelismConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ParallelismConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ParallelismConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ParallelismConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
