---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ModifyVpcAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyVpcAttribute` with a CLI
<a name="ec2_example_ec2_ModifyVpcAttribute_section"></a>

The following code examples show how to use `ModifyVpcAttribute`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Create a basic virtual private network](ec2_example_vpc_GettingStartedCLI_section.md)
+  [Getting started with graph databases](ec2_example_ec2_GettingStarted_064_section.md)

------
#### [ CLI ]

**AWS CLI**
**To modify the enableDnsSupport attribute**
This example modifies the `enableDnsSupport` attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is `true`, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not. If the command succeeds, no output is returned.
Command:

```
aws ec2 modify-vpc-attribute --vpc-id {{vpc-a01106c2}} --enable-dns-support "{\"Value\":false}"
```
**To modify the enableDnsHostnames attribute**
This example modifies the `enableDnsHostnames` attribute. This attribute indicates whether instances launched in the VPC get DNS hostnames. If this attribute is `true`, instances in the VPC get DNS hostnames; otherwise, they do not. If the command succeeds, no output is returned.
Command:

```
aws ec2 modify-vpc-attribute --vpc-id {{vpc-a01106c2}} --enable-dns-hostnames "{\"Value\":false}"
```
+  For API details, see [ModifyVpcAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example enables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $true
```
**Example 2: This example disables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $false
```
**Example 3: This example enables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $true
```
**Example 4: This example disables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $false
```
+  For API details, see [ModifyVpcAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example enables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $true
```
**Example 2: This example disables support for DNS hostnames for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsHostnames $false
```
**Example 3: This example enables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $true
```
**Example 4: This example disables support for DNS resolution for the specified VPC.**

```
Edit-EC2VpcAttribute -VpcId vpc-12345678 -EnableDnsSupport $false
```
+  For API details, see [ModifyVpcAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
