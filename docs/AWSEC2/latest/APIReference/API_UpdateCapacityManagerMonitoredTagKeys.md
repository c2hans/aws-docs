---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateCapacityManagerMonitoredTagKeys.html
---

# UpdateCapacityManagerMonitoredTagKeys
<a name="API_UpdateCapacityManagerMonitoredTagKeys"></a>

 Activates or deactivates tag keys for monitoring by EC2 Capacity Manager. Activated tag keys are included as dimensions in capacity metric data, enabling you to group and filter metrics by tag values.

## Request Parameters
<a name="API_UpdateCapacityManagerMonitoredTagKeys_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ActivateTagKey.N**
 The tag keys to activate for monitoring. Once activated, these tag keys will be included as dimensions in capacity metric data.
Type: Array of strings
Required: No

 **ClientToken**
 Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 **DeactivateTagKey.N**
 The tag keys to deactivate. Deactivated tag keys will no longer be included as dimensions in capacity metric data.
Type: Array of strings
Required: No

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_UpdateCapacityManagerMonitoredTagKeys_ResponseElements"></a>

The following elements are returned by the service.

 **capacityManagerTagKeySet**
 The list of tag keys affected by the update, including their current status and metadata.
Type: Array of [CapacityManagerMonitoredTagKey](API_CapacityManagerMonitoredTagKey.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_UpdateCapacityManagerMonitoredTagKeys_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UpdateCapacityManagerMonitoredTagKeys_Examples"></a>

### Example
<a name="API_UpdateCapacityManagerMonitoredTagKeys_Example_1"></a>

This example activates the `Environment` and `CostCenter` tag keys for monitoring, and deactivates the `Team` tag key.

#### Sample Request
<a name="API_UpdateCapacityManagerMonitoredTagKeys_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=UpdateCapacityManagerMonitoredTagKeys
&ActivateTagKey.1=Environment
&ActivateTagKey.2=CostCenter
&DeactivateTagKey.1=Team
&AUTHPARAMS
```

#### Sample Response
<a name="API_UpdateCapacityManagerMonitoredTagKeys_Example_1_Response"></a>

```
<UpdateCapacityManagerMonitoredTagKeysResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <capacityManagerTagKeySet>
        <item>
            <tagKey>Environment</tagKey>
            <status>activating</status>
            <statusMessage/>
            <capacityManagerProvided>false</capacityManagerProvided>
        </item>
        <item>
            <tagKey>CostCenter</tagKey>
            <status>activating</status>
            <statusMessage/>
            <capacityManagerProvided>false</capacityManagerProvided>
        </item>
        <item>
            <tagKey>Team</tagKey>
            <status>deactivating</status>
            <statusMessage/>
            <capacityManagerProvided>false</capacityManagerProvided>
        </item>
    </capacityManagerTagKeySet>
</UpdateCapacityManagerMonitoredTagKeysResponse>
```

## See Also
<a name="API_UpdateCapacityManagerMonitoredTagKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UpdateCapacityManagerMonitoredTagKeys)
