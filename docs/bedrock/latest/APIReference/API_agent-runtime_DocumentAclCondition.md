---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DocumentAclCondition.html
---

# DocumentAclCondition
<a name="API_agent-runtime_DocumentAclCondition"></a>

A condition within a document access control list (ACL) membership, specifying users and groups that are evaluated together.

## Contents
<a name="API_agent-runtime_DocumentAclCondition_Contents"></a>

 ** conditionOperator **   <a name="bedrock-Type-agent-runtime_DocumentAclCondition-conditionOperator"></a>
The logical operator for combining users and groups within this condition. Valid values: `AND` – Both a user match and a group match are required. `OR` – Either a user match or a group match is sufficient.
Type: String
Valid Values: `AND | OR`
Required: No

 ** groups **   <a name="bedrock-Type-agent-runtime_DocumentAclCondition-groups"></a>
The list of group entries in this condition.
Type: Array of [DocumentAclGroup](API_agent-runtime_DocumentAclGroup.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3000 items.
Required: No

 ** users **   <a name="bedrock-Type-agent-runtime_DocumentAclCondition-users"></a>
The list of user entries in this condition.
Type: Array of [DocumentAclUser](API_agent-runtime_DocumentAclUser.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3000 items.
Required: No

## See Also
<a name="API_agent-runtime_DocumentAclCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/DocumentAclCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/DocumentAclCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/DocumentAclCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
