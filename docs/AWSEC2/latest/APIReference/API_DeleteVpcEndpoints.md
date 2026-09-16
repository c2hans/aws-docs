---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpoints.html
---

# DeleteVpcEndpoints
<a name="API_DeleteVpcEndpoints"></a>

Deletes the specified VPC endpoints.

When you delete a gateway endpoint, we delete the endpoint routes in the route tables for the endpoint.

When you delete a Gateway Load Balancer endpoint, we delete its endpoint network interfaces. You can only delete Gateway Load Balancer endpoints when the routes that are associated with the endpoint are deleted.

When you delete an interface endpoint, we delete its endpoint network interfaces.

## Request Parameters
<a name="API_DeleteVpcEndpoints_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpcEndpointId.N**
The IDs of the VPC endpoints.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_DeleteVpcEndpoints_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **unsuccessful**
Information about the VPC endpoints that were not successfully deleted.
Type: Array of [UnsuccessfulItem](API_UnsuccessfulItem.md) objects

## Errors
<a name="API_DeleteVpcEndpoints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteVpcEndpoints_Examples"></a>

### Example
<a name="API_DeleteVpcEndpoints_Example_1"></a>

This example deletes endpoint `vpce-aa22bb33`.

#### Sample Request
<a name="API_DeleteVpcEndpoints_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteVpcEndpoints
&VpcEndpointId.1=vpce-aa22bb33
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteVpcEndpoints_Example_1_Response"></a>

```
<DeleteVpcEndpointsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <unsuccessful/>
    <requestId>b59c2643-789a-4bf7-aac4-example</requestId>
</DeleteVpcEndpointsResponse>
```

## See Also
<a name="API_DeleteVpcEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteVpcEndpoints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteVpcEndpoints)
