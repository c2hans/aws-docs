---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ConnectionAlias.html
---

# ConnectionAlias
<a name="API_ConnectionAlias"></a>

Describes a connection alias. Connection aliases are used for cross-Region redirection. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

## Contents
<a name="API_ConnectionAlias_Contents"></a>

 ** AliasId **   <a name="WorkSpaces-Type-ConnectionAlias-AliasId"></a>
The identifier of the connection alias.
Type: String
Length Constraints: Minimum length of 13. Maximum length of 68.
Pattern: `^wsca-[0-9a-z]{8,63}$`
Required: No

 ** Associations **   <a name="WorkSpaces-Type-ConnectionAlias-Associations"></a>
The association status of the connection alias.
Type: Array of [ConnectionAliasAssociation](API_ConnectionAliasAssociation.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

 ** ConnectionString **   <a name="WorkSpaces-Type-ConnectionAlias-ConnectionString"></a>
The connection string specified for the connection alias. The connection string must be in the form of a fully qualified domain name (FQDN), such as `www.example.com`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[.0-9a-zA-Z\-]{1,255}$`
Required: No

 ** OwnerAccountId **   <a name="WorkSpaces-Type-ConnectionAlias-OwnerAccountId"></a>
The identifier of the AWS account that owns the connection alias.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** State **   <a name="WorkSpaces-Type-ConnectionAlias-State"></a>
The current state of the connection alias.
Type: String
Valid Values: `CREATING | CREATED | DELETING`
Required: No

## See Also
<a name="API_ConnectionAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ConnectionAlias)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ConnectionAlias)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ConnectionAlias)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
