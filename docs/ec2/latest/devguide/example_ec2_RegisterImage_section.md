---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RegisterImage_section.html
---

# Use `RegisterImage` with a CLI
<a name="example_ec2_RegisterImage_section"></a>

The following code examples show how to use `RegisterImage`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To register an AMI using a manifest file**
The following `register-image` example registers an AMI using the specified manifest file in Amazon S3.

```
aws ec2 register-image \
    --name {{my-image}} \
    --image-location {{amzn-s3-demo-bucket/myimage/image.manifest.xml}}
```
Output:

```
{
    "ImageId": "ami-1234567890EXAMPLE"
}
```
For more information, see [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) in the *Amazon EC2 User Guide*.
**Example 2: To register an AMI using a snapshot of a root device**
The following `register-image` example registers an AMI using the specified snapshot of an EBS root volume as device `/dev/xvda`. The block device mapping also includes an empty 100 GiB EBS volume as device `/dev/xvdf`.

```
aws ec2 register-image \
    --name {{my-image}} \
    --root-device-name {{/dev/xvda}} \
    --block-device-mappings {{DeviceName=/dev/xvda,Ebs={SnapshotId=snap-0db2cf683925d191f}}} {{DeviceName=/dev/xvdf,Ebs={VolumeSize=100}}}
```
Output:

```
{
    "ImageId": "ami-1a2b3c4d5eEXAMPLE"
}
```
For more information, see [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) in the *Amazon EC2 User Guide*.
+  For API details, see [RegisterImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example registers an AMI using the specified manifest file in Amazon S3.**

```
Register-EC2Image -ImageLocation amzn-s3-demo-bucket/my-web-server-ami/image.manifest.xml -Name my-web-server-ami
```
+  For API details, see [RegisterImage](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example registers an AMI using the specified manifest file in Amazon S3.**

```
Register-EC2Image -ImageLocation amzn-s3-demo-bucket/my-web-server-ami/image.manifest.xml -Name my-web-server-ami
```
+  For API details, see [RegisterImage](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
