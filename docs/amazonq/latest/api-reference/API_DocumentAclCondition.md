---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclCondition.html
---

# DocumentAclCondition
<a name="API_DocumentAclCondition"></a>

Represents a condition in the document's ACL, specifying access rules for users and groups.

## Contents
<a name="API_DocumentAclCondition_Contents"></a>

 ** groups **   <a name="qbusiness-Type-DocumentAclCondition-groups"></a>
An array of group identifiers that this condition applies to. Groups listed here are subject to the access rule defined by this condition.
Type: Array of [DocumentAclGroup](API_DocumentAclGroup.md) objects
Required: No

 ** memberRelation **   <a name="qbusiness-Type-DocumentAclCondition-memberRelation"></a>
The logical relation between members in the condition, determining how multiple user or group conditions are combined.
Type: String
Valid Values: `AND | OR`
Required: No

 ** users **   <a name="qbusiness-Type-DocumentAclCondition-users"></a>
An array of user identifiers that this condition applies to. Users listed here are subject to the access rule defined by this condition.
Type: Array of [DocumentAclUser](API_DocumentAclUser.md) objects
Required: No

## See Also
<a name="API_DocumentAclCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAclCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAclCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAclCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
