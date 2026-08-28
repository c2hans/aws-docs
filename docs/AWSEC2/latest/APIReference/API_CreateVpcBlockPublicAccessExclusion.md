---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpcBlockPublicAccessExclusion.html
---

# CreateVpcBlockPublicAccessExclusion
<a name="API_CreateVpcBlockPublicAccessExclusion"></a>

Create a VPC Block Public Access (BPA) exclusion. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateVpcBlockPublicAccessExclusion_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InternetGatewayExclusionMode**
The exclusion mode for internet gateway traffic.
+  `allow-bidirectional`: Allow all internet traffic to and from the excluded VPCs and subnets.
+  `allow-egress`: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.
Type: String
Valid Values: `allow-bidirectional | allow-egress`
Required: Yes

 **SubnetId**
A subnet ID.
Type: String
Required: No

 **TagSpecification.N**
 `tag` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
A VPC ID.
Type: String
Required: No

## Response Elements
<a name="API_CreateVpcBlockPublicAccessExclusion_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpcBlockPublicAccessExclusion**
Details about an exclusion.
Type: [VpcBlockPublicAccessExclusion](API_VpcBlockPublicAccessExclusion.md) object

## Errors
<a name="API_CreateVpcBlockPublicAccessExclusion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateVpcBlockPublicAccessExclusion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpcBlockPublicAccessExclusion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
