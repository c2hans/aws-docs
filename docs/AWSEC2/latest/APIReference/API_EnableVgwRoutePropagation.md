---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.html
---

# EnableVgwRoutePropagation
<a name="API_EnableVgwRoutePropagation"></a>

Enables a virtual private gateway (VGW) to propagate routes to the specified route table of a VPC.

## Request Parameters
<a name="API_EnableVgwRoutePropagation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GatewayId**
The ID of the virtual private gateway that is attached to a VPC. The virtual private gateway must be attached to the same VPC that the routing tables are associated with.
Type: String
Required: Yes

 **RouteTableId**
The ID of the route table. The routing table must be associated with the same VPC that the virtual private gateway is attached to.
Type: String
Required: Yes

## Response Elements
<a name="API_EnableVgwRoutePropagation_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_EnableVgwRoutePropagation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_EnableVgwRoutePropagation_Examples"></a>

### Example
<a name="API_EnableVgwRoutePropagation_Example_1"></a>

This example enables the specified virtual private gateway to propagate routes automatically to the route table with the ID `rtb-c98a35a0`.

#### Sample Request
<a name="API_EnableVgwRoutePropagation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=EnableVgwRoutePropagation
&RouteTableID=rtb-c98a35a0
&GatewayId=vgw-d8e09e8a
&AUTHPARAMS
```

#### Sample Response
<a name="API_EnableVgwRoutePropagation_Example_1_Response"></a>

```
<EnableVgwRoutePropagation xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4f35a1b2-c2c3-4093-b51f-abb9d7311990</requestId>
    <return>true</return>
</EnableVgwRoutePropagation>
```

## See Also
<a name="API_EnableVgwRoutePropagation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableVgwRoutePropagation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableVgwRoutePropagation)
