---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListApplications_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListApplications` with a CLI
<a name="codedeploy_example_codedeploy_ListApplications_section"></a>

The following code examples show how to use `ListApplications`.

------
#### [ CLI ]

**AWS CLI**
**To get information about applications**
The following `list-applications` example displays information about all applications that are associated with the user's AWS account.

```
aws deploy list-applications
```
Output:

```
{
    "applications": [
        "WordPress_App",
        "MyOther_App"
    ]
}
```
+  For API details, see [ListApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-applications.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of available applications.**

```
Get-CDApplicationList
```
**Output:**

```
CodeDeployDemoApplication
CodePipelineDemoApplication
```
+  For API details, see [ListApplications](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available applications.**

```
Get-CDApplicationList
```
**Output:**

```
CodeDeployDemoApplication
CodePipelineDemoApplication
```
+  For API details, see [ListApplications](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
