---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TargetNetwork.html
---

# TargetNetwork
<a name="API_TargetNetwork"></a>

Describes a target network associated with a Client VPN endpoint.

## Contents
<a name="API_TargetNetwork_Contents"></a>

 ** associationId **
The ID of the association.
Type: String
Required: No

 ** AvailabilityZoneIdSet.N **
The Availability Zone IDs for the target network association, if the Client VPN endpoint uses a Transit Gateway.
Type: Array of strings
Required: No

 ** AvailabilityZoneSet.N **
The Availability Zone names for the target network association, if the Client VPN endpoint uses a Transit Gateway.
Type: Array of strings
Required: No

 ** clientVpnEndpointId **
The ID of the Client VPN endpoint with which the target network is associated.
Type: String
Required: No

 ** SecurityGroups.N **
The IDs of the security groups applied to the target network association.
Type: Array of strings
Required: No

 ** status **
The current state of the target network association.
Type: [AssociationStatus](API_AssociationStatus.md) object
Required: No

 ** targetNetworkId **
The ID of the subnet specified as the target network.
Type: String
Required: No

 ** vpcId **
The ID of the VPC in which the target network (subnet) is located.
Type: String
Required: No

## See Also
<a name="API_TargetNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TargetNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TargetNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TargetNetwork)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
