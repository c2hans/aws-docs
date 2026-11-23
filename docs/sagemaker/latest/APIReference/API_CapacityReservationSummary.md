---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationSummary.html
---

# CapacityReservationSummary

Summary information about a SageMaker Capacity Reservation.

## Contents
<a name="API_CapacityReservationSummary_Contents"></a>

 ** AvailabilityZoneId **   <a name="sagemaker-Type-CapacityReservationSummary-AvailabilityZoneId"></a>
The ID of the Availability Zone of the reserved instances, for example `use1-az1`. An Availability Zone ID identifies the same physical zone in every account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-CapacityReservationSummary-CreationTime"></a>
The time when the SageMaker Capacity Reservation was created.
Type: Timestamp
Required: Yes

 ** InstanceType **   <a name="sagemaker-Type-CapacityReservationSummary-InstanceType"></a>
The SageMaker AI instance type of the reserved instances, for example `ml.p5.48xlarge`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Owner **   <a name="sagemaker-Type-CapacityReservationSummary-Owner"></a>
The ID of the AWS account that owns the SageMaker Capacity Reservation.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d+`
Required: Yes

 ** SMCapacityReservationArn **   <a name="sagemaker-Type-CapacityReservationSummary-SMCapacityReservationArn"></a>
The Amazon Resource Name (ARN) of the SageMaker Capacity Reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]+:[0-9]{12}:sm-capacity-reservation/smcr-[0-9a-z]{12}`
Required: Yes

 ** SMCapacityReservationId **   <a name="sagemaker-Type-CapacityReservationSummary-SMCapacityReservationId"></a>
The ID of the SageMaker Capacity Reservation. The ID is the last part of the ARN and starts with `smcr-`.
Type: String
Pattern: `smcr-[0-9a-z]{12}`
Required: Yes

 ** StartTime **   <a name="sagemaker-Type-CapacityReservationSummary-StartTime"></a>
The time when the reserved instances become available.
Type: Timestamp
Required: Yes

 ** Status **   <a name="sagemaker-Type-CapacityReservationSummary-Status"></a>
The status of the SageMaker Capacity Reservation. SageMaker AI sets the status from the start and end times of the reservation. Valid values:
Scheduled
The current time is before `StartTime`.
Active
The current time is between `StartTime` and `EndTime`. You can use the reserved instances.
Expired
The current time is at or after `EndTime`.
Type: String
Valid Values: `Scheduled | Active | Expired`
Required: Yes

 ** TotalInstanceCount **   <a name="sagemaker-Type-CapacityReservationSummary-TotalInstanceCount"></a>
The number of instances in the SageMaker Capacity Reservation.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** AvailabilityZone **   <a name="sagemaker-Type-CapacityReservationSummary-AvailabilityZone"></a>
The name of the Availability Zone of the reserved instances, for example `us-east-1a`. Availability Zone names can map to different physical zones in different accounts. To identify the same zone across accounts, use `AvailabilityZoneId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[a-z]+\-[0-9a-z\-]+`
Required: No

 ** EndTime **   <a name="sagemaker-Type-CapacityReservationSummary-EndTime"></a>
The time when the SageMaker Capacity Reservation ends. This value is not returned if the reservation has no end time.
Type: Timestamp
Required: No

## See Also
<a name="API_CapacityReservationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationSummary)
