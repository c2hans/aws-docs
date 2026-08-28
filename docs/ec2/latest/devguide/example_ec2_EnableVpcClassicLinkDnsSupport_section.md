---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_EnableVpcClassicLinkDnsSupport_section.html
---

# Use `EnableVpcClassicLinkDnsSupport` with a CLI
<a name="example_ec2_EnableVpcClassicLinkDnsSupport_section"></a>

The following code examples show how to use `EnableVpcClassicLinkDnsSupport`.

------
#### [ CLI ]

**AWS CLI**
**To enable ClassicLink DNS support for a VPC**
This example enables ClassicLink DNS support for `vpc-88888888`.
Command:

```
aws ec2 enable-vpc-classic-link-dns-support --vpc-id {{vpc-88888888}}
```
Output:

```
{
  "Return": true
}
```
+  For API details, see [EnableVpcClassicLinkDnsSupport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vpc-classic-link-dns-support.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables vpc-0b12d3456a7e8910d to support DNS hostname resolution for ClassicLink**

```
Enable-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d -Region eu-west-1
```
+  For API details, see [EnableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables vpc-0b12d3456a7e8910d to support DNS hostname resolution for ClassicLink**

```
Enable-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d -Region eu-west-1
```
+  For API details, see [EnableVpcClassicLinkDnsSupport](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
