---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointConnectionNotifications.html
---

# DeleteVpcEndpointConnectionNotifications
<a name="API_DeleteVpcEndpointConnectionNotifications"></a>

Deletes the specified VPC endpoint connection notifications.

## Request Parameters
<a name="API_DeleteVpcEndpointConnectionNotifications_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ConnectionNotificationId.N**
The IDs of the notifications.
Type: Array of strings
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteVpcEndpointConnectionNotifications_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **unsuccessful**
Information about the notifications that could not be deleted successfully.
Type: Array of [UnsuccessfulItem](API_UnsuccessfulItem.md) objects

## Errors
<a name="API_DeleteVpcEndpointConnectionNotifications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteVpcEndpointConnectionNotifications_Examples"></a>

### Example
<a name="API_DeleteVpcEndpointConnectionNotifications_Example_1"></a>

This example deletes connection notification `vpce-nfn-04bcb952bc8af7123`.

#### Sample Request
<a name="API_DeleteVpcEndpointConnectionNotifications_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteVpcEndpointConnectionNotifications
&ConnectionNotificationId.1=vpce-nfn-04bcb952bc8af7123
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteVpcEndpointConnectionNotifications_Example_1_Response"></a>

```
<DeleteVpcEndpointConnectionNotificationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>2bf45d2e-a871-4375-9a93-f4188example</requestId>
    <unsuccessful/>
</DeleteVpcEndpointConnectionNotificationsResponse>
```

## See Also
<a name="API_DeleteVpcEndpointConnectionNotifications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteVpcEndpointConnectionNotifications)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
