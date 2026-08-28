---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_CreatePlacementGroup_section.html
---

# Use `CreatePlacementGroup` with a CLI
<a name="example_ec2_CreatePlacementGroup_section"></a>

The following code examples show how to use `CreatePlacementGroup`.

------
#### [ CLI ]

**AWS CLI**
**To create a placement group**
This example command creates a placement group with the specified name.
Command:

```
aws ec2 create-placement-group --group-name {{my-cluster}} --strategy {{cluster}}
```
**To create a partition placement group**
This example command creates a partition placement group named `HDFS-Group-A` with five partitions.
Command:

```
aws ec2 create-placement-group --group-name {{HDFS-Group-A}} --strategy {{partition}} --partition-count {{5}}
```
+  For API details, see [CreatePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-placement-group.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a placement group with the specified name.**

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster
```
+  For API details, see [CreatePlacementGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a placement group with the specified name.**

```
New-EC2PlacementGroup -GroupName my-placement-group -Strategy cluster
```
+  For API details, see [CreatePlacementGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
