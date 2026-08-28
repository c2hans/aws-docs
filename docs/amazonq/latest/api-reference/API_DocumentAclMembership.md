---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclMembership.html
---

# DocumentAclMembership
<a name="API_DocumentAclMembership"></a>

Represents membership rules in the document's ACL, defining how users or groups are associated with access permissions.

## Contents
<a name="API_DocumentAclMembership_Contents"></a>

 ** conditions **   <a name="qbusiness-Type-DocumentAclMembership-conditions"></a>
An array of conditions that define the membership rules. Each condition specifies criteria for users or groups to be included in this membership.
Type: Array of [DocumentAclCondition](API_DocumentAclCondition.md) objects
Required: No

 ** memberRelation **   <a name="qbusiness-Type-DocumentAclMembership-memberRelation"></a>
The logical relation between members in the membership rule, determining how multiple conditions are combined.
Type: String
Valid Values: `AND | OR`
Required: No

## See Also
<a name="API_DocumentAclMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAclMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAclMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAclMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
