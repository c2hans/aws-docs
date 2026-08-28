---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RunScheduledInstances_section.html
---

# Use `RunScheduledInstances` with a CLI
<a name="example_ec2_RunScheduledInstances_section"></a>

The following code examples show how to use `RunScheduledInstances`.

------
#### [ CLI ]

**AWS CLI**
**To launch a Scheduled Instance**
This example launches the specified Scheduled Instance in a VPC.
Command:

```
aws ec2 run-scheduled-instances --scheduled-instance-id {{sci-1234-1234-1234-1234-123456789012}} --instance-count {{1}} --launch-specification {{file://launch-specification.json}}
```
Launch-specification.json:

```
{
  "ImageId": "ami-12345678",
  "KeyName": "my-key-pair",
  "InstanceType": "c4.large",
  "NetworkInterfaces": [
    {
        "DeviceIndex": 0,
        "SubnetId": "subnet-12345678",
        "AssociatePublicIpAddress": true,
        "Groups": ["sg-12345678"]
    }
  ],
  "IamInstanceProfile": {
      "Name": "my-iam-role"
  }
}
```
Output:

```
{
  "InstanceIdSet": [
      "i-1234567890abcdef0"
  ]
}
```
This example launches the specified Scheduled Instance in EC2-Classic.
Command:

```
aws ec2 run-scheduled-instances --scheduled-instance-id {{sci-1234-1234-1234-1234-123456789012}} --instance-count {{1}} --launch-specification {{file://launch-specification.json}}
```
Launch-specification.json:

```
{
  "ImageId": "ami-12345678",
  "KeyName": "my-key-pair",
  "SecurityGroupIds": ["sg-12345678"],
  "InstanceType": "c4.large",
  "Placement": {
    "AvailabilityZone": "us-west-2b"
  }
  "IamInstanceProfile": {
      "Name": "my-iam-role"
  }
}
```
Output:

```
{
  "InstanceIdSet": [
      "i-1234567890abcdef0"
  ]
}
```
+  For API details, see [RunScheduledInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-scheduled-instances.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example launches the specified Scheduled Instance.**

```
New-EC2ScheduledInstance -ScheduledInstanceId sci-1234-1234-1234-1234-123456789012 -InstanceCount 1 `
-IamInstanceProfile_Name my-iam-role `
-LaunchSpecification_ImageId ami-12345678 `
-LaunchSpecification_InstanceType c4.large `
-LaunchSpecification_SubnetId subnet-12345678`
-LaunchSpecification_SecurityGroupId sg-12345678
```
+  For API details, see [RunScheduledInstances](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example launches the specified Scheduled Instance.**

```
New-EC2ScheduledInstance -ScheduledInstanceId sci-1234-1234-1234-1234-123456789012 -InstanceCount 1 `
-IamInstanceProfile_Name my-iam-role `
-LaunchSpecification_ImageId ami-12345678 `
-LaunchSpecification_InstanceType c4.large `
-LaunchSpecification_SubnetId subnet-12345678`
-LaunchSpecification_SecurityGroupId sg-12345678
```
+  For API details, see [RunScheduledInstances](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
