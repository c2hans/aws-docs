---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableCapacityManager.html
---

# DisableCapacityManager
<a name="API_DisableCapacityManager"></a>

 Disables EC2 Capacity Manager for your account. This stops data ingestion and removes access to capacity analytics and optimization recommendations. Previously collected data is retained but no new data will be processed.

## Request Parameters
<a name="API_DisableCapacityManager_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
 Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DisableCapacityManager_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerStatus**
 The current status of Capacity Manager after the disable operation.
Type: String
Valid Values: `enabled | disabled`

 **organizationsAccess**
 Indicates whether Organizations access is enabled. This will be `false` after disabling Capacity Manager.
Type: Boolean

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisableCapacityManager_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisableCapacityManager_Examples"></a>

### Example
<a name="API_DisableCapacityManager_Example_1"></a>

This example disables Capacity Manager for your account.

#### Sample Request
<a name="API_DisableCapacityManager_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisableCapacityManager
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableCapacityManager_Example_1_Response"></a>

```
<DisableCapacityManagerResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerStatus>disabled</capacityManagerStatus>
    <organizationsAccess>false</organizationsAccess>
</DisableCapacityManagerResponse>
```

## See Also
<a name="API_DisableCapacityManager_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableCapacityManager)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableCapacityManager)
