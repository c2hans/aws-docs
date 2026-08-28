---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_UpdateEnvironment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateEnvironment` with a CLI
<a name="cloud9_example_cloud9_UpdateEnvironment_section"></a>

The following code examples show how to use `UpdateEnvironment`.

------
#### [ CLI ]

**AWS CLI**
**To change the settings of an existing AWS Cloud9 development environment**
This example changes the specified settings of the specified existing AWS Cloud9 development environment.
Command:

```
aws cloud9 update-environment --environment-id {{8a34f51ce1e04a08882f1e811bd706EX}} --name {{my-changed-demo-env}} --description {{"My changed demonstration development environment."}}
```
Output:

```
None.
```
+  For API details, see [UpdateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the specified settings of the specified existing AWS Cloud9 development environment.**

```
Update-C9Environment -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Description "My changed demonstration development environment." -Name my-changed-demo-env
```
+  For API details, see [UpdateEnvironment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the specified settings of the specified existing AWS Cloud9 development environment.**

```
Update-C9Environment -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Description "My changed demonstration development environment." -Name my-changed-demo-env
```
+  For API details, see [UpdateEnvironment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
