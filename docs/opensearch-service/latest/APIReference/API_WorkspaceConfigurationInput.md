---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_WorkspaceConfigurationInput.html
---

# WorkspaceConfigurationInput
<a name="API_WorkspaceConfigurationInput"></a>

Configuration for creating a new workspace when attaching a data source to an OpenSearch application. The workspace is created after the data source is successfully attached.

## Contents
<a name="API_WorkspaceConfigurationInput_Contents"></a>

 ** name **   <a name="opensearchservice-Type-WorkspaceConfigurationInput-name"></a>
The name of the workspace to create. Must be between 1 and 40 characters and can contain alphanumeric characters, parentheses, brackets, hyphens, underscores, and spaces.
Type: String
Required: Yes

 ** workspaceType **   <a name="opensearchservice-Type-WorkspaceConfigurationInput-workspaceType"></a>
The type of workspace to create, which determines the use-case features enabled for the workspace. Valid values are `OBSERVABILITY`, `SECURITY_ANALYTICS`, and `SEARCH`.
Type: String
Required: Yes

## See Also
<a name="API_WorkspaceConfigurationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/WorkspaceConfigurationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/WorkspaceConfigurationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/WorkspaceConfigurationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
