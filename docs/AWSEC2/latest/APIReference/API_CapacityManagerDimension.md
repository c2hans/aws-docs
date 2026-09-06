---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityManagerDimension.html
---

# CapacityManagerDimension
<a name="API_CapacityManagerDimension"></a>

 Represents dimension values for capacity metrics, including resource identifiers, geographic information, and reservation details used for grouping and filtering capacity data.

## Contents
<a name="API_CapacityManagerDimension_Contents"></a>

 ** accountId **
 The AWS account ID that owns the capacity resource.
Type: String
Required: No

 ** accountName **
 The name of the AWS account that owns the capacity resource. This dimension is only available when Organizations access is enabled for Capacity Manager.
Type: String
Required: No

 ** availabilityZoneId **
 The unique identifier of the Availability Zone where the capacity resource is located.
Type: String
Required: No

 ** instanceFamily **
 The EC2 instance family of the capacity resource.
Type: String
Required: No

 ** instancePlatform **
 The platform or operating system of the instance.
Type: String
Required: No

 ** instanceType **
 The specific EC2 instance type of the capacity resource.
Type: String
Required: No

 ** reservationArn **
 The Amazon Resource Name (ARN) of the capacity reservation. This provides a unique identifier that can be used across AWS services to reference the specific reservation.
Type: String
Required: No

 ** reservationCreateTimestamp **
 The timestamp when the capacity reservation was originally created, in milliseconds since epoch. This differs from the start timestamp as reservations can be created before they become active.
Type: Timestamp
Required: No

 ** reservationEndDateType **
 The type of end date for the capacity reservation. This indicates whether the reservation has a fixed end date, is open-ended, or follows a specific termination pattern.
Type: String
Valid Values: `limited | unlimited`
Required: No

 ** reservationEndTimestamp **
 The timestamp when the capacity reservation expires and is no longer available, in milliseconds since epoch. After this time, the reservation will not provide any capacity.
Type: Timestamp
Required: No

 ** reservationId **
 The unique identifier of the capacity reservation.
Type: String
Required: No

 ** reservationInstanceMatchCriteria **
 The instance matching criteria for the capacity reservation, determining how instances are matched to the reservation.
Type: String
Required: No

 ** reservationStartTimestamp **
 The timestamp when the capacity reservation becomes active and available for use, in milliseconds since epoch. This is when the reservation begins providing capacity.
Type: Timestamp
Required: No

 ** reservationState **
 The current state of the capacity reservation.
Type: String
Valid Values: `active | expired | cancelled | scheduled | pending | failed | delayed | unsupported | payment-pending | payment-failed | retired`
Required: No

 ** reservationType **
 The type of capacity reservation.
Type: String
Valid Values: `capacity-block | odcr`
Required: No

 ** reservationUnusedFinancialOwner **
 The AWS account ID that is financially responsible for unused capacity reservation costs.
Type: String
Required: No

 ** resourceRegion **
 The AWS Region where the capacity resource is located.
Type: String
Required: No

 ** TagSet.N **
 The tags associated with the capacity resource, represented as key-value pairs. Only tags that have been activated for monitoring via `UpdateCapacityManagerMonitoredTagKeys` are included.
Type: Array of [CapacityManagerTagDimension](API_CapacityManagerTagDimension.md) objects
Required: No

 ** tenancy **
 The tenancy of the EC2 instances associated with this capacity dimension. Valid values are 'default' for shared tenancy, 'dedicated' for dedicated instances, or 'host' for dedicated hosts.
Type: String
Valid Values: `default | dedicated`
Required: No

## See Also
<a name="API_CapacityManagerDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityManagerDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityManagerDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityManagerDimension)
