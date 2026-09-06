---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ParallelismConfigurationDescription.html
---

# ParallelismConfigurationDescription
<a name="API_ParallelismConfigurationDescription"></a>

Describes parameters for how a Managed Service for Apache Flink application executes multiple tasks simultaneously.

## Contents
<a name="API_ParallelismConfigurationDescription_Contents"></a>

 ** AutoScalingEnabled **   <a name="APIReference-Type-ParallelismConfigurationDescription-AutoScalingEnabled"></a>
Describes whether the Managed Service for Apache Flink service can increase the parallelism of the application in response to increased throughput.
Type: Boolean
Required: No

 ** ConfigurationType **   <a name="APIReference-Type-ParallelismConfigurationDescription-ConfigurationType"></a>
Describes whether the application uses the default parallelism for the Managed Service for Apache Flink service.
Type: String
Valid Values: `DEFAULT | CUSTOM`
Required: No

 ** CurrentParallelism **   <a name="APIReference-Type-ParallelismConfigurationDescription-CurrentParallelism"></a>
Describes the current number of parallel tasks that a Managed Service for Apache Flink application can perform. If `AutoScalingEnabled` is set to True, Managed Service for Apache Flink can increase this value in response to application load. The service can increase this value up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the `CurrentParallelism` value down to the `Parallelism` setting.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Parallelism **   <a name="APIReference-Type-ParallelismConfigurationDescription-Parallelism"></a>
Describes the initial number of parallel tasks that a Managed Service for Apache Flink application can perform. If `AutoScalingEnabled` is set to True, then Managed Service for Apache Flink can increase the `CurrentParallelism` value in response to application load. The service can increase `CurrentParallelism` up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 64 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the `CurrentParallelism` value down to the `Parallelism` setting.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** ParallelismPerKPU **   <a name="APIReference-Type-ParallelismConfigurationDescription-ParallelismPerKPU"></a>
Describes the number of parallel tasks that a Managed Service for Apache Flink application can perform per Kinesis Processing Unit (KPU) used by the application.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ParallelismConfigurationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ParallelismConfigurationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ParallelismConfigurationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ParallelismConfigurationDescription)
