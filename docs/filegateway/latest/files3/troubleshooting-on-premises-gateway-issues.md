---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html
---

# Troubleshooting: on-premises gateway issues
<a name="troubleshooting-on-premises-gateway-issues"></a>

You can find information following about typical issues that you might encounter working with your on-premises gateways, and how to allow Support to connect to your gateway to assist with troubleshooting.

The following table lists typical issues that you might encounter working with your on-premises gateways.

| Issue | Action to Take |
| --- | --- |
| You cannot find the IP address of your gateway. | Use the hypervisor client to connect to your host to find the gateway IP address.[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html)<br />If you are still having trouble finding the gateway IP address:[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html) |
| You're having network or firewall problems. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html)  |
| Your gateway's activation fails when you click the **Proceed to Activation** button in the Storage Gateway Management Console. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html)  |
| You need to improve bandwidth between your gateway and AWS. | You can improve the bandwidth from your gateway to AWS by setting up your internet connection to AWS on a network adapter (NIC) separate from that connecting your applications and the gateway VM. Taking this approach is useful if you have a high-bandwidth connection to AWS and you want to avoid bandwidth contention, especially during a snapshot restore. For high-throughput workload needs, you can use [Direct Connect](https://aws.amazon.com/directconnect/) to establish a dedicated network connection between your on-premises gateway and AWS. To measure the bandwidth of the connection from your gateway to AWS, use the `CloudBytesDownloaded` and `CloudBytesUploaded` metrics of the gateway. For more on this subject, see [Performance and optimization](Performance.md). Improving your internet connectivity helps to ensure that your upload buffer does not fill up. |
| Throughput to or from your gateway drops to zero. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/troubleshooting-on-premises-gateway-issues.html)You can view the throughput to and from your gateway from the Amazon CloudWatch console. For more information about measuring throughput to and from your gateway to AWS, see [Performance and optimization](Performance.md). |
| You are having trouble importing (deploying) Storage Gateway on Microsoft Hyper-V. | See [Troubleshooting: Microsoft Hyper-V setup](troubleshooting-hyperv-setup.md), which discusses some of the common issues of deploying a gateway on Microsoft Hyper-V. |
| You receive a message that says: "The data that has been written to the volume in your gateway isn't securely stored at AWS". | You receive this message if your gateway VM was created from a clone or snapshot of another gateway VM. If this isn’t the case, contact Support. |

## Troubleshooting: Security scans show open NFS ports
<a name="troubleshoot-open-nfs-ports"></a>

Certain NFS ports are enabled by default, even on gateways that you only use with SMB file shares. If you use third-party security software such as Qualys to scan the network where your File Gateway is deployed, the scan results might report these open NFS ports as a potential security vulnerability. If you only use your gateway with SMB file shares and you want to disable the unused NFS ports for security reasons, use the following procedure:

**To disable NFS ports on a File Gateway:**

1. Access the gateway local console command prompt using the procedure outlined in [Running Storage Gateway commands on the local console](MaintenanceGatewayConsole-fgw.md).

1. Enter the following commands to disable NFS traffic:

   **IPv4**

   ```
   iptables -I INPUT -p udp -m udp --dport 111 -j DROP
   iptables -I INPUT -p udp -m udp --dport 2049 -j DROP
   iptables -I INPUT -p udp -m udp --dport 20048 -j DROP
   iptables -I INPUT -p tcp -m tcp --dport 111 -j DROP
   iptables -I INPUT -p tcp -m tcp --dport 2049 -j DROP
   iptables -I INPUT -p tcp -m tcp --dport 20048 -j DROP
   ```

   **IPv6**

   ```
   ip6tables -I INPUT -p udp -m udp --dport 111 -j DROP
   ip6tables -I INPUT -p udp -m udp --dport 2049 -j DROP
   ip6tables -I INPUT -p udp -m udp --dport 20048 -j DROP
   ip6tables -I INPUT -p tcp -m tcp --dport 111 -j DROP
   ip6tables -I INPUT -p tcp -m tcp --dport 2049 -j DROP
   ip6tables -I INPUT -p tcp -m tcp --dport 20048 -j DROP
   ```

1. Enter the following command to confirm that the blocked NFS ports appear in the IP tables:

   **IPv4**

   ```
   iptables -n -L -v --line-numbers
   ```

   **IPv6**

   ```
   ip6tables -n -L -v --line-numbers
   ```

## Turning on Support access to help troubleshoot your gateway hosted on-premises
<a name="enable-support-access-on-premises"></a>

Storage Gateway provides a local console you can use to perform several maintenance tasks, including allowing Support to access your gateway to assist you with troubleshooting gateway issues. By default, Support access to your gateway is turned off. You turn on this access through the host's local console. To give Support access to your gateway, you first log in to the local console for the host, navigate to the Storage Gateway's console, and then connect to the support server.

**To turn on Support access to your gateway**

1. Log in to your host's local console.
   + VMware ESXi – for more information, see [Accessing the Gateway Local Console with VMware ESXi](accessing-local-console.md#MaintenanceConsoleWindowVMware-common).
   + Microsoft Hyper-V – for more information, see [Access the Gateway Local Console with Microsoft Hyper-V](accessing-local-console.md#MaintenanceConsoleWindowHyperV-common).

1. At the prompt, enter the corresponding numeral to select **Gateway Console**.

1. Enter **h** to open the list of available commands.

1.

   Do one of the following:
   + If your gateway is using a public endpoint, in the **AVAILABLE COMMANDS** window, enter **open-support-channel** to connect to customer support for Storage Gateway. Allow TCP port 22 so you can open a support channel to AWS. When you connect to customer support, Storage Gateway assigns you a support number. Make a note of your support number.
   + If your gateway is using a VPC endpoint, in the **AVAILABLE COMMANDS** window, enter **open-support-channel**. If your gateway is not activated, provide the VPC endpoint or IP address to connect to customer support for Storage Gateway. Allow TCP port 22 so you can open a support channel to AWS. When you connect to customer support, Storage Gateway assigns you a support number. Make a note of your support number.
**Note**
The channel number is not a Transmission Control Protocol/User Datagram Protocol (TCP/UDP) port number. Instead, the gateway makes a Secure Shell (SSH) (TCP 22) connection to Storage Gateway servers and provides the support channel for the connection.

1. After the support channel is established, provide your support service number to Support so Support can provide troubleshooting assistance.

1. When the support session is completed, enter **q** to end it. Don't close the session until Amazon Web Services Support notifies you that the support session is complete.

1. Enter **exit** to log out of the Storage Gateway console.

1. Follow the prompts to exit the local console.
