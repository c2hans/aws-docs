---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_UpdateDocumentDefaultVersion_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateDocumentDefaultVersion` with a CLI
<a name="ssm_example_ssm_UpdateDocumentDefaultVersion_section"></a>

The following code examples show how to use `UpdateDocumentDefaultVersion`.

------
#### [ CLI ]

**AWS CLI**
**To update the default version of a document**
The following `update-document-default-version` example updates the default version of a Systems Manager document.

```
aws ssm update-document-default-version \
    --name {{"Example"}} \
    --document-version {{"2"}}
```
Output:

```
{
    "Description": {
        "Name": "Example",
        "DefaultVersion": "2"
    }
}
```
For more information, see [Writing SSM Document Content](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html#writing-ssm-doc-content) in the *AWS Systems Manager User Guide*.
+  For API details, see [UpdateDocumentDefaultVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document-default-version.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This updates the default version of a document. You can obtain the available document versions with the "Get-SSMDocumentVersionList" cmdlet.**

```
Update-SSMDocumentDefaultVersion -Name "RunShellScript" -DocumentVersion "2"
```
**Output:**

```
DefaultVersion Name
-------------- ----
2              RunShellScript
```
+  For API details, see [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This updates the default version of a document. You can obtain the available document versions with the "Get-SSMDocumentVersionList" cmdlet.**

```
Update-SSMDocumentDefaultVersion -Name "RunShellScript" -DocumentVersion "2"
```
**Output:**

```
DefaultVersion Name
-------------- ----
2              RunShellScript
```
+  For API details, see [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
