---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListDeploymentInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDeploymentInstances` with a CLI
<a name="codedeploy_example_codedeploy_ListDeploymentInstances_section"></a>

The following code examples show how to use `ListDeploymentInstances`.

------
#### [ CLI ]

**AWS CLI**
**To get information about deployment instances**
The following `list-deployment-instances` example displays information about all deployment instances that are associated with the specified deployment.

```
aws deploy list-deployment-instances \
    --deployment-id {{d-A1B2C3111}} \
    --instance-status-filter {{Succeeded}}
```
Output:

```
{
    "instancesList": [
        "i-EXAMPLE11",
        "i-EXAMPLE22"
    ]
}
```
+  For API details, see [ListDeploymentInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-deployment-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of instance IDs for the specified deployment.**

```
Get-CDDeploymentInstanceList -DeploymentId d-QZMRGSTEX
```
**Output:**

```
i-254e22EX
i-274e22EX
i-3b4e22EX
```
+  For API details, see [ListDeploymentInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of instance IDs for the specified deployment.**

```
Get-CDDeploymentInstanceList -DeploymentId d-QZMRGSTEX
```
**Output:**

```
i-254e22EX
i-274e22EX
i-3b4e22EX
```
+  For API details, see [ListDeploymentInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
