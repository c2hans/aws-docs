---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_RegisterOnPremisesInstance_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RegisterOnPremisesInstance` with a CLI
<a name="codedeploy_example_codedeploy_RegisterOnPremisesInstance_section"></a>

The following code examples show how to use `RegisterOnPremisesInstance`.

------
#### [ CLI ]

**AWS CLI**
**To register an on-premises instance**
The following `register-on-premises-instance` example registers an on-premises instance with AWS CodeDeploy. It does not create the specified IAM user, nor does it associate in AWS CodeDeploy any on-premises instances tags with the registered instance.

```
aws deploy register-on-premises-instance \
    --instance-name {{AssetTag12010298EX}} \
    --iam-user-arn {{arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser-OnPrem}}
```
This command produces no output.
+  For API details, see [RegisterOnPremisesInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-on-premises-instance.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example registers an on-premises instance with the specified name and IAM user.**

```
Register-CDOnPremiseInstance -IamUserArn arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser -InstanceName AssetTag12010298EX
```
+  For API details, see [RegisterOnPremisesInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example registers an on-premises instance with the specified name and IAM user.**

```
Register-CDOnPremiseInstance -IamUserArn arn:aws:iam::80398EXAMPLE:user/CodeDeployDemoUser -InstanceName AssetTag12010298EX
```
+  For API details, see [RegisterOnPremisesInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
