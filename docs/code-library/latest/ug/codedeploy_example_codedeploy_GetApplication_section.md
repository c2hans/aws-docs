---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_GetApplication_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetApplication` with a CLI
<a name="codedeploy_example_codedeploy_GetApplication_section"></a>

The following code examples show how to use `GetApplication`.

------
#### [ CLI ]

**AWS CLI**
**To get information about an application**
The following `get-application` example displays information about an application that is associated with the user's AWS account.

```
aws deploy get-application --application-name {{WordPress_App}}
```
Output:

```
{
    "application": {
        "applicationName": "WordPress_App",
        "applicationId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
        "createTime": 1407878168.078,
        "linkedToGitHub": false
    }
}
```
+  For API details, see [GetApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets information about the specified application.**

```
Get-CDApplication -ApplicationName CodeDeployDemoApplication
```
**Output:**

```
ApplicationId                           ApplicationName              CreateTime              LinkedToGitHub
-------------                           ---------------              ----------              --------------
e07fb938-091e-4f2f-8963-4d3e8EXAMPLE    CodeDeployDemoApplication    7/20/2015 9:49:48 PM    False
```
+  For API details, see [GetApplication](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified application.**

```
Get-CDApplication -ApplicationName CodeDeployDemoApplication
```
**Output:**

```
ApplicationId                           ApplicationName              CreateTime              LinkedToGitHub
-------------                           ---------------              ----------              --------------
e07fb938-091e-4f2f-8963-4d3e8EXAMPLE    CodeDeployDemoApplication    7/20/2015 9:49:48 PM    False
```
+  For API details, see [GetApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
