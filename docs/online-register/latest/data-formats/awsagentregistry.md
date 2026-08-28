---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awsagentregistry.html
---

# Data retrieval APIs for AWS Agent Registry
<a name="awsagentregistry"></a>

AWS Agent Registry provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="agent-registry-GetDiscoverableRegistryRecord"></a>[GetDiscoverableRegistryRecord](https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_BatchGetDiscoverableRegistryRecord.html) | Retrieve an individual approved registry record. This is a permission-only action used for fine-grained access control with BatchGetApprovedRegistryRecord | Read |
| <a name="agent-registry-GetRegistry"></a>[GetRegistry](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GetRegistry.html) | Retrieve an existing registry | Read |
| <a name="agent-registry-GetRegistryRecord"></a>[GetRegistryRecord](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GetRegistryRecord.html) | Retrieve an existing registry record | Read |
| <a name="agent-registry-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/agent-registry/latest/APIReference/) | Retrieve the resource-based policy for a specified resource | Read |
| <a name="agent-registry-InvokeRegistryMcp"></a>[InvokeRegistryMcp](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-mcp-endpoint.html) | Invoke an MCP operation against an existing registry | Read |
| <a name="agent-registry-ListDiscoverableRegistryRecords"></a>[ListDiscoverableRegistryRecords](https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_ListDiscoverableRegistryRecords.html) | List approved registry records in a registry | List |
| <a name="agent-registry-ListRegistries"></a>[ListRegistries](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListRegistries.html) | List existing registries | List |
| <a name="agent-registry-ListRegistryRecords"></a>[ListRegistryRecords](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListRegistryRecords.html) | List existing registry records in a registry | List |
| <a name="agent-registry-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListTagsForResource.html) | List tags for an Agent Registry resource | List |
| <a name="agent-registry-SearchDiscoverableRegistryRecords"></a>[SearchDiscoverableRegistryRecords](https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_SearchDiscoverableRegistryRecords.html) | Search for registry records | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
