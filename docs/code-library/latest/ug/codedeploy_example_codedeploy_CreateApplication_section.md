---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_CreateApplication_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateApplication` with a CLI
<a name="codedeploy_example_codedeploy_CreateApplication_section"></a>

The following code examples show how to use `CreateApplication`.

------
#### [ CLI ]

**AWS CLI**
**To create an application**
The following `create-application` example creates an application and associates it with the user's AWS account.

```
aws deploy create-application --application-name {{MyOther_App}}
```
Output:

```
{
    "applicationId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
}
```
+  For API details, see [CreateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-application.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new application with the specified name.**

```
New-CDApplication -ApplicationName MyNewApplication
```
**Output:**

```
f19e4b61-2231-4328-b0fd-e57f5EXAMPLE
```
+  For API details, see [CreateApplication](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new application with the specified name.**

```
New-CDApplication -ApplicationName MyNewApplication
```
**Output:**

```
f19e4b61-2231-4328-b0fd-e57f5EXAMPLE
```
+  For API details, see [CreateApplication](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
