---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointConnectionNotification.html
---

# ModifyVpcEndpointConnectionNotification
<a name="API_ModifyVpcEndpointConnectionNotification"></a>

Modifies a connection notification for VPC endpoint or VPC endpoint service. You can change the SNS topic for the notification, or the events for which to be notified.

## Request Parameters
<a name="API_ModifyVpcEndpointConnectionNotification_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ConnectionEvents.N**
The events for the endpoint. Valid values are `Accept`, `Connect`, `Delete`, and `Reject`.
Type: Array of strings
Required: No

 **ConnectionNotificationArn**
The ARN for the SNS topic for the notification.
Type: String
Required: No

 **ConnectionNotificationId**
The ID of the notification.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_ModifyVpcEndpointConnectionNotification_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_ModifyVpcEndpointConnectionNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcEndpointConnectionNotification_Examples"></a>

### Example
<a name="API_ModifyVpcEndpointConnectionNotification_Example_1"></a>

The following example modifies notification `vpce-nfn-abccb952bc8af7123` by modifying the endpoint events and the SNS topic ARN.

#### Sample Request
<a name="API_ModifyVpcEndpointConnectionNotification_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcEndpointConnectionNotification
&ConnectionNotificationId=vpce-nfn-abccb952bc8af7123
&ConnectionNotificationArn=arn:aws:sns:us-east-1:123456789012:mytopic
&ConnectionEvents.1=Accept
&ConnectionEvents.2=Reject
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcEndpointConnectionNotification_Example_1_Response"></a>

```
<ModifyVpcEndpointConnectionNotificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>08d80840-f750-42db-a6f8-2cd32example</requestId>
    <return>true</return>
</ModifyVpcEndpointConnectionNotificationResponse>
```

## See Also
<a name="API_ModifyVpcEndpointConnectionNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcEndpointConnectionNotification)
