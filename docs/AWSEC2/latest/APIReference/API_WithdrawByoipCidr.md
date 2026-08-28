---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_WithdrawByoipCidr.html
---

# WithdrawByoipCidr
<a name="API_WithdrawByoipCidr"></a>

Stops advertising an address range that is provisioned as an address pool.

You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.

It can take a few minutes before traffic to the specified addresses stops routing to AWS because of BGP propagation delays.

## Request Parameters
<a name="API_WithdrawByoipCidr_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cidr**
The address range, in CIDR notation.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_WithdrawByoipCidr_ResponseElements"></a>

The following elements are returned by the service.

 **byoipCidr**
Information about the address pool.
Type: [ByoipCidr](API_ByoipCidr.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_WithdrawByoipCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_WithdrawByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/WithdrawByoipCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/WithdrawByoipCidr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
