---
source_url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amplifygen3.html
---

# Actions, resources, and condition keys for AWS Amplify Gen 3

AWS Amplify Gen 3 (service prefix: `amplifygen3`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amplify/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amplify/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/amplifygen3/amplifygen3.json) for this service.

**Topics**
+ [Actions defined by AWS Amplify Gen 3](#list_amplifygen3-actions-as-permissions)
+ [Permission-only actions for AWS Amplify Gen 3](#list_amplifygen3-permission-only-actions)
+ [Resource types defined by AWS Amplify Gen 3](#list_amplifygen3-resources-for-iam-policies)
+ [Condition keys for AWS Amplify Gen 3](#list_amplifygen3-policy-keys)

## Actions defined by AWS Amplify Gen 3
<a name="list_amplifygen3-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

- **   [AcceptForkPullRequestDeployment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_AcceptForkPullRequestDeployment.html)  **
  - **Description:** Grants permission to accept a pull request deployment from a forked repository
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelGradualRollout](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CancelGradualRollout.html)  **
  - **Description:** Grants permission to cancel a gradual rollout for an alias of an environment
  - **Resource types (\*required):** [Alias\*](#list_amplifygen3-resource-Alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [Connect](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to connect to an Amplify Gen 3 backend as a service identity, through the REST interface or Postgres relay
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateApp.html)  **
  - **Description:** Grants permission to create a new App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDeployment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateDeployment.html)  **
  - **Description:** Grants permission to create a deployment for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateDomainAssociation.html)  **
  - **Description:** Grants permission to create a new domain association for an App
  - **Resource types (\*required):** [DomainAssociation\*](#list_amplifygen3-resource-DomainAssociation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create a new environment for an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegrationConfiguration](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateIntegrationConfiguration.html)  **
  - **Description:** Grants permission to create a new integration configuration
  - **Resource types (\*required):** [IntegrationConfiguration\*](#list_amplifygen3-resource-IntegrationConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIntegrationConnection](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateIntegrationConnection.html)  **
  - **Description:** Grants permission to create a connection between an integration configuration and an environment
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNetworkConnector](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateNetworkConnector.html)  **
  - **Description:** Grants permission to create a new network connector
  - **Resource types (\*required):** [NetworkConnector\*](#list_amplifygen3-resource-NetworkConnector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSourceUpload](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateSourceUpload.html)  **
  - **Description:** Grants permission to create a source upload and retrieve a pre-signed URL for uploading source artifacts
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteAlias](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteAlias.html)  **
  - **Description:** Grants permission to delete an alias for an environment of an App
  - **Resource types (\*required):** [Alias\*](#list_amplifygen3-resource-Alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteApp.html)  **
  - **Description:** Grants permission to delete an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBackendFromApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteBackendFromApp.html)  **
  - **Description:** Grants permission to delete the backend from an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteBranch.html)  **
  - **Description:** Grants permission to delete a branch for an environment of an App
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDeployment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteDeployment.html)  **
  - **Description:** Grants permission to delete a deployment for an environment of an App
  - **Resource types (\*required):** [Deployment\*](#list_amplifygen3-resource-Deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteDomainAssociation.html)  **
  - **Description:** Grants permission to delete a domain association for an App
  - **Resource types (\*required):** [DomainAssociation\*](#list_amplifygen3-resource-DomainAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete an environment for an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironmentVariables](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteEnvironmentVariables.html)  **
  - **Description:** Grants permission to delete environment variables for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGitConnection](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteGitConnection.html)  **
  - **Description:** Grants permission to delete a Git connection
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteIdentityProviderConfig](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteIdentityProviderConfig.html)  **
  - **Description:** Grants permission to delete the identity provider configuration for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegrationConfiguration](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteIntegrationConfiguration.html)  **
  - **Description:** Grants permission to delete an integration configuration
  - **Resource types (\*required):** [IntegrationConfiguration\*](#list_amplifygen3-resource-IntegrationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIntegrationConnection](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteIntegrationConnection.html)  **
  - **Description:** Grants permission to delete an integration connection
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [DeleteNetworkConnector](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteNetworkConnector.html)  **
  - **Description:** Grants permission to delete a network connector
  - **Resource types (\*required):** [NetworkConnector\*](#list_amplifygen3-resource-NetworkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSourceUpload](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DeleteSourceUpload.html)  **
  - **Description:** Grants permission to delete a source upload
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [DisableAccessControl](https://docs.aws.amazon.com/amplify/latest/APIReference/API_DisableAccessControl.html)  **
  - **Description:** Grants permission to disable access control for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableAccessControl](https://docs.aws.amazon.com/amplify/latest/APIReference/API_EnableAccessControl.html)  **
  - **Description:** Grants permission to enable access control for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccessControl](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetAccessControl.html)  **
  - **Description:** Grants permission to retrieve the access control configuration for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAlias](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetAlias.html)  **
  - **Description:** Grants permission to retrieve an alias for an environment of an App
  - **Resource types (\*required):** [Alias\*](#list_amplifygen3-resource-Alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApiKey](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetApiKey.html)  **
  - **Description:** Grants permission to retrieve an API key of a branch
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetApp.html)  **
  - **Description:** Grants permission to retrieve an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetBranch.html)  **
  - **Description:** Grants permission to retrieve a branch for an environment of an App
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDeployment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetDeployment.html)  **
  - **Description:** Grants permission to retrieve a deployment for an environment of an App
  - **Resource types (\*required):** [Deployment\*](#list_amplifygen3-resource-Deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetDomainAssociation.html)  **
  - **Description:** Grants permission to retrieve a domain association for an App
  - **Resource types (\*required):** [DomainAssociation\*](#list_amplifygen3-resource-DomainAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainConnectUrl](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetDomainConnectUrl.html)  **
  - **Description:** Grants permission to retrieve a domain connect redirect URL for one-click DNS setup
  - **Resource types (\*required):** [DomainAssociation\*](#list_amplifygen3-resource-DomainAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetEnvironment.html)  **
  - **Description:** Grants permission to retrieve an environment for an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironmentsForNetworkConnector](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetEnvironmentsForNetworkConnector.html)  **
  - **Description:** Grants permission to retrieve the environments associated with a network connector
  - **Resource types (\*required):** [NetworkConnector\*](#list_amplifygen3-resource-NetworkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetFile](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetFile.html)  **
  - **Description:** Grants permission to retrieve a file from a repository
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   [GetFolder](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetFolder.html)  **
  - **Description:** Grants permission to retrieve a folder from a repository
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   [GetIdentityProviderConfig](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetIdentityProviderConfig.html)  **
  - **Description:** Grants permission to retrieve the identity provider configuration for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegrationConfiguration](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetIntegrationConfiguration.html)  **
  - **Description:** Grants permission to retrieve an integration configuration
  - **Resource types (\*required):** [IntegrationConfiguration\*](#list_amplifygen3-resource-IntegrationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIntegrationConnection](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetIntegrationConnection.html)  **
  - **Description:** Grants permission to retrieve an integration connection
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   [GetNetworkConnector](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetNetworkConnector.html)  **
  - **Description:** Grants permission to retrieve a network connector
  - **Resource types (\*required):** [NetworkConnector\*](#list_amplifygen3-resource-NetworkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRestoreWindow](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetRestoreWindow.html)  **
  - **Description:** Grants permission to retrieve the point-in-time restore window of a branch
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSourceUpload](https://docs.aws.amazon.com/amplify/latest/APIReference/API_GetSourceUpload.html)  **
  - **Description:** Grants permission to retrieve a source upload
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   [ListAccessControls](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListAccessControls.html)  **
  - **Description:** Grants permission to list access control configurations for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAliases](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListAliases.html)  **
  - **Description:** Grants permission to list aliases for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApiKeys](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListApiKeys.html)  **
  - **Description:** Grants permission to list the API keys of a branch
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListApps](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListApps.html)  **
  - **Description:** Grants permission to list Apps
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListBranches](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListBranches.html)  **
  - **Description:** Grants permission to list branches for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeploymentsForApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListDeploymentsForApp.html)  **
  - **Description:** Grants permission to list deployments for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDeploymentsForEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListDeploymentsForEnvironment.html)  **
  - **Description:** Grants permission to list deployments for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainAssociationsForAccount](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListDomainAssociationsForAccount.html)  **
  - **Description:** Grants permission to list domain associations for an account
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListDomainAssociationsForApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListDomainAssociationsForApp.html)  **
  - **Description:** Grants permission to list domain associations for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironmentVariables](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListEnvironmentVariables.html)  **
  - **Description:** Grants permission to list environment variables for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEnvironments](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list environments for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGitBranches](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListGitBranches.html)  **
  - **Description:** Grants permission to list branches for a repository
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListGitConnections](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListGitConnections.html)  **
  - **Description:** Grants permission to list Git connections
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListIntegrationConfigurations](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListIntegrationConfigurations.html)  **
  - **Description:** Grants permission to list integration configurations
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListIntegrationConnections](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListIntegrationConnections.html)  **
  - **Description:** Grants permission to list integration connections
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListIntegrationTypes](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListIntegrationTypes.html)  **
  - **Description:** Grants permission to list the available integration types
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListNetworkConnectors](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListNetworkConnectors.html)  **
  - **Description:** Grants permission to list network connectors
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListPlanViolations](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListPlanViolations.html)  **
  - **Description:** Grants permission to list the resources in your account that a target plan tier does not support
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Read

- **   [ListRepositories](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListRepositories.html)  **
  - **Description:** Grants permission to list repositories for a Git connection
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListSourceUploads](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListSourceUploads.html)  **
  - **Description:** Grants permission to list source uploads
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [Alias](#list_amplifygen3-resource-Alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [App](#list_amplifygen3-resource-App) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Branch](#list_amplifygen3-resource-Branch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Deployment](#list_amplifygen3-resource-Deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [DomainAssociation](#list_amplifygen3-resource-DomainAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Environment](#list_amplifygen3-resource-Environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [IntegrationConfiguration](#list_amplifygen3-resource-IntegrationConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NetworkConnector](#list_amplifygen3-resource-NetworkConnector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutEnvironmentVariables](https://docs.aws.amazon.com/amplify/latest/APIReference/API_PutEnvironmentVariables.html)  **
  - **Description:** Grants permission to set environment variables for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutIdentityProviderConfig](https://docs.aws.amazon.com/amplify/latest/APIReference/API_PutIdentityProviderConfig.html)  **
  - **Description:** Grants permission to set the identity provider configuration for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetCache](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ResetCache.html)  **
  - **Description:** Grants permission to purge cached content by cache tag for a deployment of an environment
  - **Resource types (\*required):** [Deployment\*](#list_amplifygen3-resource-Deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RestoreBranch](https://docs.aws.amazon.com/amplify/latest/APIReference/API_RestoreBranch.html)  **
  - **Description:** Grants permission to restore a branch to a point in time into a new branch
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResumeBackend](https://docs.aws.amazon.com/amplify/latest/APIReference/API_ResumeBackend.html)  **
  - **Description:** Grants permission to resume the paused backend of an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RevokeApiKey](https://docs.aws.amazon.com/amplify/latest/APIReference/API_RevokeApiKey.html)  **
  - **Description:** Grants permission to revoke an API key of a branch
  - **Resource types (\*required):** [Branch\*](#list_amplifygen3-resource-Branch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RotateIdentityProviderSecret](https://docs.aws.amazon.com/amplify/latest/APIReference/API_RotateIdentityProviderSecret.html)  **
  - **Description:** Grants permission to rotate the client secret of the identity provider configuration for an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAuthorizationFlow](https://docs.aws.amazon.com/amplify/latest/APIReference/API_StartAuthorizationFlow.html)  **
  - **Description:** Grants permission to start an authorization flow for connecting a Git provider
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** Write

- **   [StartCacheRevalidation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_StartCacheRevalidation.html)  **
  - **Description:** Grants permission to revalidate cached content by cache tag for a deployment of an environment
  - **Resource types (\*required):** [Deployment\*](#list_amplifygen3-resource-Deployment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/amplify/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [Alias](#list_amplifygen3-resource-Alias) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [App](#list_amplifygen3-resource-App) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [Branch](#list_amplifygen3-resource-Branch) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [Deployment](#list_amplifygen3-resource-Deployment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [DomainAssociation](#list_amplifygen3-resource-DomainAssociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [Environment](#list_amplifygen3-resource-Environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationConfiguration](#list_amplifygen3-resource-IntegrationConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [NetworkConnector](#list_amplifygen3-resource-NetworkConnector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_amplifygen3-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [Alias](#list_amplifygen3-resource-Alias) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [App](#list_amplifygen3-resource-App) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [Branch](#list_amplifygen3-resource-Branch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [Deployment](#list_amplifygen3-resource-Deployment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [DomainAssociation](#list_amplifygen3-resource-DomainAssociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [Environment](#list_amplifygen3-resource-Environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [IntegrationConfiguration](#list_amplifygen3-resource-IntegrationConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Resource types (\*required):** [NetworkConnector](#list_amplifygen3-resource-NetworkConnector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_amplifygen3-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccessControl](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateAccessControl.html)  **
  - **Description:** Grants permission to update the access control configuration for an environment of an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAliasRouting](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateAliasRouting.html)  **
  - **Description:** Grants permission to update the routing configuration of an alias for an environment of an App
  - **Resource types (\*required):** [Alias\*](#list_amplifygen3-resource-Alias)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApp](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateApp.html)  **
  - **Description:** Grants permission to update an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainAssociation](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateDomainAssociation.html)  **
  - **Description:** Grants permission to update a domain association for an App
  - **Resource types (\*required):** [DomainAssociation\*](#list_amplifygen3-resource-DomainAssociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update an environment for an App
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIntegrationConfiguration](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateIntegrationConfiguration.html)  **
  - **Description:** Grants permission to update an integration configuration
  - **Resource types (\*required):** [IntegrationConfiguration\*](#list_amplifygen3-resource-IntegrationConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkConnector](https://docs.aws.amazon.com/amplify/latest/APIReference/API_UpdateNetworkConnector.html)  **
  - **Description:** Grants permission to update a network connector
  - **Resource types (\*required):** [NetworkConnector\*](#list_amplifygen3-resource-NetworkConnector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

## Permission-only actions for AWS Amplify Gen 3
<a name="list_amplifygen3-permission-only-actions"></a>

The following actions are defined by AWS Amplify Gen 3 but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.

- **   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to configure vended log delivery for AmplifyGen3
  - **Resource types (\*required):** [Environment\*](#list_amplifygen3-resource-Environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [AssociateWebACL](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to associate a WebACL with an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWebACL](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to disassociate a WebACL from an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetWebACLForResource](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to retrieve the WebACL associated with an App
  - **Resource types (\*required):** [App\*](#list_amplifygen3-resource-App)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListResourcesForWebACL](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  **
  - **Description:** Grants permission to list the resources associated with a WebACL
  - **Resource types (\*required):**
  - **Condition keys:**
  - **Access level:** List

## Resource types defined by AWS Amplify Gen 3
<a name="list_amplifygen3-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.

| Resource types | ARN | Condition keys |
| --- | --- | --- |
|  [Alias](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:app/${AppName}/environment/${EnvironmentName}/alias/${AliasName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [App](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:app/${AppName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [Branch](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:app/${AppName}/environment/${EnvironmentName}/branch/${BranchName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [Deployment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:app/${AppName}/environment/${EnvironmentName}/deployment/${DeploymentId} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [DomainAssociation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:app/${AppName}/domain/${DomainName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [Environment](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:app/${AppName}/environment/${EnvironmentName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [IntegrationConfiguration](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:integration-configuration/${IntegrationName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |
|  [NetworkConnector](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)  | arn:${Partition}:amplifygen3:${Region}:${Account}:network-connector/${NetworkConnectorName} | [aws:ResourceTag/${TagKey}](#list_amplifygen3-aws_ResourceTag___TagKey_) |

## Condition keys for AWS Amplify Gen 3
<a name="list_amplifygen3-policy-keys"></a>

AWS Amplify Gen 3 defines the following condition keys that can be used in the `Condition` element of an IAM policy.

| Condition keys | Description | Type |
| --- | --- | --- |
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String |
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the presence of tag key-value pairs in the request | String |
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString |
