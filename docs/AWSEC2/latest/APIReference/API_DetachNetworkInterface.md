---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachNetworkInterface.html
---

# DetachNetworkInterface
<a name="API_DetachNetworkInterface"></a>

Detaches a network interface from an instance.

## Request Parameters
<a name="API_DetachNetworkInterface_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AttachmentId**
The ID of the attachment.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Force**
Specifies whether to force a detachment.
+ Use the `Force` parameter only as a last resort to detach a network interface from a failed instance.
+ If you use the `Force` parameter to detach a network interface, you might not be able to attach a different network interface to the same index on the instance without first stopping and starting the instance.
+ If you force the detachment of a network interface, the [instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) might not get updated. This means that the attributes associated with the detached network interface might still be visible. The instance metadata will get updated when you stop and start the instance.
Type: Boolean
Required: No

## Response Elements
<a name="API_DetachNetworkInterface_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DetachNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DetachNetworkInterface_Examples"></a>

### Example
<a name="API_DetachNetworkInterface_Example_1"></a>

This example detaches the specified elastic network interface (ENI).

#### Sample Request
<a name="API_DetachNetworkInterface_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DetachNetworkInterface
&AttachmentId=eni-attach-d94b09b0
&AUTHPARAMS
```

#### Sample Response
<a name="API_DetachNetworkInterface_Example_1_Response"></a>

```
<DetachNetworkInterfaceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ce540707-0635-46bc-97da-33a8a362a0e8</requestId>
    <return>true</return>
</DetachNetworkInterfaceResponse>
```

## See Also
<a name="API_DetachNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DetachNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DetachNetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
