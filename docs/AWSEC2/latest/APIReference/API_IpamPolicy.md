---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPolicy.html
---

# IpamPolicy
<a name="API_IpamPolicy"></a>

Information about an IPAM policy.

An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to AWS resources. Each rule maps an AWS service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple AWS Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual AWS account or an entity within AWS Organizations.

## Contents
<a name="API_IpamPolicy_Contents"></a>

 ** ipamId **
The ID of the IPAM this policy belongs to.
Type: String
Required: No

 ** ipamPolicyArn **
The Amazon Resource Name (ARN) of the IPAM policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamPolicyId **
The ID of the IPAM policy.
Type: String
Required: No

 ** ipamPolicyRegion **
The Region of the IPAM policy.
Type: String
Required: No

 ** ownerId **
The account ID that owns the IPAM policy.
Type: String
Required: No

 ** state **
The state of the IPAM policy.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** stateMessage **
A message about the state of the IPAM policy.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the IPAM policy.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
