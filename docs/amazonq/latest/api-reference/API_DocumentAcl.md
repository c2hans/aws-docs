---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAcl.html
---

# DocumentAcl
<a name="API_DocumentAcl"></a>

Represents the Access Control List (ACL) for a document, containing both allowlist and denylist conditions.

## Contents
<a name="API_DocumentAcl_Contents"></a>

 ** allowlist **   <a name="qbusiness-Type-DocumentAcl-allowlist"></a>
The allowlist conditions for the document. Users or groups matching these conditions are granted access to the document.
Type: [DocumentAclMembership](API_DocumentAclMembership.md) object
Required: No

 ** denyList **   <a name="qbusiness-Type-DocumentAcl-denyList"></a>
The denylist conditions for the document. Users or groups matching these conditions are denied access to the document, overriding allowlist permissions.
Type: [DocumentAclMembership](API_DocumentAclMembership.md) object
Required: No

## See Also
<a name="API_DocumentAcl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DocumentAcl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DocumentAcl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DocumentAcl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
