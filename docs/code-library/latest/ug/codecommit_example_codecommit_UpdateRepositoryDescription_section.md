---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_UpdateRepositoryDescription_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateRepositoryDescription` with a CLI
<a name="codecommit_example_codecommit_UpdateRepositoryDescription_section"></a>

The following code examples show how to use `UpdateRepositoryDescription`.

------
#### [ CLI ]

**AWS CLI**
**To change the description for a repository**
This example changes the description for an AWS CodeCommit repository. This command produces output only if there are errors.
Command:

```
aws codecommit update-repository-description --repository-name {{MyDemoRepo}} --repository-description {{"This description was changed"}}
```
Output:

```
None.
```
+  For API details, see [UpdateRepositoryDescription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-description.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the description for the specified repository.**

```
Update-CCRepositoryDescription -RepositoryName MyDemoRepo -RepositoryDescription "This is an updated description."
```
+  For API details, see [UpdateRepositoryDescription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the description for the specified repository.**

```
Update-CCRepositoryDescription -RepositoryName MyDemoRepo -RepositoryDescription "This is an updated description."
```
+  For API details, see [UpdateRepositoryDescription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
