---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamResourceCidr.html
---

# ModifyIpamResourceCidr
<a name="API_ModifyIpamResourceCidr"></a>

Modify a resource CIDR. You can use this action to transfer resource CIDRs between scopes and ignore resource CIDRs that you do not want to manage. If set to false, the resource will not be tracked for overlap, it cannot be auto-imported into a pool, and it will be removed from any pool it has an allocation in.

For more information, see [Move resource CIDRs between scopes](https://docs.aws.amazon.com/vpc/latest/ipam/move-resource-ipam.html) and [Change the monitoring state of resource CIDRs](https://docs.aws.amazon.com/vpc/latest/ipam/change-monitoring-state-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_ModifyIpamResourceCidr_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CurrentIpamScopeId**
The ID of the current scope that the resource CIDR is in.
Type: String
Required: Yes

 **DestinationIpamScopeId**
The ID of the scope you want to transfer the resource CIDR to.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Monitored**
Determines if the resource is monitored by IPAM. If a resource is monitored, the resource is discovered by IPAM and you can view details about the resource’s CIDR.
Type: Boolean
Required: Yes

 **ResourceCidr**
The CIDR of the resource you want to modify.
Type: String
Required: Yes

 **ResourceId**
The ID of the resource you want to modify.
Type: String
Required: Yes

 **ResourceRegion**
The AWS Region of the resource you want to modify.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyIpamResourceCidr_ResponseElements"></a>

The following elements are returned by the service.

 **ipamResourceCidr**
The CIDR of the resource.
Type: [IpamResourceCidr](API_IpamResourceCidr.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpamResourceCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpamResourceCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpamResourceCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpamResourceCidr)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
