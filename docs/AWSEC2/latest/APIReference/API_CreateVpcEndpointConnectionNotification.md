---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcEndpointConnectionNotification.html
---

# CreateVpcEndpointConnectionNotification
<a name="API_CreateVpcEndpointConnectionNotification"></a>

Creates a connection notification for a specified VPC endpoint or VPC endpoint service. A connection notification notifies you of specific endpoint events. You must create an SNS topic to receive notifications. For more information, see [Creating an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) in the *Amazon SNS Developer Guide*.

You can create a connection notification for interface endpoints only.

## Request Parameters
<a name="API_CreateVpcEndpointConnectionNotification_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ConnectionEvents.N**
The endpoint events for which to receive notifications. Valid values are `Accept`, `Connect`, `Delete`, and `Reject`.
Type: Array of strings
Required: Yes

 **ConnectionNotificationArn**
The ARN of the SNS topic for the notifications.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ServiceId**
The ID of the endpoint service.
Type: String
Required: No

 **VpcEndpointId**
The ID of the endpoint.
Type: String
Required: No

## Response Elements
<a name="API_CreateVpcEndpointConnectionNotification_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String

 **connectionNotification**
Information about the notification.
Type: [ConnectionNotification](API_ConnectionNotification.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateVpcEndpointConnectionNotification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpcEndpointConnectionNotification_Examples"></a>

### Example 1
<a name="API_CreateVpcEndpointConnectionNotification_Example_1"></a>

This example creates a notification for the endpoint `vpce-1234151a02f327123`. The notification is sent when the endpoint is rejected or deleted.

#### Sample Request
<a name="API_CreateVpcEndpointConnectionNotification_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpcEndpointConnectionNotification
&VpcEndpointId=vpce-1234151a02f327123
&ConnectionNotificationArn=arn:aws:sns:us-east-1:123456789012:endpointtopic
&ConnectionEvents.1=Reject
&ConnectionEvents.2=Delete
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpcEndpointConnectionNotification_Example_1_Response"></a>

```
<CreateVpcEndpointConnectionNotificationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>6bf51e2a-a99e-4839-af31-a0d72example</requestId>
    <connectionNotification>
        <connectionNotificationArn>arn:aws:sns:us-east-1:123456789012:endpointtopic</connectionNotificationArn>
        <connectionEvents>
            <item>Delete</item>
            <item>Reject</item>
        </connectionEvents>
        <connectionNotificationType>Topic</connectionNotificationType>
        <connectionNotificationState>Enabled</connectionNotificationState>
        <connectionNotificationId>vpce-nfn-04bcb952bc8af759b</connectionNotificationId>
        <vpcEndpointId>vpce-1234151a02f327123</vpcEndpointId>
    </connectionNotification>
</CreateVpcEndpointConnectionNotificationResponse>
```

## See Also
<a name="API_CreateVpcEndpointConnectionNotification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpcEndpointConnectionNotification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
