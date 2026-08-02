---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachNetworkInterface.html
---

# AttachNetworkInterface
<a name="API_AttachNetworkInterface"></a>

Attaches a network interface to an instance.

## Request Parameters
<a name="API_AttachNetworkInterface_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DeviceIndex**
The index of the device for the network interface attachment.
Type: Integer
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EnaQueueCount**
The number of ENA queues to be created with the instance.
Type: Integer
Required: No

 **EnaSrdSpecification**
Configures ENA Express for the network interface that this action attaches to the instance.
Type: [EnaSrdSpecification](API_EnaSrdSpecification.md) object
Required: No

 **InstanceId**
The ID of the instance.
Type: String
Required: Yes

 **NetworkCardIndex**
The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.
Type: Integer
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

## Response Elements
<a name="API_AttachNetworkInterface_ResponseElements"></a>

The following elements are returned by the service.

 **attachmentId**
The ID of the network interface attachment.
Type: String

 **networkCardIndex**
The index of the network card.
Type: Integer

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AttachNetworkInterface_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AttachNetworkInterface_Examples"></a>

### Example
<a name="API_AttachNetworkInterface_Example_1"></a>

This example attaches the specified network interface to the specified instance.

#### Sample Request
<a name="API_AttachNetworkInterface_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AttachNetworkInterface
&DeviceIndex=1
&InstanceId=i-1234567890abcdef0
&NetworkInterfaceId=eni-ffda3197
&AUTHPARAMS
```

#### Sample Response
<a name="API_AttachNetworkInterface_Example_1_Response"></a>

```
<AttachNetworkInterfaceResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ace8cd1e-e685-4e44-90fb-92014d907212</requestId>
    <attachmentId>eni-attach-d94b09b0</attachmentId>
</AttachNetworkInterfaceResponse>
```

## See Also
<a name="API_AttachNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AttachNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AttachNetworkInterface)
