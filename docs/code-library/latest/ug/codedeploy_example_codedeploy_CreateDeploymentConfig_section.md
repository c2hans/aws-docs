---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_CreateDeploymentConfig_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateDeploymentConfig` with a CLI
<a name="codedeploy_example_codedeploy_CreateDeploymentConfig_section"></a>

The following code examples show how to use `CreateDeploymentConfig`.

------
#### [ CLI ]

**AWS CLI**
**To create a custom deployment configuration**
The following `create-deployment-config` example creates a custom deployment configuration and associates it with the user's AWS account.

```
aws deploy create-deployment-config \
    --deployment-config-name {{ThreeQuartersHealthy}} \
    --minimum-healthy-hosts {{type=FLEET_PERCENT,value=75}}
```
Output:

```
{
    "deploymentConfigId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
}
```
+  For API details, see [CreateDeploymentConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-config.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new deployment configuration with the specified name and behavior.**

```
New-CDDeploymentConfig -DeploymentConfigName AtLeastTwoHealthyHosts -MinimumHealthyHosts_Type HOST_COUNT -MinimumHealthyHosts_Value 2
```
**Output:**

```
0f3e8187-44ef-42da-aeed-b6823EXAMPLE
```
+  For API details, see [CreateDeploymentConfig](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new deployment configuration with the specified name and behavior.**

```
New-CDDeploymentConfig -DeploymentConfigName AtLeastTwoHealthyHosts -MinimumHealthyHosts_Type HOST_COUNT -MinimumHealthyHosts_Value 2
```
**Output:**

```
0f3e8187-44ef-42da-aeed-b6823EXAMPLE
```
+  For API details, see [CreateDeploymentConfig](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
