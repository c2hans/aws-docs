---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_RemoveTagsFromOnPremisesInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RemoveTagsFromOnPremisesInstances` with a CLI
<a name="codedeploy_example_codedeploy_RemoveTagsFromOnPremisesInstances_section"></a>

The following code examples show how to use `RemoveTagsFromOnPremisesInstances`.

------
#### [ CLI ]

**AWS CLI**
**To remove tags from one or more on-premises instances**
The following `remove-tags-from-on-premises-instances` example disassociates the specified on-premises tags in AWS CodeDeploy from on-premises instances. It does not deregister the on-premises instances in AWS CodeDeploy, nor uninstall the AWS CodeDeploy Agent from the instance, nor remove the on-premises configuration file from the instances, nor delete the IAM users that are associated with the instances.

```
aws deploy remove-tags-from-on-premises-instances \
    --instance-names {{AssetTag12010298EX}} {{AssetTag23121309EX}} \
    --tags {{Key=Name,Value=CodeDeployDemo-OnPrem}}
```
This command produces no output.
+  For API details, see [RemoveTagsFromOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/remove-tags-from-on-premises-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified tag for the on-premises instance with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the tag without a prompt.**

```
Remove-CDOnPremiseInstanceTag -InstanceName AssetTag12010298EX -Tag @{"Key" = "Name"; "Value" = "CodeDeployDemo-OnPrem"}
```
+  For API details, see [RemoveTagsFromOnPremisesInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified tag for the on-premises instance with the specified name. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the tag without a prompt.**

```
Remove-CDOnPremiseInstanceTag -InstanceName AssetTag12010298EX -Tag @{"Key" = "Name"; "Value" = "CodeDeployDemo-OnPrem"}
```
+  For API details, see [RemoveTagsFromOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
