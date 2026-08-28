---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAclUser.html
---

# DocumentAclUser
<a name="API_DocumentAclUser"></a>

Represents a user in the document's ACL, used to define access permissions for individual users.

## Contents
<a name="API_DocumentAclUser_Contents"></a>

 ** id **   <a name="qbusiness-Type-DocumentAclUser-id"></a>
The unique identifier of the user in the document's ACL. This is used to identify the user when applying access rules.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** type **   <a name="qbusiness-Type-DocumentAclUser-type"></a>
The type of the user. This indicates the scope of the user's applicability in access control.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

## See Also
<a name="API_DocumentAclUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAclUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAclUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAclUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
