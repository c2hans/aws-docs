---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AnalysisAclRule.html
---

# AnalysisAclRule
<a name="API_AnalysisAclRule"></a>

Describes a network access control (ACL) rule.

## Contents
<a name="API_AnalysisAclRule_Contents"></a>

 ** cidr **
The IPv4 address range, in CIDR notation.
Type: String
Required: No

 ** egress **
Indicates whether the rule is an outbound rule.
Type: Boolean
Required: No

 ** portRange **
The range of ports.
Type: [PortRange](API_PortRange.md) object
Required: No

 ** protocol **
The protocol.
Type: String
Required: No

 ** ruleAction **
Indicates whether to allow or deny traffic that matches the rule.
Type: String
Required: No

 ** ruleNumber **
The rule number.
Type: Integer
Required: No

## See Also
<a name="API_AnalysisAclRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AnalysisAclRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AnalysisAclRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AnalysisAclRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
