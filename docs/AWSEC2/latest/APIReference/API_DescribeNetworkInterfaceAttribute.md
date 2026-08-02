---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaceAttribute.html
---

# DescribeNetworkInterfaceAttribute
<a name="API_DescribeNetworkInterfaceAttribute"></a>

Describes a network interface attribute. You can specify only one attribute at a time.

## Request Parameters
<a name="API_DescribeNetworkInterfaceAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The attribute of the network interface. This parameter is required.
Type: String
Valid Values: `description | groupSet | sourceDestCheck | attachment | associatePublicIpAddress`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeNetworkInterfaceAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **associatePublicIpAddress**
Indicates whether to assign a public IPv4 address to a network interface. This option can be enabled for any network interface but will only apply to the primary network interface (eth0).
Type: Boolean

 **attachment**
The attachment (if any) of the network interface.
Type: [NetworkInterfaceAttachment](API_NetworkInterfaceAttachment.md) object

 **description**
The description of the network interface.
Type: [AttributeValue](API_AttributeValue.md) object

 **groupSet**
The security groups associated with the network interface.
Type: Array of [GroupIdentifier](API_GroupIdentifier.md) objects

 **networkInterfaceId**
The ID of the network interface.
Type: String

 **requestId**
The ID of the request.
Type: String

 **sourceDestCheck**
Indicates whether source/destination checking is enabled.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

## Errors
<a name="API_DescribeNetworkInterfaceAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeNetworkInterfaceAttribute_Examples"></a>

### Example
<a name="API_DescribeNetworkInterfaceAttribute_Example_1"></a>

This example describes the `sourceDestCheck` attribute of the specified network interface.

#### Sample Request
<a name="API_DescribeNetworkInterfaceAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeNetworkInterfaceAttribute
&NetworkInterfaceId=eni-686ea200
&Attribute=sourceDestCheck
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeNetworkInterfaceAttribute_Example_1_Response"></a>

```
<DescribeNetworkInterfaceAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a20c6b2-d71c-45fb-bba7-37306850544b</requestId>
  <networkInterfaceId>eni-686ea200</networkInterfaceId>
  <sourceDestCheck>
    <value>true</value>
  </sourceDestCheck>
</DescribeNetworkInterfaceAttributeResponse>
```

## See Also
<a name="API_DescribeNetworkInterfaceAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeNetworkInterfaceAttribute)
