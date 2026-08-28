---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_SyncConfiguration.html
---

# SyncConfiguration
<a name="API_SyncConfiguration"></a>

Information, such as repository, branch, provider, and resource names for a specific sync configuration.

## Contents
<a name="API_SyncConfiguration_Contents"></a>

 ** Branch **   <a name="codeconnections-Type-SyncConfiguration-Branch"></a>
The branch associated with a specific sync configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** OwnerId **   <a name="codeconnections-Type-SyncConfiguration-OwnerId"></a>
The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** ProviderType **   <a name="codeconnections-Type-SyncConfiguration-ProviderType"></a>
The connection provider type associated with a specific sync configuration, such as GitHub.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: Yes

 ** RepositoryLinkId **   <a name="codeconnections-Type-SyncConfiguration-RepositoryLinkId"></a>
The ID of the repository link associated with a specific sync configuration.
Type: String
Pattern: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$`
Required: Yes

 ** RepositoryName **   <a name="codeconnections-Type-SyncConfiguration-RepositoryName"></a>
The name of the repository associated with a specific sync configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.*$`
Required: Yes

 ** ResourceName **   <a name="codeconnections-Type-SyncConfiguration-ResourceName"></a>
The name of the connection resource associated with a specific sync configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[0-9A-Za-z]+[0-9A-Za-z_\\-]*$`
Required: Yes

 ** RoleArn **   <a name="codeconnections-Type-SyncConfiguration-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(-[\w]+)*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** SyncType **   <a name="codeconnections-Type-SyncConfiguration-SyncType"></a>
The type of sync for a specific sync configuration.
Type: String
Valid Values: `CFN_STACK_SYNC`
Required: Yes

 ** ConfigFile **   <a name="codeconnections-Type-SyncConfiguration-ConfigFile"></a>
The file path to the configuration file associated with a specific sync configuration. The path should point to an actual file in the sync configurations linked repository.
Type: String
Required: No

 ** PublishDeploymentStatus **   <a name="codeconnections-Type-SyncConfiguration-PublishDeploymentStatus"></a>
Whether to enable or disable publishing of deployment status to source providers.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** PullRequestComment **   <a name="codeconnections-Type-SyncConfiguration-PullRequestComment"></a>
A toggle that specifies whether to enable or disable pull request comments for the sync configuration to be created.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** TriggerResourceUpdateOn **   <a name="codeconnections-Type-SyncConfiguration-TriggerResourceUpdateOn"></a>
When to trigger Git sync to begin the stack update.
Type: String
Valid Values: `ANY_CHANGE | FILE_CHANGE`
Required: No

## See Also
<a name="API_SyncConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/SyncConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/SyncConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/SyncConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
