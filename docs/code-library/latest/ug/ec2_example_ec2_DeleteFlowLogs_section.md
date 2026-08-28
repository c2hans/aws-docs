---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DeleteFlowLogs_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteFlowLogs` with a CLI
<a name="ec2_example_ec2_DeleteFlowLogs_section"></a>

The following code examples show how to use `DeleteFlowLogs`.

------
#### [ CLI ]

**AWS CLI**
**To delete a flow log**
The following `delete-flow-logs` example deletes the specified flow log.

```
aws ec2 delete-flow-logs --flow-log-id {{fl-11223344556677889}}
```
Output:

```
{
    "Unsuccessful": []
}
```
+  For API details, see [DeleteFlowLogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example removes the given FlowLogId fl-01a2b3456a789c01**

```
Remove-EC2FlowLog -FlowLogId fl-01a2b3456a789c01
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2FlowLog (DeleteFlowLogs)" on target "fl-01a2b3456a789c01".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteFlowLogs](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example removes the given FlowLogId fl-01a2b3456a789c01**

```
Remove-EC2FlowLog -FlowLogId fl-01a2b3456a789c01
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2FlowLog (DeleteFlowLogs)" on target "fl-01a2b3456a789c01".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteFlowLogs](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
