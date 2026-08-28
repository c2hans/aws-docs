---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointPayerResponsibility.html
---

# ModifyVpcEndpointPayerResponsibility
<a name="API_ModifyVpcEndpointPayerResponsibility"></a>

Modifies the billing account for VPC endpoint usage/charges.

## Request Parameters
<a name="API_ModifyVpcEndpointPayerResponsibility_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PayerResponsibility**
The AWS account to which the usage of VPC endpoint is charged.
Type: String
Valid Values: `vpc-endpoint-account | vpc-endpoint-service-account`
Required: Yes

 **Scope**
The scope of usage/charges for which the billing account is being modified.
Type: String
Valid Values: `vpc-endpoint-charges`
Required: Yes

 **ServiceId**
The ID of the VPC endpoint service.
Type: String
Required: No

 **VpcEndpointId**
The ID of the VPC endpoint.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcEndpointPayerResponsibility_ResponseElements"></a>

The following elements are returned by the service.

 **payerResponsibilitySet**
The payer responsibility settings for the VPC endpoint.
Type: Array of [PayerResponsibilityEntry](API_PayerResponsibilityEntry.md) objects

 **requestId**
The ID of the request.
Type: String

 **vpcEndpointId**
The ID of the VPC endpoint.
Type: String

## Errors
<a name="API_ModifyVpcEndpointPayerResponsibility_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcEndpointPayerResponsibility_Examples"></a>

### Example
<a name="API_ModifyVpcEndpointPayerResponsibility_Example_1"></a>

This example sets the billing account for endpoint `vpce-0c1308d7312217123` to the service owner account for endpoint service `vpce-svc-abc5ebb7d9579a2b3`.

#### Sample Request
<a name="API_ModifyVpcEndpointPayerResponsibility_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcEndpointPayerResponsibility
&ServiceId=vpce-svc-abc5ebb7d9579a2b3
&VpcEndpointId=vpce-0c1308d7312217123
&PayerResponsibility=vpc-endpoint-service-account
&Scope=vpc-endpoint-charges
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcEndpointPayerResponsibility_Example_1_Response"></a>

```
<ModifyVpcEndpointPayerResponsibilityResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>986a2264-8a40-4da8-8f11-e8aaexample</requestId>
    <vpcEndpointId>vpce-0c1308d7312217123</vpcEndpointId>
    <payerResponsibilitySet>
        <item>
            <scope>vpc-endpoint-charges</scope>
            <payerResponsibilityType>vpc-endpoint-service-account</payerResponsibilityType>
        </item>
    </payerResponsibilitySet>
</ModifyVpcEndpointPayerResponsibilityResponse>
```

## See Also
<a name="API_ModifyVpcEndpointPayerResponsibility_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcEndpointPayerResponsibility)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
