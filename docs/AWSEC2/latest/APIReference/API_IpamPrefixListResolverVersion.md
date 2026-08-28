---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamPrefixListResolverVersion.html
---

# IpamPrefixListResolverVersion
<a name="API_IpamPrefixListResolverVersion"></a>

Describes a version of an IPAM prefix list resolver.

Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.

 **Version example:**

 **Initial State (Version 1)**

Production environment:
+ vpc-prod-web (10.1.0.0/16) - tagged env=prod
+ vpc-prod-db (10.2.0.0/16) - tagged env=prod

Resolver rule: Include all VPCs tagged env=prod

 **Version 1 CIDRs:** 10.1.0.0/16, 10.2.0.0/16

 **Infrastructure Change (Version 2)**

New VPC added:
+ vpc-prod-api (10.3.0.0/16) - tagged env=prod

IPAM automatically detects the change and creates a new version.

 **Version 2 CIDRs:** 10.1.0.0/16, 10.2.0.0/16, 10.3.0.0/16

## Contents
<a name="API_IpamPrefixListResolverVersion_Contents"></a>

 ** version **
The version number of the IPAM prefix list resolver.
Each version is a snapshot of what CIDRs matched your rules at that moment in time. The version number increments every time the CIDR list changes due to infrastructure changes.
Type: Long
Required: No

## See Also
<a name="API_IpamPrefixListResolverVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamPrefixListResolverVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamPrefixListResolverVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamPrefixListResolverVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
