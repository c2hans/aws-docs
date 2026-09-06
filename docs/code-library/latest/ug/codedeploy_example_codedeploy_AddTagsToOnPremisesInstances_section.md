---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_AddTagsToOnPremisesInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `AddTagsToOnPremisesInstances` with a CLI
<a name="codedeploy_example_codedeploy_AddTagsToOnPremisesInstances_section"></a>

The following code examples show how to use `AddTagsToOnPremisesInstances`.

------
#### [ CLI ]

**AWS CLI**
**To add tags to on-premises instances**
The following `add-tags-to-on-premises-instances` example associates in AWS CodeDeploy the same on-premises instance tag to two on-premises instances. It does not register the on-premises instances with AWS CodeDeploy.

```
aws deploy add-tags-to-on-premises-instances \
    --instance-names {{AssetTag12010298EX}} {{AssetTag23121309EX}} \
    --tags {{Key=Name,Value=CodeDeployDemo-OnPrem}}
```
This command produces no output.
+  For API details, see [AddTagsToOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/add-tags-to-on-premises-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds an on-premises instance tag with the specified key and value for the specified on-premises instance.**

```
Add-CDOnPremiseInstanceTag -InstanceName AssetTag12010298EX -Tag @{"Key" = "Name"; "Value" = "CodeDeployDemo-OnPrem"}
```
+  For API details, see [AddTagsToOnPremisesInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds an on-premises instance tag with the specified key and value for the specified on-premises instance.**

```
Add-CDOnPremiseInstanceTag -InstanceName AssetTag12010298EX -Tag @{"Key" = "Name"; "Value" = "CodeDeployDemo-OnPrem"}
```
+  For API details, see [AddTagsToOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
