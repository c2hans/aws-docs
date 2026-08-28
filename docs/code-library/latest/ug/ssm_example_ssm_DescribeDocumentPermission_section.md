---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_DescribeDocumentPermission_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeDocumentPermission` with a CLI
<a name="ssm_example_ssm_DescribeDocumentPermission_section"></a>

The following code examples show how to use `DescribeDocumentPermission`.

------
#### [ CLI ]

**AWS CLI**
**To describe document permissions**
The following `describe-document-permission` example displays permission details about a Systems Manager document that is shared publicly.

```
aws ssm describe-document-permission \
    --name {{"Example"}} \
    --permission-type {{"Share"}}
```
Output:

```
{
    "AccountIds": [
        "all"
    ],
    "AccountSharingInfoList": [
        {
            "AccountId": "all",
            "SharedDocumentVersion": "$DEFAULT"
        }
    ]
}
```
For more information, see [Share a Systems Manager Document](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-how-to-share.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [DescribeDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists all the versions for a document.**

```
Get-SSMDocumentVersionList -Name "RunShellScript"
```
**Output:**

```
CreatedDate          DocumentVersion IsDefaultVersion Name
-----------          --------------- ---------------- ----
2/24/2017 5:25:13 AM 1               True             RunShellScript
```
+  For API details, see [DescribeDocumentPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists all the versions for a document.**

```
Get-SSMDocumentVersionList -Name "RunShellScript"
```
**Output:**

```
CreatedDate          DocumentVersion IsDefaultVersion Name
-----------          --------------- ---------------- ----
2/24/2017 5:25:13 AM 1               True             RunShellScript
```
+  For API details, see [DescribeDocumentPermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
