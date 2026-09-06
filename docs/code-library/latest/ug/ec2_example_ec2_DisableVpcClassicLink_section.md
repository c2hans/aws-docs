---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DisableVpcClassicLink_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DisableVpcClassicLink` with a CLI
<a name="ec2_example_ec2_DisableVpcClassicLink_section"></a>

The following code examples show how to use `DisableVpcClassicLink`.

------
#### [ CLI ]

**AWS CLI**
**To disable ClassicLink for a VPC**
This example disables ClassicLink for vpc-8888888.
Command:

```
aws ec2 disable-vpc-classic-link --vpc-id {{vpc-88888888}}
```
Output:

```
{
  "Return": true
}
```
+  For API details, see [DisableVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example disables EC2VpcClassicLink for the vpc-01e23c4a5d6db78e9. It returns either True or False**

```
Disable-EC2VpcClassicLink -VpcId vpc-01e23c4a5d6db78e9
```
+  For API details, see [DisableVpcClassicLink](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example disables EC2VpcClassicLink for the vpc-01e23c4a5d6db78e9. It returns either True or False**

```
Disable-EC2VpcClassicLink -VpcId vpc-01e23c4a5d6db78e9
```
+  For API details, see [DisableVpcClassicLink](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
