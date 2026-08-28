---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_UntagRole_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UntagRole` with a CLI
<a name="iam_example_iam_UntagRole_section"></a>

The following code examples show how to use `UntagRole`.

------
#### [ CLI ]

**AWS CLI**
**To remove a tag from a role**
The following `untag-role` command removes any tag with the key name 'Department' from the specified role.

```
aws iam untag-role \
    --role-name {{my-role}} \
    --tag-keys {{Department}}
```
This command produces no output.
For more information, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *AWS IAM User Guide*.
+  For API details, see [UntagRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/untag-role.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"
```
+  For API details, see [UntagRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the tag from the role named "MyRoleName" with tag key as "abac". To remove multiple tags, provide a comma separted tag keys list.**

```
Remove-IAMRoleTag -RoleName MyRoleName -TagKey "abac","xyzw"
```
+  For API details, see [UntagRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
