---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager.html
---

# Automate adding or updating Windows registry entries using AWS Systems Manager
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager"></a>

*Appasaheb Bagali, Amazon Web Services*

## Summary
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager-summary"></a>

AWS Systems Manager is a remote management tool for Amazon Elastic Compute Cloud (Amazon EC2) instances. Systems Manager provides visibility and control over your infrastructure on Amazon Web Services. This versatile tool can be used to fix Windows registry changes that are identified as vulnerabilities by the security vulnerability scan report.

This pattern covers the steps to keep your EC2 instances that are running Windows operating system secure by automating registry changes that are recommended for the safety of your environment. The pattern uses the Run command to run a Command document. The code is attached, and a portion of it is included in the *Code* section.

## Prerequisites and limitations
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager-prereqs"></a>
+ An active AWS account
+ Permissions to access the EC2 instance and Systems Manager

## Architecture
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager-architecture"></a>

**Target technology stack**
+ A virtual private cloud (VPC), with two subnets and a network address translation (NAT) gateway
+ A Systems Manager Command document to add or update the registry name and value
+ Systems Manager Run Command to run the Command document on the specified EC2 instances

**Target architecture**

![How to automatically add or update Windows registry entries using AWS Systems Manager.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2ecf680d-9f36-4070-8a19-2af262db7fcc/images/c992bcb0-d894-4aa7-9bb3-3d60c9c79e8d.png)

## Tools
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager-tools"></a>

**Tools**
+ [IAM policies and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) – AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
+ [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Amazon Simple Storage Service (Amazon S3) is storage for the internet. It is designed to make web-scale computing easier for developers. In this pattern, an S3 bucket is used to store the Systems Manager logs.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) – AWS Systems Manager is an AWS service that you can use to view and control your infrastructure on AWS. Systems Manager helps you maintain security and compliance by scanning your *managed instances* and reporting (or taking corrective action on) any policy violations it detects.
+ [AWS Systems Manager Command document](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) – AWS Systems Manager Command documents are used by Run Command. Most Command documents are supported on all Linux and Windows Server operating systems supported by Systems Manager.
+ [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html) – AWS Systems Manager Run Command gives you a way to manage the configuration of your managed instances remotely and securely. Using Run Command, you can automate common administrative tasks and perform one-time configuration changes at scale.

**Code**

You can use the following example code to add or update a Microsoft Windows registry name to `Version`, registry path to `HKCU:\Software\ScriptingGuys\Scripts`, and value to `2`.

```
#Windows registry path which needs to add/update
$registryPath ='HKCU:\\Software\\ScriptingGuys\\Scripts'
#Windows registry Name  which needs to add/update
$Name = 'Version'
#Windows registry value  which needs to add/update
$value = 2
# Test-Path cmdlet to see if the registry key exists.
IF(!(Test-Path $registryPath))
        {
           New-Item -Path $registryPath -Force | Out-Null
           New-ItemProperty -Path $registryPath -Name $name -Value     $value ` -PropertyType DWORD -                 Force | Out-        Null
        } ELSE {
                      New-ItemProperty -Path $registryPath -Name $name -Value $value ` -PropertyType            DWORD        -Force | Out-Null
            }
echo 'Registry Path:'$registryPath
 echo 'Registry Name:'$registryPath
 echo 'Registry Value:'(Get-ItemProperty -Path $registryPath -Name $Name).version
```

The full Systems Manager Command document JavaScript Object Notation (JSON) code example is attached.

## Epics
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager-epics"></a>

### Set up a VPC
<a name="set-up-a-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | On the AWS Management Console, create a VPC that has public and private subnets and a NAT gateway. For more information, see the [AWS documentation](https://docs.aws.amazon.com/batch/latest/userguide/create-public-private-vpc.html). | Cloud administrator |
| Create security groups. | Ensure that each security group allows access for Remote Desktop Protocol (RDP) from the source IP address. | Cloud administrator |

### Create an IAM policy and an IAM role
<a name="create-an-iam-policy-and-an-iam-role"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM policy. | Create an IAM policy that provides access to Amazon S3, Amazon EC2, and Systems Manager. | Cloud administrator |
| Create an IAM role. | Create an IAM role, and attach the IAM policy that provides access to Amazon S3, Amazon EC2, and Systems Manager. | Cloud administrator |

### Run the automation
<a name="run-the-automation"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Systems Manager Command document. | Create a Systems Manager Command document that will deploy the Microsoft Windows registry changes to add or update. | Cloud administrator |
| Run the Systems Manager Run Command. | Run the Systems Manager Run Command, selecting the Command document and the Systems Manager target instances. This pushes the Microsoft Windows registry change in the selected Command document to the target instances. | Cloud administrator |

## Related resources
<a name="automate-adding-or-updating-windows-registry-entries-using-aws-systems-manager-resources"></a>
+ [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
+ [AWS Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html)
+ [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html)

## Attachments
<a name="attachments-2ecf680d-9f36-4070-8a19-2af262db7fcc"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/2ecf680d-9f36-4070-8a19-2af262db7fcc/attachments/attachment.zip)
