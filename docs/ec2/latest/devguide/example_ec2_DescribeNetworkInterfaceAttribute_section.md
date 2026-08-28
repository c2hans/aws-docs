---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_DescribeNetworkInterfaceAttribute_section.html
---

# Use `DescribeNetworkInterfaceAttribute` with a CLI
<a name="example_ec2_DescribeNetworkInterfaceAttribute_section"></a>

The following code examples show how to use `DescribeNetworkInterfaceAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To describe the attachment attribute of a network interface**
This example command describes the `attachment` attribute of the specified network interface.
Command:

```
aws ec2 describe-network-interface-attribute --network-interface-id {{eni-686ea200}} --attribute {{attachment}}
```
Output:

```
{
  "NetworkInterfaceId": "eni-686ea200",
  "Attachment": {
      "Status": "attached",
      "DeviceIndex": 0,
      "AttachTime": "2015-05-21T20:02:20.000Z",
      "InstanceId": "i-1234567890abcdef0",
      "DeleteOnTermination": true,
      "AttachmentId": "eni-attach-43348162",
      "InstanceOwnerId": "123456789012"
  }
}
```
**To describe the description attribute of a network interface**
This example command describes the `description` attribute of the specified network interface.
Command:

```
aws ec2 describe-network-interface-attribute --network-interface-id {{eni-686ea200}} --attribute {{description}}
```
Output:

```
{
  "NetworkInterfaceId": "eni-686ea200",
  "Description": {
      "Value": "My description"
  }
}
```
**To describe the groupSet attribute of a network interface**
This example command describes the `groupSet` attribute of the specified network interface.
Command:

```
aws ec2 describe-network-interface-attribute --network-interface-id {{eni-686ea200}} --attribute {{groupSet}}
```
Output:

```
{
  "NetworkInterfaceId": "eni-686ea200",
  "Groups": [
      {
          "GroupName": "my-security-group",
          "GroupId": "sg-903004f8"
      }
  ]
}
```
**To describe the sourceDestCheck attribute of a network interface**
This example command describes the `sourceDestCheck` attribute of the specified network interface.
Command:

```
aws ec2 describe-network-interface-attribute --network-interface-id {{eni-686ea200}} --attribute {{sourceDestCheck}}
```
Output:

```
{
  "NetworkInterfaceId": "eni-686ea200",
  "SourceDestCheck": {
      "Value": true
  }
}
```
+  For API details, see [DescribeNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interface-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute Attachment
```
**Output:**

```
Attachment         : Amazon.EC2.Model.NetworkInterfaceAttachment
```
**Example 2: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute Description
```
**Output:**

```
Description        : My description
```
**Example 3: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute GroupSet
```
**Output:**

```
Groups             : {my-security-group}
```
**Example 4: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute SourceDestCheck
```
**Output:**

```
SourceDestCheck    : True
```
+  For API details, see [DescribeNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute Attachment
```
**Output:**

```
Attachment         : Amazon.EC2.Model.NetworkInterfaceAttachment
```
**Example 2: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute Description
```
**Output:**

```
Description        : My description
```
**Example 3: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute GroupSet
```
**Output:**

```
Groups             : {my-security-group}
```
**Example 4: This example describes the specified network interface.**

```
Get-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-12345678 -Attribute SourceDestCheck
```
**Output:**

```
SourceDestCheck    : True
```
+  For API details, see [DescribeNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ec2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
