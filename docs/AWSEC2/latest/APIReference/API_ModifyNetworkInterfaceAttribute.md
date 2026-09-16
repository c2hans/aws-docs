---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyNetworkInterfaceAttribute.html
---

# ModifyNetworkInterfaceAttribute
<a name="API_ModifyNetworkInterfaceAttribute"></a>

Modifies the specified network interface attribute. You can specify only one attribute at a time. You can use this action to attach and detach security groups from an existing EC2 instance.

## Request Parameters
<a name="API_ModifyNetworkInterfaceAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociatedSubnetId.N**
A list of subnet IDs to associate with the network interface.
Type: Array of strings
Required: No

 **AssociatePublicIpAddress**
Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network interface but will only apply to the primary network interface (eth0).
Type: Boolean
Required: No

 **Attachment**
Information about the interface attachment. If modifying the `delete on termination` attribute, you must specify the ID of the interface attachment.
Type: [NetworkInterfaceAttachmentChanges](API_NetworkInterfaceAttachmentChanges.md) object
Required: No

 **ConnectionTrackingSpecification**
A connection tracking specification.
Type: [ConnectionTrackingSpecificationRequest](API_ConnectionTrackingSpecificationRequest.md) object
Required: No

 **Description**
A description for the network interface.
Type: [AttributeValue](API_AttributeValue.md) object
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EnablePrimaryIpv6**
If you’re modifying a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 IP address. A primary IPv6 address is an IPv6 GUA address associated with an ENI that you have enabled to use a primary IPv6 address. Use this option if the instance that this ENI will be attached to relies on its IPv6 address not changing. AWS will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.
Type: Boolean
Required: No

 **EnaSrdSpecification**
Updates the ENA Express configuration for the network interface that’s attached to the instance.
Type: [EnaSrdSpecification](API_EnaSrdSpecification.md) object
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

 **SecurityGroupId.N**
Changes the security groups for the network interface. The new set of groups you specify replaces the current set. You must specify at least one group, even if it's just the default security group in the VPC. You must specify the ID of the security group, not the name.
Type: Array of strings
Required: No

 **SourceDestCheck**
Enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. If the value is `true`, source/destination checks are enabled; otherwise, they are disabled. The default value is `true`. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

## Response Elements
<a name="API_ModifyNetworkInterfaceAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyNetworkInterfaceAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyNetworkInterfaceAttribute_Examples"></a>

### Example
<a name="API_ModifyNetworkInterfaceAttribute_Example_1"></a>

This example sets source/destination checking to `false` for the specified network interface.

#### Sample Request
<a name="API_ModifyNetworkInterfaceAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyNetworkInterfaceAttribute
&NetworkInterfaceId=eni-ffda3197
&SourceDestCheck.Value=false
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyNetworkInterfaceAttribute_Example_1_Response"></a>

```
<ModifyNetworkInterfaceAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>657a4623-5620-4232-b03b-427e852d71cf</requestId>
    <return>true</return>
</ModifyNetworkInterfaceAttributeResponse>
```

## See Also
<a name="API_ModifyNetworkInterfaceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyNetworkInterfaceAttribute)
