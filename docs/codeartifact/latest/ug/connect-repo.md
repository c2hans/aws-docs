---
source_url: https://docs.aws.amazon.com/codeartifact/latest/ug/connect-repo.html
---

# Connect to a repository
<a name="connect-repo"></a>

After you have configured your profile and credentials to authenticate to your AWS account, decide which repository to use in CodeArtifact. You have the following options:
+ Create a repository. For more information, see [Creating a Repository](create-repo.md).
+ Use a repository that already exists in your account. You can use the `list-repositories` command to find the repositories created in your AWS account. For more information, see [List repositories](list-repos.md).
+ Use a repository in a different AWS account. For more information, see [Repository policies](repo-policies.md).

## Use a package manager client
<a name="using-a-package-manager-client"></a>

After you know which repository you want to use, see one of the following topics.
+ [Using CodeArtifact with Maven](using-maven.md)
+ [Using CodeArtifact with npm](using-npm.md)
+ [Using CodeArtifact with NuGet](using-nuget.md)
+ [Using CodeArtifact with Python](using-python.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
