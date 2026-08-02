---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_UpdateDeploymentGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateDeploymentGroup` with a CLI
<a name="codedeploy_example_codedeploy_UpdateDeploymentGroup_section"></a>

The following code examples show how to use `UpdateDeploymentGroup`.

------
#### [ CLI ]

**AWS CLI**
**To change information about a deployment group**
The following `update-deployment-group` example changes the settings of a deployment group that is associated with the specified application.

```
aws deploy update-deployment-group \
    --application-name {{WordPress_App}} \
    --auto-scaling-groups {{My_CodeDeployDemo_ASG}} \
    --current-deployment-group-name {{WordPress_DG}} \
    --deployment-config-name {{CodeDeployDefault.AllAtOnce}} \
    --ec2-tag-filters {{Key=Name,Type=KEY_AND_VALUE,Value=My_CodeDeployDemo}} \
    --new-deployment-group-name {{My_WordPress_DepGroup}} \
    --service-role-arn {{arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo-2}}
```
This command produces no output.
+  For API details, see [UpdateDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/update-deployment-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the name of the specified deployment group for the specified application.**

```
Update-CDDeploymentGroup -ApplicationName MyNewApplication -CurrentDeploymentGroupName MyNewDeploymentGroup -NewDeploymentGroupName MyNewDeploymentGroup-2
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
Update-CDDeploymentGroup -ApplicationName MyNewApplication -CurrentDeploymentGroupName MyNewDeploymentGroup -NewDeploymentGroupName MyNewDeploymentGroup-2 -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
+  For API details, see [UpdateDeploymentGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the name of the specified deployment group for the specified application.**

```
Update-CDDeploymentGroup -ApplicationName MyNewApplication -CurrentDeploymentGroupName MyNewDeploymentGroup -NewDeploymentGroupName MyNewDeploymentGroup-2
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
Update-CDDeploymentGroup -ApplicationName MyNewApplication -CurrentDeploymentGroupName MyNewDeploymentGroup -NewDeploymentGroupName MyNewDeploymentGroup-2 -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
+  For API details, see [UpdateDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
