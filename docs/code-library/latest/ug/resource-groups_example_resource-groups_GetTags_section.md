---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups_example_resource-groups_GetTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetTags` with a CLI
<a name="resource-groups_example_resource-groups_GetTags_section"></a>

The following code examples show how to use `GetTags`.

------
#### [ CLI ]

**AWS CLI**
**To retrieve the tags attached to a resource group**
The following `get-tags` example displays the tag key and value pairs attached to the specified resource group (the group itself, not its members).

```
aws resource-groups get-tags \
    --arn {{arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer}}
```
Output:

```
{
    "Arn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer",
    "Tags": {
        "QueryType": "tags",
        "QueryResources": "ec2-instances"
    }
}
```
+  For API details, see [GetTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists tags for the given resource group arn**

```
Get-RGResourceTag -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes
```
**Output:**

```
Key       Value
---       -----
Instances workboxes
```
+  For API details, see [GetTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists tags for the given resource group arn**

```
Get-RGResourceTag -Arn arn:aws:resource-groups:eu-west-1:123456789012:group/workboxes
```
**Output:**

```
Key       Value
---       -----
Instances workboxes
```
+  For API details, see [GetTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
