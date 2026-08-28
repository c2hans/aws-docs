---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_ModifyNetworkInterfaceAttribute_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ModifyNetworkInterfaceAttribute` with a CLI
<a name="ec2_example_ec2_ModifyNetworkInterfaceAttribute_section"></a>

The following code examples show how to use `ModifyNetworkInterfaceAttribute`.

------
#### [ CLI ]

**AWS CLI**
**To modify the attachment attribute of a network interface**
This example command modifies the `attachment` attribute of the specified network interface.
Command:

```
aws ec2 modify-network-interface-attribute --network-interface-id {{eni-686ea200}} --attachment {{AttachmentId=eni-attach-43348162,DeleteOnTermination=false}}
```
**To modify the description attribute of a network interface**
This example command modifies the `description` attribute of the specified network interface.
Command:

```
aws ec2 modify-network-interface-attribute --network-interface-id {{eni-686ea200}} --description {{"My description"}}
```
**To modify the groupSet attribute of a network interface**
This example command modifies the `groupSet` attribute of the specified network interface.
Command:

```
aws ec2 modify-network-interface-attribute --network-interface-id {{eni-686ea200}} --groups {{sg-903004f8}} {{sg-1a2b3c4d}}
```
**To modify the sourceDestCheck attribute of a network interface**
This example command modifies the `sourceDestCheck` attribute of the specified network interface.
Command:

```
aws ec2 modify-network-interface-attribute --network-interface-id {{eni-686ea200}} --no-source-dest-check
```
+  For API details, see [ModifyNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-network-interface-attribute.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example modifies the specified network interface so that the specified attachment is deleted on termination.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Attachment_AttachmentId eni-attach-1a2b3c4d -Attachment_DeleteOnTermination $true
```
**Example 2: This example modifies the description of the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Description "my description"
```
**Example 3: This example modifies the security group for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Groups sg-1a2b3c4d
```
**Example 4: This example disables source/destination checking for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck $false
```
+  For API details, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example modifies the specified network interface so that the specified attachment is deleted on termination.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Attachment_AttachmentId eni-attach-1a2b3c4d -Attachment_DeleteOnTermination $true
```
**Example 2: This example modifies the description of the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Description "my description"
```
**Example 3: This example modifies the security group for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -Groups sg-1a2b3c4d
```
**Example 4: This example disables source/destination checking for the specified network interface.**

```
Edit-EC2NetworkInterfaceAttribute -NetworkInterfaceId eni-1a2b3c4d -SourceDestCheck $false
```
+  For API details, see [ModifyNetworkInterfaceAttribute](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
