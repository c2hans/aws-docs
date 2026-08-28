---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_VpcPeeringAuthorization.html
---

# VpcPeeringAuthorization
<a name="API_VpcPeeringAuthorization"></a>

Represents an authorization for a VPC peering connection between the VPC for an Amazon GameLift Servers fleet and another VPC on an account you have access to. This authorization must exist and be valid for the peering connection to be established. Authorizations are valid for 24 hours after they are issued.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_VpcPeeringAuthorization_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreationTime **   <a name="gameliftservers-Type-VpcPeeringAuthorization-CreationTime"></a>
Time stamp indicating when this authorization was issued. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** ExpirationTime **   <a name="gameliftservers-Type-VpcPeeringAuthorization-ExpirationTime"></a>
Time stamp indicating when this authorization expires (24 hours after issuance). Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"`).
Type: Timestamp
Required: No

 ** GameLiftAwsAccountId **   <a name="gameliftservers-Type-VpcPeeringAuthorization-GameLiftAwsAccountId"></a>
A unique identifier for the AWS account that you use to manage your Amazon GameLift Servers fleet. You can find your Account ID in the AWS Management Console under account settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PeerVpcAwsAccountId **   <a name="gameliftservers-Type-VpcPeeringAuthorization-PeerVpcAwsAccountId"></a>
The authorization's peer VPC AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** PeerVpcId **   <a name="gameliftservers-Type-VpcPeeringAuthorization-PeerVpcId"></a>
A unique identifier for a VPC with resources to be accessed by your Amazon GameLift Servers fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the [VPC Dashboard](https://console.aws.amazon.com/vpc/) in the AWS Management Console. Learn more about VPC peering in [VPC Peering with Amazon GameLift Servers Fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_VpcPeeringAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/VpcPeeringAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/VpcPeeringAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/VpcPeeringAuthorization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
