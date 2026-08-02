---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ReservedCapacitySummary.html
---

# ReservedCapacitySummary
<a name="API_ReservedCapacitySummary"></a>

Details of a reserved capacity for the training plan.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see ` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `.

## Contents
<a name="API_ReservedCapacitySummary_Contents"></a>

 ** InstanceType **   <a name="sagemaker-Type-ReservedCapacitySummary-InstanceType"></a>
The instance type for the reserved capacity.
Type: String
Valid Values: `ml.p4d.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.trn1.32xlarge | ml.trn2.48xlarge | ml.p6-b200.48xlarge | ml.p4de.24xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge`
Required: Yes

 ** ReservedCapacityArn **   <a name="sagemaker-Type-ReservedCapacitySummary-ReservedCapacityArn"></a>
The Amazon Resource Name (ARN); of the reserved capacity.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:reserved-capacity/.*`
Required: Yes

 ** Status **   <a name="sagemaker-Type-ReservedCapacitySummary-Status"></a>
The current status of the reserved capacity.
Type: String
Valid Values: `Pending | Active | Scheduled | Expired | Failed`
Required: Yes

 ** TotalInstanceCount **   <a name="sagemaker-Type-ReservedCapacitySummary-TotalInstanceCount"></a>
The total number of instances in the reserved capacity.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** AvailabilityZone **   <a name="sagemaker-Type-ReservedCapacitySummary-AvailabilityZone"></a>
The availability zone for the reserved capacity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-z]+\-[0-9a-z\-]+`
Required: No

 ** AvailabilityZoneId **   <a name="sagemaker-Type-ReservedCapacitySummary-AvailabilityZoneId"></a>
The Availability Zone ID of the reserved capacity.
Type: String
Pattern: `[a-z]{3}\d-az\d`
Required: No

 ** DurationHours **   <a name="sagemaker-Type-ReservedCapacitySummary-DurationHours"></a>
The number of whole hours in the total duration for this reserved capacity.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 87600.
Required: No

 ** DurationMinutes **   <a name="sagemaker-Type-ReservedCapacitySummary-DurationMinutes"></a>
The additional minutes beyond whole hours in the total duration for this reserved capacity.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 59.
Required: No

 ** EndTime **   <a name="sagemaker-Type-ReservedCapacitySummary-EndTime"></a>
The end time of the reserved capacity.
Type: Timestamp
Required: No

 ** ReservedCapacityType **   <a name="sagemaker-Type-ReservedCapacitySummary-ReservedCapacityType"></a>
The type of reserved capacity.
Type: String
Valid Values: `UltraServer | Instance`
Required: No

 ** StartTime **   <a name="sagemaker-Type-ReservedCapacitySummary-StartTime"></a>
The start time of the reserved capacity.
Type: Timestamp
Required: No

 ** UltraServerCount **   <a name="sagemaker-Type-ReservedCapacitySummary-UltraServerCount"></a>
The number of UltraServers included in this reserved capacity.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** UltraServerType **   <a name="sagemaker-Type-ReservedCapacitySummary-UltraServerType"></a>
The type of UltraServer included in this reserved capacity, such as ml.u-p6e-gb200x72.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ml.[a-z0-9\-.]+`
Required: No

## See Also
<a name="API_ReservedCapacitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ReservedCapacitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ReservedCapacitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ReservedCapacitySummary)
