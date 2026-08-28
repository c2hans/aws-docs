---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UltraServer.html
---

# UltraServer
<a name="API_UltraServer"></a>

Represents a high-performance compute server used for distributed training in SageMaker AI. An UltraServer consists of multiple instances within a shared NVLink interconnect domain.

## Contents
<a name="API_UltraServer_Contents"></a>

 ** AvailabilityZone **   <a name="sagemaker-Type-UltraServer-AvailabilityZone"></a>
The name of the Availability Zone where the UltraServer is provisioned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-z]+\-[0-9a-z\-]+`
Required: Yes

 ** InstanceType **   <a name="sagemaker-Type-UltraServer-InstanceType"></a>
The Amazon EC2 instance type used in the UltraServer.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.trn1.32xlarge | ml.trn2.48xlarge | ml.p6-b200.48xlarge | ml.p4de.24xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge`
Required: Yes

 ** TotalInstanceCount **   <a name="sagemaker-Type-UltraServer-TotalInstanceCount"></a>
The total number of instances in this UltraServer.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** UltraServerId **   <a name="sagemaker-Type-UltraServer-UltraServerId"></a>
The unique identifier for the UltraServer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!\s*$).+`
Required: Yes

 ** UltraServerType **   <a name="sagemaker-Type-UltraServer-UltraServerType"></a>
The type of UltraServer, such as ml.u-p6e-gb200x72.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ml.[a-z0-9\-.]+`
Required: Yes

 ** AvailableInstanceCount **   <a name="sagemaker-Type-UltraServer-AvailableInstanceCount"></a>
The number of instances currently available for use in this UltraServer.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** AvailableSpareInstanceCount **   <a name="sagemaker-Type-UltraServer-AvailableSpareInstanceCount"></a>
The number of available spare instances in the UltraServer.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ConfiguredSpareInstanceCount **   <a name="sagemaker-Type-UltraServer-ConfiguredSpareInstanceCount"></a>
The number of spare instances configured for this UltraServer to provide enhanced resiliency.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** HealthStatus **   <a name="sagemaker-Type-UltraServer-HealthStatus"></a>
The overall health status of the UltraServer.
Type: String
Valid Values: `OK | Impaired | Insufficient-Data`
Required: No

 ** InUseInstanceCount **   <a name="sagemaker-Type-UltraServer-InUseInstanceCount"></a>
The number of instances currently in use in this UltraServer.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** UnhealthyInstanceCount **   <a name="sagemaker-Type-UltraServer-UnhealthyInstanceCount"></a>
The number of instances in this UltraServer that are currently in an unhealthy state.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_UltraServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UltraServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UltraServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UltraServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
