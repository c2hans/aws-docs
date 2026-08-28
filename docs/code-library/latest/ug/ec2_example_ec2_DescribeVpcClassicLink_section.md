---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DescribeVpcClassicLink_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeVpcClassicLink` with a CLI
<a name="ec2_example_ec2_DescribeVpcClassicLink_section"></a>

The following code examples show how to use `DescribeVpcClassicLink`.

------
#### [ CLI ]

**AWS CLI**
**To describe the ClassicLink status of your VPCs**
This example lists the ClassicLink status of vpc-88888888.
Command:

```
aws ec2 describe-vpc-classic-link --vpc-id {{vpc-88888888}}
```
Output:

```
{
  "Vpcs": [
    {
      "ClassicLinkEnabled": true,
      "VpcId": "vpc-88888888",
      "Tags": [
        {
          "Value": "classiclinkvpc",
          "Key": "Name"
        }
      ]
    }
  ]
}
```
This example lists only VPCs that are enabled for Classiclink (the filter value of `is-classic-link-enabled` is set to `true`).
Command:

```
aws ec2 describe-vpc-classic-link --filter {{"Name=is-classic-link-enabled,Values=true"}}
```
+  For API details, see [DescribeVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-classic-link.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Above example returns all the VPCs with their ClassicLinkEnabled state for the region**

```
Get-EC2VpcClassicLink -Region eu-west-1
```
**Output:**

```
ClassicLinkEnabled Tags   VpcId
------------------ ----   -----
False              {Name} vpc-0fc1ff23f45b678eb
False              {}     vpc-01e23c4a5d6db78e9
False              {Name} vpc-0123456b078b9d01f
False              {}     vpc-12cf3b4f
False              {Name} vpc-0b12d3456a7e8901d
```
+  For API details, see [DescribeVpcClassicLink](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Above example returns all the VPCs with their ClassicLinkEnabled state for the region**

```
Get-EC2VpcClassicLink -Region eu-west-1
```
**Output:**

```
ClassicLinkEnabled Tags   VpcId
------------------ ----   -----
False              {Name} vpc-0fc1ff23f45b678eb
False              {}     vpc-01e23c4a5d6db78e9
False              {Name} vpc-0123456b078b9d01f
False              {}     vpc-12cf3b4f
False              {Name} vpc-0b12d3456a7e8901d
```
+  For API details, see [DescribeVpcClassicLink](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
