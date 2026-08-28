---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonmanagedgrafana.html
---

# Data retrieval APIs for Amazon Managed Grafana
<a name="amazonmanagedgrafana"></a>

Amazon Managed Grafana provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="grafana-DescribeWorkspace"></a>[DescribeWorkspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html) | Describe a workspace | Read |
| <a name="grafana-DescribeWorkspaceAuthentication"></a>[DescribeWorkspaceAuthentication](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html) | Describe authentication providers on a workspace | Read |
| <a name="grafana-DescribeWorkspaceConfiguration"></a>[DescribeWorkspaceConfiguration](https://docs.aws.amazon.com/grafana/latest/APIReference/API_DescribeWorkspaceConfiguration.html) | Describe the current configuration string for the given workspace | Read |
| <a name="grafana-ListPermissions"></a>[ListPermissions](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html) | List the permissions on a wokspace | List |
| <a name="grafana-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListTagsForResource.html) | List tags associated with a workspace | Read |
| <a name="grafana-ListVersions"></a>[ListVersions](https://docs.aws.amazon.com/grafana/latest/APIReference/API_ListVersions.html) | List all available supported Grafana versions. Optionally, include a workspace to list the versions to which it can be upgraded | List |
| <a name="grafana-ListWorkspaceServiceAccountTokens"></a>[ListWorkspaceServiceAccountTokens](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html) | List service account tokens for a workspace | Read |
| <a name="grafana-ListWorkspaceServiceAccounts"></a>[ListWorkspaceServiceAccounts](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html) | List service accounts for a workspace | Read |
| <a name="grafana-ListWorkspaces"></a>[ListWorkspaces](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-and-IAM.html) | List workspaces | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
