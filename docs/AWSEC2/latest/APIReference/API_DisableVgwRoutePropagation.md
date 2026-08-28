---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisableVgwRoutePropagation.html
---

# DisableVgwRoutePropagation
<a name="API_DisableVgwRoutePropagation"></a>

Disables a virtual private gateway (VGW) from propagating routes to a specified route table of a VPC.

## Request Parameters
<a name="API_DisableVgwRoutePropagation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GatewayId**
The ID of the virtual private gateway.
Type: String
Required: Yes

 **RouteTableId**
The ID of the route table.
Type: String
Required: Yes

## Response Elements
<a name="API_DisableVgwRoutePropagation_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DisableVgwRoutePropagation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisableVgwRoutePropagation_Examples"></a>

### Example
<a name="API_DisableVgwRoutePropagation_Example_1"></a>

This example disables the virtual private gateway `vgw-d8e09e8a` from automatically propagating routes to the route table with ID `rtb-c98a35a0`.

#### Sample Request
<a name="API_DisableVgwRoutePropagation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisableVgwRoutePropagationResponse
&RouteTableId=rtb-c98a35a0
&GatewayId=vgw-d8e09e8a
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisableVgwRoutePropagation_Example_1_Response"></a>

```
<DisableVgwRoutePropagationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>4f35a1b2-c2c3-4093-b51f-abb9d7311990</requestId>
    <return>true</return>
</DisableVgwRoutePropagationResponse>
```

## See Also
<a name="API_DisableVgwRoutePropagation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisableVgwRoutePropagation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisableVgwRoutePropagation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
