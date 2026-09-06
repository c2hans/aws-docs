---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_Tag_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `Tag` with a CLI
<a name="resource-groups_example_resource-groups_Tag_section"></a>

The following code examples show how to use `Tag`.

------
#### [ CLI ]

**AWS CLI**
**To attach a tag to a resource group**
The following `tag` example attaches the specified tag key and value pairs to the specified resource group (the group itself, not its members).

```
aws resource-groups tag \
    --tags {{QueryType=tags,QueryResources=ec2-instances}} \
    --arn {{arn:aws:resource-groups:us-west-2:128716708097:group/tbq-WebServer}}
```
Output:

```
{
    "Arn": "arn:aws:resource-groups:us-west-2:128716708097:group/tbq-WebServer",
    "Tags": {
        "QueryType": "tags",
        "QueryResources": "ec2-instances"
    }
}
```
For more information, see [Manage tags](https://docs.aws.amazon.com/ARG/latest/userguide/tagging-resources.html) in the *AWS Resource Groups User Guide*.
+  For API details, see [Tag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/tag.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds tag key 'Instances' with value 'workboxes' to the given resource group arn**

```
Add-RGResourceTag -Tag @{Instances="workboxes"} -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes
```
**Output:**

```
Arn                                                            Tags
---                                                            ----
arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes {[Instances, workboxes]}
```
+  For API details, see [Tag](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds tag key 'Instances' with value 'workboxes' to the given resource group arn**

```
Add-RGResourceTag -Tag @{Instances="workboxes"} -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes
```
**Output:**

```
Arn                                                            Tags
---                                                            ----
arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes {[Instances, workboxes]}
```
+  For API details, see [Tag](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
