---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckSource.html
---

# HealthCheckSource

A complex type that contains information about a health check source: its ID, its status, and the virtual private cloud (VPC), subnets, and security groups from which Route 53 sends health check requests to private endpoints.

## Contents
<a name="API_HealthCheckSource_Contents"></a>

 ** HealthCheckSourceConfig **   <a name="Route53-Type-HealthCheckSource-HealthCheckSourceConfig"></a>
The virtual private cloud (VPC), subnets, and security groups for the health check source.
Type: [HealthCheckSourceConfig](API_HealthCheckSourceConfig.md) object
Required: Yes

 ** HealthCheckSourceId **   <a name="Route53-Type-HealthCheckSource-HealthCheckSourceId"></a>
The ID of the health check source. Route 53 assigns this ID when it creates the source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** HealthCheckSourceStatus **   <a name="Route53-Type-HealthCheckSource-HealthCheckSourceStatus"></a>
The current status of the health check source. The health check source status can have one of the following values:
+  `CREATE_PENDING` - Route 53 accepted the request to create the source and hasn't started creating it. You can't use the source in a health check until its status is `CREATE_COMPLETED`.
+  `CREATE_IN_PROGRESS` - Route 53 is creating the source. You can't use the source in a health check until its status is `CREATE_COMPLETED`.
+  `CREATE_COMPLETED` - The source is ready to use.
+  `CREATE_FAILED` - Route 53 couldn't create the source. `StatusReasonCode` and `StatusReason` explain why.
+  `DELETE_PENDING` - Route 53 accepted the request to delete the source and hasn't started deleting it.
+  `DELETE_IN_PROGRESS` - Route 53 is deleting the source.
+  `DELETE_COMPLETED` - Route 53 has deleted the source. You can't retrieve a health check source in this status: `GetHealthCheckSource` returns `NoSuchHealthCheckSource`.
+  `DELETE_FAILED` - Route 53 couldn't delete the source. `StatusReasonCode` and `StatusReason` explain why.
If the status is `CREATE_FAILED`, fix the cause that `StatusReasonCode` indicates, and then either retry `CreateHealthCheckSource` with the same `CallerReference` and settings, or delete the source and create a new one. If the status is `DELETE_FAILED`, retry the `DeleteHealthCheckSource` request.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_COMPLETED | CREATE_FAILED | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_COMPLETED | DELETE_FAILED`
Required: Yes

 ** StatusReason **   <a name="Route53-Type-HealthCheckSource-StatusReason"></a>
A description of why the health check source has a status of `CREATE_FAILED` or `DELETE_FAILED`, and what you can do about it. The text corresponds to the value of `StatusReasonCode`. Route 53 returns this member only when `StatusReasonCode` is present.
Type: String
Required: No

 ** StatusReasonCode **   <a name="Route53-Type-HealthCheckSource-StatusReasonCode"></a>
A code that indicates why the health check source has a status of `CREATE_FAILED` or `DELETE_FAILED`. Route 53 returns this member only when the status is one of those values. The code can have one of the following values:
+  `INSUFFICIENT_SUBNET_IPS` - One of the specified subnets doesn't have enough free private IP addresses. Check the available IP addresses in each subnet, and delete network interfaces that you don't need.
+  `EC2_LIMIT_EXCEEDED` - Your account reached an Amazon virtual private cloud (VPC) quota for network interfaces or security groups. Delete network interfaces that you don't need, specify fewer security groups, or request a quota increase.
+  `INVALID_SUBNET` - One of the specified subnets doesn't exist or isn't valid, or an `AvailabilityZoneId` doesn't match the Availability Zone of its subnet. Check that each subnet ID is correct, that the subnet exists, and that each `AvailabilityZoneId` matches its subnet.
+  `INVALID_SECURITY_GROUP` - One of the specified security groups doesn't exist or isn't valid. Check that each security group ID is correct and that the security group exists.
+  `INVALID_CONFIGURATION` - The combination of VPC, subnets, and security groups isn't valid. Check that `VpcId` is correct and exists, that each subnet is in that VPC, and that the security groups for each subnet are in the same VPC as that subnet.
+  `SLR_MISSING_OR_NOT_ASSUMABLE` - Route 53 couldn't assume its service-linked role in your account. In IAM, check that the service-linked role for Route 53 private endpoint health checks exists and that no deletion task for it is in progress.
+  `INTERNAL_ERROR` - Route 53 encountered an internal error. Contact AWS Support and provide the health check source ID.
Type: String
Valid Values: `INSUFFICIENT_SUBNET_IPS | EC2_LIMIT_EXCEEDED | INVALID_SUBNET | INVALID_SECURITY_GROUP | INVALID_CONFIGURATION | SLR_MISSING_OR_NOT_ASSUMABLE | INTERNAL_ERROR`
Required: No

## See Also
<a name="API_HealthCheckSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53-2013-04-01/HealthCheckSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53-2013-04-01/HealthCheckSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53-2013-04-01/HealthCheckSource)
