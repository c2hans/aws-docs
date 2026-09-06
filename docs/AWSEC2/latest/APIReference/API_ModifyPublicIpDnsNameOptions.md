---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyPublicIpDnsNameOptions.html
---

# ModifyPublicIpDnsNameOptions
<a name="API_ModifyPublicIpDnsNameOptions"></a>

Modify public hostname options for a network interface. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_ModifyPublicIpDnsNameOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **HostnameType**
The public hostname type. For more information, see [EC2 instance hostnames, DNS names, and domains](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html) in the *Amazon EC2 User Guide*.
+  `public-dual-stack-dns-name`: A dual-stack public hostname for a network interface. Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.
+  `public-ipv4-dns-name`: An IPv4-enabled public hostname for a network interface. Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.
+  `public-ipv6-dns-name`: An IPv6-enabled public hostname for a network interface. Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.
Type: String
Valid Values: `public-dual-stack-dns-name | public-ipv4-dns-name | public-ipv6-dns-name`
Required: Yes

 **NetworkInterfaceId**
A network interface ID.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyPublicIpDnsNameOptions_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **successful**
Whether or not the request was successful.
Type: Boolean

## Errors
<a name="API_ModifyPublicIpDnsNameOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyPublicIpDnsNameOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyPublicIpDnsNameOptions)
