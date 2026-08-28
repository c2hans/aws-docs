---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateDhcpOptions.html
---

# AssociateDhcpOptions
<a name="API_AssociateDhcpOptions"></a>

Associates a set of DHCP options (that you've previously created) with the specified VPC, or associates no DHCP options with the VPC.

After you associate the options with the VPC, any existing instances and all new instances that you launch in that VPC use the options. You don't need to restart or relaunch the instances. They automatically pick up the changes within a few hours, depending on how frequently the instance renews its DHCP lease. You can explicitly renew the lease using the operating system on the instance.

For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_AssociateDhcpOptions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DhcpOptionsId**
The ID of the DHCP options set, or `default` to associate no DHCP options with the VPC.
Type: String
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
<a name="API_AssociateDhcpOptions_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_AssociateDhcpOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateDhcpOptions_Examples"></a>

### Example 1
<a name="API_AssociateDhcpOptions_Example_1"></a>

This example associates the DHCP options with the ID `dopt-7a8b9c2d` with the VPC with the ID `vpc-1a2b3c4d`.

#### Sample Request
<a name="API_AssociateDhcpOptions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateDhcpOptions
&DhcpOptionsId=dopt-7a8b9c2d
&VpcId=vpc-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateDhcpOptions_Example_1_Response"></a>

```
<AssociateDhcpOptionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <return>true</return>
</AssociateDhcpOptionsResponse>
```

### Example 2
<a name="API_AssociateDhcpOptions_Example_2"></a>

This example changes the VPC with the ID `vpc-1a2b3c4d` to have no associated DHCP options set.

#### Sample Request
<a name="API_AssociateDhcpOptions_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateDhcpOptions
&DhcpOptionsId=default
&VpcId=vpc-1a2b3c4d
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateDhcpOptions_Example_2_Response"></a>

```
<AssociateDhcpOptionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
   <return>true</return>
</AssociateDhcpOptionsResponse>
```

## See Also
<a name="API_AssociateDhcpOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateDhcpOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateDhcpOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
