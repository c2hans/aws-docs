---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_ListDocumentVersions_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDocumentVersions` with a CLI
<a name="ssm_example_ssm_ListDocumentVersions_section"></a>

The following code examples show how to use `ListDocumentVersions`.

------
#### [ CLI ]

**AWS CLI**
**To list document versions**
The following `list-document-versions` example lists all versions for a Systems Manager document.

```
aws ssm list-document-versions \
    --name {{"Example"}}
```
Output:

```
{
    "DocumentVersions": [
        {
            "Name": "Example",
            "DocumentVersion": "1",
            "CreatedDate": 1583257938.266,
            "IsDefaultVersion": true,
            "DocumentFormat": "YAML",
            "Status": "Active"
        }
    ]
}
```
For more information, see [Sending Commands that Use the Document Version Parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-version.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [ListDocumentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-versions.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists all the versions for a document.**

```
Get-SSMDocumentVersionList -Name "AWS-UpdateSSMAgent"
```
**Output:**

```
CreatedDate       : 6/1/2021 5:19:10 PM
DocumentFormat    : JSON
DocumentVersion   : 1
IsDefaultVersion  : True
Name              : AWS-UpdateSSMAgent
Status            : Active
```
+  For API details, see [ListDocumentVersions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists all the versions for a document.**

```
Get-SSMDocumentVersionList -Name "AWS-UpdateSSMAgent"
```
**Output:**

```
CreatedDate       : 6/1/2021 5:19:10 PM
DocumentFormat    : JSON
DocumentVersion   : 1
IsDefaultVersion  : True
Name              : AWS-UpdateSSMAgent
Status            : Active
```
+  For API details, see [ListDocumentVersions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
