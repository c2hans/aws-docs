---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ModifyIdFormat_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyIdFormat` with a CLI
<a name="ec2_example_ec2_ModifyIdFormat_section"></a>

The following code examples show how to use `ModifyIdFormat`.

------
#### [ CLI ]

**AWS CLI**
**To enable the longer ID format for a resource**
The following `modify-id-format` example enables the longer ID format for the `instance` resource type.

```
aws ec2 modify-id-format \
    --resource {{instance}} \
    --use-long-ids
```
**To disable the longer ID format for a resource**
The following `modify-id-format` example disables the longer ID format for the `instance` resource type.

```
aws ec2 modify-id-format \
    --resource {{instance}} \
    --no-use-long-ids
```
The following `modify-id-format` example enables the longer ID format for all supported resource types that are within their opt-in period.

```
aws ec2 modify-id-format \
    --resource {{all-current}} \
    --use-long-ids
```
+  For API details, see [ModifyIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-id-format.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $true
```
**Example 2: This example disables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $false
```
+  For API details, see [ModifyIdFormat](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $true
```
**Example 2: This example disables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $false
```
+  For API details, see [ModifyIdFormat](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
