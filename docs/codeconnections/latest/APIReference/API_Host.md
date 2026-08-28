---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Host.html
---

# Host
<a name="API_Host"></a>

A resource that represents the infrastructure where a third-party provider is installed. The host is used when you create connections to an installed third-party provider type, such as GitHub Enterprise Server. You create one host for all connections to that provider.

**Note**
A host created through the CLI or the SDK is in `PENDING` status by default. You can make its status `AVAILABLE` by setting up the host in the console.

## Contents
<a name="API_Host_Contents"></a>

 ** HostArn **   <a name="codeconnections-Type-Host-HostArn"></a>
The Amazon Resource Name (ARN) of the host.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:(codestar-connections|codeconnections):.+:[0-9]{12}:host\/.+`
Required: No

 ** Name **   <a name="codeconnections-Type-Host-Name"></a>
The name of the host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** ProviderEndpoint **   <a name="codeconnections-Type-Host-ProviderEndpoint"></a>
The endpoint of the infrastructure where your provider type is installed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

 ** ProviderType **   <a name="codeconnections-Type-Host-ProviderType"></a>
The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: No

 ** Status **   <a name="codeconnections-Type-Host-Status"></a>
The status of the host, such as PENDING, AVAILABLE, VPC\_CONFIG\_DELETING, VPC\_CONFIG\_INITIALIZING, and VPC\_CONFIG\_FAILED\_INITIALIZATION.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*`
Required: No

 ** StatusMessage **   <a name="codeconnections-Type-Host-StatusMessage"></a>
The status description for the host.
Type: String
Required: No

 ** VpcConfiguration **   <a name="codeconnections-Type-Host-VpcConfiguration"></a>
The VPC configuration provisioned for the host.
Type: [VpcConfiguration](API_VpcConfiguration.md) object
Required: No

## See Also
<a name="API_Host_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/Host)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/Host)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/Host)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
