---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteIpam.html
---

# DeleteIpam
<a name="API_DeleteIpam"></a>

Delete an IPAM. Deleting an IPAM removes all monitored data associated with the IPAM including the historical data for CIDRs.

For more information, see [Delete an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/delete-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_DeleteIpam_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cascade**
Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes. You cannot delete the IPAM with this option if there is a pool in your public scope. If you use this option, IPAM does the following:
+ Deallocates any CIDRs allocated to VPC resources (such as VPCs) in pools in private scopes.
**Note**
No VPC resources are deleted as a result of enabling this option. The CIDR associated with the resource will no longer be allocated from an IPAM pool, but the CIDR itself will remain unchanged.
+ Deprovisions all IPv4 CIDRs provisioned to IPAM pools in private scopes.
+ Deletes all IPAM pools in private scopes.
+ Deletes all non-default private scopes in the IPAM.
+ Deletes the default public and private scopes and the IPAM.
Type: Boolean
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamId**
The ID of the IPAM to delete.
Type: String
Required: Yes

## Response Elements
<a name="API_DeleteIpam_ResponseElements"></a>

The following elements are returned by the service.

 **ipam**
Information about the results of the deletion.
Type: [Ipam](API_Ipam.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DeleteIpam_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteIpam_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteIpam)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteIpam)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
