---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AnalysisSecurityGroupRule.html
---

# AnalysisSecurityGroupRule
<a name="API_AnalysisSecurityGroupRule"></a>

Describes a security group rule.

## Contents
<a name="API_AnalysisSecurityGroupRule_Contents"></a>

 ** cidr **
The IPv4 address range, in CIDR notation.
Type: String
Required: No

 ** direction **
The direction. The following are the possible values:
+ egress
+ ingress
Type: String
Required: No

 ** portRange **
The port range.
Type: [PortRange](API_PortRange.md) object
Required: No

 ** prefixListId **
The prefix list ID.
Type: String
Required: No

 ** protocol **
The protocol name.
Type: String
Required: No

 ** securityGroupId **
The security group ID.
Type: String
Required: No

## See Also
<a name="API_AnalysisSecurityGroupRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AnalysisSecurityGroupRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AnalysisSecurityGroupRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AnalysisSecurityGroupRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
