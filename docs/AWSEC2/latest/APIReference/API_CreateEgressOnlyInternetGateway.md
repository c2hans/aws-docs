---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateEgressOnlyInternetGateway.html
---

# CreateEgressOnlyInternetGateway
<a name="API_CreateEgressOnlyInternetGateway"></a>

[IPv6 only] Creates an egress-only internet gateway for your VPC. An egress-only internet gateway is used to enable outbound communication over IPv6 from instances in your VPC to the internet, and prevents hosts outside of your VPC from initiating an IPv6 connection with your instance.

## Request Parameters
<a name="API_CreateEgressOnlyInternetGateway_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to assign to the egress-only internet gateway.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC for which to create the egress-only internet gateway.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateEgressOnlyInternetGateway_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String

 **egressOnlyInternetGateway**
Information about the egress-only internet gateway.
Type: [EgressOnlyInternetGateway](API_EgressOnlyInternetGateway.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateEgressOnlyInternetGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateEgressOnlyInternetGateway_Examples"></a>

### Example
<a name="API_CreateEgressOnlyInternetGateway_Example_1"></a>

This example creates an egress-only internet gateway in VPC vpc-1a2b3c4d.

#### Sample Request
<a name="API_CreateEgressOnlyInternetGateway_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateEgressOnlyInternetGateway
&VpcId=vpc-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateEgressOnlyInternetGateway_Example_1_Response"></a>

```
<CreateEgressOnlyInternetGatewayResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>c617595f-6c29-4a00-a941-example</requestId>
    <egressOnlyInternetGateway>
        <attachmentSet>
            <item>
                <state>attached</state>
                <vpcId>vpc-1a2b3c4d</vpcId>
            </item>
        </attachmentSet>
        <egressOnlyInternetGatewayId>eigw-01eadbd45ecd7943f</egressOnlyInternetGatewayId>
    </egressOnlyInternetGateway>
</CreateEgressOnlyInternetGatewayResponse>
```

## See Also
<a name="API_CreateEgressOnlyInternetGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateEgressOnlyInternetGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateEgressOnlyInternetGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
