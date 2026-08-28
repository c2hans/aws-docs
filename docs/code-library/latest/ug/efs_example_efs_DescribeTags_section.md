---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/efs_example_efs_DescribeTags_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeTags` with a CLI
<a name="efs_example_efs_DescribeTags_section"></a>

The following code examples show how to use `DescribeTags`.

------
#### [ CLI ]

**AWS CLI**
**To describe the tags for a file system**
The following `describe-tags` example describes the tags for the specified file system.

```
aws efs describe-tags \
    --file-system-id {{fs-c7a0456e}}
```
Output:

```
{
    "Tags": [
        {
            "Key": "Name",
            "Value": "my-file-system"
        },
        {
            "Key": "Department",
            "Value": "Business Intelligence"
        }
    ]
}
```
For more information, see [Managing file system tags](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-tags.html) in the *Amazon Elastic File System User Guide*.
+  For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-tags.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the collection of tags currently associated with the specified file system.**

```
Get-EFSTag -FileSystemId fs-1a2b3c4d
```
**Output:**

```
Key         Value
---         -----
Name        My File System
tagkey1     tagvalue1
tagkey2     tagvalue2
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the collection of tags currently associated with the specified file system.**

```
Get-EFSTag -FileSystemId fs-1a2b3c4d
```
**Output:**

```
Key         Value
---         -----
Name        My File System
tagkey1     tagvalue1
tagkey2     tagvalue2
```
+  For API details, see [DescribeTags](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
