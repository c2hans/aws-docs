---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPrefixListResolverTarget.html
---

# IpamPrefixListResolverTarget
<a name="API_IpamPrefixListResolverTarget"></a>

Describes an IPAM prefix list resolver target.

An IPAM prefix list resolver target is an association between a specific customer-managed prefix list and an IPAM prefix list resolver. The target enables the resolver to synchronize CIDRs selected by its rules into the specified prefix list, which can then be referenced in AWS resources.

## Contents
<a name="API_IpamPrefixListResolverTarget_Contents"></a>

 ** desiredVersion **
The desired version of the prefix list that this target should synchronize with.
Type: Long
Required: No

 ** ipamPrefixListResolverId **
The ID of the IPAM prefix list resolver associated with this target.
Type: String
Required: No

 ** ipamPrefixListResolverTargetArn **
The Amazon Resource Name (ARN) of the IPAM prefix list resolver target.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamPrefixListResolverTargetId **
The ID of the IPAM prefix list resolver target.
Type: String
Required: No

 ** lastSyncedVersion **
The version of the prefix list that was last successfully synchronized by this target.
Type: Long
Required: No

 ** ownerId **
The ID of the AWS account that owns the IPAM prefix list resolver target.
Type: String
Required: No

 ** prefixListId **
The ID of the managed prefix list associated with this target.
Type: String
Required: No

 ** prefixListRegion **
The AWS Region where the prefix list associated with this target is located.
Type: String
Required: No

 ** state **
The current state of the IPAM prefix list resolver target. Valid values include `create-in-progress`, `create-complete`, `create-failed`, `modify-in-progress`, `modify-complete`, `modify-failed`, `delete-in-progress`, `delete-complete`, and `delete-failed`.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | sync-in-progress | sync-complete | sync-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** stateMessage **
A message describing the current state of the IPAM prefix list resolver target, including any error information.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the IPAM prefix list resolver target.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trackLatestVersion **
Indicates whether this target automatically tracks the latest version of the prefix list.
Type: Boolean
Required: No

## See Also
<a name="API_IpamPrefixListResolverTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPrefixListResolverTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPrefixListResolverTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPrefixListResolverTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
