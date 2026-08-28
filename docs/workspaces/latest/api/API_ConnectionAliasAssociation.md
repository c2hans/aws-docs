---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ConnectionAliasAssociation.html
---

# ConnectionAliasAssociation
<a name="API_ConnectionAliasAssociation"></a>

Describes a connection alias association that is used for cross-Region redirection. For more information, see [ Cross-Region Redirection for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/cross-region-redirection.html).

## Contents
<a name="API_ConnectionAliasAssociation_Contents"></a>

 ** AssociatedAccountId **   <a name="WorkSpaces-Type-ConnectionAliasAssociation-AssociatedAccountId"></a>
The identifier of the AWS account that associated the connection alias with a directory.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** AssociationStatus **   <a name="WorkSpaces-Type-ConnectionAliasAssociation-AssociationStatus"></a>
The association status of the connection alias.
Type: String
Valid Values: `NOT_ASSOCIATED | ASSOCIATED_WITH_OWNER_ACCOUNT | ASSOCIATED_WITH_SHARED_ACCOUNT | PENDING_ASSOCIATION | PENDING_DISASSOCIATION`
Required: No

 ** ConnectionIdentifier **   <a name="WorkSpaces-Type-ConnectionAliasAssociation-ConnectionIdentifier"></a>
The identifier of the connection alias association. You use the connection identifier in the DNS TXT record when you're configuring your DNS routing policies.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `^[a-zA-Z0-9]+$`
Required: No

 ** ResourceId **   <a name="WorkSpaces-Type-ConnectionAliasAssociation-ResourceId"></a>
The identifier of the directory associated with a connection alias.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ConnectionAliasAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ConnectionAliasAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ConnectionAliasAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ConnectionAliasAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
