---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/iam_example_iam_PutGroupPolicy_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutGroupPolicy` with a CLI
<a name="iam_example_iam_PutGroupPolicy_section"></a>

The following code examples show how to use `PutGroupPolicy`.

------
#### [ CLI ]

**AWS CLI**
**To add a policy to a group**
The following `put-group-policy` command adds a policy to the IAM group named `Admins`.

```
aws iam put-group-policy \
    --group-name {{Admins}} \
    --policy-document {{file://AdminPolicy.json}} \
    --policy-name {{AdminRoot}}
```
This command produces no output.
The policy is defined as a JSON document in the *AdminPolicy.json* file. (The file name and extension do not have significance.)
For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *AWS IAM User Guide*.
+  For API details, see [PutGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/put-group-policy.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates an inline policy named `AppTesterPolicy` and embeds it in the IAM group `AppTesters`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes the file `apptesterpolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMGroupPolicy -GroupName AppTesters -PolicyName AppTesterPolicy -PolicyDocument (Get-Content -Raw apptesterpolicy.json)
```
+  For API details, see [PutGroupPolicy](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates an inline policy named `AppTesterPolicy` and embeds it in the IAM group `AppTesters`. If an inline policy with the same name already exists, then it is overwritten. The JSON policy content comes the file `apptesterpolicy.json`. Note that you must use the `-Raw` parameter to successfully process the content of the JSON file.**

```
Write-IAMGroupPolicy -GroupName AppTesters -PolicyName AppTesterPolicy -PolicyDocument (Get-Content -Raw apptesterpolicy.json)
```
+  For API details, see [PutGroupPolicy](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
