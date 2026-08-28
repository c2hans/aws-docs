---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamScope.html
---

# IpamScope
<a name="API_IpamScope"></a>

In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.

For more information, see [How IPAM works](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Contents
<a name="API_IpamScope_Contents"></a>

 ** description **
The description of the scope.
Type: String
Required: No

 ** externalAuthorityConfiguration **
The external authority configuration for this IPAM scope, if configured.
The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.
In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to AWS while using Amazon VPC IPAM to manage subnets within those ranges.
Type: [IpamScopeExternalAuthorityConfiguration](API_IpamScopeExternalAuthorityConfiguration.md) object
Required: No

 ** ipamArn **
The ARN of the IPAM.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamRegion **
The AWS Region of the IPAM scope.
Type: String
Required: No

 ** ipamScopeArn **
The Amazon Resource Name (ARN) of the scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1283.
Required: No

 ** ipamScopeId **
The ID of the scope.
Type: String
Required: No

 ** ipamScopeType **
The type of the scope.
Type: String
Valid Values: `public | private`
Required: No

 ** isDefault **
Defines if the scope is the default scope or not.
Type: Boolean
Required: No

 ** ownerId **
The AWS account ID of the owner of the scope.
Type: String
Required: No

 ** poolCount **
The number of pools in the scope.
Type: Integer
Required: No

 ** state **
The state of the IPAM scope.
Type: String
Valid Values: `create-in-progress | create-complete | create-failed | modify-in-progress | modify-complete | modify-failed | delete-in-progress | delete-complete | delete-failed | isolate-in-progress | isolate-complete | restore-in-progress`
Required: No

 ** TagSet.N **
The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_IpamScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamScope)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
