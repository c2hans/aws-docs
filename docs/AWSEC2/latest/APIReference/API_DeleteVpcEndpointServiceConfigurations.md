---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpcEndpointServiceConfigurations.html
---

# DeleteVpcEndpointServiceConfigurations
<a name="API_DeleteVpcEndpointServiceConfigurations"></a>

Deletes the specified VPC endpoint service configurations. Before you can delete an endpoint service configuration, you must reject any `Available` or `PendingAcceptance` interface endpoint connections that are attached to the service.

## Request Parameters
<a name="API_DeleteVpcEndpointServiceConfigurations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **ServiceId.N**
The IDs of the services.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_DeleteVpcEndpointServiceConfigurations_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **unsuccessful**
Information about the service configurations that were not deleted, if applicable.
Type: Array of [UnsuccessfulItem](API_UnsuccessfulItem.md) objects

## Errors
<a name="API_DeleteVpcEndpointServiceConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteVpcEndpointServiceConfigurations_Examples"></a>

### Example
<a name="API_DeleteVpcEndpointServiceConfigurations_Example_1"></a>

This example deletes your VPC endpoint service configuration `vpce-svc-03d5ebb7d9579a2b3`.

#### Sample Request
<a name="API_DeleteVpcEndpointServiceConfigurations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteVpcEndpointServiceConfigurations
ServiceId.1=vpce-svc-03d5ebb7d9579a2b3
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteVpcEndpointServiceConfigurations_Example_1_Response"></a>

```
<DeleteVpcEndpointServiceConfigurationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>12345d2e-a871-4375-9a93-f4188example</requestId>
    <unsuccessful/>
</DeleteVpcEndpointServiceConfigurations>
```

## See Also
<a name="API_DeleteVpcEndpointServiceConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteVpcEndpointServiceConfigurations)
