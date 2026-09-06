---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_DeregisterOnPremisesInstance_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeregisterOnPremisesInstance` with a CLI
<a name="codedeploy_example_codedeploy_DeregisterOnPremisesInstance_section"></a>

The following code examples show how to use `DeregisterOnPremisesInstance`.

------
#### [ CLI ]

**AWS CLI**
**To deregister an on-premises instance**
The following `deregister-on-premises-instance` example deregisters an on-premises instance with AWS CodeDeploy, but it does not delete the IAM user associated with the instance, nor does it disassociate in AWS CodeDeploy the on-premises instance tags from the instance. It also does not uninstall the AWS CodeDeploy Agent from the instance nor remove the on-premises configuration file from the instance.

```
aws deploy deregister-on-premises-instance --instance-name {{AssetTag12010298EX}}
```
This command produces no output.
+  For API details, see [DeregisterOnPremisesInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister-on-premises-instance.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deregisters the on-premises instance with the specified name.**

```
Unregister-CDOnPremiseInstance -InstanceName AssetTag12010298EX
```
+  For API details, see [DeregisterOnPremisesInstance](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deregisters the on-premises instance with the specified name.**

```
Unregister-CDOnPremiseInstance -InstanceName AssetTag12010298EX
```
+  For API details, see [DeregisterOnPremisesInstance](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
