---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_CreateDeploymentGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateDeploymentGroup` with a CLI
<a name="codedeploy_example_codedeploy_CreateDeploymentGroup_section"></a>

The following code examples show how to use `CreateDeploymentGroup`.

------
#### [ CLI ]

**AWS CLI**
**To create a deployment group**
The following `create-deployment-group` example creates a deployment group and associates it with the specified application and the user's AWS account.

```
aws deploy create-deployment-group \
    --application-name {{WordPress_App}} \
    --auto-scaling-groups {{CodeDeployDemo-ASG}} \
    --deployment-config-name {{CodeDeployDefault.OneAtATime}} \
    --deployment-group-name {{WordPress_DG}} \
    --ec2-tag-filters {{Key=Name,Value=CodeDeployDemo,Type=KEY_AND_VALUE}} \
    --service-role-arn {{arn:aws:iam::123456789012:role/CodeDeployDemoRole}}
```
Output:

```
{
    "deploymentGroupId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
}
```
+  For API details, see [CreateDeploymentGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/create-deployment-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a deployment group with the specified name, Auto Scaling group, deployment configuration, tag, and service role, for the specified application.**

```
New-CDDeploymentGroup -ApplicationName MyNewApplication -AutoScalingGroup CodeDeployDemo-ASG -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -Ec2TagFilter @{Key="Name"; Type="KEY_AND_VALUE"; Value="CodeDeployDemo"} -ServiceRoleArn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo
```
**Output:**

```
16bbf199-95fd-40fc-a909-0bbcfEXAMPLE
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
New-CDDeploymentGroup -ApplicationName MyNewApplication -AutoScalingGroup CodeDeployDemo-ASG -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -Ec2TagFilter @{Key="Name"; Type="KEY_AND_VALUE"; Value="CodeDeployDemo"} -ServiceRoleArn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
**Output:**

```
16bbf199-95fd-40fc-a909-0bbcfEXAMPLE
```
+  For API details, see [CreateDeploymentGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a deployment group with the specified name, Auto Scaling group, deployment configuration, tag, and service role, for the specified application.**

```
New-CDDeploymentGroup -ApplicationName MyNewApplication -AutoScalingGroup CodeDeployDemo-ASG -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -Ec2TagFilter @{Key="Name"; Type="KEY_AND_VALUE"; Value="CodeDeployDemo"} -ServiceRoleArn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo
```
**Output:**

```
16bbf199-95fd-40fc-a909-0bbcfEXAMPLE
```
**Example 2: This example shows how to specify groups of EC2 instance tags that an instance must be identified by in order for it to be included in the replacement environment for a blue/green deployment.**

```
New-CDDeploymentGroup -ApplicationName MyNewApplication -AutoScalingGroup CodeDeployDemo-ASG -DeploymentConfigName CodeDeployDefault.OneAtATime -DeploymentGroupName MyNewDeploymentGroup -Ec2TagFilter @{Key="Name"; Type="KEY_AND_VALUE"; Value="CodeDeployDemo"} -ServiceRoleArn arn:aws:iam::80398EXAMPLE:role/CodeDeployDemo -Ec2TagSetList @(@{Key="key1";Type="KEY_ONLY"},@{Key="Key2";Type="KEY_AND_VALUE";Value="Value2"}),@(@{Key="Key3";Type="VALUE_ONLY";Value="Value3"})
```
**Output:**

```
16bbf199-95fd-40fc-a909-0bbcfEXAMPLE
```
+  For API details, see [CreateDeploymentGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
