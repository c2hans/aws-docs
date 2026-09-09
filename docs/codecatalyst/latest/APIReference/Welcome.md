---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

**Important**
Amazon CodeCatalyst is no longer open to new customers. For more information, see [How to migrate from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

Welcome to the Amazon CodeCatalyst API reference. This reference provides descriptions of operations and data types for Amazon CodeCatalyst. You can use the Amazon CodeCatalyst API to work with the following objects.

Spaces, by calling the following:
+  [DeleteSpace](API_DeleteSpace.md), which deletes a space.
+  [GetSpace](API_GetSpace.md), which returns information about a space.
+  [GetSubscription](API_GetSubscription.md), which returns information about the AWS account used for billing purposes and the billing plan for the space.
+  [ListSpaces](API_ListSpaces.md), which retrieves a list of spaces.
+  [UpdateSpace](API_UpdateSpace.md), which changes one or more values for a space.

Projects, by calling the following:
+  [CreateProject](API_CreateProject.md) which creates a project in a specified space.
+  [GetProject](API_GetProject.md), which returns information about a project.
+  [ListProjects](API_ListProjects.md), which retrieves a list of projects in a space.

Users, by calling the following:
+  [GetUserDetails](API_GetUserDetails.md), which returns information about a user in Amazon CodeCatalyst.

Source repositories, by calling the following:
+  [CreateSourceRepository](API_CreateSourceRepository.md), which creates an empty Git-based source repository in a specified project.
+  [CreateSourceRepositoryBranch](API_CreateSourceRepositoryBranch.md), which creates a branch in a specified repository where you can work on code.
+  [DeleteSourceRepository](API_DeleteSourceRepository.md), which deletes a source repository.
+  [GetSourceRepository](API_GetSourceRepository.md), which returns information about a source repository.
+  [GetSourceRepositoryCloneUrls](API_GetSourceRepositoryCloneUrls.md), which returns information about the URLs that can be used with a Git client to clone a source repository.
+  [ListSourceRepositories](API_ListSourceRepositories.md), which retrieves a list of source repositories in a project.
+  [ListSourceRepositoryBranches](API_ListSourceRepositoryBranches.md), which retrieves a list of branches in a source repository.

Dev Environments and the AWS Toolkits, by calling the following:
+  [CreateDevEnvironment](API_CreateDevEnvironment.md), which creates a Dev Environment, where you can quickly work on the code stored in the source repositories of your project.
+  [DeleteDevEnvironment](API_DeleteDevEnvironment.md), which deletes a Dev Environment.
+  [GetDevEnvironment](API_GetDevEnvironment.md), which returns information about a Dev Environment.
+  [ListDevEnvironments](API_ListDevEnvironments.md), which retrieves a list of Dev Environments in a project.
+  [ListDevEnvironmentSessions](API_ListDevEnvironmentSessions.md), which retrieves a list of active Dev Environment sessions in a project.
+  [StartDevEnvironment](API_StartDevEnvironment.md), which starts a specified Dev Environment and puts it into an active state.
+  [StartDevEnvironmentSession](API_StartDevEnvironmentSession.md), which starts a session to a specified Dev Environment.
+  [StopDevEnvironment](API_StopDevEnvironment.md), which stops a specified Dev Environment and puts it into an stopped state.
+  [StopDevEnvironmentSession](API_StopDevEnvironmentSession.md), which stops a session for a specified Dev Environment.
+  [UpdateDevEnvironment](API_UpdateDevEnvironment.md), which changes one or more values for a Dev Environment.

Workflows, by calling the following:
+  [GetWorkflow](API_GetWorkflow.md), which returns information about a workflow.
+  [GetWorkflowRun](API_GetWorkflowRun.md), which returns information about a specified run of a workflow.
+  [ListWorkflowRuns](API_ListWorkflowRuns.md), which retrieves a list of runs of a specified workflow.
+  [ListWorkflows](API_ListWorkflows.md), which retrieves a list of workflows in a specified project.
+  [StartWorkflowRun](API_StartWorkflowRun.md), which starts a run of a specified workflow.

Security, activity, and resource management in Amazon CodeCatalyst, by calling the following:
+  [CreateAccessToken](API_CreateAccessToken.md), which creates a personal access token (PAT) for the current user.
+  [DeleteAccessToken](API_DeleteAccessToken.md), which deletes a specified personal access token (PAT).
+  [ListAccessTokens](API_ListAccessTokens.md), which lists all personal access tokens (PATs) associated with a user.
+  [ListEventLogs](API_ListEventLogs.md), which retrieves a list of events that occurred during a specified time period in a space.
+  [VerifySession](API_VerifySession.md), which verifies whether the calling user has a valid Amazon CodeCatalyst login and session.

**Note**
If you are using the Amazon CodeCatalyst APIs with an SDK or the AWS CLI, you must configure your computer to work with Amazon CodeCatalyst and single sign-on (SSO). For more information, see [Setting up to use the AWS CLI with Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html) and the SSO documentation for your SDK.

This document was last published on September 9, 2026.
