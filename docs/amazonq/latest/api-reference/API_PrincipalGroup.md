---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PrincipalGroup.html
---

# PrincipalGroup
<a name="API_PrincipalGroup"></a>

Provides information about a group associated with the principal.

## Contents
<a name="API_PrincipalGroup_Contents"></a>

 ** access **   <a name="qbusiness-Type-PrincipalGroup-access"></a>
Provides information about whether to allow or deny access to the principal.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** membershipType **   <a name="qbusiness-Type-PrincipalGroup-membershipType"></a>
The type of group.
Type: String
Valid Values: `INDEX | DATASOURCE`
Required: No

 ** name **   <a name="qbusiness-Type-PrincipalGroup-name"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_PrincipalGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/PrincipalGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/PrincipalGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/PrincipalGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
