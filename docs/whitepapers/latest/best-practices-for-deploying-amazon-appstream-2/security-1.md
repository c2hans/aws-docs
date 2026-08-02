---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/security-1.html
---

# Security
<a name="security-1"></a>

 Cloud security at Amazon Web Services (AWS) is the highest priority. Security and compliance is a shared responsibility between AWS and the customer. For more information, refer to the [https://aws.amazon.com/compliance/shared-responsibility-model/](https://aws.amazon.com/compliance/shared-responsibility-model/). As an AWS and WorkSpaces Applications customer, it is important to implement security measures on different layers such as stack, fleet, image, and networking.

 Due to its ephemeral nature, WorkSpaces Applications is often preferred as a secure solution to application and desktop delivery. Consider whether antivirus solutions that are commonplace in Windows deployments are relevant in your use cases for an environment that is predefined and purged at the end of a user session. Antivirus adds overhead to virtualized instances, making it is a best practice to mitigate unnecessary activities. For example, scanning the system volume (which is ephemeral) at boot, for instance, does not add to the overall security of WorkSpaces Applications.

 The two key questions for security WorkSpaces Applications are centered on:
+  Is persisting user state beyond the session a requirement?
+  How much access should a user have within a session?

## Securing persistent data
<a name="securing-persistent-data"></a>

 Deployments of WorkSpaces Applications can require the user state to persist in some form. It might be to persist data for individual users, or to persist data for collaboration using a shared folder. WorkSpaces Applications instance storage is ephemeral and has no encryption option.

 WorkSpaces Applications provides user state persistence through home folders and application settings in Amazon S3. Some use cases require greater control over user state persistence. For these use cases, AWS recommends using a Server Message Block (SMB) file share.

### User state and data
<a name="user-state-and-data"></a>

Because most Windows applications perform best and most securely when co-located with application data created by the user, it is a best practice to keep this data in the same AWS Region as WorkSpaces Applications fleets. Encrypting this data is a best practice. The default behavior of the user home folder is to encrypt files and folders at rest using Amazon S3-managed encryption keys from the AWS key management services (AWS KMS). It is important to note that AWS Administrative Users with access to the AWS Console or Amazon S3 bucket will be able to access those files directly.

In designs that require a Server Message Block (SMB) target from a Windows File Share to store user files and folders, the process is either automatic or requires configuration.

 *Table 5 — Options for securing user data*

|   **SMB target**   |  **Encryption-at-rest**  |  **Encryption-in-transit**  |   **Antivirus (AV)**   |
| --- | --- | --- | --- |
|  FSx for Windows File Server  |  [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-at-rest.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-at-rest.html)  |  [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-in-transit.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-in-transit.html)  |  AV installed on a remote instance performs scan on mapped drive  |
|  **File Gateway, AWS Storage Gateway**  |  By default, all data stored by AWS Storage Gateway in S3 is encrypted server-side with Amazon S3-Managed Encryption Keys (SSE-S3). You can optionally configure different gateway types to encrypt stored data with AWS Key Management Service (KMS)  |  All data transferred between any type of gateway appliance and AWS storage is encrypted using SSL.  |  AV installed on a remote instance performs scan on mapped drive  |
|  EC2-based Windows File Servers  |  [Enable EBS encryption](https://docs.aws.amazon.com/kms/latest/developerguide/services-ebs.html)  |  PowerShell; Set- SmbServerConfiguration – EncryptData $True  |  AV installed on server performs scan on local drives  |

## Endpoint security and antivirus
<a name="endpoint-security-and-antivirus"></a>

The brief ephemeral nature of Amazon WorkSpaces Applications instances and the lack of persistency of data means a different approach is required to ensure user experience and performance is not compromised by activities that would be required on a persistent desktop. Endpoint Security agents are installed in WorkSpaces Applications images when there is an organizational policy or when used with external data ingress e.g. e-mail, files ingress, external web browsing.

### Removing unique identifiers
<a name="removing-unique-iidentifiers"></a>

Endpoint Security agents may have a globally unique identifier (GUID) which must be reset during the fleet instance creation process. Vendors have instructions on installing their products in images which will ensure a new GUID is generated for each instance generated from an image.

To ensure the GUID is not generated, install the Endpoint Security agent as the last action before running the WorkSpaces Applications Assistant to generate the image.

### Performance optimization
<a name="performance-optimization"></a>

Endpoint Security Vendors provide switches and setting that optimize the performance of WorkSpaces Applications. The settings vary between vendors and can be found in their documentation, typically in a section on VDI. Some common settings include but are not limited to are:
+ Turn off boot up scans to ensure instance creation, startup and login times are minimized
+ Turn off scheduled scans to prevent unnecessary scans
+ Turn off signature caches to prevent file enumeration
+ Enable VDI optimized IO settings
+ Exclusions required by applications to ensure performance

Endpoint security vendors provide instructions for use with virtual desktop environments which optimize performance.
+ Trend Micro Office Scan [Support for Virtual Desktop Infrastructure - Apex One/OfficeScan (trendmicro.com)](https://success.trendmicro.com/solution/1055260-best-practice-for-setting-up-virtual-desktop-infrastructure-vdi-in-officescan)
+ CrowdStrike and [How to Install the CrowdStrike Falcon in the Data Center](https://www.crowdstrike.com/blog/tech-center/install-falcon-datacenter/)
+ Sophos and [Sophos Central Endpoint: How to install on a gold image to avoid duplicate identities](https://support.sophos.com/support/s/article/KB-000035040?language=en_US) and [Sophos Central: Best practices when installing Windows Endpoints in Virtual Desktop Environments](https://support.sophos.com/support/s/article/KB-000039009?language=en_US)
+ McAfee and [McAfee Agent provisioning and deployment on Virtual Desktop Infrastructure systems](https://kc.mcafee.com/corporate/index?page=content&id=KB87654)
+ Microsoft Endpoint Security and [Configuring Microsoft Defender Antivirus for non-persistent VDI machines - Microsoft Tech Community](https://techcommunity.microsoft.com/t5/microsoft-defender-for-endpoint/configuring-microsoft-defender-antivirus-for-non-persistent-vdi/ba-p/1489633)

### Scanning exclusions
<a name="scanning-exclusions"></a>

 If security software is installed in WorkSpaces Applications instances, the security software must not interfere with the following processes.

 *Table 6 — WorkSpaces Applications processes security software must not interfere with the following processes.*

|  **Service**  |  **Processes**  |
| --- | --- |
|  AmazonCloudWatchAgent  |  "C:\\Program Files\\Amazon\\AmazonCloudWatchAgent\\start-amazon- cloudwatch-agent.exe"  |
|  AmazonSSMAgent  |  "C:\\Program Files\\Amazon\\SSM\\amazon-ssm-agent.exe"  |
|  NICE DCV  |  "C:\\Program Files\\NICE\\DCV\\Server\\bin\\dcvserver.exe" "C:\\Program Files\\NICE\\DCV\\Server\\bin\\dcvagent.exe"  |
|  WorkSpaces Applications  |  "C:\\ProgramFiles\\Amazon\\AppStream2\\StorageConnector\\StorageConnector.exe" <br /> In the folder "C:\\Program Files\\Amazon\\Photon\\" <br /> ".\\Agent\\PhotonAgent.exe"<br /> ".\\Agent\\s5cmd.exe"<br /> ".\\WebServer\\PhotonAgentWebServer.exe"<br /> ".\\CustomShell\\PhotonWindowsAppSwitcher.exe"<br /> ".\\CustomShell\\PhotonWindowsCustomShell.exe"<br /> ".\\CustomShell\\PhotonWindowsCustomShellBackground.exe"  |

### Folders
<a name="folders"></a>

 If security software is installed in WorkSpaces Applications instances, the software must not interfere with the following folders:

**Example**

```
    C:\Program Files\Amazon\*
    C:\ProgramData\Amazon\*
    C:\Program Files (x86)\AWS Tools\*
    C:\Program Files (x86)\AWS SDK for .NET\*
    C:\Program Files\NICE\*
    C:\ProgramData\NICE\*
    C:\AppStream\*
    C:\Program Files\Internet Explorer\*
    C:\Program Files\nodejs\
```

### Endpoint security console hygiene
<a name="endpoint-security-console-hygiene"></a>

Amazon WorkSpaces Applications will create new unique instances each time a user connects beyond the idle and disconnect timeouts. The instances will have a unique name and will build up in endpoint security management condoles. Setting unused aged machines over 4 or more days old (or lower depending on WorkSpaces Applications session timeouts) to be deleted will minimize the number of expired instances in the console.

## Network exclusions
<a name="network-exclusions"></a>

 The WorkSpaces Applications management network range (`198.19.0.0/16`) and following ports and addresses should not be blocked by any security / firewall or antivirus solutions within WorkSpaces Applications instances.

 *Table 7 — Ports in WorkSpaces Applications streaming instances security software must not interfere with*

|  **Port**  |   **Usage**   |
| --- | --- |
|  8300, 3128  |  This is used for establishing the streaming connection  |
|  8000  |  This is used for managing the streaming instance by WorkSpaces Applications  |
|  8443  |  This is used for managing the streaming instance by WorkSpaces Applications  |
|  53  |  DNS  |

 *Table 8 — WorkSpaces Applications managed service addresses security software must not interfere with*

|  **Port**  |  **Usage**  |
| --- | --- |
|  169.254.169.123  |  NTP  |
|  169.254.169.249  |  NVIDIA GRID License Service  |
|  169.254.169.250  |  KMS  |
|  169.254.169.251  |  KMS  |
|  169.254.169.253  |  DNS  |
|  169.254.169.254  |  Metadata  |

## Securing a WorkSpaces Applications session
<a name="securing-an-appstream-session"></a>

### Limiting application and operating system controls
<a name="limiting-application-and-operating-system-controls"></a>

 WorkSpaces Applications gives the administrator the ability to specify exactly which applications can be launched from the web page in application streaming mode. This does not, however, guarantee that only those applications specified can be run.

 Windows utilities and applications can be launched through the operating system through additional means. AWS recommends using [https://aws.amazon.com/blogs/desktop-and-application-streaming/using-microsoft-applocker-to-manage-application-experience-on-amazon-appstream-2-0/](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-microsoft-applocker-to-manage-application-experience-on-amazon-appstream-2-0/) to ensure that only the applications that your organization requires can be run. The default rules must be modified, as they grant everyone path access to critical system directories.

**Note**
 Windows Server 2016 and 2019 require the Windows Application Identity service to be running to enforce AppLocker rules. Application access from WorkSpaces Applications using Microsoft AppLocker is detailed in the [WorkSpaces Applications Admin Guide.](https://docs.aws.amazon.com/appstream2/latest/developerguide/data-protection.html#application-access)

 For fleet instances joined to an Active Directory domain, use Group Policy Objects (GPOs) to deliver user and system settings to secure the users application and resource access.

## Firewalls and routing
<a name="firewalls-and-routing"></a>

 When creating a WorkSpaces Applications fleet, subnets and a Security Group must be assigned. Subnets have existing assignments of Network Access Control Lists (NACLs) and route table(s). You can associate [up to five security groups](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-security-groups.html) while launching a new image builder or while creating a new fleet Security Groups can have up to [five assignments from the existing Security Groups](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-security-groups.html). For each security group, you add rules that control the outbound and inbound network traffic from and to your instances

A NACL is an optional layer of security for your VPC that acts as a stateless firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. For more information about the differences between security groups and network ACLs, see [the compare security groups and NACLs page](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison).

When designing and applying Security Group and NACL rules, consider the AWS Well-Architected best practices for least privilege. *Least privilege* is a principle of granting only the permissions required to complete a task.

For customers who have a high-speed private network connecting their on premise environment to AWS (via an AWS Direct Connect), you may consider using the VPC Endpoints for WorkSpaces Applications, which will mean the streaming traffic will be routed via your private network connectivity rather than going across the public internet. For more information on this topic, see the WorkSpaces Applications streaming interface VPC endpoint section of this document.

## Data loss prevention
<a name="data-loss-prevention"></a>

We'll look at two kinds of data loss prevention.

### Client to WorkSpaces Applications Instance Data Transfer Controls
<a name="client-to-AppStream-instance-data-transfer-controls"></a>

 *Table 9 — Guidance for controlling data ingress and egress*

|  **Setting**  |  **Options**  |  **Guidance**  |
| --- | --- | --- |
|  Clipboard  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/security-1.html)  |  Disabling this setting does not disable copy and paste within the session. If copying data into the session is required, choose Paste to remote session only to minimize the potential for data leakage.  |
|  File transfer  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/security-1.html)  |  Avoid enabling this setting to prevent data leakage.  |
|  Print to local device  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/security-1.html)  |  If printing is required, use network mapped printers that are controlled and monitored by your organization.  |

 Consider the advantages of the existing organizational data transfer solution over the stack settings. These configurations are not designed to replace a comprehensive secure data transfer solution.

## Controlling egress traffic from the WorkSpaces Applications instance
<a name="controlling-egress-traffic"></a>

Where data loss is a concern, it’s important to cover off what a User can access once they are inside of their WorkSpaces Applications instance. What does the network exit (or egress) path look like? It is a common requirement to have public internet access available to the end user inside their WorkSpaces Applications instance, so placing a WebProxy or Content Filtering Solution in the network path needs to be considered. Other considerations include a local Antivirus application and other endpoint security measures inside the WorkSpaces Applications instance (see the section “Endpoint Security and Antivirus” for more information).

## Using AWS services
<a name="using-aws-services"></a>

### AWS Identity and Access Management
<a name="aws-identity-and-access-management"></a>

 Using an IAM role to access AWS services, and being specific in the IAM policy attached to it, is a best practice that provides only the users in WorkSpaces Applications sessions have access without managing additional credentials. Follow the [https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html#best-practices-for-using-iam-role-with-streaming-instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html#best-practices-for-using-iam-role-with-streaming-instances).

 Create [https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html) that are created to persist user data in both home folders and application settings persistence. This [https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html#s3-iam-policy-restricted-access](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html#s3-iam-policy-restricted-access) from access.

### VPC endpoints
<a name="vpc-endpoints-1"></a>

 A VPC endpoint enables private connections between your VPC and supported AWS services and VPC endpoint services powered by AWS PrivateLink. AWS PrivateLink is a technology that enables you to privately access services by using private IP addresses. Traffic between your VPC and the other service does not leave the Amazon network. If public internet access is required only for AWS services, VPC endpoints remove the requirement for NAT gateways and internet gateways altogether.

 In environments where automation routines or developers require making API calls for WorkSpaces Applications, [https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html). For example, if there are EC2 instances in private subnets without public internet access, a VPC endpoint for WorkSpaces Applications API can be used to call WorkSpaces Applications API operations such as [https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html). The following diagram shows an example setup where WorkSpaces Applications API and streaming VPC endpoints are consumed by Lambda functions and EC2 instances.

![A reference architecture diagram for VPC endpoint](http://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/images/vpc-endpoint.jpeg)

 *VPC endpoint*

 The streaming VPC endpoint allows you to stream sessions through a VPC endpoint. The streaming interface endpoint maintains the streaming traffic within your VPC. Streaming traffic includes pixel, USB, user input, audio, clipboard, file upload and download, and printer traffic. To use the VPC endpoint, the VPC endpoint setting must be enabled at the WorkSpaces Applications stack. This serves as an alternative to streaming user sessions over the public internet from locations that have limited internet access and would benefit from accessing through a Direct Connect instance. Streaming user sessions through a VPC endpoint require the following:
+  The Security Groups that are associated with the interface endpoint must allow inbound access to port `443` (TCP) and ports `1400–1499` (TCP) from the IP address range from which your users connect.
+  The Network Access Control List for the subnets must allow outbound traffic from ephemeral network ports `1024-65535` (TCP) to the IP address range from which your users connect.
+  Internet connectivity is required to authenticate users and deliver the web assets that WorkSpaces Applications requires to function.

 To learn more about restricting traffic to AWS services with WorkSpaces Applications, see the administration guide for [https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html).

 When full public internet access is required, it’s a best practice to disable Internet Explorer Enhanced Security Configuration (ESC) on the Image Builder. For more information, see the WorkSpaces Applications administration guide to [https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets.html#customize-fleets-disable-ie-esc](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets.html#customize-fleets-disable-ie-esc).
