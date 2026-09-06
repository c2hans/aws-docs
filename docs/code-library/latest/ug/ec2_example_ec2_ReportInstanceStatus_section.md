---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ReportInstanceStatus_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ReportInstanceStatus` with a CLI
<a name="ec2_example_ec2_ReportInstanceStatus_section"></a>

The following code examples show how to use `ReportInstanceStatus`.

------
#### [ CLI ]

**AWS CLI**
**To report status feedback for an instance**
This example command reports status feedback for the specified instance.
Command:

```
aws ec2 report-instance-status --instances {{i-1234567890abcdef0}} --status {{impaired}} --reason-codes {{unresponsive}}
```
+  For API details, see [ReportInstanceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/report-instance-status.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example reports status feedback for the specified instance.**

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive
```
+  For API details, see [ReportInstanceStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example reports status feedback for the specified instance.**

```
Send-EC2InstanceStatus -Instance i-12345678 -Status impaired -ReasonCode unresponsive
```
+  For API details, see [ReportInstanceStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
