---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcAttribute.html
---

# DescribeVpcAttribute
<a name="API_DescribeVpcAttribute"></a>

Describes the specified attribute of the specified VPC. You can specify only one attribute at a time.

## Request Parameters
<a name="API_DescribeVpcAttribute_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Attribute**
The VPC attribute.
Type: String
Valid Values: `enableDnsSupport | enableDnsHostnames | enableNetworkAddressUsageMetrics`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_DescribeVpcAttribute_ResponseElements"></a>

The following elements are returned by the service.

 **enableDnsHostnames**
Indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is `true`, instances in the VPC get DNS hostnames; otherwise, they do not.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **enableDnsSupport**
Indicates whether DNS resolution is enabled for the VPC. If this attribute is `true`, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **enableNetworkAddressUsageMetrics**
Indicates whether Network Address Usage metrics are enabled for your VPC.
Type: [AttributeBooleanValue](API_AttributeBooleanValue.md) object

 **requestId**
The ID of the request.
Type: String

 **vpcId**
The ID of the VPC.
Type: String

## Errors
<a name="API_DescribeVpcAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeVpcAttribute_Examples"></a>

### Example 1
<a name="API_DescribeVpcAttribute_Example_1"></a>

This example describes the `enableDnsSupport` attribute of the specified VPC. The sample response indicates that DNS resolution is supported.

#### Sample Request
<a name="API_DescribeVpcAttribute_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcAttribute
&VpcId=vpc-1a2b3c4d
&Attribute=enableDnsSupport
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcAttribute_Example_1_Response"></a>

```
<DescribeVpcAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <vpcId>vpc-1a2b3c4d</vpcId>
  <enableDnsSupport>
    <value>true</value>
  </enableDnsSupport>
</DescribeVpcAttributeResponse>
```

### Example 2
<a name="API_DescribeVpcAttribute_Example_2"></a>

This request describes the `enableDnsHostnames` attribute of the specified VPC. The sample response indicates that DNS hostnames are supported.

#### Sample Request
<a name="API_DescribeVpcAttribute_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeVpcAttribute
&VpcId=vpc-1a2b3c4d
&Attribute=enableDnsHostnames
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeVpcAttribute_Example_2_Response"></a>

```
<DescribeVpcAttributeResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
  <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
  <vpcId>vpc-1a2b3c4d</vpcId>
   <enableDnsHostnames>
    <value>true</value>
   </enableDnsHostnames>
</DescribeVpcAttributeResponse>
```

## See Also
<a name="API_DescribeVpcAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcAttribute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
