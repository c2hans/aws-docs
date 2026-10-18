---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ApprovalPattern.html
---

# ApprovalPattern
<a name="API_ApprovalPattern"></a>

Tool-invocation pattern primitive used to express both an agent-requested approval and a finalized approval. The primitive is uniform across AWS and third-party tools: a tool identifier plus a map of argument pins that narrow which invocations the pattern matches.

## Contents
<a name="API_ApprovalPattern_Contents"></a>

 ** argumentPins **   <a name="devopsagent-Type-ApprovalPattern-argumentPins"></a>
Argument constraints that narrow which tool invocations the pattern matches. For AWS tools, the map must include `operation` (the IAM action, e.g. `ec2:AuthorizeSecurityGroupIngress`) and `resource\_arn` (the resource ARN or ARN glob); additional narrowing arguments go in further pin keys. The same `{tool, argumentPins}` shape is used uniformly for AWS and third-party tools, with tool-specific keys for third-party tools. Requests whose argument pins are collectively too large are rejected with a ValidationException.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 131072.
Required: Yes

 ** tool **   <a name="devopsagent-Type-ApprovalPattern-tool"></a>
Identifier of the tool the pattern applies to (e.g. `use\_aws` for AWS actions, or a third-party tool name).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ApprovalPattern_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/ApprovalPattern)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/ApprovalPattern)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/ApprovalPattern)
