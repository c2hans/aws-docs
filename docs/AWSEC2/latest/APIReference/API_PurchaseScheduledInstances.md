---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseScheduledInstances.html
---

# PurchaseScheduledInstances
<a name="API_PurchaseScheduledInstances"></a>

**Note**
You can no longer purchase Scheduled Instances.

Purchases the Scheduled Instances with the specified schedule.

Scheduled Instances enable you to purchase Amazon EC2 compute capacity by the hour for a one-year term. Before you can purchase a Scheduled Instance, you must call [DescribeScheduledInstanceAvailability](API_DescribeScheduledInstanceAvailability.md) to check for available schedules and obtain a purchase token. After you purchase a Scheduled Instance, you must call [RunScheduledInstances](API_RunScheduledInstances.md) during each scheduled time period.

After you purchase a Scheduled Instance, you can't cancel, modify, or resell your purchase.

## Request Parameters
<a name="API_PurchaseScheduledInstances_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that ensures the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PurchaseRequest.N**
The purchase requests.
Type: Array of [PurchaseRequest](API_PurchaseRequest.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## Response Elements
<a name="API_PurchaseScheduledInstances_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **scheduledInstanceSet**
Information about the Scheduled Instances.
Type: Array of [ScheduledInstance](API_ScheduledInstance.md) objects

## Errors
<a name="API_PurchaseScheduledInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PurchaseScheduledInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/PurchaseScheduledInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PurchaseScheduledInstances)
