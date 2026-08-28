---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Principal.html
---

# Principal
<a name="API_Principal"></a>

Provides user and group information used for filtering documents to use for generating Amazon Q Business conversation responses.

## Contents
<a name="API_Principal_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="qbusiness-Type-Principal-group"></a>
 The group associated with the principal.
Type: [PrincipalGroup](API_PrincipalGroup.md) object
Required: No

 ** user **   <a name="qbusiness-Type-Principal-user"></a>
The user associated with the principal.
Type: [PrincipalUser](API_PrincipalUser.md) object
Required: No

## See Also
<a name="API_Principal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Principal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Principal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Principal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
