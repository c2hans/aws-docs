---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html
---

# DeleteRoute
<a name="API_DeleteRoute"></a>

Deletes the specified route from the specified route table.

## Request Parameters
<a name="API_DeleteRoute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DestinationCidrBlock**
The IPv4 CIDR range for the route. The value you specify must match the CIDR for the route exactly.
Type: String
Required: No

 **DestinationIpv6CidrBlock**
The IPv6 CIDR range for the route. The value you specify must match the CIDR for the route exactly.
Type: String
Required: No

 **DestinationPrefixListId**
The ID of the prefix list for the route.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RouteTableId**
The ID of the route table.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteRoute_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteRoute_Examples"></a>

### Example 1
<a name="API_DeleteRoute_Example_1"></a>

This example deletes the route with destination IPv4 CIDR `172.16.1.0/24` from the specified route table.

#### Sample Request
<a name="API_DeleteRoute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteRoute
&RouteTableId=rtb-1122334455667788a
&DestinationCidrBlock=172.16.1.0/24
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteRoute_Example_1_Response"></a>

```
<DeleteRouteResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</DeleteRouteResponse>
```

### Example 2
<a name="API_DeleteRoute_Example_2"></a>

This example deletes the route with destination IPv6 CIDR `::/0` from the specified route table.

#### Sample Request
<a name="API_DeleteRoute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteRoute
&RouteTableId=rtb-1122334455667788a
&DestinationIpv6CidrBlock=::/0
&AUTHPARAMS
```

## See Also
<a name="API_DeleteRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteRoute)
