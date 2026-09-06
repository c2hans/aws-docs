---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListOnPremisesInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListOnPremisesInstances` with a CLI
<a name="codedeploy_example_codedeploy_ListOnPremisesInstances_section"></a>

The following code examples show how to use `ListOnPremisesInstances`.

------
#### [ CLI ]

**AWS CLI**
**To get information about one or more on-premises instances**
The following `list-on-premises-instances` example retrieves a list of available on-premises instance names for instances that are registered in AWS CodeDeploy and also have the specified on-premises instance tag associated in AWS CodeDeploy with the instance.

```
aws deploy list-on-premises-instances \
    --registration-status {{Registered}} \
    --tag-filters {{Key=Name,Value=CodeDeployDemo-OnPrem,Type=KEY_AND_VALUE}}
```
Output:

```
{
    "instanceNames": [
        "AssetTag12010298EX"
    ]
}
```
+  For API details, see [ListOnPremisesInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-on-premises-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of available on-premises instance names.**

```
Get-CDOnPremiseInstanceList
```
**Output:**

```
AssetTag12010298EX
AssetTag12010298EX-2
```
+  For API details, see [ListOnPremisesInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available on-premises instance names.**

```
Get-CDOnPremiseInstanceList
```
**Output:**

```
AssetTag12010298EX
AssetTag12010298EX-2
```
+  For API details, see [ListOnPremisesInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
