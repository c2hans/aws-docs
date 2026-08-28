---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ModifyHosts_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyHosts` with a CLI
<a name="ec2_example_ec2_ModifyHosts_section"></a>

The following code examples show how to use `ModifyHosts`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To enable auto-placement for a Dedicated Host**
The following `modify-hosts` example enables auto-placement for a Dedicated Host so that it accepts any untargeted instance launches that match its instance type configuration.

```
aws ec2 modify-hosts \
    --host-id {{h-06c2f189b4EXAMPLE}} \
    --auto-placement {{on}}
```
Output:

```
{
    "Successful": [
        "h-06c2f189b4EXAMPLE"
    ],
    "Unsuccessful": []
}
```
For more information, see [Modify the auto-placement setting for a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-host-auto-placement.html) in the *Amazon EC2 User Guide*.
**Example 2: To enable host recovery for a Dedicated Host**
The following `modify-hosts` example enables host recovery for the specified Dedicated Host.

```
aws ec2 modify-hosts \
    --host-id {{h-06c2f189b4EXAMPLE}} \
    --host-recovery {{on}}
```
Output:

```
{
    "Successful": [
        "h-06c2f189b4EXAMPLE"
    ],
    "Unsuccessful": []
}
```
For more information, see [Modify the auto-placement setting for a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-host-auto-placement.html) in the *Amazon EC2 User Guide*.
+  For API details, see [ModifyHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-hosts.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example modifies the AutoPlacement settings to off for the dedicated host h-01e23f4cd567890f3**

```
Edit-EC2Host -HostId h-03e09f8cd681609f3 -AutoPlacement off
```
**Output:**

```
Successful            Unsuccessful
----------            ------------
{h-01e23f4cd567890f3} {}
```
+  For API details, see [ModifyHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example modifies the AutoPlacement settings to off for the dedicated host h-01e23f4cd567890f3**

```
Edit-EC2Host -HostId h-03e09f8cd681609f3 -AutoPlacement off
```
**Output:**

```
Successful            Unsuccessful
----------            ------------
{h-01e23f4cd567890f3} {}
```
+  For API details, see [ModifyHosts](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
