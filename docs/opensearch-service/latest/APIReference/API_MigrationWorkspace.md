---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_MigrationWorkspace.html
---

# MigrationWorkspace
<a name="API_MigrationWorkspace"></a>

The target workspace configuration for a migration. You can specify an existing workspace by ID or request creation of a new workspace.

## Contents
<a name="API_MigrationWorkspace_Contents"></a>

 ** createWorkspace **   <a name="opensearchservice-Type-MigrationWorkspace-createWorkspace"></a>
Specifies whether to create a new workspace as the migration target. If `true`, you must also specify `name`.
Type: Boolean
Required: No

 ** name **   <a name="opensearchservice-Type-MigrationWorkspace-name"></a>
The name of the new workspace to create. Required when `createWorkspace` is `true`.
Type: String
Required: No

 ** type **   <a name="opensearchservice-Type-MigrationWorkspace-type"></a>
The type of the new workspace to create.
Type: String
Required: No

 ** workspaceId **   <a name="opensearchservice-Type-MigrationWorkspace-workspaceId"></a>
The unique identifier of an existing workspace to use as the migration target. Specify either this parameter or `createWorkspace`.
Type: String
Required: No

## See Also
<a name="API_MigrationWorkspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/MigrationWorkspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/MigrationWorkspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/MigrationWorkspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
