---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVpcClassicLinkDnsSupport.html
---

# DisableVpcClassicLinkDnsSupport
<a name="API_DisableVpcClassicLinkDnsSupport"></a>

**Note**
This action is deprecated.

Disables ClassicLink DNS support for a VPC. If disabled, DNS hostnames resolve to public IP addresses when addressed between a linked EC2-Classic instance and instances in the VPC to which it's linked.

You must specify a VPC ID in the request.

## Request Parameters
<a name="API_DisableVpcClassicLinkDnsSupport_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **VpcId**
The ID of the VPC.
Type: String
Required: No

## Response Elements
<a name="API_DisableVpcClassicLinkDnsSupport_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_DisableVpcClassicLinkDnsSupport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisableVpcClassicLinkDnsSupport_Examples"></a>

### Example
<a name="API_DisableVpcClassicLinkDnsSupport_Example_1"></a>

This example disables ClassicLink DNS support for `vpc-8888888`.

#### Sample Request
<a name="API_DisableVpcClassicLinkDnsSupport_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisableVpcClassicLinkDnsSupport
&VpcId=vpc-8888888
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableVpcClassicLinkDnsSupport_Example_1_Response"></a>

```
<DisableVpcClassicLinkDnsSupportResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
  <return>true</return>
</DisableVpcClassicLinkDnsSupportResponse>
```

## See Also
<a name="API_DisableVpcClassicLinkDnsSupport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableVpcClassicLinkDnsSupport)
