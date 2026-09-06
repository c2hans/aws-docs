---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcAttribute.html
---

# ModifyVpcAttribute
<a name="API_ModifyVpcAttribute"></a>

Modifies the specified attribute of the specified VPC.

## Request Parameters
<a name="API_ModifyVpcAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **EnableDnsHostnames**
Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not.
You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute. You can only enable DNS hostnames if you've enabled DNS support.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **EnableDnsSupport**
Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled.
You cannot modify the DNS resolution and DNS hostnames attributes in the same request. Use separate requests for each attribute.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **EnableNetworkAddressUsageMetrics**
Indicates whether Network Address Usage metrics are enabled for your VPC.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object
Required: No

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_ModifyVpcAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcAttribute_Examples"></a>

### Example
<a name="API_ModifyVpcAttribute_Example_1"></a>

This example disables support for DNS hostnames in the specified VPC.

#### Sample Request
<a name="API_ModifyVpcAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcAttribute
&VpcId=vpc-1a2b3c4d
&EnableDnsHostnames.Value=false
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcAttribute_Example_1_Response"></a>

```
<ModifyVpcAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d742de94-5f3e-4c3d-b6d4-440cexample</requestId>
    <return>true</return>
</ModifyVpcAttributeResponse>
```

## See Also
<a name="API_ModifyVpcAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcAttribute)
