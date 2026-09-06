---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachInternetGateway.html
---

# AttachInternetGateway
<a name="API_AttachInternetGateway"></a>

Attaches an internet gateway or a virtual private gateway to a VPC, enabling connectivity between the internet and the VPC. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_AttachInternetGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InternetGatewayId**
The ID of the internet gateway.
Type: String
Required: Yes

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_AttachInternetGateway_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_AttachInternetGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AttachInternetGateway_Examples"></a>

### Example
<a name="API_AttachInternetGateway_Example_1"></a>

This example attaches the internet gateway with the ID `igw-eaad4883` to the VPC with the ID `vpc-11ad4878`.

#### Sample Request
<a name="API_AttachInternetGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AttachInternetGateway
&InternetGatewayId=igw-eaad4883
&VpcId=vpc-11ad4878
&AUTHPARAMS
```

#### Sample Response
<a name="API_AttachInternetGateway_Example_1_Response"></a>

```
<AttachInternetGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</AttachInternetGatewayResponse>
```

## See Also
<a name="API_AttachInternetGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AttachInternetGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AttachInternetGateway)
