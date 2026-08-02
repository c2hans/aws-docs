---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseCapacityBlock.html
---

# PurchaseCapacityBlock
<a name="API_PurchaseCapacityBlock"></a>

Purchase the Capacity Block for use with your account. With Capacity Blocks you ensure GPU capacity is available for machine learning (ML) workloads. You must specify the ID of the Capacity Block offering you are purchasing.

## Request Parameters
<a name="API_PurchaseCapacityBlock_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityBlockOfferingId**
The ID of the Capacity Block offering.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstancePlatform**
The type of operating system for which to reserve capacity.
Type: String
Valid Values: `Linux/UNIX | Red Hat Enterprise Linux | SUSE Linux | Windows | Windows with SQL Server | Windows with SQL Server Enterprise | Windows with SQL Server Standard | Windows with SQL Server Web | Linux with SQL Server Standard | Linux with SQL Server Web | Linux with SQL Server Enterprise | RHEL with SQL Server Standard | RHEL with SQL Server Enterprise | RHEL with SQL Server Web | RHEL with HA | RHEL with HA and SQL Server Standard | RHEL with HA and SQL Server Enterprise | Ubuntu Pro`
Required: Yes

 **TagSpecification.N**
The tags to apply to the Capacity Block during launch.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_PurchaseCapacityBlock_ResponseElements"></a>

The following elements are returned by the service.

 **capacityBlockSet**
The Capacity Block.
Type: Array of [CapacityBlock](API_CapacityBlock.md) objects

 **capacityReservation**
The Capacity Reservation.
Type: [CapacityReservation](API_CapacityReservation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_PurchaseCapacityBlock_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PurchaseCapacityBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/PurchaseCapacityBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PurchaseCapacityBlock)
