---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_RepositorySyncDefinition.html
---

# RepositorySyncDefinition
<a name="API_RepositorySyncDefinition"></a>

The definition for a repository with a sync configuration.

## Contents
<a name="API_RepositorySyncDefinition_Contents"></a>

 ** Branch **   <a name="codeconnections-Type-RepositorySyncDefinition-Branch"></a>
The branch specified for a repository sync definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** Directory **   <a name="codeconnections-Type-RepositorySyncDefinition-Directory"></a>
The configuration file for a repository sync definition. This value comes from creating or updating the `config-file` field of a `sync-configuration`.
Type: String
Required: Yes

 ** Parent **   <a name="codeconnections-Type-RepositorySyncDefinition-Parent"></a>
The parent resource specified for a repository sync definition.
Type: String
Required: Yes

 ** Target **   <a name="codeconnections-Type-RepositorySyncDefinition-Target"></a>
The target resource specified for a repository sync definition. In some cases, such as CFN\_STACK\_SYNC, the parent and target resource are the same.
Type: String
Required: Yes

## See Also
<a name="API_RepositorySyncDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/RepositorySyncDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/RepositorySyncDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/RepositorySyncDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
