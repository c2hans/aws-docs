---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs-ram.html
---

# Cross-account sharing for private model hubs with AWS Resource Access Manager
<a name="jumpstart-curated-hubs-ram"></a>

After creating a private model hub, you can share the hub to the necessary accounts using AWS Resource Access Manager (AWS RAM). For more information on creating a private hub, see [Create a private model hub](jumpstart-curated-hubs-admin-guide-create.md). The following page gives in-depth information about managed permissions related to private hubs within AWS RAM. For information about how to create a resource share within AWS RAM, see [Set up cross-account hub sharing](jumpstart-curated-hubs-ram-setup.md).

## Managed permissions for curated private hubs
<a name="jumpstart-curated-hubs-ram-permissions"></a>

The available access permissions are read, read and use, and full access permissions. The permission name, description, and list of specific APIs available for each permission are listed in the following:
+ Read permission (`AWSRAMPermissionSageMaker AIHubRead`): The read privilege allows resource consumer accounts to read contents in the shared hubs and view details and metadata.
  + `DescribeHub`: Retrieves details about a hub and its configuration
  + `DescribeHubContent`: Retrieves details about a model available in a specific hub
  + `ListHubContent`: Lists all models available in a hub
  + `ListHubContentVersions`: Lists the version of all models available in a hub
+ Read and use permission (`AWSRAMPermissionSageMaker AIHubReadAndUse`): The read and use privilege allows resource consumer accounts to read contents in the shared hubs and deploy available models for inference.
  + `DescribeHub`: Retrieves details about a hub and its configuration
  + `DescribeHubContent`: Retrieves details about a model available in a specific hub
  + `ListHubContent`: Lists all models available in a hub
  + `ListHubContentVersions`: Lists the version of all models available in a hub
  + `DeployHubModel`: Allows access to deploy available open-weight hub models for inference
+ Full access permission (`AWSRAMPermissionSageMaker AIHubFullAccessPolicy`): The full access privilege allows resource consumer accounts to read contents in the shared hubs, add and remove hub content, and deploy available models for inference.
  + `DescribeHub`: Retrieves details about a hub and its configuration
  + `DescribeHubContent`: Retrieves details about a model available in a specific hub
  + `ListHubContent`: Lists all models available in a hub
  + `ListHubContentVersions`: Lists the version of all models available in a hub
  + `ImportHubContent`: Imports hub content
  + `DeleteHubContent`: Deletes hub content
  + `CreateHubContentReference`: Creates a hub content reference that shares a model from the SageMaker AI **Public models** hub to a private hub
  + `DeleteHubContentReference`: Delete a hub content reference that shares a model from the SageMaker AI **Public models** hub to a private hub
  + `DeployHubModel`: Allows access to deploy available open-weight hub models for inference

`DeployHubModel` permissions are not required for proprietary models.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
