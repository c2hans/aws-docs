---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PurchaseCapacityBlockExtension.html
---

# PurchaseCapacityBlockExtension
<a name="API_PurchaseCapacityBlockExtension"></a>

Purchase the Capacity Block extension for use with your account. You must specify the ID of the Capacity Block extension offering you are purchasing.

## Request Parameters
<a name="API_PurchaseCapacityBlockExtension_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityBlockExtensionOfferingId**
The ID of the Capacity Block extension offering to purchase.
Type: String
Required: Yes

 **CapacityReservationId**
The ID of the Capacity reservation to be extended.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_PurchaseCapacityBlockExtension_ResponseElements"></a>

The following elements are returned by the service.

 **capacityBlockExtensionSet**
The purchased Capacity Block extensions.
Type: Array of [CapacityBlockExtension](API_CapacityBlockExtension.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_PurchaseCapacityBlockExtension_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PurchaseCapacityBlockExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/PurchaseCapacityBlockExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PurchaseCapacityBlockExtension)
