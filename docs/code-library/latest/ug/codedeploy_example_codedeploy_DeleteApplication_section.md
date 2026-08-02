---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_DeleteApplication_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteApplication` with a CLI
<a name="codedeploy_example_codedeploy_DeleteApplication_section"></a>

The following code examples show how to use `DeleteApplication`.

------
#### [ CLI ]

**AWS CLI**
**To delete an application**
The following `delete-application` example deletes the specified application that is associated with the user's AWS account.

```
aws deploy delete-application --application-name {{WordPress_App}}
```
This command produces no output.
+  For API details, see [DeleteApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/delete-application.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the application with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the application without a prompt.**

```
Remove-CDApplication -ApplicationName MyNewApplication
```
+  For API details, see [DeleteApplication](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the application with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the application without a prompt.**

```
Remove-CDApplication -ApplicationName MyNewApplication
```
+  For API details, see [DeleteApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
