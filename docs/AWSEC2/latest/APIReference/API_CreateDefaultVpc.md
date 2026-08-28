---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultVpc.html
---

# CreateDefaultVpc
<a name="API_CreateDefaultVpc"></a>

Creates a default VPC with a size `/16` IPv4 CIDR block and a default subnet in each Availability Zone. For more information about the components of a default VPC, see [Default VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) in the *Amazon VPC User Guide*. You cannot specify the components of the default VPC yourself.

If you deleted your previous default VPC, you can create a default VPC. You cannot have more than one default VPC per Region.

## Request Parameters
<a name="API_CreateDefaultVpc_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_CreateDefaultVpc_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpc**
Information about the VPC.
Type: [Vpc](API_Vpc.md) object

## Errors
<a name="API_CreateDefaultVpc_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateDefaultVpc_Examples"></a>

### Example
<a name="API_CreateDefaultVpc_Example_1"></a>

This example creates a default VPC.

#### Sample Request
<a name="API_CreateDefaultVpc_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateDefaultVpc
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateDefaultVpc_Example_1_Response"></a>

```
<CreateDefaultVpcResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>056298f3-5f3e-48fb-9221-7c0example</requestId>
    <vpc>
        <cidrBlock>172.31.0.0/16</cidrBlock>
        <dhcpOptionsId>dopt-61079b07</dhcpOptionsId>
        <instanceTenancy>default</instanceTenancy>
        <ipv6CidrBlockAssociationSet/>
        <isDefault>true</isDefault>
        <state>pending</state>
        <tagSet/>
        <vpcId>vpc-3f139646</vpcId>
    </vpc>
</CreateDefaultVpcResponse>
```

## See Also
<a name="API_CreateDefaultVpc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateDefaultVpc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateDefaultVpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
