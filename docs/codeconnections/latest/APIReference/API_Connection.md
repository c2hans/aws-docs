---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

A resource that is used to connect third-party source providers with services like CodePipeline.

Note: A connection created through CloudFormation, the CLI, or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by updating the connection in the console.

## Contents
<a name="API_Connection_Contents"></a>

 ** ConnectionArn **   <a name="codeconnections-Type-Connection-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the connection. The ARN is used as the connection reference when the connection is shared between AWS services.
The ARN is never reused if the connection is deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: No

 ** ConnectionName **   <a name="codeconnections-Type-Connection-ConnectionName"></a>
The name of the connection. Connection names must be unique in an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\s\S]*`
Required: No

 ** ConnectionStatus **   <a name="codeconnections-Type-Connection-ConnectionStatus"></a>
The current status of the connection.
Type: String
Valid Values: `PENDING | AVAILABLE | ERROR`
Required: No

 ** HostArn **   <a name="codeconnections-Type-Connection-HostArn"></a>
The Amazon Resource Name (ARN) of the host associated with the connection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: No

 ** OwnerAccountId **   <a name="codeconnections-Type-Connection-OwnerAccountId"></a>
The identifier of the external provider where your third-party code repository is configured. For Bitbucket, this is the account ID of the owner of the Bitbucket repository.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** ProviderType **   <a name="codeconnections-Type-Connection-ProviderType"></a>
The name of the external provider where your third-party code repository is configured.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/Connection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
