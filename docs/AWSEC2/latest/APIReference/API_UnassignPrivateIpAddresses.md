---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html
---

# UnassignPrivateIpAddresses
<a name="API_UnassignPrivateIpAddresses"></a>

Unassigns the specified secondary private IP addresses or IPv4 Prefix Delegation prefixes from a network interface.

## Request Parameters
<a name="API_UnassignPrivateIpAddresses_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Ipv4Prefix.N**
The IPv4 prefixes to unassign from the network interface.
Type: Array of strings
Required: No

 **NetworkInterfaceId**
The ID of the network interface.
Type: String
Required: Yes

 **PrivateIpAddress.N**
The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to unassign more than one IP address.
Type: Array of strings
Required: No

## Response Elements
<a name="API_UnassignPrivateIpAddresses_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_UnassignPrivateIpAddresses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UnassignPrivateIpAddresses_Examples"></a>

### Example
<a name="API_UnassignPrivateIpAddresses_Example_1"></a>

The following example unassigns two secondary private IP addresses from the specified network interface.

#### Sample Request
<a name="API_UnassignPrivateIpAddresses_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=UnassignPrivateIpAddresses
&NetworkInterfaceId=eni-197d9972
&PrivateIpAddress.1=10.0.2.60
&PrivateIpAddress.2=10.0.2.65
&AUTHPARAMS
```

#### Sample Response
<a name="API_UnassignPrivateIpAddresses_Example_1_Response"></a>

```
<UnassignPrivateIpAddresses xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</UnassignPrivateIpAddresses>
```

## See Also
<a name="API_UnassignPrivateIpAddresses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/UnassignPrivateIpAddresses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/UnassignPrivateIpAddresses)
