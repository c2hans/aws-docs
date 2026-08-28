---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnConcentrator.html
---

# DeleteVpnConcentrator
<a name="API_DeleteVpnConcentrator"></a>

Deletes the specified VPN concentrator.

## Request Parameters
<a name="API_DeleteVpnConcentrator_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **VpnConcentratorId**
The ID of the VPN concentrator to delete.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteVpnConcentrator_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_DeleteVpnConcentrator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteVpnConcentrator_Examples"></a>

### Example
<a name="API_DeleteVpnConcentrator_Example_1"></a>

This example deletes VPN Concentrator `vcn-0767cb7521c5c4945`.

#### Sample Request
<a name="API_DeleteVpnConcentrator_Example_1_Request"></a>

```
https://ec2.us-east-1.amazonaws.com/?Version=2016-11-15&Action=DeleteVpnConcentrator
&VpnConcentratorId=vcn-0767cb7521c5c4945
```

#### Sample Response
<a name="API_DeleteVpnConcentrator_Example_1_Response"></a>

```
<DeleteVpnConcentratorResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>2912d285-2e87-4e3b-aa4b-80772cc5913b</requestId>
    <return>true</return>
</DeleteVpnConcentratorResponse>
```

## See Also
<a name="API_DeleteVpnConcentrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteVpnConcentrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteVpnConcentrator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
