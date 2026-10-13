---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ReservedCapacityOffering.html
---

# ReservedCapacityOffering
<a name="API_ReservedCapacityOffering"></a>

Details about a reserved capacity offering for a training plan offering.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.

## Contents
<a name="API_ReservedCapacityOffering_Contents"></a>

 ** InstanceCount **   <a name="sagemaker-Type-ReservedCapacityOffering-InstanceCount"></a>
The number of instances in the reserved capacity offering.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 256.
Required: Yes

 ** InstanceType **   <a name="sagemaker-Type-ReservedCapacityOffering-InstanceType"></a>
The instance type for the reserved capacity offering.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.trn1.32xlarge | ml.trn2.48xlarge | ml.p6-b200.48xlarge | ml.p4de.24xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge`
Required: Yes

 ** AvailabilityZone **   <a name="sagemaker-Type-ReservedCapacityOffering-AvailabilityZone"></a>
The availability zone for the reserved capacity offering.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-z]+\-[0-9a-z\-]+`
Required: No

 ** DurationHours **   <a name="sagemaker-Type-ReservedCapacityOffering-DurationHours"></a>
The number of whole hours in the total duration for this reserved capacity offering.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 87600.
Required: No

 ** DurationMinutes **   <a name="sagemaker-Type-ReservedCapacityOffering-DurationMinutes"></a>
The additional minutes beyond whole hours in the total duration for this reserved capacity offering.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.
Required: No

 ** EndTime **   <a name="sagemaker-Type-ReservedCapacityOffering-EndTime"></a>
The end time of the reserved capacity offering.
Type: Timestamp
Required: No

 ** ExtensionEndTime **   <a name="sagemaker-Type-ReservedCapacityOffering-ExtensionEndTime"></a>
The end time of the extension for the reserved capacity offering.
Type: Timestamp
Required: No

 ** ExtensionStartTime **   <a name="sagemaker-Type-ReservedCapacityOffering-ExtensionStartTime"></a>
The start time of the extension for the reserved capacity offering.
Type: Timestamp
Required: No

 ** ReservedCapacityType **   <a name="sagemaker-Type-ReservedCapacityOffering-ReservedCapacityType"></a>
The type of reserved capacity offering.
Type: String
Valid Values: `UltraServer | Instance`
Required: No

 ** StartTime **   <a name="sagemaker-Type-ReservedCapacityOffering-StartTime"></a>
The start time of the reserved capacity offering.
Type: Timestamp
Required: No

 ** UltraServerCount **   <a name="sagemaker-Type-ReservedCapacityOffering-UltraServerCount"></a>
The number of UltraServers included in this reserved capacity offering.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** UltraServerType **   <a name="sagemaker-Type-ReservedCapacityOffering-UltraServerType"></a>
The type of UltraServer included in this reserved capacity offering, such as ml.u-p6e-gb200x72.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ml.[a-z0-9\-.]+`
Required: No

## See Also
<a name="API_ReservedCapacityOffering_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ReservedCapacityOffering)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ReservedCapacityOffering)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ReservedCapacityOffering)
