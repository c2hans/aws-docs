---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ConnectionAliasPermission.html
---

# ConnectionAliasPermission
<a name="API_ConnectionAliasPermission"></a>

Describes the permissions for a connection alias. Connection aliases are used for cross-Region redirection. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

## Contents
<a name="API_ConnectionAliasPermission_Contents"></a>

 ** AllowAssociation **   <a name="WorkSpaces-Type-ConnectionAliasPermission-AllowAssociation"></a>
Indicates whether the specified AWS account is allowed to associate the connection alias with a directory.
Type: Boolean
Required: Yes

 ** SharedAccountId **   <a name="WorkSpaces-Type-ConnectionAliasPermission-SharedAccountId"></a>
The identifier of the AWS account that the connection alias is shared with.
Type: String
Pattern: `^\d{12}$`
Required: Yes

## See Also
<a name="API_ConnectionAliasPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ConnectionAliasPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ConnectionAliasPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ConnectionAliasPermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
